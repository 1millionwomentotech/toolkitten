var fs = require('fs');
var util = require('util');

var boggle = [
  ['G', 'I', 'Z', 'D'],
  ['U', 'E', 'K', 'H'],
  ['Q', 'S', 'E', 'L'],
  ['M', 'N', 'O', 'P']
];

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

  word += (letter === 'Q' ? 'QU' : letter); // account for the "Qu" die

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


  // visited[i][j] = true;
  // str = str + board[i][j];
  //
  // // If str is present in dictionary, then return it
  // if (dictionaryTrie.isWord(str)) {
  //   console.log("test", str);
  //   return str;
  // }

  // Traverse 8 adjacent cells of boggle[i][j]
  // for (var row = i - 1; row >= 0 && row <= i + 1 && row < height; row++) {
  //   for (var col = j - 1; col >= 0 && col <= j + 1 && col < width; col++) {
  //     console.log(row,  col);
  //     // console.log(visited[row][col], row,  col);
  //     // if (!visited[row][col]) {
  //     //   console.log(str);
  //     //   return findWordsUtil(dictionaryTrie, board, visited, row, col, str);
  //     // }
  //   }
  // }

  // str = str.length -1;
  // visited[i][j] = false;
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

console.log(findWords(boggle));