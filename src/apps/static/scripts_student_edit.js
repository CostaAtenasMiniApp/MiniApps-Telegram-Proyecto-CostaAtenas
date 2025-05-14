document.addEventListener('DOMContentLoaded', function() {
    // Validación básica del formulario
    const form = document.querySelector('.student-form');
    
    form.addEventListener('submit', function(e) {
        let isValid = true;
        
        // Validar campos requeridos
        const requiredFields = form.querySelectorAll('[required]');
        requiredFields.forEach(field => {
            if (!field.value.trim()) {
                field.style.borderColor = 'var(--color-error)';
                isValid = false;
            } else {
                field.style.borderColor = '';
            }
        });
        
        // Validar email
        const emailField = form.querySelector('#email');
        if (emailField && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(emailField.value)) {
            emailField.style.borderColor = 'var(--color-error)';
            isValid = false;
        }
        
        if (!isValid) {
            e.preventDefault();
            alert('Por favor complete todos los campos requeridos correctamente.');
        }
    });
    
    // Mostrar/ocultar secciones adicionales
    const toggleButtons = document.querySelectorAll('.toggle-section');
    toggleButtons.forEach(button => {
        button.addEventListener('click', function() {
            const sectionId = this.getAttribute('data-target');
            const section = document.getElementById(sectionId);
            if (section) {
                section.classList.toggle('visible');
                this.textContent = section.classList.contains('visible') ? 
                    'Ocultar detalles' : 'Mostrar más detalles';
            }
        });
    });
});