var nameCond, ageCond, heightCond, petCond;
var firstName = prompt("Your NAME, sir: ");
var lastName = prompt("Just the last plix: ");
var age = prompt("You old or a gamer?");
var height = prompt("Big boi? How tall?");
var petName = prompt("What do the beebs call you?");
alert("Thanks man, we're processing your beastliness");

nameCond = (firstName[0] === lastName[0]);
ageCond = (age > 20 && age < 30);
heightCond = (height >= 170);
petCond = (petName[petName.length - 1] === "y");

if (nameCond && ageCond && heightCond && petCond) {
  console.log("YOU ARE A BEAST!!");
} else {
  console.log("Leave, Norman.");
}
