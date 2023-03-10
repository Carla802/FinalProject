import os
from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient

# Créer une instance de l'application Flask
app = Flask(__name__)

# Connecter à la base de données MongoDB
client = MongoClient('my-mongo-projet')

# Récupérer une référence à la base de données 'mydb'
db = client.mydb

# Créer une collection 'users' dans la base de données 'mydb'
collection = db.users

# Insérer plusieurs documents dans la collection 'users'
posts = [
    {"username": "Laura Llinares", "password": "22"},
    {"username": "Karim Benzema", "password": "34"},
    {"username": "Jolyane Mak", "password": "8"},
    {"username": "Timothé", "password": "21"}
]
collection.insert_many(posts)

# Définir la route pour la page de connexion ('login')
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Récupérer le nom d'utilisateur et le mot de passe depuis le formulaire
        username = request.form['username']
        password = request.form['password']
        # Vérifier si l'utilisateur existe dans la base de données
        user = db.users.find_one({'username': username, 'password': password})
        if user:
            # Si l'utilisateur existe, sauvegarder son nom d'utilisateur dans une variable de session
            session['username'] = username
            return redirect(url_for('file_content'))
        else:
            # Si l'utilisateur n'existe pas, afficher un message d'erreur
            error = 'Invalid login credentials'
            return render_template('login.html', error=error)
    else:
        # Si la méthode HTTP est 'GET', afficher la page de connexion
        return render_template('login.html')

# Définir la route pour afficher le contenu du fichier ('file_content')
@app.route('/file_content')
def file_content():
    # Vérifier si l'utilisateur est connecté
    if 'username' not in session:
        return redirect(url_for('login'))
    # Lire le contenu du fichier et le retourner
    with open('/app/TEST.txt', 'r') as f:
        content = f.read()
    return f'Hello {session["username"]}! Here is the content of the file: {content}'

# Exécuter l'application Flask
if __name__ == '__main__':
    # Générer une clé secrète pour la session
    app.secret_key = os.urandom(24)
    # Lancer l'application sur l'adresse '0.0.0.0' et le port '5000'
    app.run(host='0.0.0.0', port=5000, debug=True)
