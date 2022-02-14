from get_module import get_info

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

def span_ind_efectividad(x, etiqueta):
    if len(x) > 0:
        span_ind_efectividad = genera_span(x)
        span_ind_efectividad = f"{etiqueta} <br> {span_ind_efectividad}"
    else:
        span_ind_efectividad = ""
    return span_ind_efectividad