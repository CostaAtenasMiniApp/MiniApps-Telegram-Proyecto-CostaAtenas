// Almacenar datos de los formularios temporalmente
const formDataStore = {
    'identificacion-form': null,
    'estadisticos-form': null,
    'legal-form': null
};

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
                const currentForm = document.querySelector('form');
                if (!currentForm) return;
                if (currentForm.checkValidity()) {
                    // Guardar datos del formulario actual
                    formDataStore[currentForm.id] = new FormData(currentForm);

                    const nextSection = parseInt(this.dataset.next);
                    loadSection(nextSection);
                } else {
                    currentForm.reportValidity(); // Mostrar mensajes de validación
                }
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

    // Validar y enviar todos los formularios
    const legalForm = document.getElementById('legal-form');
    if (legalForm) {
        legalForm.addEventListener('submit', function(e) {
            e.preventDefault();

            // Guardar datos del formulario legal antes de enviar
            formDataStore['legal-form'] = new FormData(this);

            // Combinar todos los datos en un solo FormData
            const combinedFormData = new FormData();
            for (const formId in formDataStore) {
                if (formDataStore[formId]) {
                    for (const [key, value] of formDataStore[formId].entries()) {
                        combinedFormData.append(key, value);
                    }
                }
            }

            // Enviar los datos al servidor
            fetch('/registration', {
                method: 'POST',
                body: combinedFormData
            })
                .then(response => {
                    if (response.ok) {
                        alert('Formulario enviado correctamente');
                        // Opcional: Limpiar formDataStore y reiniciar el formulario
                        formDataStore['identificacion-form'] = null;
                        formDataStore['estadisticos-form'] = null;
                        formDataStore['legal-form'] = null;
                        loadSection(1); // Volver a la primera sección
                    } else {
                        alert('Error al enviar el formulario');
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert('Error al enviar el formulario');
                });
        });
    }
}