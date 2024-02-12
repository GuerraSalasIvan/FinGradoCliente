import requests

class helper:
    def obtener_lugares_select():
        response = requests.get('http://127.0.0.1:8000/api/v1/ubicacion')
        lugares = response.json()
        
        lista_lugares = [("","Ninguno")]
        for lugar in lugares:
            lista_lugares.append((lugar['id'],lugar['calle']))
        return lista_lugares
    
    def obtener_deportes_select():
        response = requests.get('http://127.0.0.1:8000/api/v1/deporte')
        deportes = response.json()
        lista_deportes = [("","Ninguno")]
        for deporte in deportes:
            lista_deportes.append((deporte['id'],deporte['deporte']))
        return lista_deportes
    
    def obtener_usuarios_select():
        response = requests.get('http://127.0.0.1:8000/api/v1/usuarios')
        usuarios = response.json()
        lista_usuarios = [("","Ninguno")]
        for usuario in usuarios:
            lista_usuarios.append((usuario['id'],usuario['rol']['first_name']))
        return lista_usuarios
    
    def obtener_ligas_select():
        response = requests.get('http://127.0.0.1:8000/api/v1/ligas')
        ligas = response.json()
        lista_ligas = []
        cont = 1
        for liga in ligas:
            lista_ligas.append((cont,liga['liga']))
            cont = cont + 1
        return lista_ligas
    
    def obtener_equipos_select():
        response = requests.get('http://127.0.0.1:8000/api/v1/equipos')
        equipos = response.json()
        lista_equipos = [("","Ninguno")]
        for equipo in equipos:
            lista_equipos.append((equipo['id'],equipo['nombre']))
        return lista_equipos
    
    def obtener_equipo(id):
        response = requests.get('http://127.0.0.1:8000/api/v1/equipos/'+str(id))
        equipo = response.json()
        return equipo
    
    def obtener_ubicacion(id):
        response = requests.get('http://127.0.0.1:8000/api/v1/ubicacion/'+str(id))
        ubicacion = response.json()
        return ubicacion
    
    def obtener_perfil_publico(id):
        response = requests.get('http://127.0.0.1:8000/api/v1/perfil_publico/'+str(id))
        perfil_publico = response.json()
        return perfil_publico
    