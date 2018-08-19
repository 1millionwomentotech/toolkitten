var M = 'land'
var o = 'water'

//Fixed 11*11 world:
// world = [
//   [o, o, o, o, M, M, M, M, M, M, M],
//   [o, o, o, o, M, M, M, M, M, M, M],
//   [o, o, o, o, M, M, M, M, o, o, o],
//   [o, o, o, o, M, M, M, o, o, o, o],
//   [o, o, o, o, o, M, M, M, o, o, o],
//   [o, o, o, o, o, M, o, o, o, o, o],
//   [o, o, o, o, o, o, o, o, o, o, o],
//   [o, o, o, o, o, o, o, o, o, o, o],
//   [o, o, o, o, o, M, o, o, o, o, o],
//   [o, o, o, o, o, o, o, o, o, o, o],
//   [o, o, o, o, o, o, o, o, o, o, o]
// ]


function printWorldItems() {
  console.log("Print board:")
  for (var i = 0; i < world.length; i++){
    for (var n = 0; n < world[i].length; n++) {
      console.log(world[i][n])
    }
  }
}

//printWorldItems()

//Random n*n world:
function getRandomIntInclusive(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min; //The maximum is inclusive and the minimum is inclusive 
}

function randomWorld(n, a, b){
  options = [a, b]
  board = []
  for (var i=0; i<n; i++){
    board.push([])
  }
  for (var x = 0; x < board.length; x++) {
    for (var i = 0; i < n; i++){
      board[x].push(options[getRandomIntInclusive(0, 1)])
    //console.log(board[x])
    }
  }
var M = 'land';
var o = 'water';
var world;

//Fixed 11*11 world:
// world = [
//   [o, o, o, o, M, M, M, M, M, M, M],
//   [o, o, o, o, M, M, M, M, M, M, M],
//   [o, o, o, o, M, M, M, M, o, o, o],
//   [o, o, o, o, M, M, M, o, o, o, o],
//   [o, o, o, o, o, M, M, M, o, o, o],
//   [o, o, o, o, o, M, o, o, o, o, o],
//   [o, o, o, o, o, o, o, o, o, o, o],
//   [o, o, o, o, o, o, o, o, o, o, o],
//   [o, o, o, o, o, M, o, o, o, o, o],var M = 'land';
var o = 'water';
var world;

//Fixed 11*11 world:
// world = [
//   [o, o, o, o, M, M, M, M, M, M, M],
//   [o, o, o, o, M, M, M, M, M, M, M],
//   [o, o, o, o, M, M, M, M, o, o, o],
//   [o, o, o, o, M, M, M, o, o, o, o],
//   [o, o, o, o, o, M, M, M, o, o, o],
//   [o, o, o, o, o, M, o, o, o, o, o],
//   [o, o, o, o, o, o, o, o, o, o, o],
//   [o, o, o, o, o, o, o, o, o, o, o],
//   [o, o, o, o, o, M, o, o, o, o, o],
//   [o, o, o, o, o, o, o, o, o, o, o],
//   [o, o, o, o, o, o, o, o, o, o, o]
// ]


function printWorldItems() {
  console.log("Print board:");
  for (var i = 0; i < world.length; i++){
    for (var n = 0; n < world[i].length; n++) {
      console.log(world[i][n]);
    }
  }
}

//printWorldItems()

//Random n*n world:
function getRandomIntInclusive(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min; //The maximum is inclusive and the minimum is inclusive 
}

function randomWorld(n, a, b){
  var options = [a, b];
  var board = [];
  for (var i=0; i<n; i++){
    board.push([]);
  }
  for (var x = 0; x < board.length; x++) {
    for (i = 0; i < n; i++){
      board[x].push(options[getRandomIntInclusive(0, 1)]);
    //console.log(board[x])
    }
  }

  console.log(board);
  return board;
}

world = randomWorld(11, M, o);
//console.log(printWorldItems());

//Continent counter:
function continentCounter(world, x, y){
    if (world[y][x] != 'land'){
        return 0;
    }
    var size = 1;
    world[y][x] = 'counted land';
    // ...then we count all of the neighboring eight tiles​
    // (and, of course, their neighbors by way of the recursion).​
    // row above
    if (x == world.length -1 || y == world.length - 1 || x == 0 || y == 0){
      return 1;
    }
    else{
      size = size + continentCounter(world, x-1, y-1);
      //console.log('first recursion size: ' , size);
      size = size + continentCounter(world, x  , y-1);
      size = size + continentCounter(world, x+1, y-1);

      // same row
      size = size + continentCounter(world, x-1, y  );
      size = size + continentCounter(world, x+1, y  );

      // row below
      size = size + continentCounter(world, x-1, y+1);
      size = size + continentCounter(world, x  , y+1);
      size = size + continentCounter(world, x+1, y+1);
      return size;
    }
}


console.log('Continent size is ' + (continentCounter(world, 5, 5)) + ' tiles.');
//   [o, o, o, o, o, o, o, o, o, o, o],
//   [o, o, o, o, o, o, o, o, o, o, o]
// ]


function printWorldItems() {
  console.log("Print board:");
  for (var i = 0; i < world.length; i++){
    for (var n = 0; n < world[i].length; n++) {
      console.log(world[i][n]);
    }
  }
}

//printWorldItems()

//Random n*n world:
function getRandomIntInclusive(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min; //The maximum is inclusive and the minimum is inclusive 
}

function randomWorld(n, a, b){
  var options = [a, b];
  var board = [];
  for (var i=0; i<n; i++){
    board.push([]);
  }
  for (var x = 0; x < board.length; x++) {
    for (i = 0; i < n; i++){
      board[x].push(options[getRandomIntInclusive(0, 1)]);
    //console.log(board[x])
    }
  }

  console.log(board);
  return board;
}

world = randomWorld(11, M, o);
//console.log(printWorldItems());

//Continent counter:
function continentCounter(world, x, y){
    if (world[y][x] != 'land'){
        return 0;
    }
    var size = 1;
    world[y][x] = 'counted land';
    // ...then we count all of the neighboring eight tiles​
    // (and, of course, their neighbors by way of the recursion).​
    // row above
    if (x == world.length -1 || y == world.length - 1 || x == 0 || y == 0){
      return 1;
    }
    else{
      size = size + continentCounter(world, x-1, y-1);
      //console.log('first recursion size: ' , size);
      size = size + continentCounter(world, x  , y-1);
      size = size + continentCounter(world, x+1, y-1);

      // same row
      size = size + continentCounter(world, x-1, y  );
      size = size + continentCounter(world, x+1, y  );

      // row below
      size = size + continentCounter(world, x-1, y+1);
      size = size + continentCounter(world, x  , y+1);
      size = size + continentCounter(world, x+1, y+1);
      return size;
    }
}


console.log('Continent size is ' + (continentCounter(world, 5, 5)) + ' tiles.');
  console.log(board)
  return board;
}

world = randomWorld(11, M, o);
//console.log(printWorldItems());

//Continent counter:
function continentCounter(world, x, y){
    if (world[y][x] != 'land'){
        return 0;
    }
    var size = 1;
    world[y][x] = 'counted land';
    // ...then we count all of the neighboring eight tiles​
    // (and, of course, their neighbors by way of the recursion).​
    // row above
    if (x == world.length -1 || y == world.length - 1 || x == 0 || y == 0){
      return 1
    }
    else{
      size = size + continentCounter(world, x-1, y-1);
      //console.log('first recursion size: ' , size);
      size = size + continentCounter(world, x  , y-1);
      size = size + continentCounter(world, x+1, y-1);

      // same row
      size = size + continentCounter(world, x-1, y  );
      size = size + continentCounter(world, x+1, y  );

      // row below
      size = size + continentCounter(world, x-1, y+1);
      size = size + continentCounter(world, x  , y+1);
      size = size + continentCounter(world, x+1, y+1);
      return size
    }
}


console.log('Continent size is ' + (continentCounter(world, 5, 5)) + ' tiles.');
