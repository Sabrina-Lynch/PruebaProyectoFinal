from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from app.database import get_db
from app.models import Prestamo, Libro
from app.schemas import PrestamoCreate, PrestamoOut
from app.auth import get_current_user
from app.models import Usuario

router = APIRouter(prefix="/prestamos", tags=["Préstamos"])

## Crear un nuevo préstamo

@router.post("/", response_model=PrestamoOut)

def crear_prestamo(
    prestamo: PrestamoCreate,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
):
    libro = db.query(Libro).filter(Libro.id == prestamo.libro_id).first()
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    if not libro.disponible:
        raise HTTPException(status_code=400, detail="El libro no está disponible")
    nuevo_prestamo = Prestamo(libro_id=prestamo.libro_id, usuario_id=usuario.id)
    libro.disponible = False
    db.add(nuevo_prestamo)
    db.commit()
    db.refresh(nuevo_prestamo)
    return nuevo_prestamo


## Devolver un libro

@router.put("/{prestamo_id}/devolver", response_model=PrestamoOut)

def devolver_libro(
    prestamo_id: int,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
):
    prestamo = db.query(Prestamo).filter(Prestamo.id == prestamo_id).first()
    if not prestamo:
        raise HTTPException(status_code=404, detail="Préstamo no encontrado")
    if prestamo.usuario_id != usuario.id:
        raise HTTPException(status_code=403, detail="No puedes devolver un libro que no pediste")
    if prestamo.fecha_devolucion:
        raise HTTPException(status_code=400, detail="El libro ya fue devuelto")
    prestamo.fecha_devolucion = datetime.utcnow()
    libro = db.query(Libro).filter(Libro.id == prestamo.libro_id).first()
    libro.disponible = True
    db.commit()
    db.refresh(prestamo)
    return prestamo


## Obtener todos los préstamos del usuario autenticado

@router.get("/mis-prestamos", response_model=list[PrestamoOut])

def obtener_mis_prestamos(
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
):
    return db.query(Prestamo).filter(Prestamo.usuario_id == usuario.id).all()
