import requests

class helper:
    def obtener_lugares_select():
        response = requests.get('http://127.0.0.1:8000/api/v1/ubicacion')
        lugares = response.json()
        
        lista_lugares = [("","Ninguno")]
        for lugar in lugares:
            lista_lugares.append((lugar['nombre'],lugar['calle']))
        return lista_lugares
    
    def obtener_deportes_select():
        response = requests.get('http://127.0.0.1:8000/api/v1/deporte')
        deportes = response.json()
        lista_deportes = [("","Ninguno")]
        for deporte in deportes:
            lista_deportes.append((deporte['id'],deporte['deporte']))
        return lista_deportes
    
    def obtener_ligas_select():
        response = requests.get('http://127.0.0.1:8000/api/v1/ligas')
        ligas = response.json()
        lista_ligas = []
        cont = 1
        for liga in ligas:
            lista_ligas.append((cont,liga['liga']))
            cont = cont + 1
        return lista_ligas
    
    def obtener_equipo(id):
        response = requests.get('http://127.0.0.1:8000/api/v1/equipos/'+str(id))
        equipo = response.json()
        return equipo
    