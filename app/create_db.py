from app.database import Base, engine
from app import models

print("Creando las tablas en la base de datos...")

Base.metadata.create_all(bind=engine)
print("¡Listo! Base de datos creada.")
