/*
 * Hours in a year. How many hours are in a year?
 */
var result1 = 365*24;
document.querySelector("#q1").innerHTML = result1
/*
 * Minutes in a decade. How many minutes are in a decade?
 */
var result2 = 10*365*24*60;
document.querySelector("#q2").innerHTML = result2
/*
 * Your age in seconds. How many seconds old are you?
 */
var result3 = 48*365*24*60*60;
document.querySelector("#q3").innerHTML = result3
/*
 * Cristina Tarantino: 32 yesterday! How many milliseconds old is she?
 */
var result4 = 32*365*24*60*60*1000;
document.querySelector("#q4").innerHTML = result4
/*
 * How many days does it take for a 32-bit system to timeout, if it has a bug with integer overflow?
 */
var result5 = Math.round((Math.pow(2,31)-1)/60/60/24);
document.querySelector("#q5").innerHTML = result5
/*
 * How about a 64-bit system?
 */
var result6 = Math.round((Math.pow(2,63)-1)/60/60/24);
document.querySelector("#q6").innerHTML = result6
/*
 * Calculate your age accurately based on your birthday 
 * (maybe use time of day e.g. 8:23am if you know it, use 12:00 noon midday)
 */
var today = new Date();
var birthDate = new Date("1970/07/06");
var age = today.getFullYear() - birthDate.getFullYear();
var m = today.getMonth() - birthDate.getMonth();
    if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
        age--;
    }
var d = today.getDate() - birthDate.getDate();
    if (d < 0 || (d === 0 && today.getDate() < birthDate.getDate())) {
        m--;
    }

document.querySelector("#q7y").innerHTML = age;
document.querySelector("#q7m").innerHTML = m;
document.querySelector("#q7d").innerHTML = d;
/*
 * Music
 * A 440 Hz
 * 1 octave is double the frequency
 * tempered piano
 * A' 880 Hz
 * Calculate and console.log the frequency each of the 12 notes between A and A'
 * Hint: the notes are NOT in a linear scale, but in a geometric scale
 */
 
var notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "H"];
var frequency = [440,0,0,0,0,0,0,0,0,0,0,0];
var i=1;
while (i<notes.length){
    frequency[i]=Math.round(440*Math.pow(2,i/12));
    i++;
} 
document.querySelector("#q8A1").innerHTML = frequency[1];
document.querySelector("#q8B").innerHTML = frequency[2];
document.querySelector("#q8C").innerHTML = frequency[3];
document.querySelector("#q8C1").innerHTML = frequency[4];
document.querySelector("#q8D").innerHTML = frequency[5];
document.querySelector("#q8D1").innerHTML = frequency[6];
document.querySelector("#q8E").innerHTML = frequency[7];
document.querySelector("#q8F").innerHTML = frequency[8];
document.querySelector("#q8F1").innerHTML = frequency[9];
document.querySelector("#q8G").innerHTML = frequency[10];
document.querySelector("#q8G1").innerHTML = frequency[11];

/*
 * Planets
 * Calculate and console log how many 'minutes' the Moon travels in a day.
 * Hint: first calculate how many degrees the Moons travels in the sky when 
 * the Earth returns to the same position during its daily rotation.
 * calculation: 360 / 24*60 (minutes/day) = 13.2 / x
 */
document.querySelector("#q9").innerHTML = 13.2*24*60/360;

/*
 * Full name greeting. 
 *Write a program that asks for a person’s first name, then middle, and then last. 
 *Finally, it should greet the person using their full name.
 */
var name = prompt("Please enter your name:");
var middle = prompt("Please enter your middle name:");
var last = prompt("Please enter your last name:");
document.querySelector("#q10").innerHTML = name + " " + middle  + " " + last

/*
 *Bigger, better favorite number.</br> 
 *Write a program that asks for a person’s favorite number. 
 *Have your program add 1 to the number, and then suggest the result as a bigger and 
 *better favorite number. (Do be tactful about it, though.)
*/
var number = prompt("Enter your favorite number:");
var better = parseInt(number) + 1
alert('This is a better number: ' + better)

/*
Angry boss. Write an angry boss program that rudely asks what you want. 
Whatever you answer, the angry boss should yell it back to you and then fire you. 
For example, if you type in I want a raise, it should yell back like this: 
```
WHADDAYA MEAN "I WANT A RAISE"?!? YOU'RE FIRED!!
``` 
*/
var say = prompt("What did you say?");
alert('WHADDAYYA MEAN \"' + say.toUpperCase() + "\"?!? YOU'RE FIRED!!");

/*
Generate table of content 
*/
function myFunction() {
    document.getElementById("title").style.textAlign = "center";
    document.getElementById("ch1").style.textAlign = "left";
    document.getElementById("pg1").style.textAlign = "right";
    document.getElementById("ch2").style.textAlign = "left";
    document.getElementById("pg2").style.textAlign = "right";
    document.getElementById("ch3").style.textAlign = "left";
    document.getElementById("pg3").style.textAlign = "right";
}


/*
- Generate a random number 
    - between 1 and 10
    - between 1 and 100
    - between 1930 and 1950
*/

document.querySelector("#rand1").innerHTML = Math.floor(Math.random() * 10 + 1);
document.querySelector("#rand2").innerHTML = Math.floor(Math.random() * 100 + 1);

function selectFrom(lowerValue, upperValue) {
    var choices = upperValue - lowerValue + 1;
    return Math.floor(Math.random() * choices + lowerValue);
}
document.querySelector("#rand3").innerHTML = selectFrom(1930, 1950);

