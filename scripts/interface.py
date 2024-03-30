from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from extract_dataset import get_data
from lyrics_generator import def_model

app = FastAPI()


app.mount("/front", StaticFiles(directory="../static"), name="front")


class InputData(BaseModel):  # création des classes de nos inputs utilisateurs
    sentence: str
    
class Prompt(BaseModel):
    prompt: str

@app.post("/dataset")
async def dataset(inpt: InputData):
    
    i= get_data(inpt.sentence) # permet, grâce à la fonction get_data du fichier extract_dataset, de récupérer notre corpus avec la date rentrée par l'utilisateur

    above = """<!DOCTYPE html>
<html lang="en">
  <head>
    <link rel="stylesheet" href="styles.css">
    <meta charset="utf-8" />
    <title>This is the dataset</title>
  </head>
  <body>
  <ol>
  <h3>
"""
    below = """
    </h3>
  </ol>
  </body>
</html>
"""

    html_content = "\n".join([above, i, below])
    return HTMLResponse(content=html_content, status_code=200) #renvoie le return de la fonction "get_data" indiquant la fin du chargement de la collecte de data
    

    
@app.post("/generate")
async def generate(inpt:Prompt):  
    
    generated= def_model(inpt.prompt)   # permet de récupérer la fonction qui entraine notre modèle du fichier lyric_generator 
        
    above = """<!DOCTYPE html>
<html lang="en">
  <head>
    <link rel="stylesheet" href="styles.css">
    <meta charset="utf-8" />
    <title>Hey ! Here's your TRENDY song based on the hot 100 billboard!!</title>
  </head>
  <body>
  <ol>
  <h3>
"""
    below = """
    </h3>
  </ol>
  </body>
</html>
"""
   
    html_contentt = "\n".join([above, generated, below])
    return HTMLResponse(content=html_contentt, status_code=200) # renvoie les paroles de lyrics générées
    






