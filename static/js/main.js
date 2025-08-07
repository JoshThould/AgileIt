// JavaScript code to animate Title "AgileIt" with a red color effect

document.addEventListener('DOMContentLoaded', () => {
 const itSpan = document.querySelector('.it');
const text = 'It';
let index = 0;
let direction = 1;

function typeLoop() {
  itSpan.textContent = text.slice(0, index);

  index += direction;

  if (index > text.length) {
    direction = -1;
    setTimeout(typeLoop, 1000); // pause before deleting
  } else if (index < 0) {
    direction = 1;
    setTimeout(typeLoop, 500); // pause before retyping
  } else {
    setTimeout(typeLoop, 300); // typing speed
  }
}

typeLoop();

});

