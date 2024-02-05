import requests

class helper:
    def obtener_lugares_select():
        response = requests.get('http://127.0.0.1:8000/api/v1/perfil_publico')
        lugares = response.json()
        
        lista_lugares = [("","Ninguna")]
        for lugar in lugares:
            lista_lugares.append(lugar['lugar_fav'])
        return lista_lugares