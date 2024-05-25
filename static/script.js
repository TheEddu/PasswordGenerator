document.getElementById('password-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    
    // Capturar valores do formulário
    const length = parseInt(document.getElementById('length').value);
    const includeUppercase = document.getElementById('include-uppercase').checked;
    const includeNumbers = document.getElementById('include-numbers').checked;
    const includeSpecialChars = document.getElementById('include-special-chars').checked;
    
    // Enviar dados para o backend Flask
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
    
    // Receber a resposta do backend
    const result = await response.json();
    
    // Exibir a senha gerada
    document.getElementById('result').textContent = `Senha gerada: ${result.password}`;
});
