var promise1 = new Promise(function(resolve, reject){
  // success value, failure reason
  setTimeout(resolve, 100, 'Good morning Ladies!')
});

console.log(promise1);

var promise2 = new Promise((resolve, reject) => {
  setTimeout(function(){
    resolve("Success!")
  }, 250)
});

promise2.then((successMessage) => {
  console.log("Yay! " + successMessage)
});


const promise3 = promise2().then(successCallback, failureCallback)

function myAsyncFunction(url) {
  return new Promise((resolve, reject) => {
    const xhr = new XMLHttpRequest();
    xhr.open('GET', url);
    xhr.onload = () => resolve(xhr.responseText);
    xhr.onerror = () => reject(xhr.statusText);
    xhr.send();
  });
}



