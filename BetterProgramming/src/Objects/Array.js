/*
File: Array.js
Aim: Example of array.
     Explain why it is good or bad.
*/

// Generate array
// Assume it is very long, like 1,000,000 elements.
let arr = [4, 5, 70, 29, ...., ];

// Example of Good
// Access to the 7,364th element,
// it only requires ONE operation.
console.log("The 7,364th element is", arr[7363]);

// Example of Bad
// Tell if 365 is in the array, and where it first appears,
// it may require 1,000,000 operations to find an answer.
let found = false;
for (let i = 0; i <arr.length; i++) {
    if (arr[i] === 365) {
        console.log("Found 365 in the array at", i)
        found = true;
        return
    }
}
if (!found) {
    console.log("The 365 is not in the array")
}