import json
alumno = {"nombre": "Ana", "nota": 17}
texto = json.dumps(alumno) # diccionario -> texto JSON
print(texto, type(texto))
de_vuelta = json.loads(texto) # texto JSON -> diccionario
print(de_vuelta["nota"])