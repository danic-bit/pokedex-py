# pokedex-py
Conexion y consumo de APIs

Ejecutar archivo main.py -> ingresar nombre pokemon -> resultados en salida_pok.html

Se utlizan librerias json y requests para obtención de datos desde PokéApi, documentación disponible en : https://pokeapi.co/docs/v2.

El proyecto incluye la renderización de:
-Imagen del pokemon (version frontal normal)
-Nombre pohemon etapa previa (si aparece)
-Estadísticas
-Tipo
-Comentario, mensaje en español y aleatorio
-Indicadores de combate (super eficaz contra, debil contra, resistente contra, poco eficiente contra, inmune contra, ineficaz contra, etc).
Renderización condicionada a las caractéristicas de cada pokemon, según su tipo. Si no posee algunos de estos indicadores, no aparece la etiqueta ni el tipo.

Se crean funciones para generar un codigo más eficiente (por ej., def info_combate linea 58)
Incluye modularización: validacion, generacion span, generacion comentarios, obtencion etapa previa, entre otros.
