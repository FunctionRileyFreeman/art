const dot = document.getElementById('movingDot');

function moveDot() {
  const maxX = window.innerWidth - dot.clientWidth;
  const maxY = window.innerHeight - dot.clientHeight;

  const randomX = Math.floor(Math.random() * maxX);
  const randomY = Math.floor(Math.random() * maxY);

  const randomColor = '#' + Math.floor(Math.random() * 16777215).toString(16);
  
  const randomSize = Math.floor(Math.random() * 40) + 10; // Random size between 10px and 50px

  dot.style.left = `${randomX}px`;
  dot.style.top = `${randomY}px`;
  dot.style.backgroundColor = randomColor;
  dot.style.width = `${randomSize}px`;
  dot.style.height = `${randomSize}px`;
}

setInterval(moveDot, 1000); // Change dot position, size, and color every second
