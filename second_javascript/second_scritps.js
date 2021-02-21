document.addEventListener("DOMContentLoaded", function () {
  let firstName = "London";
  let lastName = "Tipton";
  let fullName = "My full name is " + firstName + " " + lastName + ".";
  let templateLiteralFullName = `My full name is ${firstName} ${lastName}.`;
  console.log("Concatenated: " + fullName);
  console.log(`Literal: ${templateLiteralFullName}`);

  let paras = document.getElementsByTagName("p");
  console.log(paras);
  console.log(paras[4]);

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
  // BODMAS
  console.log("1 + 1 = " + (1 + 1));
  console.log("2 * 5 = " + 2 * 5);
  console.log("5 * 5 + 5 = " + (5 * 5 + 5));
  console.log("(5 + 5) * 5 = " + (5 + 5) * 5);

  let x = 6;
  let y = 10;
  let z = x * y;
  console.log("z = " + z);
  console.log("z++ = " + z++);
  console.log("z-- = " + z--);

  let a = 1;
  a += 2;
  console.log("a = " + a);
  a *= 3;
  console.log("a = " + a);
  a -= 1;
  console.log("a = " + a);
  a %= 3;
  console.log("a = " + a);
});
