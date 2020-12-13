from pydantic import BaseModel


class Reserva(BaseModel):
    id: int
    quien_reserva: str
    fecha_entrada: str
    fecha_salida: str
    numero_noches: int
    tipo_habitacion: str
    numero_personas: int
    numero_habitacion: int
    precio: int


reservas = {
    1: Reserva(id=1, quien_reserva="Leonardo Santos",fecha_entrada="20-11-2020", fecha_salida="18-12-2020",numero_noches=15, tipo_habitacion="doble", numero_personas=2,numero_habitacion=106,precio=285000),
    2: Reserva(id=2, quien_reserva="Andres Gomez",fecha_entrada="10-12-2020", fecha_salida="14-12-2020",numero_noches=4, tipo_habitacion="sencilla", numero_personas=1,numero_habitacion=109,precio=96000)
}


def obtener_reservas():
    # Haga lo que tenga que hacer para conectarse a la base de datos y obtener todas las reservas
    lista_reservas = []
    for e in reservas:
        lista_reservas.append(reservas[e])
    return lista_reservas


def crear_reserva(reserva: Reserva):
    if reserva.id in reservas:
        return False
    else:
        reservas[reserva.id] = reserva
        return True
