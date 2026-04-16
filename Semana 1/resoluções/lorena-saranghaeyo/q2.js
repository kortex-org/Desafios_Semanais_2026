// Q2

const student = true;
const credits = true;
const restaurant = true;
// const result = restaurant && (student || credits); // Am I wrong?
const result = student || (credits && restaurant); // Can enter even if the restaurant is closed?

console.log(result ? "$1$" : "$0$");
