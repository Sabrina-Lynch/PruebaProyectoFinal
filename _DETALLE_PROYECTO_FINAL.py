"""Proyecto Final: Sistema de Gestión de Biblioteca. 

Visión General del proyecto:
-	Objetivo Principal: Desarrollar una API funcional para gestionar préstamos de libros en una biblioteca, integrando todos los conceptos clave del curso en un proyecto realista y cohesivo. 
-	Tecnologías: Python, FastAPI, SQLAlchemy, SQLite, Git, JWT

Requisitos Clave: 
1)	Modelo de Datos (SQLAlchemy): Libros, Usuarios, Préstamos con relaciones 1:N.
2)	Endpoints (FastAPI): Autenticación JWT (/registro, /login) y CRUD básico (/libros, /prestar, /devolver).
3)	Validaciones: Un libro no puede prestarse si ya está en préstamo.

Configuración y Modelos:
a)	Setup Inicial: Crear entorno virtual, instalar dependencias, inicializar Git.
b)	Modelos SQLAlchemy: Definir clases en models.py (atributos, relaciones)
c)	Conexión a DB: Configurar SQLite con create_engine y sessionmaker.

Autenticación y Endpoints:
-	Autenticación JWT: Implementar /registro y /login con hash y tokens.
-	GET /libros: Consulta simple con SQLAlchemy.
-	POST /prestar: Verificar token, validar disponibilidad, registrar préstamo.

Lógica y Refinamiento
•	Devoluciones y Validaciones: Implementar POST /devolver/{id} y validar pertenencia del préstamo.
•	Testing y Documentación: Probar en Swagger UI y agregar descripciones a los endpoints.
•	Git y Preparación para Demo: Commits finales, push a GitHub, preparar script de demostración.

Clase Final: Demo y Resolución
•	Demo de Proyectos: Cada uno muestra funcionamiento básico, uso de Swagger UI y repositorio GitHub.
•	Resolución de Errores Comunes: Abordar problemas típicos: relaciones SQLAlchemy, tokens JWT, disponibilidad de libros.
•	Feedback y Cierre: Revisión de consignas y sugerencias de mejora.

Enfoque del Proyecto:
1.	Enfoque Incremental: Construir una base sólida: luego funcionalidad crítica y finalmente validaciones.
2.	Soluciones dentro del alcance: Errores claros para libros no disponibles; solo actualizar fecha de devolución.
3.	Gestión del Tiempo: Priorizar endpoints clave y usar datos "mock" si es necesario.

Notas Clave
1.	No añadir temas nuevos: Sin roles de usuario, sin frontend, sin despliegue en la nube.
2.	Priorizar integración: Que funcione el flujo básico (autenticación → CRUD → DB).
3.	Demo simple pero efectiva: Mostrar registro, login, préstamo y devolución

Elementos Opcionales
1.	Documentación en Swagger: Descripciones detalladas usando decoradores de FastAPI.
2.	Historial de Préstamos: Endpoint GET /mis-prestamos para préstamos activos del usuario.
3.	Script de Poblado Inicial de BD: Insertar datos de ejemplo al iniciar la app.
4.	Validación de Entradas con Regex: Validar formato de email y contraseña con Pydantic.
5.	Manejo de Errores Personalizados: Mensajes claros con HTTPException de FastAPI.
6.	Búsqueda de Libros: Filtrar libros por autor o título con parámetros de query.

"""