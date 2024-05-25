from flask import Flask, request, jsonify, render_template
import random
import string

app = Flask(__name__)

def generate_password(length=12, include_uppercase=True, include_numbers=True, include_special_chars=True):
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_password', methods=['POST'])
def generate_password_endpoint():
    data = request.json
    length = data.get('length', 12)
    include_uppercase = data.get('include_uppercase', True)
    include_numbers = data.get('include_numbers', True)
    include_special_chars = data.get('include_special_chars', True)

    password = generate_password(length, include_uppercase, include_numbers, include_special_chars)
    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(debug=True)
