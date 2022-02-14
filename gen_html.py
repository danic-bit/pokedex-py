
def generacion_html():

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