// Q3

const height = 5;
for (let i = 0; i < height; i++) {
    let spaces = " ".repeat(height - i - 1);
    let leaves = "X".repeat(2 * i + 1);

    console.log(spaces + leaves);
};

console.log(" ".repeat(height - 1) + "X");
