document.addEventListener("DOMContentLoaded", function () {
  console.log("Hello World!");

  for (let num = 5; num < 11; num++) {
    console.log(num);
  }

  const items = ['apricot', 'banana', 'cherry'];
 
  for (let i = items.length - 1; i >= 0; i--) {
    console.log(`${i}. ${items[i]}`);
  }
   
  // Prints: 2. cherry
  // Prints: 1. banana
  // Prints: 0. apricot


















});
