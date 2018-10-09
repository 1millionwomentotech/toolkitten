// 1.
const result1 = true && false;
let result1_answer = false

// 2.
const result2 = true || false;
let result2_answer = true

// 3. 
const result3 = true && (true || false);
let result3_answer = true

// 4. 
const result4 = !true || false;
let result4_answer = false

// 5. 
const result5 = !(true && false);
let result5_answer = true

// 6. 
const result6 = !undefined;
let result6_answer = true

// 7.
const likesPizza = true;
const hasPizza = false;
const eatsPizza = likesPizza && hasPizza;
const result7 = eatsPizza;
let result7_answer = false

// 8. 
const result8 = (null === undefined);
let result8_answer = false

// 9.
const result9 = (0 < 10) && true;
let result9_answer = true

// 10. 
const ordersPizza = true;
const makesPizza = false;
const hasPizza1 = ordersPizza || makesPizza;
const result10 = hasPizza1;
let result10_answer = true

// 11.
const firstName = 'Candice';
const lastName = null;
const hasFullName = !!firstName && !!lastName;
const result11 = hasFullName;
let result11_answer = false

// 12.
const emptyStr = '';
const result12 = !!emptyStr;
let result12_answer = false

// 13. 
const result13 = (true || false) === false;
let result13_answer = false

// 14.
const result14 = true && !false;
let result14_answer = true

// 15.
const hasPizza2 = true;
const canAffordGoodPizza = false;
const hasLowStandards = true;
const enjoysPizza = hasPizza2 && (canAffordGoodPizza || hasLowStandards);
const result15 = enjoysPizza;
let result15_answer = true


// STRETCH QUESTIONS (NOT REQUIRED)

// 16. 
const mondayHours = 4;
const tuesdayHours = 0;
const wednesdayHours = 2;
const workedThisWeek = (!!mondayHours || !!tuesdayHours || !!wednesdayHours);
const result16 = workedThisWeek;
let result16_answer = true

// 17.
const result17 = !(true && false) || (false && true);
let result17_answer = true

// 18.
const result18 = ((0 < 12) || !0) === false;
let result18_answer = false

// 19.
const orderedFood = false;
const madeFood = false;
const hasFood = orderedFood || madeFood;
const isHungry = true;
const likesFood = false;
const wantsFood = !hasFood && isHungry && likesFood;
const result19 = wantsFood;
let result19_answer = false

// 20. 
const result20 = !(!true || false) && !(false || (true && false));
let result20_answer = true