# Spécifie l'image de base pour construire notre conteneur Docker
FROM python

# Définit le répertoire de travail pour notre application dans le conteneur
WORKDIR /app

# Copie le fichier requirements.txt depuis le répertoire de construction local vers le répertoire de travail dans le conteneur
COPY requirements.txt .

# Exécute la commande "pip install" pour installer les dépendances Python spécifiées dans requirements.txt
RUN pip install -r requirements.txt

# Copie le fichier app.py depuis le répertoire de construction local vers le répertoire de travail dans le conteneur
COPY app.py .

# Spécifie la commande par défaut à exécuter lorsque le conteneur est démarré
CMD [ "python", "./app.py" ]


