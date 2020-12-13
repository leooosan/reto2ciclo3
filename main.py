from fastapi import FastAPI, HTTPException
import db

app = FastAPI()


@app.get("/reservas/")
async def obtener_reservas():
    reservas = db.obtener_reservas()
    return reservas


@app.post("/reservas/crear/")
async def crear_reserva(reserva: db.Reserva):
    creada_exitosamente = db.crear_reserva(reserva)
    if creada_exitosamente:
        return {"mensaje": "Reserva creada correctamente"}
    else:
        raise HTTPException(
            status_code=400, detail="error, Reserva con ese id ya exisitia")
