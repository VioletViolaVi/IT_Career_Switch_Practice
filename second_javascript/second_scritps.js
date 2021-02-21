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
});
