from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Usuario
from app.schemas import UsuarioCreate, UsuarioOut, Token
from app.auth import hashear_contraseña, verificar_contraseña, crear_token_acceso
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
import os

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

## Registro de usuario
@router.post("/registro", response_model=UsuarioOut)
def registrar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    usuario_existente = db.query(Usuario).filter(Usuario.email == usuario.email).first()
    if usuario_existente:
        raise HTTPException(status_code=400, detail="El email ya está registrado")
    usuario_nuevo = Usuario(
        nombre=usuario.nombre,
        email=usuario.email,
        contraseña=hashear_contraseña(usuario.contraseña)
    )
    db.add(usuario_nuevo)
    db.commit()
    db.refresh(usuario_nuevo)
    return usuario_nuevo

## Login de usuario
@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.email == form_data.username).first()
    if not usuario or not verificar_contraseña(form_data.password, usuario.contraseña):
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    access_token = crear_token_acceso(
        data={"sub": str(usuario.id)},
        expires_delta=timedelta(minutes=int(os.getenv("TOKEN_EXPIRA_MINUTOS")))
    )
    return {"access_token": access_token, "token_type": "bearer"}