// Aqui o código está definindo que quando o formulário com ID password-form for enviado, essa função deve ser executada.
document.getElementById('password-form').addEventListener('submit', async function(event) {
    // Aqui o código está definindo que quando o formulário com ID password-form for enviado, essa função deve ser executada.
    event.preventDefault();
    
    // Pega o valor digitado no campo de comprimento da senha e transforma em número.
    const length = parseInt(document.getElementById('length').value);
    // Verifica se as checkbox estão marcadas (true ou false).
    const includeUppercase = document.getElementById('include-uppercase').checked;
    const includeNumbers = document.getElementById('include-numbers').checked;
    const includeSpecialChars = document.getElementById('include-special-chars').checked;
    
    // Envia uma requisição POST para o backend Flask, com os dados do formulário convertidos em JSON. O Flask usa essas informações para gerar a senha com base nas opções selecionadas.
    const response = await fetch('/generate_password', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            length: length,
            include_uppercase: includeUppercase,
            include_numbers: includeNumbers,
            include_special_chars: includeSpecialChars
        }),
    });
    
    // “Espera” a resposta do servidor (no formato JSON). Aqui ele pega a senha gerada que o Flask retornou.
    const result = await response.json();
    
    // Exibe a senha gerada dentro da <div id="result"> na tela.
    document.getElementById('result').textContent = `Senha gerada: ${result.password}`;
});
