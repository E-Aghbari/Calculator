const display = document.getElementById('numero');
const container = document.getElementById('button-container');
const backSpace = document.getElementById('backspace');

container.addEventListener('click', function(event) {
  if (event.target.name === "number") {
    if(display.value === '0' ){
      display.value = ''
    }
    display.value = display.value + event.target.value;
  } else if (event.target.name === "operator") {
    display.value = display.value + event.target.value;
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
  }, 500 );

  document.body.addEventListener('mouseup', () => {
    if (mouseTimer) clearTimeout(mouseTimer)
  });
})
