document.addEventListener("DOMContentLoaded", function () {
  
  let timeBtn = document.getElementById("timeBtn"); // gets btn
  let timeBtnAnswer = document.getElementById("timeBtnAnswer"); // gets answer blank
  let todayTime = Date(); // gets time, date, day

  timeBtn.addEventListener("click", function () {
      timeBtnAnswer.innerText = todayTime; // puts time, date, day in answer blank
  });





























  // for (let num = 5; num < 11; num++) {
  //   console.log(num);
  // }

  // const items = ['apricot', 'banana', 'cherry'];

  // for (let i = items.length - 1; i >= 0; i--) {
  //   console.log(`${i}. ${items[i]}`);
  // }

  // // Prints: 2. cherry
  // // Prints: 1. banana
  // // Prints: 0. apricot
});
