from get_module import get_info

#modulo obtiene informacion del etapa preevolucion del pokemon

def obtener_pok_previo(pok_n):

    url_previa = f"https://pokeapi.co/api/v2/pokemon-species/{pok_n}"

    #se invoca al funcion get info para traer la info de la url_previa
    data_etapa_previa = get_info(url_previa)


    pok_etapa_previa = data_etapa_previa['evolves_from_species']

    if pok_etapa_previa is not None:
        pok_etapa_previa = pok_etapa_previa['name']

    else:
        pok_etapa_previa = "" #si no, pok etapa previa es vacío

    if pok_etapa_previa != "":
        pok_etapa_previa = f"Etapa anterior: {pok_etapa_previa}"

    return pok_etapa_previa
