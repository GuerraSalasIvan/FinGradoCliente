import requests

class helper:
       
    def obtener_lugares_select():
        response = requests.get('http://127.0.0.1:8000/api/v1/ubicacion')
        lugares = response.json()
        
        lista_lugares = [("","Ninguno")]
        for lugar in lugares:
            lista_lugares.append((lugar['id'],lugar['calle']))
        return lista_lugares
    
    def obtener_colores_select():
        response = requests.get('http://127.0.0.1:8000/api/v1/color')
        colores = response.json()
        
        lista_colores = [("","Ninguno")]
        for color in colores:
            lista_colores.append((color['id'],color['color']))
        return lista_colores
    
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
    
    def obtener_rel_equi_ubi():
        response = requests.get('http://127.0.0.1:8000/api/v1/rel_equi_ubi')
        rel_equi_ubi = response.json()
        return rel_equi_ubi
    
    def obtener_ubicacion(id):
        response = requests.get('http://127.0.0.1:8000/api/v1/ubicacion/'+str(id))
        ubicacion = response.json()
        return ubicacion
    
    def obtener_partido(id):
        response = requests.get('http://127.0.0.1:8000/api/v1/partido/'+str(id))
        partido = response.json()
        return partido
    
    def obtener_perfil_publico(id):
        response = requests.get('http://127.0.0.1:8000/api/v1/perfil_publico/'+str(id))
        perfil_publico = response.json()
        return perfil_publico
    
    def obtener_token_session(usuario,password):
        token_url = 'http://127.0.0.1:8000/oauth2/token/'
        data = {
            'grant_type': 'password',
            'username': usuario,
            'password': password,
            'client_id': 'app',
            'client_secret': 'app',
        }
        
        response = requests.post(token_url, data=data)
        respuesta = response.json()
        if response.status_code==200:
            return respuesta.get('access_token')
        else:
            raise Exception(respuesta.get("error_descripcion"))