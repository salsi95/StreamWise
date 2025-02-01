import requests
from dotenv import load_dotenv
import os
load_dotenv()

import numpy as np

api_key = os.getenv("API_KEY")

def buscar_genero_api():

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


def buscar_genero (df):
    dicc_generos = {}
    for i in range(df.shape[0]):
        if df.iloc[i,0] in dicc_generos:
            dicc_generos[df.iloc[i,0]].append(df.iloc[i,3])
        else:
            dicc_generos[df.iloc[i,0]] = [df.iloc[i,3]]
    return dicc_generos


def aplicar_generos(col_index, dicc_generos):
    if col_index in dicc_generos:

        lista = dicc_generos[col_index]
        dicc_generos.pop(col_index)
        return lista
    else:
        return np.nan