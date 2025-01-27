import requests
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("API_KEY")

def buscar_genero():

    url = "https://moviesdatabase.p.rapidapi.com/titles/utils/genres"

    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "moviesdatabase.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    print(response)

    return response.json()







def buscar_peliculas (genero, ano, pagina):

    url = "https://moviesdatabase.p.rapidapi.com/titles"

    querystring = {"genre":genero,"year":ano,"page":pagina,"limit":"50"}

    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "moviesdatabase.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response.json()




def obtener_datos (dicc_peliculas):
    todas_pelis = {}
    for genero in dicc_peliculas.keys():
        for llamada in dicc_peliculas[genero]:
            try:
                for pelicula in llamada['results']:
                    lista_peli=[]
                    lista_peli.append(pelicula['titleText']['text']) #Titulo
                    lista_peli.append(pelicula['titleType']['text']) #Type
                    lista_peli.append(genero)#Genero
                    lista_peli.append(pelicula['releaseYear']['year'])#año
                    todas_pelis[pelicula['id']] = lista_peli
            except:
                pass

    return todas_pelis

