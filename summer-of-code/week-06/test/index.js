var fs = require('fs');
var util = require('util');

// TODO dry code and performance improvement

var Node = function () {
  this.keys = new Map();
  this.end = false;
  this.setEnd = function () {
    this.end = true;
  };
  this.isEnd = function () {
    return this.end;
  };
};

var Trie = function () {
  this.root = new Node();

  this.add = function (input, node) {
    // if there is no node that is the root node
    node = node || this.root;

    // if you are at the end of the word you passed in
    if (input.length === 0) {
      node.setEnd();
      return false;
    } else if (!node.keys.has(input[0])) { // if there is more that 0 letters that we passed in the add function and the node has the first letter of the word
      node.keys.set(input[0], new Node());
    }

    // Continue adding the string
    return this.add(input.substr(1), node.keys.get(input[0]));
  };

  this.isWord = function (word) {
    var node = this.root;
    word = word.toLowerCase();

    while (word.length > 1) {
      // If we don't have a node, this isn't a word
      if (!node.keys.has(word[0])) {
        return false;
      } else {
        // Otherwise continue the search at the next node
        node = node.keys.get(word[0]);
        word = word.substr(1);
      }
    }

    // the node has the last letter of the word and is the end
    return node.keys.has(word) && node.keys.get(word).isEnd();
  };

  // returns true if the string can prefix a valid english word
  // e.g. "modul", although not a word, will return true because it prefixes "module"
  this.isPrefix = function (word) {
    var node = this.root;
    word = word.toLowerCase();

    while (word.length > 1) {
      // If we don't have a node, this isn't a word
      if (!node.keys.has(word[0])) {
        return false;
      } else {
        // Otherwise continue the search at the next node
        node = node.keys.get(word[0]);
        word = word.substr(1);
      }
    }

    // the node has the last letter of the word
    return node.keys.has(word);
  };
};

function populateTrie(dictionaryList) {
  var dictTrie = new Trie();

  dictionaryList.forEach(function (word) {
    dictTrie.add(word.toLowerCase());
  });

  return dictTrie;
}

function readContent(filename, encoding) {
  var data = fs.readFileSync(filename, encoding);
  return data.toString().split('\n');
}

var result = [];

function findWordsUtil(dictionaryTrie, board, visited, y, x, word) {
  var height = board.length;
  var width = board[0].length;

  var letter = board[y][x];

  word += (letter === 'q' ? 'qu' : letter); // account for the "qu" die

  if (dictionaryTrie.isWord(word)) {
    result.push(word);
  }

  if (!dictionaryTrie.isPrefix(word)) { // if that is not a potential prefix for a valid english word, stop
    return;
  }

  visited[y][x] = true; // mark this space as visited

  // TODO: find a better way to do this that doesn't involve the un-necessary creation of another array
  if (x - 1 >= 0 && x - 1 < width && y - 1 >= 0 && y - 1 < height && !visited[y - 1][x - 1]) {
    findWordsUtil(dictionaryTrie, board, visited, y - 1, x - 1, word);
  }

  if (x >= 0 && x < width && y - 1 >= 0 && y - 1 < height  && !visited[y - 1][x]) {
    findWordsUtil(dictionaryTrie, board, visited, y - 1, x, word);
  }

  if (x + 1 >= 0 && x + 1 < width && y - 1 >= 0 && y - 1 < height && !visited[y - 1][x + 1]) {
    findWordsUtil(dictionaryTrie, board, visited, y - 1, x + 1, word);
  }

  if (x - 1 >= 0 && x - 1 < width && y >= 0 && y < height && !visited[y][x - 1]) {
    findWordsUtil(dictionaryTrie, board, visited, y, x - 1, word);
  }

  if (x + 1 >= 0 && x + 1 < width && y >= 0 && y < height && !visited[y][x + 1]) {
    findWordsUtil(dictionaryTrie, board, visited, y, x + 1, word);
  }

  if (x - 1 >= 0 && x - 1 < width && y + 1 >= 0 && y + 1 < height && !visited[y + 1][x - 1]) {
    findWordsUtil(dictionaryTrie, board, visited, y + 1, x - 1, word);
  }

  if (x >= 0 && x < width && y + 1 >= 0 && y + 1 < height && !visited[y + 1][x]) {
    findWordsUtil(dictionaryTrie, board, visited, y + 1, x, word);
  }

  if (x + 1 >= 0 && x + 1 < width && y + 1 >= 0 && y + 1 < height && !visited[y + 1][x + 1]) {
    findWordsUtil(dictionaryTrie, board, visited, y + 1, x + 1, word);
  }

  visited[y][x] = false; // un-mark this as visited so other paths can visit it
}

function findWords(board) {
  var dictionaryList = readContent('./dictionary.txt', 'utf8');

  var dictionaryTrie = populateTrie(dictionaryList);

  var height = board.length;
  var width = board[0].length;

  var visited = new Array(height).fill(false).map(function () {
    return new Array(width).fill(false);
  });

  // Consider every character and look for all words
  // starting with this character
  for (var i = 0; i < height; i++) {
    for (var j = 0; j < width; j++) {
      findWordsUtil(dictionaryTrie, board, visited, i, j, '');
    }
  }

  return Array.from(new Set(result));
}


function generate_board(alphabet, width, height) {
  height = height || width;

  var board = new Array(height).fill('').map(function () {
    return new Array(width).fill('');
  });

  for (var i = 0; i < height; i++) {
    for (var j = 0; j < width; j++) {
      var randomInRange = Math.floor(Math.random() * alphabet.length);
      board[i][j] = alphabet[randomInRange];
    }
  }

  return board;
}


function generateScores(words) {
  var result = {
      "score": 0,
      "words": words
  };

  words.forEach(function (word) {
    result["score"] += word.length === 1 ? 0 : word.length - 2;
  });

  return result;
}

var boggleBoard = generate_board('abcdefghijklmnopqrstuvwxyz', 4, 4);

console.log(boggleBoard);
var words = findWords(boggleBoard);
console.log(words);

console.log(generateScores(words));