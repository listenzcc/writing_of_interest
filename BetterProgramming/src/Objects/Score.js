/*
File: Score.js
Aim: Example of the scoring object
*/

// We think the obj is the collection of scores.
// It records the raw scores and knows how to convert them into discrete scores.

// The raw scores
let obj = [79, 54, 80, 90];

// The scoring thresholds
obj.thresholds = {
    A: 90,
    B: 80,
    C: 70,
    D: 60,
    E: 0,
};

// Scoring the raw scores
obj.score = (e, i, t) => {
    for (let s in t.thresholds) {
        if (e >= t.thresholds[s]) {
            return [i, s];
        }
    }
};

// See what we got
// [ [ 0, 'C' ], [ 1, 'E' ], [ 2, 'B' ], [ 3, 'A' ] ]
console.log(obj.map(obj.score));
