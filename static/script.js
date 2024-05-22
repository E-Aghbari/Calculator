const display = document.getElementById('numero');
const container = document.getElementById('button-container');
const backSpace = document.getElementById('backspace');

container.addEventListener('click', function(event) {
  if (event.target.tagName === "BUTTON") {
    display.value = display.value + event.target.value;
    console.log(display.value)
  }
})

backSpace.addEventListener('click', () => {
  let field = display.value;
  display.value = field.substring(0, field.length - 1)
})

backSpace.addEventListener('mousedown', () => {
  
  let mouseTimer;
  mouseTimer = setTimeout( () => {
    if (backSpace.onmousedown = true) {
      display.value = "";
    }
  }, 1500 );

  document.body.addEventListener('mouseup', () => {
    if (mouseTimer) clearTimeout(mouseTimer)
  });
})
