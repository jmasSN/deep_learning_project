import billboard
import pandas as pd 
import requests
import re


def get_data(date): #la date doit être au format YYYY-MM-DD
    chart = billboard.ChartData('hot-100', date= date) #permet de récuperer le top 100 billboard selon la date d'entrée
    data=[i for i in chart] #mise en liste du top chart. Un élément de la liste est un tuple associant l'artiste au nom de la musique

    with open("data_song.txt", "w") as doc: # création et écriture du fichier regroupant toutes les paroles 

        for son in data:
            url = f"https://api.lyrics.ovh/v1/{son.artist}/{son.title}" #Deuxième api utilisée permet de récupérer les paroles de la musique grâce à l'indice de la liste avec l'attribut artist et title permis par l'api billboard
            response = requests.get(url)
    
            if response.status_code == 200: #vérification de la réussite de la requête
                response = requests.get(url).json()  # récupération du contenu de la requête au format json
                lyrics_text= response['lyrics']    # seul la clé 'lyrics' nous intéresse 
                lyrics_net= re.sub("Paroles.*?\\r\\n","",lyrics_text) # nettoyage du titre des lyrics 
                
                doc.write(lyrics_net) 
                
    return "Dataset prêt, tu peux maintenant passer à la génération du model!"
                
         
        
