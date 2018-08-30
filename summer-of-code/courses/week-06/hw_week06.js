/*
 * Week 6
 * Day 1
 * HW: how do we fix loop bug in closures?
 */
/*  
 *ES6 solution: let
 *ECMAScript 6 (ES6), the newest version of JavaScript, is now starting to be implemented in many evergreen browsers 
 *and backend systems. There are also transpilers like Babel that will convert ES6 to ES5 to allow usage of new features on older systems.
 *
 *ES6 introduces new let and const keywords that are scoped differently than var-based variables. For example, in a loop with 
 *a let-based index, each iteration through the loop will have a new value of i where each value is scoped inside the loop
 */

function celebrityIDCreator (theCelebrities) {
    var i
    var uniqueID = 100
    for (let i = 0; i < theCelebrities.length; i++) {
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

  var juliaID = createIdForRomComCelebs[1]
  console.log(juliaID.id())

  var megID = createIdForRomComCelebs[2]
  console.log(megID.id())
/*
  HW: countdown exercise
  https://github.com/advanced-js/countdown
  Build a very simple kitchen timer: modify the countdown() function in countdown.js 
  to take a number of seconds, then print each second counting down to zero.

  countdown(3);

  // should print

  // 3...
  // 2...
  // 1...
  // 0
*/



function countdown(count) {
    var timerId = setInterval(function() {
        console.log(count);
        count--;

        if(count < 0) {
            clearInterval(timerId);;
        }
    }, 1000);
}


countdown(prompt("Enter countdown value"));

/*
Homework Day2:
- Person and Coder classes coded as shown on the video
    create a person class
    int age
    string favorite food
    string name
    void sayName() //console log the name
    void patCat(Cat&)
    void greetPerson(Person&)

    instantiate the person(string,int)

    create a coder class that extends the Person
    int age
    string favorite food
    string name
    void sayName() //console log the name
    void patCat(Cat&)
    void greetPerson(Person&)
    ++++
    float coding_skill
    array coding_languages
    int add(int a, int b) // function to add two integers together
    instantiate the coder(string,int,float)

    Person Ilona("Ilona",16)
    Coder IlonaC("Ilona",17, infinity)



- re-implement the underscore.js library's
following three methods in plain JavaScript
using only for loops, forEach (https://underscorejs.org/#each)
  1. each
  2. map
  3. reduce

*/

function Person(name, age, favFood) {
    this.name = name;
    this.age = age;
    this.favFood = favFood;
    this.sayName = function() {
      return this.name;
    };
    this.patCat = function() {
        return "Pat a cat";
      };
    this.greetPerson = function() {
      alert("Nice meeting you! My name is " + this.name + ".");
    };
  }

var person1 = new Person('ana', 32, 'salsa');
person1.name
person1.sayName()
person1.patCat()
person1.greetPerson()

function Coder(name, age, favFood, codingSkill, codingLang) {
    Person.call(this, name, age, favFood);
  
    this.codingSkill = codingSkill;
    this.codingLang = codingLang;
    this.add2numb = function(a,b) {
        return a+b;
      };

  }

var coder1 = new Coder('jaro', 40, 'pizza', 99, ['PHP', 'Java'])
console.log(coder1)
coder1.add2numb(2,3)




//trying  https://underscorejs.org/ _.each
//each from 
//_.each(list, iteratee, [context]) 
//Alias: forEach
//Iterates over a list of elements, yielding each in turn to an iteratee function. 
//The iteratee is bound to the context object, if one is passed. Each invocation of iteratee
// is called with three arguments: (element, index, list). If list is a JavaScript object, 
//iteratee's arguments will be (value, key, list). Returns the list for chaining. 


var each_array = function(){
    var people = ["polona", "nina", "jana"]
    
    _.each(people, function(name,key){
        console.log(name);
        console.log(key);
       }) 
  }

each_array();

var each_object = function(){
    var people_object = {name : "nina", age : "33", gender : "female"}
    
  _.each(people_object, function(name,key){
        console.log(name);
        console.log(key);
       })
  }

 
each_object();


// Call iterator(value, key, collection) for each element of collection.
// Accepts both arrays and objects.
//
// Note: _.each does not have a return value, but rather simply runs the
// iterator function over each item in the input collection.
_ = {};
_.each = function(collection, callBack) {
    if (Array.isArray(collection)) {
      for (var i = 0; i < collection.length; i++) {
        callBack(collection[i], i, collection);
      }
    } else {
      for (var key in collection) {
        callBack(collection[key], key, collection);
      }
    }
};

_.each(["polona", "nina", "jana"], console.log);
_.each({name : "nina", age : "33", gender : "female"}, console.log);

//trying  https://underscorejs.org/ _.map
//_.map(list, iteratee, [context])
// Alias: collect
//Produces a new array of values by mapping each value in list through a transformation function (iteratee). 
//The iteratee is passed three arguments: the value, then the index (or key) of the iteration, and finally a reference 
//to the entire list.

//_.map([1, 2, 3], function(num){ return num * 3; });
//=> [3, 6, 9]
//_.map({one: 1, two: 2, three: 3}, function(num, key){ return num * 3; });
//=> [3, 6, 9]
//_.map([[1, 2], [3, 4]], _.first);
//=> [1, 3]

var numbers = [1, 2, 3]
var numbersMultiplied = _.map(numbers, function(value, index, items){
    return value *3
});
console.log(numbersMultiplied);