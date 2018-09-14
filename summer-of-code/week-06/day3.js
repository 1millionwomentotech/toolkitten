function foo(b) {
  var a = 10;
  return a + b + 11;
}

function bar(x) {
  var y = 3;
  return foo(x * y);
}

console.log(bar(17)) //
console.log('My next')


// while (queue.waitForMessage()) {
//   queue.processNextMessage();
// }

const s = new Date().getSeconds();

setTimeout(function() {
  console.log("Ran after " + (new Date().getSeconds() - s) + " seconds");
}, 500);

while(true) {
  if (new Date().getSeconds() - s >= 2) {
    console.log("Good, 2 seconds have passed, we were happily looping");
    break;
  }
}

(function() {

  console.log('Kasia W: This is the start.');

  setTimeout(function cb(){
    console.log('kat Martin: This is a message from the 0th callback');
  });

  console.log('Rocio Pena: This is just a incoming <3')

  setTimeout(function cb1(){
    console.log('Krystal: Bless you! I\'m sending this be well messsage from call back 1')
  });

  console.log('Virginia: This is the end.')

})();

















