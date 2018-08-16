var a = "Sara Gottschalk".length;
var b = "Bituin Callanta".length;

if (a > b) {
    console.log("They are equal in length.");

} else if (a == 20) {
    console.log("Length is twenty.");

} else if (a == 21) {
    console.log("Length is twenty-one.");

} else {
    console.log("a isn't bigger than b", a, b);
}

// var input = ''
// while (input != "bye") {
//     input = prompt()
// }
// alert('Come again soon!')


// var input = ''
// while (true) {
//     input = prompt()
//     if (input == "bye") {
//         break;
//     }
// }
// alert('Come again soon!')



// Codeshare https://codeshare.io/G6lKK0

// var i // while loop that counts number of women in #1millionwomentotech
// var i = 0;
// // while until we reach the mission of 1 million, 1 millionth woman INCLUDED

// // some nice celebration

// // @Rox
// // @Rameela

// while (i < 1000000) {
//     i = i + 1;
// }
// console.log("We have reached One million");

// // @Bituin


// // @Mara

// while (i < 1000000) {
//     input = prompt("Your name:");
//     i++;
//     alert(input, "is our wonderful wonderwoman numer:", i);
// }

// alert("Yeiii, we achieved the mission <3");

// // @Jessi_RS
// while (i <= 1000000) {
//     message = prompt("You are our wonderwoman number: ", i, "");
//     i++;
// }

// alert("")

// // @AnaSustic
// while (i <= 1000000) {
//     i++;
//     console.log("We now have" + i + "ladies in 1mwtt!");

// }
// console.log("We will celebrate now!");


// add your names into the students array
var students = ["Rocio", "Jessica Sanchez", "Rameela Azeez", "Nwamaka Okafor", "Sara Gottschalk","Mara Catalina", "Bituin Callanta", "Krystal", "Anusha Lihala", "Ana Sustic", "Rox Arten", "Angela Balyseviene", "Cristina Tarantino"
]

var student0 = students[0]
var student1 = students[1]

console.log(student0, student1)


// for loops

for (i = 0; i < 1000001; i++) {
    console.log(i)
}



// Q&A

Please put your questions/code here and I'll go through them ;)

// Mara..hehe sorry
//Than you :)
//Thank you very much :D :D , I am working with realtime Augmented reality applications
// with limited hardware and every nanosecond is supervaluable :) ..
//Which one is more efficient in terms of cpu usage?
//CT var t0 = performance.now(); //Thank you Cristina :)
if (condition){
  do somehtin
} else {}
// CT var t1 = performance.now();
// CT console.log("Call to doSomething took " + (t1 - t0) + " milliseconds.");
//or

//CT var t0 = performance.now();
var i = (condition ) ? if true : if false
// CT var t1 = performance.now();
// CT console.log("Call to doSomething took " + (t1 - t0) + " milliseconds.");

// https://developer.mozilla.org/en-US/docs/Web/API/Performance/now

//A: (Ilona) I don't know but we can benchmark it.
//e.g. run both 1 million times, and take system time at the beginning and end to compare.
// https://stackoverflow.com/questions/2586842/is-ternary-operator-if-else-or-logical-or-faster-in-javascript
// Note that the ternary operator is usually used for single, short statements
// and is mostly so as to help a human reader

//Marta
//BOUT THE FOR LOOPS- Which difference makes if I declare the variable in the loop or outside?
//The variable will be accessed just in the loop or it can be accessed from the rest of the program as well?
//So which one is better in terms of programming? which one will be more clean?
//sorry, no code..still a beginner!
// https://stackoverflow.com/questions/3684923/javascript-variables-declare-outside-or-inside-loop

var i = 0
for (; i < 10; i++) {
  console.log(i)
}

for (i = 0; i < 10; i++) {
  console.log(i)
}

var i = 0;
var j = "a";
var food = ["cake"]
for (; i < 10; i++) {
  console.log(i);
  j += i;
  food.push(j);
}

for (i = 0, j = "a", food = ["cake"]; i < 10; i++) {
  console.log(i)
  j += i;
  food.push(j);
}


// WARNING this is an ADVANCED question, it is NOT for beginners ;)
//
//
//
// Anusha
//Is there a 'for element in array' syntax in JS?

// for-in to iterate objects https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in
// for-of ES6 to iterate arrays https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of
// forEach to iterate arrays https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach
var array1 = ['a', 'b', 'c'];

array1.forEach(function(element) {
  console.log(element);
});

// for-of is extremely efficient

var student = {
  fname: "Anusha",
  lname: "Lihala",
  favFood: "pizza"
}

for (prop in student) {
  console.log(student[prop])
}

//A (Ilona): for, map, reduce
// for forEach, for in, for at
// map and reduce implemented underscore JS library

// map https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map
// reduce https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce

















