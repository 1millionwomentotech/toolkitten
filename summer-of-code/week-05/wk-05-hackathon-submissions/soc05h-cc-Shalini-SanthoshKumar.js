
//This file can be run from a standard html file with a script element to link this JS file

/*
### Week 5 Hackathon Challenge: Continent Counter in Javascript

Task: Calculate the size of a continent you are standing on in your 11 x 11 world in Civilization III.

Bonuses for:
- calculate continent size for all continents in the world
- random world generator
- fastest program
- benchmarking
- extension of the problem to n x n size world

*/

//STEP 1: Generate a world
// 0 is water and 1 is land
// Get grid size from user
var n = prompt("Enter the size of the fantasy world")
document.write("THE FANTASY WORLD <br> <br>")
var world = new Array();
var continents = new Array();

for(var i=0; i< parseInt(n); i++){
	world[i] = new Array();
	for(var j=0; j <  parseInt(n); j++){

		world[i][j] = Math.round(Math.random(0,1));

		document.write(world[i][j],"\t");
	}
	document.write("<br>");
	
}

var size = 0;

//Traverse through the world and search for connected land

//document.write("The continent size before checking is", size,"<br>");
for(var i=0; i< world.length; i++){

	for(var j=0; j <world.length; j++){
		size = 0;
		checkNeighbors(i,j);
		if(size !=0){
			document.write("For land starting at tile", "[",i,"]","[",j,"]",": ");
			document.write(" continent size is ", size,"<br>");
			continents.push([i,j,size]);
		}
		
	}

}	


function checkNeighbors(a, b) {
	// check 8 neighbors

	// check if the cell is valid and is land
	if( (a >=0 && a < world.length) &&(b >=0 && b < world.length) && world[a][b] == 1) {

		//document.write("Processing tile ", a, b, "<br>");
		size = size + 1;

		world[a][b] = 99; // to represent a tile that is already counted

		// list the neighbors
		var neighbors = new Array();
		neighbors[0] = [a-1,b-1];
		neighbors[1] = [a-1,b];
		neighbors[2] = [a-1,b+1];
		neighbors[3] = [a,b-1];
		neighbors[4] = [a,b+1];
		neighbors[5] = [a+1,b-1];
		neighbors[6] = [a+1,b];
		neighbors[7] = [a+1,b+1];
		
		for(var i =0; i < neighbors.length; i++){

			var row = neighbors[i][0];
			var col = neighbors[i][1];

			//document.write("Passing values ", row, col, "<br>");
			checkNeighbors(row,col);
		}
	}else

	//document.write(a,b," Does not satisfy the conditions <br>");

	return 0
}