// TODO add more comments
// TODO unit tests
// TODO add JavaScript Doc

var homework = homework || {};

homework.DAYS_IN_YEAR = 365.2422; //https://en.wikipedia.org/wiki/Year#Variation_in_the_length_of_the_year_and_the_day
homework.HOURS_IN_DAY = 24;
homework.MIN_IN_DAY = 60;
homework.SEC_IN_DAY = 60;
homework.SEC_IN_MILLISEC = 1000;
homework.YEARS_IN_DECADE = 10;

// 60 seconds/minute * 60 minutes/hour * 24 hours/day
homework.SEC_IN_DAY = homework.SEC_IN_DAY * homework.MIN_IN_DAY * homework.HOURS_IN_DAY;

// helper method for ex d1e5 and d1e6
homework.getDaysFromMaxBitReps = function (ms) {
  var max_value_per_bit_sys = Math.pow(2, ms);
  return max_value_per_bit_sys / homework.SEC_IN_MILLISEC / homework.SEC_IN_DAY;
};

// helper method for ex d1e5 and d1e6
homework.attachTimeOut = function (callback, querySelector, unitString, ms) {
  // Update the count down every 1 second
  var interval = setInterval(function () {
    var result = callback();
    document.querySelector(querySelector).innerHTML = result + " " + unitString;

    // If the count down is over, write some text
    if (result < 0) {
      clearInterval(interval);
      document.querySelector(querySelector).innerHTML = "EXPIRED";
    }
  }, ms);
};

// helper method for d1e3, d1e4, d1e7
homework.dateDistanceFromNow = function (distanceDate) {
  var today = new Date();
  return today - distanceDate;
};

//Hours in a year. How many hours are in a year?
homework.d1e1 = (function (homework) {
  homework.hours_in_year = homework.DAYS_IN_YEAR * homework.HOURS_IN_DAY;
  document.querySelector('#d1e1 .solution').innerHTML = homework.hours_in_year + " hours";
})(homework);

//Minutes in a decade. How many minutes are in a decade?
homework.d1e2 = (function (homework) {
  var min_in_decade = homework.hours_in_year * homework.YEARS_IN_DECADE * homework.MIN_IN_DAY;
  document.querySelector('#d1e2 .solution').innerHTML = min_in_decade + " minutes";
})(homework);

// Your age in seconds. How many seconds old are you? (I'm not going to check your answer, so be as accurate—or not—as you want.)
homework.d1e3 = (function (homework) {
  homework.attachTimeOut(function () {
    var ms_distance = homework.dateDistanceFromNow(new Date(1986, 7, 12, 18, 45, 0));
    return Math.floor(ms_distance / homework.SEC_IN_MILLISEC);
  }, '#d1e3 .solution', 'seconds', homework.SEC_IN_MILLISEC);
})(homework);

//Cristina Tarantino: 32 yesterday! How many milliseconds old is she hahaha? Calculate @Cristina Tarantino's age in milliseconds.
homework.d1e4 = (function (homework) {
  homework.attachTimeOut(function () {
    return homework.dateDistanceFromNow(new Date(1986, 7, 12, 18, 45, 0));
  }, '#d1e4 .solution', 'milliseconds', 1);
})(homework);

// How many days does it take for a 32-bit system to timeout, if it has a bug with integer overflow?
// The Binary Register Width of a processor determines the range of values that can be represented.
// The maximum representable value for a 32-bit system will be 2^32-1
// When an arithmetic operation (in this case the increment of a millisecond in the time)
// produces a result larger than the above we will have an `integer overflow`
// To calculate the days it will take to reach that situation for a 32-bit system
// we need to convert 2^32 milliseconds in days by dividing by 1000s then 60s then 60m and then 24h
// source https://en.wikipedia.org/wiki/Integer_overflow
homework.d1e5 = (function (homework) {
  var ms_to_overflow = homework.getDaysFromMaxBitReps(32);
  document.querySelector('#d1e5 .solution').innerHTML = ms_to_overflow + " days";
})(homework);

// How many days does it take for a 32-bit system to timeout, if it has a bug with integer overflow?
// The Binary Register Width of a processor determines the range of values that can be represented.
// The maximum representable value for a 32-bit system will be 2^64-1
// When an arithmetic operation (in this case the increment of a millisecond in the time)
// produces a result larger than the above we will have an `integer overflow`
// To calculate the days it will take to reach that situation for a 32-bit system
// we need to convert 2^64 milliseconds in days by dividing by 1000s then 60s then 60m and then 24h
// source https://en.wikipedia.org/wiki/Integer_overflow
homework.d1e6 = (function (homework) {
  var ms_to_overflow = homework.getDaysFromMaxBitReps(64);
  document.querySelector('#d1e6 .solution').innerHTML = ms_to_overflow + " days";
})(homework);

// Calculate your age accurately based on your birthday (maybe use time of day e.g. 8:23am if you know it, use 12:00 noon midday) - you will need JavaScript DateTime functionality.
homework.d1e7 = (function (homework) {
  homework.attachTimeOut(function () {
    var ms_distance = homework.dateDistanceFromNow(new Date(1986, 7, 12, 18, 45, 0));
    return Math.floor(ms_distance / homework.SEC_IN_MILLISEC);
  }, '#d1e7 .solution', 'seconds', homework.SEC_IN_MILLISEC);
})(homework);

// Music A 440 Hz 1 octave is double the frequency tempered piano A' 880 Hz Calculate and console.log the frequency each of the 12 notes between A and A'
// notes are per https://www.intmath.com/trigonometric-graphs/music.php in exponential scale
// The frequency needs to double every 12 notes because there are 7 white notes and 5 black notes in each octave.
// TODO add more comments and dry up
homework.d2e1 = (function (homework) {
  var noteList = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A'"];
  // invisible DOM so you don't interact with the DOM too much
  // because every DOM interaction is a performace hit
  var fragment = document.createDocumentFragment();
  var table = document.createElement('table');
  var headRow = document.createElement('tr');
  var headCI = document.createElement('th');
  var headCII = document.createElement('th');
  var headCIII = document.createElement('th');

  headCI.innerHTML = "Note";
  headCII.innerHTML = "Frequency in Hz";
  headCIII.innerHTML = "Difference";

  headRow.appendChild(headCI);
  headRow.appendChild(headCII);
  headRow.appendChild(headCIII);
  table.appendChild(headRow);

  for (var i = 0, note = 440; i < noteList.length; i++) {
    var row = document.createElement('tr');
    var cell_lx = document.createElement('tr');
    cell_lx.innerHTML = noteList[i];
    var cell_rx = document.createElement('td');
    var frequency = Math.round(note * Math.pow(2, i / (noteList.length - 1)) * 100) / 100;
    cell_rx.innerHTML = frequency;
    var cell_rrx = document.createElement('td');
    cell_rrx.innerHTML = Math.round((frequency - note)* 100) / 100;

    row.appendChild(cell_lx);
    row.appendChild(cell_rx);
    row.appendChild(cell_rrx);
    table.appendChild(row);
  }

  fragment.appendChild(table);
  document.querySelector('#d2e1 .solution').appendChild(fragment);
})(homework);

// Planets Calculate and console log how many 'minutes' the Moon travels in a day.
// Hint: first calculate how many degrees the Moons travels in the sky when the Earth returns to the same position during its daily rotation.
// http://myscientificbluff.blogspot.com/2009/03/why-moon-rises-50-minutes-later.html
// 360 degrees : (24 * 60) min/day = 12.2 degrees : x min/day
// x = (24 * 60 * 13.2) / 360
homework.d2e2 = (function (homework) {
  // 360 degrees divided by how long it takes the Moon to return to the same place “in the stars”
  var moon_degrees_per_day = 360/29.5;
  var min_in_day_moon = (homework.MIN_IN_DAY * homework.HOURS_IN_DAY * moon_degrees_per_day) / 360;
  document.querySelector('#d2e2 .solution').innerHTML = min_in_day_moon;
})(homework);