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

 // Configuración de Particle.js
particlesJS('particles-js', {
particles: {
    number: {
    value: 80, // Número de partículas
    density: {
        enable: true,
        value_area: 800
    }
    },
    color: {
    value: '#4e82bf' // Color de las partículas (más oscuro)
    },
    shape: {
    type: 'circle', // Forma de las partículas
    stroke: {
        width: 0,
        color: '#000000'
    },
    polygon: {
        nb_sides: 5
    }
    },
    opacity: {
    value: 0.7, // Opacidad de las partículas
    random: false,
    anim: {
        enable: false,
        speed: 1,
        opacity_min: 0.1,
        sync: false
    }
    },
    size: {
    value: 4, // Tamaño de las partículas
    random: true,
    anim: {
        enable: false,
        speed: 40,
        size_min: 0.1,
        sync: false
    }
    },
    line_linked: {
    enable: true, // Habilitar conexiones entre partículas
    distance: 150, // Distancia máxima para conectar partículas
    color: '#4e82bf', // Color de las conexiones (más oscuro)
    opacity: 0.5,
    width: 1
    },
    move: {
    enable: true, // Habilitar movimiento de partículas
    speed: 6, // Velocidad de movimiento
    direction: 'none',
    random: false,
    straight: false,
    out_mode: 'bounce', // Comportamiento al salir del contenedor
    bounce: true,
    attract: {
        enable: false,
        rotateX: 600,
        rotateY: 1200
    }
    }
},
interactivity: {
    detect_on: 'canvas',
    events: {
    onhover: {
        enable: true, // Efecto al pasar el ratón
        mode: 'repulse' // Modo: repulsión
    },
    onclick: {
        enable: true, // Efecto al hacer clic
        mode: 'push' // Modo: empujar
    },
    resize: true
    },
    modes: {
    repulse: {
        distance: 100,
        duration: 0.4
    },
    push: {
        particles_nb: 4
    }
    }
},
retina_detect: true
});