// parameters during function declaration
// function myFunction(p1, p2) {
//     return p1 ** p2
// }

// // arguments are passed in during
// // function invocation
// console.log(myFunction(3, 8))

// function toCelsius(fahrenheit) {
//   var homeOwner = "Rox"
//   console.log(homeOwner)
//   return (fahrenheit - 32) * 5 / 9
// }

// document.getElementById("anavirginia").innerHTML = toCelsius(63)


// toCelsius
// toCelsius()

// var myNum = toCelsius
// console.log(myNum)
// console.log('homeOwner', homeOwner)

function showName (firstName, lastName) {
  var nameIntro = "Your name is "
  function makeFullName () {
    return nameIntro + firstName + " " + lastName
  }
  return makeFullName();
}

document.getElementById("anavirginia").innerHTML = showName("Ashcan", "Consortia")

// $(function() {
//   var selections = []
//   $(".myButton").click(function() {
//     selections.push(this.prompt("name"))
//   })
// });

// create a button to click above and update #anavirginia to be selections

function celebrityID () {
  var celebrityID = 999
  return {
    getID: function () {
      return celebrityID
    },
    setID: function (theNewID) {
      celebrityID = theNewID
    }
  }
}

var mjID = celebrityID ();
console.log(mjID)

console.log(mjID.getID())

mjID.setID(3141)
console.log(mjID.getID())

// hoisting

x = 5

elem = document.getElementById("kasia")
elem.innerHTML = x

var x

// let and const are not hoisted
// initializations are not hoisted either

var x = 5

elem = document.getElementById("kasia")
elem.innerHTML = x + " " + y

var y = 7

// declare your variables at the top of the scope


function celebrityIDCreator (theCelebrities) {
  var i
  var uniqueID = 100
  for (i = 0; i < theCelebrities.length; i++) {
    theCelebrities[i]["id"] = function () {
      return uniqueID + i;
    }
  }
  return theCelebrities
}

var romComCelebs = [{name: "Reese Witherspoon", id:0 }, {name: "Julia Roberts", id:0 }, {name: "Meg Ryan", id:0}]

var createIdForRomComCelebs = celebrityIDCreator (romComCelebs)

var reeseID = createIdForRomComCelebs[0]
console.log(reeseID.id())
// we intended 100, 101, 102
// we got 103, 103, 103


// HW: how do we fix loop bug in closures?







