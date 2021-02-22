document.addEventListener("DOMContentLoaded", function () {
  /****************************************************************************************************/

  let firstName = "London";
  let lastName = "Tipton";
  let fullName = "My full name is " + firstName + " " + lastName + ".";
  let templateLiteralFullName = `My full name is ${firstName} ${lastName}.`;
  console.log("Concatenated: " + fullName);
  console.log(`Literal: ${templateLiteralFullName}`);

  /****************************************************************************************************/

  let paras = document.getElementsByTagName("p");
  console.log(paras);
  console.log(paras[4]);

  /****************************************************************************************************/

  let crispFlavours = [
    "Smokey Bacon",
    "Prawn Cocktail",
    "Salt and Vinegar",
    "Ready Salted",
  ];
  console.log(crispFlavours);
  console.log(crispFlavours.length);
  console.log(crispFlavours.sort());
  console.log(crispFlavours.join(" & "));
  console.log(crispFlavours.reverse());
  console.log(crispFlavours.reverse());
  console.log(crispFlavours.reverse());

  /****************************************************************************************************/

  // BODMAS
  console.log("1 + 1 = " + (1 + 1));
  console.log("2 * 5 = " + 2 * 5);
  console.log("5 * 5 + 5 = " + (5 * 5 + 5));
  console.log("(5 + 5) * 5 = " + (5 + 5) * 5);

  /****************************************************************************************************/

  let x = 6;
  let y = 10;
  let z = x * y;
  console.log("z = " + z);
  console.log("z++ = " + z++);
  console.log("z-- = " + z--);

  /****************************************************************************************************/

  let a = 1;
  a += 2;
  console.log("a = " + a);
  a *= 3;
  console.log("a = " + a);
  a -= 1;
  console.log("a = " + a);
  a %= 3;
  console.log("a = " + a);

  /****************************************************************************************************/

  let first = 6;
  let second = 7;
  if (first === second) {
    console.log("same value and type");
  } else {
    console.log("not same at all!");
  }
  console.log(`first is: ${first} and second is: ${second}.`);

  /****************************************************************************************************/

  let third = 20;
  let fourth = 20;
  if (third !== fourth) {
    console.log("diff nums.");
  } else {
    console.log("numbers same!");
  }
  console.log(`third is: ${third} and fourth is: ${fourth}.`);

  /****************************************************************************************************/

  let twenty = 20;
  let stringTwenty = "20";
  if (twenty == stringTwenty) {
    console.log("same but loosely...");
  }
  if (twenty === stringTwenty) {
    console.log("strictly the same!");
  } else {
    console.log("strictly NOT the same!");
  }
  let firstNumber = 100;
  let secondNumber = 11;
  if (firstNumber < secondNumber) {
    console.log("firstNumber is smaller than secondNumber.");
  } else {
    console.log("firstNumber is bigger than secondNumber.");
  }

  /****************************************************************************************************/

  let date = new Date();
  let dayIndexNum = date.getDay();
  console.log(`date: ${date}`);
  console.log(`dayIndexNum: ${dayIndexNum}`);
  let ukLegalAge = 18;
  let message;
  switch (ukLegalAge) {
    case 3:
      message = "you are not old enough to drink";
      break;
    case 15:
      message = "you are STILL not old enough to drink";
      break;
    case 18:
      message = "you ARE old enough to drink";
      break;
    default:
      message = "you have no human age";
      break;
  }
  console.log(message);

  /****************************************************************************************************/

  let blue = "primary colour";
  let red = "primary colour";
  let yellow = "primary colour";
  let green = "secondary colour";
  let orange = "secondary colour";
  let purple = "secondary colour";
  let purpleRed = "tertiary colour";
  let yellowGreen = "tertiary colour";
  let orangeBlue = "tertiary colour";
  let white = "white colour";
  let black = "black colour";
  let description;
  switch (red) {
    case "primary colour":
      description = "This is a primary colour.";
      break;
    case "secondary colour":
      description = "This is a secondary colour.";
      break;
    case "tertiary colour":
      description = "This is a tertiary colour.";
      break;
    case "white colour":
      description = "This is colour is white.";
      break;
    case "black colour":
      description = "This is colour is black.";
      break;
    default:
      description = "This is NOT a colour.";
      break;
  }
  console.log(`description: ${description}`);

  /****************************************************************************************************/

  let primaryColour = "primary colour";
  let secondaryColour = "secondary colour";
  let tertiaryColour = "tertiary colour";
  let colourEgs;
  switch ("tertiary colour") {
    case primaryColour:
      colourEgs = "blue, yellow, red";
      break;
    case secondaryColour:
      colourEgs = "orange, green, purple";
      break;
    case tertiaryColour:
      colourEgs = "red-purple, green-blue, orange-yellow";
      break;
    default:
      colourEgs = "not a colour example";
      break;
  }
  console.log(`colour examples: ${colourEgs}`);

  /****************************************************************************************************/

  let colourList = [
    "blue", // 0
    "red", // 1
    "yellow", // 2
    "orange", // 3
    "green", // 4
    "purple", // 5
    "yellow-green", // 6
    "purple-blue", // 7
    "red-orange", // 8
    "white", // 9
    "black", // 10
  ];
  let group;
  switch (colourList[1]) {
    case "blue":
    case "red":
    case "yellow":
      group = "This colour belongs to the PRIMARY colour group!";
      break;
    case "orange":
    case "green":
    case "purple":
      group = "This colour belongs to the SECONDARY colour group!";
      break;
    case "yellow-green":
    case "purple-blue":
    case "red-orange":
      group = "This colour belongs to the TERTIARY colour group!";
      break;
    case "white":
    case "black":
      group = "This colour either is black OR white!";
      break;
    default:
      group = "This is not a in the colour array!";
      break;
  }
  console.log(`Statement: ${group}`);
  let groupIndexing;
  switch (colourList.indexOf("orange")) {
    case 0:
    case 1:
    case 2:
      groupIndexing = "PRIMARY";
      break;
    case 3:
    case 4:
    case 5:
      groupIndexing = "SECONDARY";
      break;
    case 6:
    case 7:
    case 8:
      groupIndexing = "TERTIARY";
      break;
    case 9:
    case 10:
      groupIndexing = "Black or White";
      break;
    default:
      groupIndexing = "This is not a in the colour array!";
      break;
  }
  console.log(`New Statement: ${groupIndexing}`);

  /****************************************************************************************************/

  let drinkingAge = 12;
  drinkingAge <= 18
    ? console.log("too young to drink!")
    : console.log("old enough to drink!");
  let votingAge = 17;
  votingAge >= 18
    ? console.log("old enough to vote")
    : console.log("not old enough to vote!");
  let personAge = 26;
  personAge <= 0
    ? console.log("newborn")
    : personAge > 0 && personAge <= 5
    ? console.log("toddler")
    : personAge >= 6 && personAge <= 10
    ? console.log("child")
    : personAge >= 11 && personAge <= 12
    ? console.log("pre-teen")
    : personAge >= 13 && personAge <= 17
    ? console.log("teen")
    : personAge >= 18 && personAge <= 30
    ? console.log("young adult")
    : personAge >= 31 && personAge <= 70
    ? console.log("old adult")
    : console.log("elder");

  /****************************************************************************************************/

  let studentOne = 70;
  let studentTwo = 55;
  let bestStudentScore =
    studentOne > studentTwo
      ? `student one has the better score with: ${studentOne}%`
      : `student two has the better score with: ${studentTwo}%`;
  console.log(bestStudentScore);

  /****************************************************************************************************/

  let startNum = 0;
  while (startNum < 10) {
    console.log(`${startNum} is less than 10.`);
    startNum++;
  }

  /****************************************************************************************************/

  let foodArray = ["pizza", "burger", "chips", "noodles", "fish", "chicken"];
  let foodList = document.getElementById("foodList");
  let text = "";
  foodList.addEventListener("click", function () {
    let i = 0;
    while (i < foodArray.length) {
      text = foodArray[i];
      console.log(text);
      i++;
    }
  });

  /****************************************************************************************************/

  for (let i = 0; i < 101; i++) {
    if (i === 57) {
      break;
    }
    console.log(i);
  }

  /****************************************************************************************************/

  let namesArray = [
    "viv",
    "ann",
    "sam",
    "bob",
    "kim",
    "computer",
    "keys",
    "lamp",
    "nails",
  ];
  for (let i = 0; i < namesArray.length; i++) {
    if (namesArray[i] === "computer") {
      break; // stops at computer ie shows up till kim
    }
    console.log(namesArray[i]);
  }

  /****************************************************************************************************/

  let furniture = [
    "chair",
    "table",
    "cupboard",
    "bed",
    "sofa",
    "tv",
    "lemonade", // continue; skips past this one
    "sink",
    "washing machine",
    "cooker",
    "dish washer",
    "oven",
  ];
  for (let i = 0; i < furniture.length; i++) {
    if (furniture[i] === "lemonade") {
      continue;
    }
    console.log(furniture[i]);
  }

  /****************************************************************************************************/

  function multiplyNums(firstNum, secondNum) {
    return console.log(firstNum * secondNum);
  }
  multiplyNums(10, 5);

  function divideNums(numOne, numTwo) {
    return console.log(numOne / numTwo);
  }
  divideNums(200, 200);

  let adding = function addingNums(num1, num2) {
    return console.log(num1 + num2);
  };
  console.log(adding);
  adding(1, 59);

  let subtracting = function subtractNums(first, second) {
    return first - second;
  };
  let times100 = subtracting(10, 2) * 100;
  console.log(times100);

  function allAlphabet(a, b, c, d, e, f, g, h) {
    return arguments.length;
  }
  console.log(allAlphabet(3, 3, 3, 3));

  function allAlphabet2() {
    return arguments.length;
  }
  console.log(allAlphabet2(3, 3));

  function tooFew(a, b) {
    if (b === undefined) {
      b = 2;
    }
    return a + b;
  }
  console.log(tooFew(8));

  function tooMany(a, b, c, d) {
    return a + b + c + d;
  }
  console.log(tooMany(2, 2, 2, 2, 2, 2, 2));

  function findMax() {
    let max = -Infinity;
    for (let i = 0; i < arguments.length; i++) {
      if (arguments[i] > max) {
        max = arguments[i];
      }
    }
    return max;
  }
  final = findMax(1, 234, 500, 6789);
  console.log(final);

  let maxNum = Math.max(1, 234, 500, 6789, 0.1, 1234567);
  console.log(maxNum);

  function sumAll() {
    let sum = 0;
    for (let i = 0; i < arguments.length; i++) {
      sum += arguments[i];
    }
    return sum;
  }

  let total = sumAll(2, 2, 2, 2, 2);
  console.log(total);

  let myObject = {
    firstName: "jon",
    lastName: "smith",
    fullName: function () {
      return `My name is ${this.firstName} ${this.lastName}. Nice to meet you!`;
    },
  };
  console.log(myObject);
  console.log(myObject.firstName);
  console.log(myObject.lastName);
  console.log(myObject.fullName());

  let myObject2 = {
    firstName: "ken",
    lastName: "doodle",
    fullName: function () {
      return `Hello! My name is ${this.firstName} ${this.lastName}. Nice to meet you!`;
    },
  };
  console.log(myObject2);
  console.log(myObject2.firstName);
  console.log(myObject2.lastName);
  console.log(myObject2.fullName());

  /****************************************************************************************************/

  let myNonNumber = "55p";
  let myNumber = Number(myNonNumber);
  myNumber += 1;
  console.log(myNumber);
  console.log(typeof myNumber);

  /****************************************************************************************************/

  let aa = 10.1;
  let b = 29;
  let c = 78;

  console.log(Math.round(aa));
  console.log(Math.max(aa, b, c));
  console.log(Math.min(aa, b, c));

  let d = 34.0;
  let e = 34;
  console.log(d);
  console.log(e);

  let f = 0xbcde18;
  console.log(f);

  let g = 0.2 + 0.1;
  console.log(g);

  let h = (0.2 * 10 + 0.1 * 10) / 10;
  console.log(h);

  let i = "string";
  if (isNaN(i)) {
    console.log("this is not a number!");
  }

  let j = isNaN("this should show up as true");
  console.log(j);

  let k = isNaN(96);
  console.log(k);

  console.log(Math.floor(Math.random() * 12));

  console.log(Math.max(1, 2, 3, 4, 5));
  console.log(Math.floor(9.7));
  console.log(Math.ceil(9.1));
  console.log(Math.round(9.5));
  console.log(Math.PI);
  console.log(Math.sqrt(9));
  console.log(Math.cbrt(64));
  console.log(Math.pow(4, 4));
  console.log(Math.SQRT2); // square root of 2
  console.log(Math.SQRT1_2); // square root of 0.5

  console.log(Number.MAX_VALUE);
  console.log(Number.MIN_VALUE);

  let l = 56789;
  let m = l.toString();
  console.log(m);
  console.log(typeof m);
  let n = 8.66499416;
  let o = n.toFixed(1);
  console.log(o);

  /****************************************************************************************************/
});
