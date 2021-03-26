/*
File: HashTable.js
Aim: Example of hash table.
*/

// The size of the table
const size = 7;

// The hash seed parameter
const I64BIT_TABLE = "0123456789abcdef".split("");

// Compute hash value
function hash(input) {
    var hash = 5381;
    var i = input.length - 1;

    if (typeof input == "string") {
        for (; i > -1; i--) hash += (hash << 5) + input.charCodeAt(i);
    } else {
        for (; i > -1; i--) hash += (hash << 5) + input[i];
    }
    var value = hash & 0x7fffffff;

    var retValue = "";
    do {
        retValue += I64BIT_TABLE[value & 0xf];
    } while ((value >>= 6));

    return retValue;
}

// Convert hash value to idx of hash table
function hash2idx(h) {
    const hex = "0x" + h;
    return parseInt(hex) % size;
}

// Init empty hash table
let table = [];
for (let i = 0; i < size; i++) {
    table[i] = undefined;
}

// The pairs to be restored in the hash table
const pairs = {
    AliceBlue: "#F0F8FF",
    AntiqueWhite: "#FAEBD7",
    Aqua: "#00FFFF",
    Aquamarine: "#7FFFD4",
    Azure: "#F0FFFF",
    Beige: "#F5F5DC",
    Bisque: "#FFE4C4",
    Black: "#000000",
    BlanchedAlmond: "#FFEBCD",
};

// Insert the pairs in to the hash table
console.log("Inserting hash table");
for (const name in pairs) {
    const h = hash(name);
    const i = hash2idx(h);
    console.log("\t", name, "->", h, "->", i);

    if (table[i] === undefined) {
        table[i] = [[name, pairs[name]]];
    } else {
        table[i].push([name, pairs[name]]);
    }
}

// The generated hash table
console.log("Hash table is");
console.log(table);

/*
The output reads as following:
Inserting hash table
         AliceBlue -> bc4bc1 -> 1
         AntiqueWhite -> db6231 -> 4
         Aqua -> d345c1 -> 2
         Aquamarine -> 9c1c31 -> 4
         Azure -> cf28f -> 1
         Beige -> 18f7f -> 1
         Bisque -> e42fb1 -> 2
         Black -> 2931f -> 0
         BlanchedAlmond -> 1b398 -> 2
Hash table is
[ [ [ 'Black', '#000000' ] ],
  [ [ 'AliceBlue', '#F0F8FF' ],
    [ 'Azure', '#F0FFFF' ],
    [ 'Beige', '#F5F5DC' ] ],
  [ [ 'Aqua', '#00FFFF' ],
    [ 'Bisque', '#FFE4C4' ],
    [ 'BlanchedAlmond', '#FFEBCD' ] ],
  undefined,
  [ [ 'AntiqueWhite', '#FAEBD7' ], [ 'Aquamarine', '#7FFFD4' ] ],
  undefined,
  undefined ]
*/
