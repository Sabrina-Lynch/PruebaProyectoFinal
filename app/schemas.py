from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


## USUARIOS

class UsuarioBase(BaseModel):
    nombre: str
    email: EmailStr

class UsuarioCreate(UsuarioBase):
    contraseña: str

class UsuarioOut(UsuarioBase):
    id: int
    class Config:
        from_attributes = True


## LIBROS

class LibroBase(BaseModel):
    titulo: str
    autor: str

class LibroCreate(LibroBase):
    pass

class LibroOut(LibroBase):
    id: int
    disponible: bool
    class Config:
        from_attributes = True

## PRÉSTAMOS

class PrestamoBase(BaseModel):
    libro_id: int

class PrestamoCreate(PrestamoBase):
    pass

class PrestamoOut(BaseModel):
    id: int
    usuario_id: int
    libro_id: int
    fecha_prestamo: datetime
    fecha_devolucion: Optional[datetime]
    class Config:
        from_attributes = True


## AUTENTICACIÓN

class LoginData(BaseModel):
    email: EmailStr
    contraseña: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"