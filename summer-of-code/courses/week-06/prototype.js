// let Person = function (name, age) {
//   this.name = name
//   this.age = age
// }

// let paulaB = new Person("Paulaberpas", 16)
// console.log(paulaB)

// Person.prototype.age = 21
// Person.prototype.favFood = "green tea cake"

// Do not set prototype like this because it will BREAK
// the prototype chain
// Person.prototype = {
//   age: 21
//   favFood: "green tea cake"
// }

var o = {
  a: 2,
  m: function() {
    return this.a + 1
  }
}

console.log(o.m()) //3

var p = Object.create(o)

console.log('p.a', p.a)
p.a = 4
console.log(p.m()) //


// different ways to create objects

// 1. syntax

var o = {a: 1}
var students = ["Rox", "Cristina"]
function f() { return 2 }

// 2. constructor

function Graph() {
  this.vertices = []
  this.edges = []
}

Graph.prototype.addVertex = function (v) {
  this.vertices.push(v)
}

var g = new Graph()

// 3. Object.create

var a = {a: 1}
var b = Object.create(a) // b.a
var c = Object.create(b) // c.a

// 4. class keyword

'use strict';

class Polygon {
  constructor(height, width) {
    this.height = height
    this.width = width
  }
}

class Square extends Polygon {
  constructor(sideLength) {
    super(sideLength, sideLength)
  }
  get area() {
    return this.height * this.width
  }
  set sideLength(newLength) {
    this.height = newLength
    this.width = newLength
  }
}

new square = new Square(2)
square = new Square(2)

Homework:
- Person and Coder classes coded as shown on the video
- re-implement the underscore.js library's
following three methods in plain JavaScript
using only for loops, forEach (https://underscorejs.org/#each)
  1. each
  2. map
  3. reduce


// QUIZ: Give your best definition of an object
// Cristina physical representation of a blueprint,
//where a blueprint is a class
//@
//Virginia: a collection of properties (key-value pairs)
//Anusha: instance of class, contains both
//attributes and methods

//AnaSustic: a grouping of name-value pairs where the
// value may be data or a function

//Rocio
//an object is a copy of the main template (class)
//which will have your specific data

//KatBurkinshaw an object is a collection of key-value pairs,
//which has properties, functions and methods

//Mara : A colection of variables, properties and methods

// Rox
// An object is a collection of properties associated with
//a name(key) and a value.

//link to edit: https://glitch.com/edit/#!/join/c994d9a5-c325-44b5-b573-21413e4de341