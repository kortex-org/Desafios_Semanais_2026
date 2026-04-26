const valorCompra = 10;

const descontos = {
    'credito': 5,
    'debito': 0,
    'pix': 10
};

const formaPagamento = "credito";
const desconto = descontos[formaPagamento] ?? 0; // nullish coalescing operator, conheci hoje 💀
const valorFinal = valorCompra - (valorCompra * (desconto / 100));

console.log(`Forma de Pagamento: ${formaPagamento}\nValor: ${valorCompra}\nValor + Desconto = ${valorFinal}`);
