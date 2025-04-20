// Carga inicial
document.addEventListener('DOMContentLoaded', function() {
    loadSection(1);

    // Configurar eventos de los pasos
    document.querySelectorAll('.step').forEach(step => {
        step.addEventListener('click', function() {
            const stepNumber = parseInt(this.dataset.step);
            loadSection(stepNumber);
        });
    });
});

// Función para cargar secciones
function loadSection(sectionNumber) {
    const sectionFile = `secciones/${sectionNumber === 1 ? 'identificacion' : sectionNumber === 2 ? 'estadisticos' : 'legal'}.html`;

    fetch(sectionFile)
        .then(response => response.text())
        .then(html => {
            document.getElementById('form-container').innerHTML = html;
            updateProgressSteps(sectionNumber);
            setupSectionEvents();
        })
        .catch(error => console.error('Error loading section:', error));
}

// Actualizar la barra de progreso
function updateProgressSteps(currentStep) {
    const steps = document.querySelectorAll('.step');

    steps.forEach((step, index) => {
        step.classList.remove('active', 'completed');
        if (index + 1 < currentStep) {
            step.classList.add('completed');
        } else if (index + 1 === currentStep) {
            step.classList.add('active');
        }
    });
}

// Configurar eventos de la sección actual
function setupSectionEvents() {
    // Eventos para campos condicionales
    const proplayasRadios = document.querySelectorAll('input[name="proplayas"]');
    if (proplayasRadios.length) {
        proplayasRadios.forEach(radio => {
            radio.addEventListener('change', function() {
                document.getElementById('nodo-proplayas-group').style.display =
                    this.value === 'Si' ? 'block' : 'none';
            });
        });
    }

    const hotelRadios = document.querySelectorAll('input[name="pertenece_hotel"]');
    if (hotelRadios.length) {
        hotelRadios.forEach(radio => {
            radio.addEventListener('change', function() {
                document.getElementById('nombre-hotel-group').style.display =
                    this.value === 'Si' ? 'block' : 'none';
            });
        });
    }

    // Eventos de navegación
    const nextButtons = document.querySelectorAll('.next-btn');
    if (nextButtons.length) {
        nextButtons.forEach(btn => {
            btn.addEventListener('click', function() {
                const nextSection = parseInt(this.dataset.next);
                loadSection(nextSection);
            });
        });
    }

    const prevButtons = document.querySelectorAll('.prev-btn');
    if (prevButtons.length) {
        prevButtons.forEach(btn => {
            btn.addEventListener('click', function() {
                const prevSection = parseInt(this.dataset.prev);
                loadSection(prevSection);
            });
        });
    }

    // Validar formulario antes de enviar
    const submitForm = document.getElementById('legal-form');
    if (submitForm) {
        submitForm.addEventListener('submit', function(e) {
            e.preventDefault();
            alert('Formulario enviado correctamente');
            // Aquí iría el código para enviar los datos
            
        });
    }
}