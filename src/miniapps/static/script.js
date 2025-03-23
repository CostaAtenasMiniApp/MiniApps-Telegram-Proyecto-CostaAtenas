// Función para ejecutar un comando y cerrar la miniapp
function executeCommand(comando, bot_name) {
    const chatId = Telegram.WebApp.initDataUnsafe.user?.id; // Obtiene el ID del usuario

    if (chatId) {
        // Enviar el comando al backend
        fetch('https://tudominio.com/execute-command', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                chat_id: chatId,
                command: comando,
                bot: bot_name // Nombre del bot que ejecutará el comando
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert(`Comando "${comando}" ejecutado correctamente`);
                Telegram.WebApp.close(); // Cerrar la miniapp
            } else {
                alert('Hubo un error al ejecutar el comando');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Hubo un error al ejecutar el comando');
        });
    } else {
        alert('No se pudo obtener el ID del usuario');
    }
}