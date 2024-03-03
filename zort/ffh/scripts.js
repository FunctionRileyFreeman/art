document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('quantumCanvas');
    const ctx = canvas.getContext('2d');
    canvas.width = 600; // Match CSS dimensions
    canvas.height = 300;
  
    let isCollapsed = false;
    let wavelength = 50; // Default wavelength
  
    function drawWaveFunction() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      if (!isCollapsed) {
        ctx.beginPath();
        ctx.strokeStyle = '#007bff'; // Blue for wave function
        for (let i = 0; i < canvas.width; i++) {
          // Adjust the wavelength based on slider value
          ctx.lineTo(i, canvas.height / 2 + Math.sin(i * 0.05 * wavelength / 50) * 50);
        }
        ctx.stroke();
      } else {
        ctx.fillStyle = '#dc3545'; // Red for collapsed state
        ctx.beginPath();
        ctx.arc(canvas.width / 2, canvas.height / 2, 10, 0, Math.PI * 2);
        ctx.fill();
      }
    }
  
    document.getElementById('collapseButton').addEventListener('click', () => {
      isCollapsed = true;
      drawWaveFunction();
    });
  
    // Listener for the wavelength slider
    document.getElementById('wavelengthSlider').addEventListener('input', (e) => {
      wavelength = e.target.value;
      if (!isCollapsed) {
        drawWaveFunction();
      }
    });
  
    drawWaveFunction();
  });
  