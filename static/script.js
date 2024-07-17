const display = document.getElementById('numero');
const container = document.getElementById('button-container');
const backSpace = document.getElementById('backspace');
const form = document.getElementById('calculator-form');
const decimalButton = document.getElementById('decimal');
let expression = '';
let operator;
let longClick;


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
      //display.value = xhr.responseText;
      display.value = xhr.responseText;
    } else {
      console.error('The request failed!');
    }
  };

  // Sending data to server
  xhr.send('equation=' + encodeURIComponent(expression));
  
});


container.addEventListener('click', function(event) {
  if (event.target.name === "number") {

    if(display.value === '0' ){
      display.value = ''
    }

    display.value = display.value + event.target.value;
    expression = expression + event.target.value;
    if (operator != null){
      operator.disabled = false;
      operator = null;
    }
  } else if (event.target.name === "operator") {

    if (operator != null){
      operator.disabled = false;
      expression = expression.substring(0, expression.length - 1)
    }

    operator = event.target;
    operator.disabled = true;

    display.value = ''
    expression = expression + event.target.value;
    decimalButton.disabled = false;
  } else if (event.target.name == 'decimal'){
    display.value = display.value + event.target.value;
    expression = expression + event.target.value;
    decimalButton.disabled = true;

  }
})



backSpace.addEventListener('mousedown', () => {
  
  let mouseTimer;
  mouseTimer = setTimeout( () => {
    if (backSpace.onmousedown = true) { 
      longClick = true;
      resetCalculator();
    }
  }, 500 );


  document.body.addEventListener('mouseup', () => {
    if (mouseTimer) clearTimeout(mouseTimer)
  });
})

backSpace.addEventListener('click', () => {
  if (longClick) {
    longClick = false;
    return;
  }

  const field = display.value;
  display.value = field.substring(0, field.length - 1)
  expression = expression.substring(0, expression.length - 1)
  decimalState();
  if (display.value === ''){
    display.value = '0';
  }
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

function resetCalculator(){
  display.value = '0';
  expression = '';
  decimalState()

  if (operator != null){
  operator.disabled = false;
  }
}