# 1 Million Women To Tech 

## Week 6 Day 4 Advanced JavaScript

## Promises

Definition:

A Promise is an object representing the eventual completion or failure of an asynchronous operation.

States:

- pending
- settled `Promise.prototype.finally(onFinally)`
  - fulfilled `Promise.prototype.then()`
  - rejected `Promise.prototype.catch()`

Arguments to `then` are optional, and 
`catch(failureCallback)` is shorthand for
`

## Shortcuts

`Promise.resolve()` and `Promise.reject()` manually create an already resolved / rejected promise.


In the old days, doing several asynchronous operations in a row would lead to the classic callback pyramid of doom:

```js
doSomething(function(result) {
  doSomethingElse(result, function(newResult) {
    doThirdThing(newResult, function(finalResult) {
      console.log('Got the final result: ' + finalResult);
    }, failureCallback);
  }, failureCallback);
}, failureCallback);
```

With modern functions, we attach our callbacks to the returned promises instead, forming a promise chain:

```js
doSomething().then(function(result) {
  return doSomethingElse(result);
})
.then(function(newResult) {
  return doThirdThing(newResult);
})
.then(function(finalResult) {
  console.log('Got the final result: ' + finalResult);
})
.catch(failureCallback);
```

## Methods

Promise.all(iterable)

Promise.race(iterable)

Promise.reject(reason)

Promise.resolve(value)
 - Generally, if you don't know if a value is a promise or not, Promise.resolve(value) it instead and work with the return value as a promise.


# Reference

=> arrow function
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions

Deep dive
https://hacks.mozilla.org/2015/06/es6-in-depth-arrow-functions/

AJAX > XML Http Request

- Besides XML can be used also for HTML, JSON, plain text
- Besides HTTP protocol can be use with other protocols

HTTP Status Messages, also good example of error indexing
https://www.w3schools.com/tags/ref_httpmessages.asp

https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/Using_XMLHttpRequest

Rox Arten​: Good resource for quick checking if something is supported and in what... 
https://caniuse.com

CORS
https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS

Promises by Google Developers
https://developers.google.com/web/fundamentals/primers/promises

Promises for Dummies - written by a woman yay!
https://scotch.io/tutorials/javascript-promises-for-dummies

# HW

- Handle success and error case of `promise1`.

- Implement promise examples from https://github.com/advanced-js/deck/tree/gh-pages/demos/ajax/promises

- https://github.com/getify/You-Dont-Know-JS/blob/31e1d4ff600d88cc2ce243903ab8a3a9d15cce15/es6%20%26%20beyond/ch4.md

- Please submit an interesting exercise to drill Promises.

(e.g. Load an audio file into your computer via an API, Spotify, Audible, SoundCloud? https://www.last.fm/api)








