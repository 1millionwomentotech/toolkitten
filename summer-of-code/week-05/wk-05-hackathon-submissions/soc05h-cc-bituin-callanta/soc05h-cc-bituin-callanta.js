var arrayLength = 11;

var multiArray = new Array(arrayLength);
for (var i = 0; i < multiArray.length; i++) {
	multiArray[i] = new Array(arrayLength);
}

//first row
multiArray[0][0] = "o";
multiArray[0][1] = "o";
multiArray[0][2] = "M";
multiArray[0][3] = "M";
multiArray[0][4] = "M";
multiArray[0][5] = "M";
multiArray[0][6] = "o";
multiArray[0][7] = "o";
multiArray[0][7] = "o";
multiArray[0][9] = "o";
multiArray[0][10] = "o";

//second row
multiArray[1][0] = "o";
multiArray[1][1] = "o";
multiArray[1][2] = "M";
multiArray[1][3] = "M";
multiArray[1][4] = "M";
multiArray[1][5] = "M";
multiArray[1][6] = "o";
multiArray[1][7] = "o";
multiArray[1][8] = "o";
multiArray[1][9] = "o";
multiArray[1][10] = "o";

//third row
multiArray[2][0] = "o";
multiArray[2][1] = "o";
multiArray[2][2] = "o";
multiArray[2][3] = "o";
multiArray[2][4] = "o";
multiArray[2][5] = "o";
multiArray[2][6] = "o";
multiArray[2][7] = "o";
multiArray[2][8] = "o";
multiArray[2][9] = "o";
multiArray[2][10] = "o"; 

//fourth row
multiArray[3][0] = "o";
multiArray[3][1] = "o";
multiArray[3][2] = "o";
multiArray[3][3] = "o";
multiArray[3][4] = "o";
multiArray[3][5] = "M";
multiArray[3][6] = "o";
multiArray[3][7] = "o";
multiArray[3][8] = "o";
multiArray[3][9] = "o";
multiArray[3][10] = "o";

//fifth row
multiArray[4][0] = "o";
multiArray[4][1] = "o";
multiArray[4][2] = "o";
multiArray[4][3] = "o";
multiArray[4][4] = "M";
multiArray[4][5] = "M";
multiArray[4][6] = "o";
multiArray[4][7] = "o";
multiArray[4][8] = "o";
multiArray[4][9] = "o";
multiArray[4][10] = "o";

//sixth row
multiArray[5][0] = "o";
multiArray[5][1] = "o";
multiArray[5][2] = "o";
multiArray[5][3] = "o";
multiArray[5][4] = "o";
multiArray[5][5] = "M";
multiArray[5][6] = "o";
multiArray[5][7] = "o";
multiArray[5][8] = "o";
multiArray[5][9] = "o";
multiArray[5][10] = "o";

//seventh row
multiArray[6][0] = "M";
multiArray[6][1] = "o";
multiArray[6][2] = "o";
multiArray[6][3] = "o";
multiArray[6][4] = "o";
multiArray[6][5] = "o";
multiArray[6][6] = "o";
multiArray[6][7] = "o";
multiArray[6][8] = "o";
multiArray[6][9] = "o";
multiArray[6][10] = "o"; 

//eighth row
multiArray[7][0] = "o";
multiArray[7][1] = "o";
multiArray[7][2] = "o";
multiArray[7][3] = "o";
multiArray[7][4] = "o";
multiArray[7][5] = "o";
multiArray[7][6] = "M";
multiArray[7][7] = "M";
multiArray[7][8] = "M";
multiArray[7][9] = "o";
multiArray[7][10] = "o";
 
//ninth row
multiArray[8][0] = "o";
multiArray[8][1] = "o";
multiArray[8][2] = "M";
multiArray[8][3] = "M";
multiArray[8][4] = "M";
multiArray[8][5] = "M";
multiArray[8][6] = "o";
multiArray[8][7] = "o";
multiArray[8][8] = "o";
multiArray[8][9] = "o";
multiArray[8][10] = "o";

//tenth row
multiArray[9][0] = "o";
multiArray[9][1] = "o";
multiArray[9][2] = "o";
multiArray[9][3] = "o";
multiArray[9][4] = "o";
multiArray[9][5] = "o";
multiArray[9][6] = "o";
multiArray[9][7] = "M";
multiArray[9][8] = "M";
multiArray[9][9] = "M";
multiArray[9][10] = "o";

//eleventh row
multiArray[10][0] = "o";
multiArray[10][1] = "o";
multiArray[10][2] = "M";
multiArray[10][3] = "M";
multiArray[10][4] = "o";
multiArray[10][5] = "o";
multiArray[10][6] = "o";
multiArray[10][7] = "o";
multiArray[10][8] = "o";
multiArray[10][9] = "o";
multiArray[10][10] = "o";

alert(multiArray);
alert(multiArray.length);

// 4. Find another continent (making sure not to count any of them twice but
// also making sure each gets counted), and repeat the process.

// 5. Then find the largest two, and see whether they look like fun to play on.