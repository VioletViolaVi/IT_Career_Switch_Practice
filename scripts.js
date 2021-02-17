document.addEventListener("DOMContentLoaded", function () {
  // gets time, day, date, etc
  function timeDayDateBtn() {
    let timeBtn = document.getElementById("timeBtn"); // gets btn
    let clearTimeBtn = document.getElementById("clearTimeBtn"); // time, day, date removal btn
    let timeBtnAnswer = document.getElementById("timeBtnAnswer"); // gets answer blank
    let todayTime = Date(); // gets time, date, day

    timeBtn.addEventListener("click", function () {
      timeBtnAnswer.innerText = todayTime; // puts time, date, day in answer blank
    });

    clearTimeBtn.addEventListener("click", function () {
      if (timeBtnAnswer.innerText === todayTime) {
        // removes time, day, date
        timeBtnAnswer.innerText = "";
      }
    });
  }
  timeDayDateBtn();

  // capitalizes input
  function changeToUpper() {
    let fname = document.getElementById("fname");

    fname.addEventListener("change", function () {
      fname.value = fname.value.toUpperCase();
    });
  }
  changeToUpper();

  // changes text colour
  function textColour() {
    let textColour = document.getElementById("textColour");

    textColour.addEventListener("click", function () {
      let hashColor = "#";
      let hexCharacters = [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
      ];

      for (let hexCharacter = 0; hexCharacter < 6; hexCharacter++) {
        hashColor +=
          hexCharacters[Math.floor(Math.random() * hexCharacters.length)];
      }

      this.style.color = hashColor;
    });
  }
  textColour();

  // changes when double clicked
  function doubleClick() {
    let doubleClickHeader = document.getElementById("doubleClickHeader");
    doubleClickHeader.addEventListener("dblclick", function () {
      this.innerText = "This header was double clicked!";
    });
  }
  doubleClick();

  // changes based on mouse interactivity
  function loremPara() {
    let loremPara = document.getElementById("loremPara");

    loremPara.addEventListener("mousedown", function () {
      this.style.color = "pink";
    });
    loremPara.addEventListener("mouseup", function () {
      this.style.color = "orange";
    });

    loremPara.addEventListener("mouseenter", function () {
      this.style.fontSize = "3em";
    }); 
    loremPara.addEventListener("mouseleave", function () {
      this.style.fontSize = "2em";
      this.style.fontWeight = "100";
    });

    loremPara.addEventListener("mousemove", function () {
      this.style.fontWeight = "900";
    });

    loremPara.addEventListener("wheel", function () {
      this.style.fontSize = "0.5em";
    });
  }
  loremPara();




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
