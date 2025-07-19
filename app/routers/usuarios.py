from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import schemas, models, database, auth
from fastapi.security import OAuth2PasswordRequestForm
router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------- REGISTRO ----------
@router.post("/registro", response_model=schemas.UsuarioOut)
def registrar_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    usuario_existente = db.query(models.Usuario).filter(models.Usuario.email == usuario.email).first()
    if usuario_existente:
        raise HTTPException(status_code=400, detail="El email ya está registrado")
    usuario_nuevo = models.Usuario(
        nombre=usuario.nombre,
        email=usuario.email,
        contraseña=auth.hashear_contraseña(usuario.contraseña)
    )
    db.add(usuario_nuevo)
    db.commit()
    db.refresh(usuario_nuevo)
    return usuario_nuevo

# ---------- LOGIN ----------
@router.post("/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter(models.Usuario.email == form_data.username).first()
    if not usuario or not auth.verificar_contraseña(form_data.password, usuario.contraseña):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    access_token = auth.crear_token_acceso(data={"sub": usuario.email})
    return {"access_token": access_token, "token_type": "bearer"}
