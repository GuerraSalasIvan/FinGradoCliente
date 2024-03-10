# FinGradoCliente

Esta es la version cliente de la Api Fomento.

Para acceder a los datos de la api usamos la clase *helper*, la cual tiene tipos de metodos posibles:

Siendo x un modelo en la api:
- obtener_x_list() 
    Obtenemos 2 valores, un id y otra valor representativo del modelo x para usarlos en un selector

- obtener_x(x_id):
    Obtenemos todos los campos de una instancia de un modelo en concreto

A veces necesitamos coger todos los registros de un modelo, para ello, llamo directamente a la api desde la view y guardo el resultado en un variable.


En *url.py* encontramos todas las peticiones que podemos realizar con nuestro cliente.

En *view.py* encontramos todas las funciones necesarias para que nuestra api funcione, en estas, destacamos *equipos_lista_api*, que es nuestra pagina de inicia, en ella vemos todos los equipos registrados en la base de datos y un calendario que nos marca los dias que hay partidos programados de este mes.
