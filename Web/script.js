/* Variable declarations and conditionals (Part 1) */
let number1 = 10;
let number2 = 20;
let result;
if (number1 > number2) {
  result = "Number 1 is greater than Number 2";
} else if (number1 < number2) {
  result = "Number 1 is less than Number 2";
}
console.log(result);

/**At least 3 DOM interactions with function */
function clicked1() {
  const email = document.getElementById("email");
  const container = document.querySelector(".container");

  email.value = "habtamu@gmail.com";
  email.style.backgroundColor = "rgb(9, 136, 94)";
  container.style.backgroundColor = "rgb(9, 136, 94)";
  container.style.color = "white";
}

/**At least 2 custom functions (Part 2) with loops,  */
/**Loop with for loop  */
function clicked2() {
  for (let i = 0; i < number1; i++) {
    console.log("Loop iteration: " + i);
  }
}
function clicked3() {
  const hideShowElement = document.getElementById("hideshow");
  if (hideShowElement.style.display === "none") {
    hideShowElement.style.display = "block";
  } else {
    hideShowElement.style.display = "none";
  }
  /**Loop with while loop  */
  result = number1 ** number2;
  console.log("Result of exponentiation: " + result);
  while (number1 > 0) {
    console.log("Decrementing number1: " + number1);
    number1--;
  }
}
