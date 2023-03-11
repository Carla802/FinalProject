import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
from pymongo import MongoClient
from bson.objectid import ObjectId



# Créer une instance de l'application Flask
app = Flask(__name__)

# Connecter à la base de données MongoDB
client = MongoClient('my-mongo-projet')

# Récupérer une référence à la base de données 'mydb'
db = client.mydbprojet

# Créer une collection 'users' dans la base de données 'mydb'
collection = db.users

# Insérer plusieurs documents dans la collection 'users'
posts = [
    {"username": "Laura Llinares", "password": "22", "role": "user"},
    {"username": "Karim Benzema", "password": "34", "role": "admin"},
    {"username": "Jolyane Mak", "password": "8", "role": "user"},
    {"username": "Timothé", "password": "21", "role": "user"}
]
if db.users.count_documents({}) == 0:
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
            session['role'] = user['role']
            return redirect(url_for('file_content'))
        else:
            # Si l'utilisateur n'existe pas, afficher un message d'erreur
            error = 'Invalid login credentials'
            return render_template('login.html', error=error)
    else:
        # Si la méthode HTTP est 'GET', afficher la page de connexion
        return render_template('login.html')

# Définir la route pour la page d'inscription ('register')
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Récupérer le nom d'utilisateur et le mot de passe depuis le formulaire
        username = request.form['username']
        password = request.form['password']
        # Vérifier si l'utilisateur existe déjà dans la base de données
        if db.users.find_one({'username': username}):
            error = 'Username already taken'
            return render_template('register.html', error=error)
        else:
            # Ajouter le nouvel utilisateur à la base de données
            new_user = {"username": username, "password": password, "role": "user"}
            db.users.insert_one(new_user)
            # Rediriger l'utilisateur vers la page de connexion
            return redirect(url_for('login'))
    else:
        # Si la méthode HTTP est 'GET', afficher la page d'inscription
        return render_template('register.html')


@app.route('/file_content')
def file_content():
    # Vérifier si l'utilisateur est connecté
    if 'username' not in session:
        return redirect(url_for('login'))

    # Récupérer tous les noms d'utilisateur de la base de données
    users = db.users.find()
    print(db.users.find())

    # Lire le contenu du fichier et le retourner avec les noms d'utilisateur
    with open('/app/TEST.txt', 'r') as f:
        content = f.read()
    return render_template('file_content.html',content=content, users=users)



@app.route('/delete_user/<user_id>')
def delete_user(user_id):
    # Vérifier si l'utilisateur est connecté
    if 'username' not in session:
        return redirect(url_for('login'))

   
   
    # Supprimer l'utilisateur de la base de données
    result = db.users.delete_one({'_id': ObjectId(user_id)})
    

    return redirect(url_for('file_content'))


@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)
    session.pop('role', None)
    return redirect(url_for('login'))



@app.route('/edit/<user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    user = collection.find_one({'_id': ObjectId(user_id)})
    if request.method == 'POST':
        username = request.form['username']
        role = request.form['role']
        collection.update_one({'_id': ObjectId(user_id)}, {'$set': {'username': username, 'role': role}})
        return redirect(url_for('file_content'))
    return render_template('edit_user.html', user=user)
    return render_template('file_content.html',content=content, users=users)




# Exécuter l'application Flask
if __name__ == '__main__':
    # Générer une clé secrète pour la session
    app.secret_key = os.urandom(24)
    # Lancer l'application sur l'adresse '0.0.0.0' et le port '5000'
    app.run(host='0.0.0.0', port=5000, debug=True)
