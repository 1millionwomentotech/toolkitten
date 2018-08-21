/* If you're feeling fancy you can add interactivity
    to your site with Javascript */

// prints "hi" in the browser's dev tools console
console.log('hi');
console.log('hallo:)')
console.log('glasses "show button" left top corner and console there + f12, or open console')

// write your own anonymous function example here,
// and either console.log or place on the HTML into your own <p id="yourname">

// @Ilona
// callbacks
var sisters = ["Virginia", "Camen", "Mara", "Krystal", "Priya"]

sisters.forEach (function (eachName, index){
  console.log(index + 1 + ". " + eachName)
})

document.getElementById("demo").innerHTML = sisters

//

sisters.forEach (function (eachName, index){
  console.log("Hello " + eachName +"!")
})
document.getElementById("anusha").innerHTML = sisters


//Mara
var toPrint = "Hi: "
sisters.forEach(function(name){ // is this like in python "name in sisters" right?
  toPrint += name + ", "
    })
document.getElementById("mara").innerHTML = toPrint


//Virginia's callback
sisters.forEach (function (name) {
  console.log("Hello, " + name + ", you are AWESOME!");
})

// kasia

sisters.forEach (function (name) {
document.getElementById('kasia').innerHTML += ';)' + name })


