from fastapi import FastAPI
from app.routers import libros, usuarios, prestamos

app = FastAPI(title="Sistema de Gestión de Biblioteca")

# Incluir los routers
app.include_router(usuarios.router)
app.include_router(libros.router)
app.include_router(prestamos.router)

@app.get("/")
def root():
    return {"mensaje": "Bienvenida al Sistema de Gestión de Biblioteca"}
