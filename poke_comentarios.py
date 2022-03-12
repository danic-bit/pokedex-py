#modulo obtiene informacion del etapa preevolucion del pokemon

import random
from get_module import get_info

def obtener_comentarios(pok_n):

    url_previa = f"https://pokeapi.co/api/v2/pokemon-species/{pok_n}"

    #se invoca al funcion get info para traer la info de la url_previa
    data_etapa_previa = get_info(url_previa)

    comentarios = data_etapa_previa["flavor_text_entries"]

    filtro = []
    for item in comentarios:
        if item["language"]["name"] == 'es':
            filtro.append(item["flavor_text"].replace("\n"," "))  #("\n"," ")se sustiyue el salto de linea por espacio en blanco

    pok_comentario = random.choice(filtro)
   
    return pok_comentario

if __name__ == '__main__':
    url_previa = f"https://pokeapi.co/api/v2/pokemon-species/25"
    print(obtener_comentarios(25))
