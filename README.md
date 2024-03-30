# MakeUrTrend : génération de lyrics - Projet Deep Learning 2024 

MakeURtrend est une intelligence artificielle qui a pour objectif de générer des paroles de chansons tendances to make your own trend. 
Rentrez une date du top 100 Billboard et le début de la musique que vous souhaitez générer. 

## Modèles

- Cette IA utilise l'architecture d'un décodeur transformers, plus précisément GPT-2, disponible dans la bibliothèque Hugging Face. 
- Le résultat du modèle entraîné est présenté au moyen d'une interface web avec d'un côté une interface programmatique utilisable par un serveur ASGI, et de l'autre, une interface utilisateur. 

### Corpus 

Cette IA est entraînée sur les paroles de chansons du top 100 Billboard à la date choisie par l’utilisateur.
Le corpus est récolté au moyen de deux  API, la première pour avoir le top 100 Billboard avec le nom de l'artiste associé au titre de la musique et, la deuxième pour avoir les paroles de cette musique. Le script permettant la construction du corpus est [extract_dataset.py]()
Selon le TopChart du Billboard, les données peuvent être multilingues.

### Interface web 

Afin de lancer l'interface web et le serveur il faut : 
- se placer dans le dossier `scripts`, puis entrer dans le terminal : uvicorn interface:app 
- enfin, entrer l'adresse url suivante dans le moteur de recherche : ``http://localhost:8000/front/site_web.html``

### La documentation du projet 

Toute la documentation décrivant les étapes du projet se trouve sur l'interface utilisateur. 
