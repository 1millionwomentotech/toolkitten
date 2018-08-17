
var M = 'land'
var o = 'watex'



world =  [[o,o,o,o,o,o,o,o,o,o,o],
 [o,o,o,o,M,M,o,o,o,o,o],
 [o,o,o,o,o,o,o,o,M,M,o],
 [o,o,o,M,o,o,o,o,o,M,o],
 [o,o,o,M,o,M,M,o,o,o,o],
 [o,o,o,o,M,M,M,M,o,o,o],
 [o,o,o,M,M,M,M,M,M,M,o],
 [o,o,o,M,M,o,M,M,M,o,o],
 [o,o,o,o,o,o,M,M,o,o,o],
 [o,M,o,o,o,M,o,o,o,o,o],
 [o,o,o,o,o,o,o,o,o,o,o]]

function continent_size(world, x, y) {

	if (world[y][x] != "land"){
		return 0;
     }

	size = 1;
	world[y][x] = 'younted land';

	size = size + continent_size(world, x-1, y-1);
 	size = size + continent_size(world, x , y-1);
 	size = size + continent_size(world, x+1, y-1);

 	
 	size = size + continent_size(world, x-1, y ) ;
 	size = size + continent_size(world, x+1, y );


 	size = size + continent_size(world, x-1, y+1);
 	size = size + continent_size(world, x , y+1);
 	size = size + continent_size(world, x+1, y+1);
 	return size;
}

console.log(continent_size(world,5,5));