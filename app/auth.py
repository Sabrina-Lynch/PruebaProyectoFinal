from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

# Cargar variables del archivo .env

load_dotenv()

SECRET_KEY = os.getenv("API_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("TOKEN_EXPIRA_MINUTOS"))

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verificar_contraseña(contraseña_plana, contraseña_hashed):
    return pwd_context.verify(contraseña_plana, contraseña_hashed)


def hashear_contraseña(contraseña):
    return pwd_context.hash(contraseña)


def crear_token_acceso(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
