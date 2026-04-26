const valores = [2, 3, 4];
let impar = [];
let par = [];

for (const valor of valores) {
    valor % 2 !== 0 && impar.push(valor)
    valor % 2 === 0 && par.push(valor)
};

console.log(`Pares: ${par.length}, Ímpares: ${impar.length}`);