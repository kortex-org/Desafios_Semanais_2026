const categorias = {
    'infantil a': idade => idade <= 7,
    'infantil b': idade => idade <= 10,
    'juvenil a': idade => idade <= 13,
    'juvenil b': idade => idade <= 17,
    'adulto': idade => idade >= 18 
};

function classificarIdade(idade) {
    for (const [faixas, categoria] of Object.entries(categorias)) {
        if (categoria(idade)) return categoria
    }
};

console.log(classificarIdade(15));