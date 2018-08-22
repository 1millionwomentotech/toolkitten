document.getElementById("day1").innerHTML="1st Day Homework";

//Hours:
var x=365*24;
document.getElementById("day1Ex1").innerHTML='1 year has '+ x+' hours';

//Minutes
x=365*24*10*60;
document.getElementById("day1Ex2").innerHTML='decade has '+ x+' minutes';

//How old am I
var today= Date.now();
var MyBDay= new Date('1,24,1987, 16:15');
var bDay=(today-MyBDay.getTime())/1000;
document.getElementById("day1Ex6").innerHTML='I am '+bDay+' seconds old';

//Cristina Tarantino
var classDate=new Date('8,13,2018 9:15');
cBDay=new Date('8,12,1986');
cBDayInMS=classDate.getTime()-cBDay.getTime();
document.getElementById("day1Ex3").innerHTML='Cristina Tarantino '+ cBDayInMS+' miliseconds old';

//Optional

//32bit (64bit) system timeout
var maxInt=Math.pow(2,32);
document.getElementById('day1Ex4').innerHTML='32 bit system timeout is '+maxInt/1000/60/60/24+' days';
var maxInt=Math.pow(2,64);
document.getElementById('day1Ex5').innerHTML='64 bit system timeout is '+maxInt/1000/60/60/24+' days';

document.getElementById("day2").innerHTML="2nd Day Homework";

//Piano

var notes=['A','A#', 'B', 'C', 'C#', 'D', 'D#', 'E','F', 'F#','G', 'G#', 'A\''];
for(var i=0; i,i<=12; i++)
{
	var formula=440*Math.pow(2,i/12);
	document.getElementById("day2Ex1").innerHTML+='<p>'+notes[i]+': ' +formula+'</p>';
}

// Motion of the Moon
// Moon going once around Earth in approximately 27.3 days
var moveDeg=360/27.3; // degree per day
//min per day
var minDaily=24*60;
//min in 1 degree
var minDeg=minDaily/360;
document.getElementById("day2Ex2").innerHTML=moveDeg*minDeg +' min Moon travels in a day';

document.getElementById("day3").innerHTML="3rd Day Homework";

//full name greeting
function day3Ex1()
{
	var firstName=prompt('What is your first name?');
	var midName=prompt('What is your middle name?');
	var lastName=prompt('What is your last name?');
	alert('Nice to see you '+firstName+' '+midName+' '+lastName);
	//document.getElementById("day3Ex1").innerHTML='Nice to see you '+firstName+' '+midName+' '+lastName;

}

//Bigger, Better favarite number
function day3Ex2()
{
	var fav_number=prompt("What is your favorite number?");
	var num=parseInt(fav_number);
	alert('Don\'t you think the bigger favorite number is better!?\nI think YES, so your bigger and better favorite number is ' +(num+1)+'!!!');
}

//Angry boss
function day3Ex3()
{
	var answer=prompt("WHAT DO YOU WANT?");
	alert('WHAAAT DO YOU MEAN  "' +answer.toUpperCase()+'"???? YOU\'RE FIRED!!!')
}

//Table of contents
function day3Ex4()
{
	document.getElementById("day3Ex4").innerHTML='<div>Table of Contents</div>';
	var text=["Chapter 1:","Getting Started", "page 1", "Chapter 2:"," Numbers", "page 9", "Chapter 3:"," Letters", "page 13"]
	for (var x=0; x<text.length;x++)
	{
		if (text[x].toLowerCase().startsWith("chapter")){
			document.getElementById("day3Ex4").innerHTML+=text[x]+' ';
		}
		else if(text[x].toLowerCase().startsWith("page"))
		{
			document.getElementById("day3Ex4").innerHTML+=text[x]+' ';
		}
		else
		{
			document.getElementById("day3Ex4").innerHTML+=text[x]+' ';

		}
	}
}
day3Ex4();

//optional
//Math
document.getElementById("day3ExO1").innerHTML=Math.pow(5,10);
document.getElementById("day3ExO2").innerHTML=365%7;
document.getElementById("day3ExO3").innerHTML=Math.abs(-7);

//Random
function getRndInteger(min, max) {
    return Math.floor(Math.random() * (max - min + 1) ) + min;
}
document.getElementById("day3ExO4").innerHTML=getRndInteger(1,10);
document.getElementById("day3ExO5").innerHTML=getRndInteger(1,100);
document.getElementById("day3ExO6").innerHTML=getRndInteger(1930,1950);

//
function day3ExO7()
{
	var world=[[],[]];
	document.getElementById("day3ExO7").innerHTML='';
	for (var i = 0; i <5; i++)
 	{
 		document.getElementById("day3ExO7").innerHTML+='<div></div>';
 		for (var j = 0; j <5; j++)
		{	var ran=getRndInteger(0,1);
 			if (ran==0)
 			{
				document.getElementById("day3ExO7").innerHTML+='o';
			}
			else
			{
				document.getElementById("day3ExO7").innerHTML+='X';
			}

		}
	}
}

//Day 4 homework
document.getElementById("day4").innerHTML="4th Day Homework";

//99 bottles
function day4Ex1()
{
	var x=99;
	while (x>=0)
	{
		var y=x-1;
		
		if (x==1)
		{
			document.getElementById("day4Ex1").innerHTML+=
			"<dir>1 bottle of beer on the wall, 1 bottle of beer.</dir>Take one down and pass it around, no more bottles of beer on the wall.";
		}
		if (x==0)
		{
			document.getElementById("day4Ex1").innerHTML+=
			"<dir>No more bottles of beer on the wall, no more bottles of beer.</dir>Go to the store and buy some more, 99 bottles of beer on the wall.";
		}
		else
		{
			document.getElementById("day4Ex1").innerHTML+="<dir>"+x+" bottles of beer on the wall,"+x+
			" bottles of beer.</dir>Take one down and pass it around,"+y+" bottles of beer on the wall.";
			
		}
		x--;
	}
}
day4Ex1();

//deaf grandmae
function day4Ex2()
{
	var start_year=parseInt(prompt("Input start year: "));
	var finish_year=parseInt(prompt("Input finish year: "));
	var flag=0;
	while (true)
	{
		var text=prompt("Say something to your grandma...");
		var check=isUpper(text);
		if (check==false)
		{
			flag=0;
			alert("Grandma: HUH?! SPEAK UP, GIRL!");
		}
		else
		{
			if (text=="BYE")
			{
				flag+=1;
				if (flag==3)
				{
					alert("Grandma: BYE");
					break;
				}
			}
			else
			{
				flag=0;
				while (true)
				{
					var year=getRndInteger(start_year,finish_year);
					if ((year%4)==0)
					{
						if ((year%100)==0)
						{
							if((year%400)==0)
							{
								alert("Grandma: NO, NOT SINCE "+year+"!" );
								break;
							}
						}
						alert("Grandma: NO, NOT SINCE "+year+"!");
						break;
					}
				}
			}
		}
	}		
}
function isUpper(mystring)
{
	var flag=false;
	if(mystring!=null)
	{flag=true;
		if(mystring==''){flag=false;}
			
		
		for (var i = 0; i < mystring.length; i++)
		{
		 	if(!/A-Z/.test(mystring[i]))
		 	{
		 		flag==false;
		 		break;
		 	}
		 				
		}
	
	}

	return flag;
}

//Building and sorting an array
function day4Ex3()
{
	alert("Please input words:")
	var words=[];
	while (true)
	{
		var new_word=prompt();
		if (new_word.length==0)
		{
			break;
		}
		words.push(new_word);
	}
	alert(words.sort().join('\n'));

}

//moo
function day4Ex5()
{
	var n=parseInt(prompt("Plese input the number: "));
	while (n>0)
	{
		document.getElementById("day4Ex5").innerHTML+=" moo";
		n--;
	}
}

//Old Roman Numbers
function day4Ex6()
{
	var number=parseInt(prompt("Please input the number 1...3000: "));
	var	roman_number="";
	var m=Math.floor(number/1000);
	var d=Math.floor((number%1000)/500);
	var c=Math.floor(number%1000%500/100);
	var l=Math.floor(number%1000%500%100/50);
	var x=Math.floor(number%1000%500%100%50/10);
	var v=Math.floor(number%1000%500%100%50%10/5);
	var t=Math.floor(number%1000%500%100%50%10%5);

	var roman_number="";
	for (var i = 0; i < m; i++)
	{
		roman_number+='M';	
	}
	for (var i = 0; i < d; i++) 
	{
		roman_number+='D';	
	}	
	for (var i = 0; i < c; i++) 
	{
		roman_number+='C';	
	}
	for (var i = 0; i < l; i++) 
	{
		roman_number+='L';	
	}
	for (var i = 0; i < x; i++) 
	{
		roman_number+='X';	
	}
	for (var i = 0; i < v; i++) 
	{
		roman_number+='V';	
	}
	for (var i = 0; i < t; i++) 
	{
		roman_number+='I';	
	}

	document.getElementById("day4Ex6").innerHTML=number+" = "+roman_number;
}

//New Roman
function day4Ex7()
{
	var number=parseInt(prompt("Please input the number 1...3000: "));
	var	roman_number="";
	var m=Math.floor(number/1000);
	var d=Math.floor((number%1000)/500);
	var c=Math.floor(number%1000%500/100);
	var l=Math.floor(number%1000%500%100/50);
	var x=Math.floor(number%1000%500%100%50/10);
	var v=Math.floor(number%1000%500%100%50%10/5);
	var t=Math.floor(number%1000%500%100%50%10%5);

	var roman_number="";
	var tous=""
	var hundr=""
	var ten=""
	for (var i = 0; i < m; i++) 
	{
		roman_number+='M';
	}
	if (c==4)
	{
		if(d==0)
		{
			tous='C'+'D';
		}
		else
		{
			tous='C'+'M';
		}
		
		roman_number+=tous;
	}
	else
	{
		for (var i = 0; i < d; i++) 
		{
			roman_number+='D';
		}

		for (var i = 0; i < c; i++)
		 {
			roman_number+='C';
		}
	}
	if (x==4)
	{
		if(l==0)
		{
			hundr='X'+'L';
		}
		else
		{
			hundr='X'+'C';
		}
		roman_number+=hundr;
	}
	else
	{
		for (var i = 0; i < l; i++) 
		{
			roman_number+='L';
		}
		for (var i = 0; i < x; i++) 
		{
			roman_number+='X';
		}
	}
	if (t==4)
	{
		if(v==0)
		{
			ten='I'+'V';
		}
		else
		{
			ten='I'+'X';
		}
		roman_number+=ten;
	}
	else
	{
		for (var i = 0; i < v; i++) 
		{
			roman_number+='V';
		}
		for (var i = 0; i < t; i++) 
		{
			roman_number+='I';
		}
	}
	document.getElementById("day4Ex7").innerHTML=number+" = "+roman_number;
