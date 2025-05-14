document.addEventListener('DOMContentLoaded', function() {
    // Mejorar accesibilidad de la tabla
    const table = document.querySelector('.student-table');
    if (table) {
        // Añadir ARIA roles para mejor accesibilidad
        table.setAttribute('role', 'grid');

        // Añadir eventos para teclado
        table.querySelectorAll('tr').forEach(row => {
            row.setAttribute('role', 'row');
            row.querySelectorAll('td, th').forEach(cell => {
                cell.setAttribute('role', 'gridcell');
            });
        });

        // Hacer filas clickeables (opcional)
        table.querySelectorAll('tbody tr').forEach(row => {
            row.style.cursor = 'pointer';
            row.addEventListener('click', function() {
                const viewBtn = this.querySelector('.btn-primary');
                if (viewBtn) {
                    window.location.href = viewBtn.href;
                }
            });
        });
    }

    // Añadir mensaje si no hay estudiantes
    const tbody = document.querySelector('.student-table tbody');
    if (tbody && tbody.children.length === 0) {
        const emptyRow = document.createElement('tr');
        emptyRow.innerHTML = `
            <td colspan="6" style="text-align: center; padding: 20px;">
                No hay estudiantes registrados
            </td>
        `;
        tbody.appendChild(emptyRow);
    }
});