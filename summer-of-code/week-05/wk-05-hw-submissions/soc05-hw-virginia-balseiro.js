// Basic Exercises for Certification (REQUIRED):

// Write a program that tells you the following:
console.log('Hello Ladies!');
// Hours in a year. How many hours are in a year?
console.log('There are ' + 365*24 + ' hours in a year.');
// Minutes in a decade. How many minutes are in a decade?
console.log('There are ' + 60*24*365*10 + ' minutes in a decade.');
// Your age in seconds. How many seconds old are you? (I'm not going to check your answer, so be as accurate—or not—as you want.)
console.log('I am approximately ' + 60*60*24*365*32 + ' seconds old.')
// Cristina Tarantino: 32 yesterday! How many milliseconds old is she hahaha? Calculate @Cristina Tarantino's age in milliseconds.
console.log('Cristina is approximately ' + 1000*60*60*24*365*32 + ' milliseconds old.')


// Here are some tougher questions (OPTIONAL):


// Calculate your age accurately based on your birthday (maybe use time of day e.g. 8:23am if you know it, use 12:00 noon midday) - you will need JavaScript DateTime functionality.
today = Date.now();

birthday = new Date('May 12, 1986 11:00:00');
milliseconds = today - birthday.getTime();
console.log('My accurate age in milliseconds is ' + milliseconds);
console.log('My accurate age in seconds is ' + Math.round(milliseconds/1000));
console.log('My accurate age in minutes is ' + Math.round(milliseconds/1000/60));
console.log('My accurate age in hours is ' + Math.round(milliseconds/1000/60/60));
console.log('My accurate age in years is ' + (milliseconds/1000/60/60/24/365).toFixed(2));

// Few things to try (REQUIRED):

// Music A 440 Hz 1 octave is double the frequency tempered piano A' 880 Hz Calculate and console.log the frequency each of the 12 notes between A and A' Hint: the notes are NOT in a linear scale, but in a geometric scale
// fn = f0 * (a)n 
// where
// f0 = the frequency of one fixed note which must be defined. A common choice is setting the A above middle C (A4) at f0 = 440 Hz.
// n = the number of half steps away from the fixed note you are. If you are at a higher note, n is positive. If you are on a lower note, n is negative.
// fn = the frequency of the note n half steps away.
// a = (2)1/12 = the twelth root of 2 = the number which when multiplied by itself 12 times equals 2 = 1.059463094359... 
var f0 = 440;
var a = Math.pow(2, 1/12);
console.log("Musical notes frequency: ")
console.log("A4: " + (f0 * Math.pow(a, 1)).toFixed(2));
console.log("A#4/Bb4: " + (f0 * Math.pow(a, 2)).toFixed(2));
console.log("B4: " + (f0 * Math.pow(a, 3)).toFixed(2));
console.log("C5: " + (f0 * Math.pow(a, 4)).toFixed(2));
console.log("C#5/Db5: " + (f0 * Math.pow(a, 5)).toFixed(2));
console.log("D5: " + (f0 * Math.pow(a, 6)).toFixed(2));
console.log("D#5/Eb5: " + (f0 * Math.pow(a, 7)).toFixed(2));
console.log("E5: " + (f0 * Math.pow(a, 8)).toFixed(2));
console.log("F#5/Gb5: " + (f0 * Math.pow(a, 9)).toFixed(2));
console.log("G5: " + (f0 * Math.pow(a, 10)).toFixed(2));
console.log("G#5/Ab5: " + (f0 * Math.pow(a, 11)).toFixed(2));
console.log("A5: " + (f0 * Math.pow(a, 12)).toFixed(2));


// Planets Calculate and console log how many 'minutes' the Moon travels in a day. Hint: first calculate how many degrees the Moons travels in the sky when the Earth returns to the same position during its daily rotation.

//sidereal period of revolution: 27.3 days - time it takes the moon to move around earth in circular orbit
//circle orbit : 360 degrees
// degrees traveled by moon in 1 day: circle orbit / sidereal period of revolution
// minutes: 1 degree = 60 minute of arc - minutes = degrees * 60
var siderealPeriod = 27.3;
var circleOrbit = 360;
var degreesTraveled = (circleOrbit / siderealPeriod).toFixed(1);

var minutesTraveled = degreesTraveled * 60;

console.log('The moon travels ' + degreesTraveled + ' degrees per day, which is ' + minutesTraveled + ' minutes.');

var earthSpeed = 360/24/60;
console.log('It takes the Earth ' + degreesTraveled/earthSpeed + ' minutes to catch up with the moon!')


// A Few Things to Try
// Full name greeting. Write a program that asks for a person’s first name, then middle, and then last. Finally, it should greet the person using their full name.
var first = prompt("Type in your first name and press Enter key.");
first = first.charAt(0).toUpperCase() + first.substr(1);
var middle = prompt("Type in your middle name and press Enter key (if you don't have one, just press Enter key).");
middle = middle.charAt(0).toUpperCase() + middle.substr(1);
var last = prompt("Type in your last name and press Enter key.");
last = last.charAt(0).toUpperCase() + last.substr(1);
var greeting = document.getElementById("greeting");
if (middle != undefined) {
	greeting.innerHTML = "Hello " + first + " " + middle + " " + last + "!";
}
else {
	greeting.innerHTML = "Hello " + first + " " + last + "!";
}

// Bigger, better favorite number. Write a program that asks for a person’s favorite number. Have your program add 1 to the number, and then suggest the result as a bigger and better favorite number. (Do be tactful about it, though.)
var favNum = parseInt(prompt("Type in your favorite number"));
var favNumDiv = document.getElementById("favNum");
favNumDiv.innerHTML = "I think " + (favNum + 1) + " is a better favorite number for you!";


// A Few Things to Try
// Angry boss. Write an angry boss program that rudely asks what you want. Whatever you answer, the angry boss should yell it back to you and then fire you. For example, if you type in I want a raise, it should yell back like this:
// WHADDAYA MEAN "I WANT A RAISE"?!? YOU'RE FIRED!!

var message = prompt("WHAT DO YOU WANT?!?");
console.log("WHADDAYA MEAN " + '"' + message.toUpperCase() + '"' + "?!? YOU'RE FIRED!!")

// Table of contents. Here’s something for you to do in order to play around more with center, ljust, and rjust: write a program that will display a table of contents so that it looks like this:
// Table of Contents

// Chapter 1: Getting Started page 1 Chapter 2: Numbers page 9 Chapter 3: Letters page 13

// Optional: in JS we may prefer to 'print' these to the HTML file itself rather than the console.

contents = document.getElementById("contents");
contents.innerHTML = "<tr align='center'><th>Table of Contents</th></tr>" +
					 "<tr><td align='left'>Chapter 1: Getting Started</td><td align='right'>page 1</td></tr>" + 
					 "<tr><td align='left'>Chapter 2: Numbers</td><td align='right'>page 9</td></tr>" + 
					 "<tr><td align='left'>Chapter 3: Letters</td><td align='right'>page 13</td></tr>";

// Higher Math - Optional
// More Arithmetic - Optional
// ** pow(base, power) 365%7 abs(-7)

// Random Numbers - Optional
// Research how to generate a random number with JavaScript. (Math.random() will output a random number from 0 up to but not including 1)

// Generate a random number
// between 1 and 10
// between 1 and 100
// between 1930 and 1950
// Optional:

function getRandomNumber(min, max) {
	min = Math.ceil(min);
	max = Math.floor(max);
	return Math.floor(Math.random() * (max-min)) + min;
}

console.log("Random number between 1 and 10: " + getRandomNumber(1, 10));
console.log("Random number between 1 and 100: " + getRandomNumber(1, 100));
console.log("Random number between 1930 and 1950: " + getRandomNumber(1930, 1950));
// Then try to generate your random Civilization III world by generating a land 'X' tile or a water 'o' tile randomly:

// oooXXXoo
// oooXoXoo
// XXXooXoo

//Random n*n world:
var M = 'land';
var o = 'water';

function getRandomIntInclusive(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min; //The maximum is inclusive and the minimum is inclusive 
}

function randomWorld(n, a, b){
  var options = [a, b]
  var board = []
  for (var i=0; i<n; i++){
    board.push([])
  }
  for (var x = 0; x < board.length; x++) {
    for (var i = 0; i < n; i++){
      board[x].push(options[getRandomIntInclusive(0, 1)])
    //console.log(board[x])
    }
  }

  console.log(board)
  return board;
}

var world = randomWorld(11, M, o);

function printWorldItems() {
  console.log("Print board:")
  for (var i = 0; i < world.length; i++){
    for (var n = 0; n < world[i].length; n++) {
      console.log(world[i][n])
    }
  }
}

// A Few Things to Try
// “99 Bottles of Beer on the Wall.” Write a program that prints out the lyrics to that beloved classic, “99 Bottles of Beer on the Wall.”
for (var b = 99; b >= 0; b--){
	if (b == 1) {
		console.log(b + " bottle of beer on the wall, " + b + " bottle of beer, take it down, pass it around, no more bottles of beer on the wall");
	}
	else if (b == 0){
		console.log("No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall...");
	}
	else {
		console.log(b + " bottles of beer on the wall, " + b + " bottles of beer, take one down, pass it around, " + (b-1) + " bottles of beer on the wall");
	}
}
// Deaf grandma. Whatever you say to Grandma (whatever you type in), she should respond with this: HUH?! SPEAK UP, GIRL!
// unless you shout it (type in all capitals). If you shout, she can hear you (or at least she thinks so) and yells back:
// NO, NOT SINCE 1938!
// To make your program really believable, have Grandma shout a different year each time, maybe any year at random between 1930 and 1950. (This part is optional and would be much easier if you read the section on JavaScript’s random number generator under the Math Object.) You can’t stop talking to Grandma until you shout BYE.
// Hint: Try to think about what parts of your program should happen over and over again. All of those should be in your while loop.
// Hint: People often ask me, “How can I make random give me a number in a range not starting at zero?” But you don’t need it to. Is there something you could do to the number random returns to you?
// Deaf grandma extended. What if Grandma doesn’t want you to leave? When you shout BYE, she could pretend not to hear you. Change your previous program so that you have to shout BYE three times in a row. Make sure to test your program: if you shout BYE three times but not in a row, you should still be talking to Grandma.


var messageToGrandma = prompt("Talk to Grandma!");
var byeCount = 0;
while (byeCount < 3) {
	if (messageToGrandma == "BYE") {
		byeCount = byeCount+1;
	}

	if (byeCount == 3) {
	console.log("COME BACK SOON!");
	}

	else if (messageToGrandma != messageToGrandma.toUpperCase()){
		console.log("HUH?! SPEAK UP, GIRL!");
		messageToGrandma = prompt("Talk to Grandma!");
	}

	else if (messageToGrandma == messageToGrandma.toUpperCase()) {
		  var minYear = Math.ceil(1930);
  		  var maxYear = Math.floor(1950);
  		  var randomYear = Math.floor(Math.random() * (maxYear - minYear + 1)) + minYear; 
		console.log("NO, NOT SINCE " + randomYear + "!");
		messageToGrandma = prompt("Talk to Grandma!");
	}
} 


// Leap years. Write a program that asks for a starting year and an ending year and then puts all the leap years between them (and including them, if they are also leap years). Leap years are years divisible by 4 (like 1984 and 2004). However, years divisible by 100 are not leap years (such as 1800 and 1900) unless they are also divisible by 400 (such as 1600 and 2000, which were in fact leap years). What a mess!

var start = parseInt(prompt('Starting year: '));
var end = parseInt(prompt('Ending year: '));
var leapYears = [];
for (var l = start; l <= end; l++){
	if ((l % 4 == 0) || (l % 4 == 0 && l % 100 == 0 && l % 400 == 0)){
		console.log(l);
	}
} 
		


// Find something today in your life, that is a calculation. Go for a walk, look around the park, try to count something. Anything! And write a program about it. e.g. number of stairs, steps, windows, leaves estimated in the park, kids, dogs, estimate your books by bookshelf, toiletries, wardrobe.

// how many steps would a staircase need to have to reach the top of Mt. Everest?
//average step height: 17 cm (0.17 m)
var avgStep = 0.17;
var mtEvHeight = 8848;
//mount everest height: 8848 m
console.log("To climb Mt. Everest I would need to build a staircase with " + Math.floor(mtEvHeight/avgStep) + " steps.");
//Will your books fit in your new bookcase? find your thickest and your thinnest book, measure their width, measure the width of your shelf, and enter the amount of shelves and see how many books you can fit! Note: width expressed in centimeters!

var thinnestBook = parseFloat(prompt('Enter the width in centimeters of your thinnest book: '));
var thickestBook = parseFloat(prompt('Enter the width in centimeters of your thickest book: '));
var shelfWidth = parseFloat(prompt('Enter the width in centimeters of one of your shelves: '));
var numberOfShelves = parseInt(prompt('Enter how many shelves your bookcase has: '));

var avgBook = (thickestBook + thinnestBook) / 2;
var breathingRoom = avgBook * 2;
var availableWidth = shelfWidth - breathingRoom;
var result = Math.floor((availableWidth / avgBook) * numberOfShelves);
console.log('You can fit ' + result + ' books in your bookcase');

// A Few Things to Try
// Building and sorting an array. Write the program that asks us to type as many words as we want (one word per line, continuing until we just press Enter on an empty line) and then repeats the words back to us in alphabetical order. Make sure to test your program thoroughly; for example, does hitting Enter on an empty line always exit your program? Even on the first line? And the second?
// Hint: There’s a lovely array method that will give you a sorted version of an array: sorted(). Use it!
var word = prompt('Type a word: ')
var words = [];
while (word != ''){
	words.push(word);
	word = prompt();
}

words.sort();
console.log(words);

// Table of contents. Write a table of contents program here. Start the program with a list holding all of the information for your table of contents (chapter names, page numbers, and so on). Then print out the information from the list in a beautifully formatted table of contents. Use string formatting such as left align, right align, center.

var info = ['Table Of Contents', 'Chapter 1: Getting Started', 'page 1', 'Chapter 2: Numbers', 'page 9', 'Chapter 3: Letters', 'page 13'];
var contents2 = document.getElementById("contents2");

contents2.innerHTML = "<tr><th align='center'>" + info[0] + "</th></tr>" + 
					 "<tr><td align='left'>" + info[1] + "</td><td align='right'>" + info[2] + "</td></tr>" +
					 "<tr><td align='left'>" + info[3] + "</td><td align='right'>" + info[4] + "</td></tr>" +
					 "<tr><td align='left'>" + info[5] + "</td><td align='right'>" + info[6] + "</td></tr>";

// Thing to Try
// Write a function that prints out "moo" n times.

function moo(n){
	for (var m = 1; m <= n; m++){
		console.log("moo");
	}
}

moo(5);

// A Few Things to Try
// Old-school Roman numerals. In the early days of Roman numerals, the Romans didn’t bother with any of this new-fangled subtraction “IX” nonsense.
// No Mylady, it was straight addition, biggest to littlest—so 9 was written “VIIII,” and so on.

// Write a method that when passed an integer between 1 and 3000 (or so) returns a string containing the proper old-school Roman numeral. In other words, old_roman_numeral 4 should return 'IIII'. Make sure to test your method on a bunch of different numbers.

// Hint: Use the integer division and modulus methods.

// For reference, these are the values of the letters used: I = 1 V = 5 X = 10
// L = 50 C = 100 D = 500 M = 1000

function oldRomanNumeral(num){
	var newNum = [];
	var decimal = [1000, 500, 100, 50, 10, 5, 1];
	var roman = ['M', 'D', 'C', 'L', 'X', 'V', 'I'];
	for (var i = 0; i < decimal.length; i++){
		while (num % decimal[i] < num){
			newNum.push(roman[i]);
			num = num - decimal[i];
		}
	}
	console.log(newNum.join(''));	
}
oldRomanNumeral(4673); //should output MMMMDCLXXIII 


// “Modern” Roman numerals. Eventually, someone thought it would be terribly clever if putting a smaller number before a larger one meant you had to subtract the smaller one. As a result of this development, you must now suffer. Rewrite your previous method to return the new-style Roman numerals so when someone calls roman_numeral 4, it should return 'IV', 90 should be 'XC' etc.

function romanNumeral(num){
	var newNum = [];
	var decimal = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
	var roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
	for (var i = 0; i < decimal.length; i++){
		while (num % decimal[i] < num){
			newNum.push(roman[i]);
			num = num - decimal[i];
		}
	}
	console.log(newNum.join(''));
}

romanNumeral(4954); //should output MMMMCMLIV
	
