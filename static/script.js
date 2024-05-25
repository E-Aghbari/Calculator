const display = document.getElementById('numero');
const container = document.getElementById('button-container');
const backSpace = document.getElementById('backspace');
const form = document.getElementById('calculator-form');
const decimalButton = document.getElementById('decimal');


form.addEventListener('submit', function(event) {
  event.preventDefault(); // Prevent the traditional form submission which reloads the page.
  
  // Create a new XMLHttpRequest
  const xhr = new XMLHttpRequest();
  
  // Configure it: GET-request for the URL /calculate with parameter equation=...
  xhr.open('POST', '/', true);
 

  xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
 

  // Set up a function that is called when the request is completed
  xhr.onload = function () {
    if (xhr.status >= 200 && xhr.status < 300) {
      // This is the response from server
      console.log(xhr.responseText);
      display.value = xhr.responseText;
    } else {
      console.error('The request failed!');
    }
  };

  // Sending data to server
  xhr.send('equation=' + encodeURIComponent(display.value));
  
});


container.addEventListener('click', function(event) {
 
  if (event.target.name === "number") {

    if(display.value === '0' ){
      display.value = ''
    }
    display.value = display.value + event.target.value;
  } else if (event.target.name === "operator") {
    display.value = display.value + event.target.value;
    decimalButton.disabled = false;
  } else if (event.target.name == 'decimal'){
    display.value = display.value + event.target.value;
    decimalButton.disabled = true;

  }
})



backSpace.addEventListener('click', () => {
  const field = display.value;
  display.value = field.substring(0, field.length - 1)
  decimalState();
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

function decimalState(){
  const numbers = display.value.split(/[\+\-\*\/]/);
  const currentNumber = numbers.pop();

  if (currentNumber.includes('.')){
    decimalButton.disabled = true;
  } else {
    decimalButton.disabled = false;
  }
}
