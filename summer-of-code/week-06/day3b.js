const PI = 3.141592653589793;
// PI = 3.14;      // This will give an error
// PI = PI + 10;   // This will also give an error

var x = 10;
// Here x is 10
{
    const x = 2;
    // Here x is 2
}
// Here x is 10
console.log(x)

// You can create a const object:
const mentor = {language:"JavaScript", yearsExp:"5", mentExp:"1"};

// You can change a property:
mentor.yearsExp = "8";

// You can add a property:
mentor.codeReviewFreq = "Monthly";

console.log(mentor)

// mentor = {type:"Volvo", model:"EX60", color:"red"};    // ERROR


{
    let x = 2;
    console.log('I am x in block scope', x)
}

console.log('I am x in global scope', x)














