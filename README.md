# Patchnote Helper
Un projet pour en apprendre d'avantage n8n et les llm.  

Le but de ce projet est de crée une aide à la lecture de patchnote de jeux video.  
On communqiue avec une IA à travers un bot discord. On peut lui demander des informations sur des nouvelles mis à jour de jeux vidéos

## Objectifs visés

- Faciliter la recherche et la consommation d’information
- Améliorer la qualité de l’information en apportant des informations complémentaires pertinentes
- Réduire le temps de consommation des changelogs

## Structure des fichiers 

```
PATCHNOTE_HELPER/
├── exploration/
│   ├── chroma/
│   ├── discord/
│   └── scraping/
├── src/
│   ├── .venv/
│   ├── discord_bot/
│   ├── worflows/
│   └── prompt.txt
├── .env.example
├── .gitignore
├── docker-compose.yml
└── README.md
```

Le dossier ``exploration`` contient des tests isolé de différents technologies

Le dossier `src` contient le projet en lui même, à savoir:
- Le code du bot discord (`src/discord_bot`)
- les workflows exporté de n8n (`src/workflows`)
- le prompt utilié par l'IA qui communique avec l'utilisateur (`src/promt.txt`)
- le docker-compose qui lance toute l'infrastructure (`docker-compose.yml`)
- la documentation des variables d'environnement nécessaire (`.env.example`)

## Fonctionnement

1. Preparer la base de donnée vectorielle (`src/workflows/get_data.json`)
2. Envoyer un message au bot discord
3. le worflow (`src/workflows/discord_response.json`) execute une recherche sémantique dans la base de donnée vectorielle
4. le llm récupère ces résultats et les synthétisent selon le message initial de l'utilisateur
5. Lire la réponse dans discord et apprécier ses nouvelles connaissances

## Lancement

la commande suivante lancera tous les logiciels nécessaires:
```sh 
docker compose up --build
```
- penser à copier et compléter le fichier `.env.example` et le renommer `.env`
- Il faudrat créer un bot discord et récupérer son jeton. le bot discord doit bénéficier de l'intent ``message_content``
