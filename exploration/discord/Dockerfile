# Image de base Python
FROM python:3.11-slim

# Empêcher la création de fichiers .pyc et forcer l'affichage des logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Dossier de travail dans le conteneur
WORKDIR /app

# Copier uniquement requirements.txt pour profiter du cache Docker
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du projet
COPY . .

# Commande exécutée au démarrage du conteneur
CMD ["python", "bot.py"]
