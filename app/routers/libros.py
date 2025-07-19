from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Libro
from app.schemas import LibroCreate, LibroOut

router = APIRouter(prefix="/libros", tags=["Libros"])

# Obtener todos los libros
@router.get("/", response_model=list[LibroOut])
def obtener_libros(db: Session = Depends(get_db)):
    return db.query(Libro).all()

# Crear un nuevo libro
@router.post("/", response_model=LibroOut)
def crear_libro(libro: LibroCreate, db: Session = Depends(get_db)):
    nuevo_libro = Libro(**libro.dict())
    db.add(nuevo_libro)
    db.commit()
    db.refresh(nuevo_libro)
    return nuevo_libro

# Obtener un libro por ID
@router.get("/{libro_id}", response_model=LibroOut)
def obtener_libro(libro_id: int, db: Session = Depends(get_db)):
    libro = db.query(Libro).filter(Libro.id == libro_id).first()
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return libro

# Eliminar un libro
@router.delete("/{libro_id}")
def eliminar_libro(libro_id: int, db: Session = Depends(get_db)):
    libro = db.query(Libro).filter(Libro.id == libro_id).first()
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    db.delete(libro)
    db.commit()
    return {"mensaje": "Libro eliminado correctamente"}
