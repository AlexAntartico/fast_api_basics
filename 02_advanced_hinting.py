# Importa los tipos de datos List, Tuple y Dict del módulo typing
from typing import List, Tuple, Dict

# Anota datos básicos con Python 3.9 y versiones anteriores
price: List[int] = [213, 234, 984]  # Lista de enteros llamada 'price'
immutable_price: Tuple[int, int, int] = (231, 983, 704)  # Tupla inmutable de enteros llamada 'immutable_price'
price_dict: Dict[str, int] = {  # Diccionario con claves de tipo str y valores de tipo int llamado 'price_dict'
    'item': 123,
    'item2': 234,
}

# Anota datos básicos con versiones más recientes de Python (3.10+)
new_price: list[int] = [14, 312, 567]  # Lista de enteros llamada 'new_price' (sintaxis simplificada)
new_immutable_price: tuple[int, int, int] = (34, 542, 713)  # Tupla inmutable de enteros llamada 'new_immutable_price' (sintaxis simplificada)
new_price_dict: dict[str, int] = {  # Diccionario con claves de tipo str y valores de tipo int llamado 'new_price_dict' (sintaxis simplificada)
    'item1': 123,
    'item2': 312,
}

# Anotación con estructuras de datos complejas en Python 3.9 y versiones anteriores
from typing import Union  # Importa Union para indicar tipos de datos alternativos

x: List[Union[int, float]] = [1, 23, 4, .6]  # Lista que puede contener enteros o flotantes

# Anotación con estructuras de datos complejas en Python 3.10 y versiones posteriores
from typing import List  # Importa List (aunque ya se importó antes, se incluye aquí para mayor claridad)

y: list[Union[int | float]] = [1, 23, 4, .6]  # Lista que puede contener enteros o flotantes (sintaxis simplificada con |)


# para correr snippets ctrl + enter en vscode
from typing import Union

def mxn_to_usd(value:float) -> Union[float,None]:
    try:
        convertion_factor = 20.1
        value = value/convertion_factor
        return value
    except TypeError:
        return None

# mxn_to_usd('dfad')  # will return none
mxn_to_usd(780.3)  # will return conversion


