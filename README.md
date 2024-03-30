# MakeUrTrend : génération de lyrics - Projet Deep Learning 2024 

MakeURtrend est une intelligence artificielle qui a pour objectif de générer des paroles de chansons. Elle tire parti d'un modèle basé sur l'architecture des transformers, plus précisément GPT-2, disponible dans la bibliothèque Hugging Face. 

### Corpus 

Cette IA a été entraînée sur une vaste quantité de données comprenant des paroles de chansons populaires soit du top 100 Billboard présentes à la date rentrée par l’utilisateur.

Laissez le choix de la date d’extraction des chansons à l’utilisateur permet de le laisser générer des paroles de style varié. Une première API (Billboard100) a été utilisée afin de récupérer le Chart des 100 premières musiques du Billboard. Ces données correspondent aux titres de la musique associée à leurs artistes Ensuite, une deuxième API (LyricsOVH ) nous a permis, sur la base du nom de la musique et de l'artiste, de récuperer les paroles de cette chanson. Seules les paroles ont été conservées pour créer le dataset qui correspond à un fichier texte contenant l’intégralité des paroles du top 100. Aucun traitement supplémentaire, excepté la suppression du titre, n’a été nécéssaire sur les données et c’est la division en paragraphe qui est utilisé pour tokeniser.
Selon le TopChart du Billboard, les données peuvent être multilingues.

### Codes


### Interface web 

Afin de lancer l'interface web et le serveur il faut : 
- rentrer dans le terminal : uvicorn interface:app 
- puis, rentrer l'adresse url suivante dans le moteur de recherche : ``http://localhost:8000/front/site_web.html``

### La documentation du projet 

Toute la documentation décrivant les étapes du projet se trouve sur l'interface utilisateur. 
