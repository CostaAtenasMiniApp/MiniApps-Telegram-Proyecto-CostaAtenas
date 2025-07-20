document.addEventListener('DOMContentLoaded', () => {
  const heroImage = document.getElementById('hero-image');
  if (heroImage) {
    let rotation = 0;
    let direction = 0.1; // Speed and direction

    setInterval(() => {
      rotation += direction;
      if (rotation > 2 || rotation < -2) {
        direction *= -1; // Reverse direction
      }
      heroImage.style.transform = `rotate(${rotation}deg)`;
      heroImage.style.transition = 'transform 0.5s linear';
    }, 100); // Update every 100ms for smooth animation
  }
});
