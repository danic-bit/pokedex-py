import string
import sys
import json
import requests
import random
import poke_validation as pv
from get_module import get_info
from etapa_previa import obtener_pok_previo
from poke_comentarios import obtener_comentarios
from poke_span import genera_span
from string import Template

name = input ("Introduzca el nombre del Pokemon a buscar :")

name = pv.validate(name)

url_base = f'https://pokeapi.co/api/v2/pokemon/{name}'

data_base = get_info(url_base) #get_info es la funcion creada en get_module.

name = name.capitalize()

pok_n = data_base["id"]
#print(pok_n)

stats = data_base ["stats"]

indicadores = [item["base_stat"] for item in stats]

#ahora se iguala cada variable a un elemento de la lista (que sabemos es fija), separado por comas
pok_hp, pok_at, pok_de, pok_ate, pok_dee, pok_ve = indicadores


#obtencion de la imagen (url)
pok_img = data_base['sprites']['front_default']


#genera comentario
pok_etapa_previa = obtener_pok_previo(pok_n)


# sacar los TIPOS
tipos_lista = data_base["types"]
tipos = [item["type"]["name"] for item in tipos_lista]

# ahora se Procesa el comentario sobre el pokemon en español
pok_comentario = obtener_comentarios(pok_n)

### Generacion span tipos
span_tipo = f"Tipo <br> {genera_span(tipos)}"

### Generacion fortalezas y debilidades

url_danio = [item["type"]["url"] for item in tipos_lista]   

# obtencion de indicadores de combate

def info_combate(x):
    
    if len(url_danio) == 1:
        data_rel1 = get_info(url_danio[0])
        efectividad = data_rel1["damage_relations"][x]   

    else:
        data_rel1 = get_info(url_danio[0])
        data_rel2 = get_info(url_danio[1])
        efectividad = data_rel1["damage_relations"][x] + data_rel2["damage_relations"][x] 
        
    ind_efectividad =[item["name"] for item in efectividad]

    return set(ind_efectividad)

supef_co = info_combate("double_damage_to") 
deb_co = info_combate("double_damage_from")
res_co = info_combate("half_damage_from")
poef_co = info_combate("half_damage_to")
inm_co = info_combate("no_damage_from")
inef_co = info_combate("no_damage_to")

# obtencion de span de indicadores de combate (se condiciona la salida al html de cada span, solo si existe el indicador para cada pokemon)

def span_ind_efectividad(x, etiqueta):
    if len(x) > 0:
        span_ind_efectividad = genera_span(x)
        span_ind_efectividad = f"{etiqueta} <br> {span_ind_efectividad}"
    else:
        span_ind_efectividad = ""
    return span_ind_efectividad

span_supef_co = span_ind_efectividad(supef_co, "Super Efectivo contra: ")
span_deb_co = span_ind_efectividad(deb_co, "Debil contra: ")
span_res_co = span_ind_efectividad(res_co, "Resistente contra: ")
span_poef_co = span_ind_efectividad(poef_co, "Poco eficiente contra :")
span_inm_co = span_ind_efectividad(inm_co, "Inmune contra :")
span_inef_co = span_ind_efectividad(inef_co, "Ineficiente contra :")


###Generación del html de salida

with open('base_pok.html', 'r') as infile:
    entrada = infile.read()

document_template = Template(entrada)

#se definen los valores de las variables que se va a insertar en el template

document_template_nuevo = document_template.safe_substitute(  #document_template_nuevo recibe lo que se va a sustituir
    pok_n = pok_n,                                            #debe respetarse el orden nombre_var_html = nombre_var_python
    pok_name = name,                                          #como hay más de 1 variable, se separan por coma
    pok_etapa_previa = pok_etapa_previa,
    pok_hp = pok_hp,
    pok_at = pok_at,
    pok_de = pok_de, 
    pok_ate = pok_ate, 
    pok_dee = pok_dee, 
    pok_ve = pok_ve,
    pok_img = pok_img,
    span_tipo = span_tipo,
    pok_comentario = pok_comentario,
    span_supef_co = span_supef_co,
    span_deb_co = span_deb_co,
    span_res_co = span_res_co,
    span_poef_co = span_poef_co,
    span_inm_co = span_inm_co,
    span_inef_co = span_inef_co)

with open('salida_pok.html','w') as f:
    f.write(document_template_nuevo)
