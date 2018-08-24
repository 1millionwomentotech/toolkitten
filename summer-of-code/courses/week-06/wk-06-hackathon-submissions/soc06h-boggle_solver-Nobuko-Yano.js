//Week06 hackathon:Boggle solver
//Start of program

var size = 4
var chars_in_dices = ''

var dices = ['AAEEGN',
   'ELRTTY',
   'AOOTTW',
   'ABBJOO',
   'EHRTVW',
   'CIMOTU',
   'DISTTY',
   'EIOSST',
   'DELRVY',
   'ACHOPS',
   'HIMNQU',
   'EEINSU',
   'EEGHNW',
   'AFFKPS',
   'HLNNRZ',
   'DEILRX']
	
// initialize n * n random characters
for (var i = 0; i < size*size; i++){
	chars_in_dices = chars_in_dices + dices[i][Math.floor(Math.random() * dices[i].length)];
}

// for test1 score:8, words:["WOMEN","MILLION"]
// wordlist = WOMEN,MILLION
//chars_in_dices = "XXWOMENXXMILLION"

// for test2 score:96, words:["WOMEN","MILLION"]
// wordlist = WOMEN,MILLION
// in case if the word is found more than once in 4*4 dices
// WOMEN*12, MILLION*12 since for each word N*3,M*2,O*2 times used
//chars_in_dices = "XXWOMENNXMILLION"

console.log("chars_in_dices: "+chars_in_dices)

// count words in 
var countWords = function(wordlist, chars){
	var result = {"score":0,"words":[]}
	var j,k=0
	var added_point = 0
	
	// pick each word in a wordlist
	for(j=0; j<wordlist.length;j++){
		var temp_char = JSON.parse(JSON.stringify(chars_in_dices))
		var word = wordlist[j].trim('')
		var match = 0
		var factor = 1
		var allFactor = 1
		
		// pick each char in a word
		for(k=0; k<word.length; k++){
			
			// check if this char exists in chars_in_dices
			if(temp_char.indexOf(word[k])>-1){
				match +=1
				temp_char = temp_char.replace(word[k],'',1)
				
				// if exists, add point and word in result
				if(word.length==match){
					if(word.length<=2){
						added_point = 0
					}else{
						added_point = word.length-2
					}

					// check if the word exists more than once in a chars_in_dices
					for(k=0; k<word.length; k++){
						while(temp_char.indexOf(word[k]) >-1){
							factor +=1
							temp_char = temp_char.replace(word[k],'',1)
						}
						allFactor *=factor
						factor = 1
					}
					added_point *= allFactor

					result["score"] += added_point
					result["words"].push(word)	

					added_point = 0
					break
				}
			}
		}
		continue
	}

	console.log("length of wordlist:"+wordlist.length)
	//console.log(heapsPermute(characterArray,print))
	console.log("===== result =====")
	console.log(result)
}



// Check for the various File API support.
if (window.File && window.FileReader && window.FileList && window.Blob) {
  //do your stuff!

  function readSingleFile(evt) {
	console.log("===== start of retrieving a file =====")
	var startDate = new Date();
    //Retrieve the first (and only!) File from the FileList object
    var f = evt.target.files[0]; 

    if (f) {
      var r = new FileReader();
      r.onload = function(e) { 
	    var contents = e.target.result;
        //alert( "Got the file.\n" 
        //      +"name: " + f.name + "\n"
        //      +"type: " + f.type + "\n"
        //      +"size: " + f.size + " bytes\n"
        //      + "starts with: " + contents.substr(1, contents.indexOf("\n"))
        //);  
        var wordlist = contents.split("\n")
        countWords(wordlist, chars_in_dices)

        var endDate   = new Date();
		var seconds = (endDate.getTime() - startDate.getTime()) / 1000;
 	 	console.log("duration(in seconds) : "+ seconds)
      }
      r.readAsText(f);

    } else { 
      alert("Failed to load file");
	}
  }

  document.getElementById('wordlist').addEventListener('change', readSingleFile, false);

} else {
  alert('The File APIs are not fully supported by your browser.');
}
