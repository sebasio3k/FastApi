# FastAPI Course 🚀

Repositorio de aprendizaje y práctica para el desarrollo de APIs modernas con **FastAPI** y Python.

Este proyecto reúne los conceptos y herramientas principales utilizados durante el curso, desde la creación de endpoints y validación de datos hasta bases de datos, autenticación, programación asíncrona y migraciones.

## 📚 Temas del curso

Durante el desarrollo de este proyecto se trabajan, entre otros, los siguientes conceptos:

- ⚡ **FastAPI**
- 🐍 **Python**
- 📦 **Pydantic**
- 🗄️ **Bases de datos**
- 🔗 **SQLAlchemy**
- 🧩 **SQLModel**
- 🔐 **JWT (JSON Web Tokens)**
- 🔄 **Funciones síncronas y asíncronas**
- 🧱 **Middlewares**
- 🗃️ **Alembic**
- 🌐 **APIs REST**
- 📋 Validación y serialización de datos
- 🚨 Manejo de errores y excepciones HTTP
- 🔑 Autenticación y autorización
- 📖 Documentación automática de APIs
- Y más conceptos relacionados con el desarrollo backend en Python.

## 🛠️ Tecnologías

| Tecnología | Uso |
|---|---|
| Python | Lenguaje principal |
| FastAPI | Framework para construir la API |
| Pydantic | Validación y manejo de datos |
| SQLAlchemy | ORM y acceso a bases de datos |
| SQLModel | Modelos y persistencia de datos |
| Alembic | Migraciones de base de datos |
| JWT | Autenticación basada en tokens |

## 📁 Estructura del proyecto

La estructura puede evolucionar conforme avanza el curso. Una posible organización es:

```text
fastapi-course/
│
├── app/
│   ├── main.py
│   ├── models/
│   ├── schemas/
│   ├── routes/
│   ├── services/
│   ├── database/
│   └── middleware/
│
├── alembic/
│   └── versions/
│
├── tests/
│
├── .env
├── alembic.ini
├── requirements.txt
└── README.md
```

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone <repository-url>
cd fastapi-course
```

### 2. Crear un entorno virtual

```bash
python -m venv .venv
```

Activarlo:

**macOS / Linux**

```bash
source .venv/bin/activate
```

**Windows**

```powershell
.venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

## ▶️ Ejecutar la aplicación

Para iniciar el servidor de desarrollo:

```bash
uvicorn app.main:app --reload
```

La API estará disponible en:

```text
http://127.0.0.1:8000
```

FastAPI proporciona automáticamente documentación interactiva:

- Swagger UI: `/docs`
- ReDoc: `/redoc`

Por ejemplo:

```text
http://127.0.0.1:8000/docs
```

## 🗄️ Base de datos y migraciones

El proyecto utiliza herramientas como **SQLAlchemy**, **SQLModel** y **Alembic** para trabajar con bases de datos.

Para crear una nueva migración:

```bash
alembic revision --autogenerate -m "description"
```

Aplicar las migraciones:

```bash
alembic upgrade head
```

Consultar el estado actual:

```bash
alembic current
```

## 🔐 Autenticación

Durante el curso se implementa autenticación utilizando **JWT (JSON Web Tokens)**.

El flujo básico consiste en:

```text
Cliente
   │
   │ Login
   ▼
FastAPI
   │
   │ Verifica credenciales
   ▼
JWT
   │
   │ Token
   ▼
Cliente
   │
   │ Authorization: Bearer <token>
   ▼
Endpoint protegido
```

Esto permite proteger endpoints y controlar el acceso a determinados recursos.

> **Nota:** Las claves secretas, credenciales y variables de entorno no deben almacenarse directamente en el repositorio.

## ⚡ Sincrónico vs asíncrono

El curso también aborda la diferencia entre funciones síncronas y asíncronas en Python.

Ejemplo síncrono:

```python
def get_posts():
    ...
```

Ejemplo asíncrono:

```python
async def get_posts():
    ...
```

Y el uso de `await` para operaciones asíncronas:

```python
async def get_post():
    result = await database_operation()
    return result
```

Comprender esta diferencia es especialmente importante al trabajar con operaciones de I/O como bases de datos, archivos o peticiones HTTP.

## 🧱 Middlewares

Los middlewares permiten ejecutar lógica antes o después de procesar una petición.

Conceptualmente:

```text
Request
   │
   ▼
Middleware
   │
   ▼
Endpoint
   │
   ▼
Middleware
   │
   ▼
Response
```

Entre sus posibles usos están:

- Logging
- CORS
- Autenticación
- Medición de tiempos
- Manejo de headers
- Procesamiento común de requests/responses

## 📦 Pydantic

**Pydantic** se utiliza para definir y validar la estructura de los datos que recibe y devuelve la API.

Ejemplo:

```python
from pydantic import BaseModel


class Post(BaseModel):
    title: str
    content: str
```

Esto permite que FastAPI valide automáticamente los datos enviados por el cliente.

## 🧩 SQLAlchemy y SQLModel

El proyecto explora dos formas de trabajar con bases de datos:

### SQLAlchemy

ORM ampliamente utilizado en el ecosistema Python.

```python
class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String)
```

### SQLModel

Combina características de **Pydantic** y **SQLAlchemy**, permitiendo definir modelos que pueden utilizarse tanto para validación como para persistencia.

```python
class Post(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    content: str
```

## 🎯 Objetivo

El objetivo de este repositorio es **aprender y practicar el desarrollo de APIs REST con FastAPI**, entendiendo no solamente cómo crear endpoints, sino también cómo estructurar una aplicación backend y trabajar con las herramientas que normalmente forman parte de un proyecto real.

## 📌 Estado del proyecto

🚧 **En desarrollo — Curso en progreso**

El repositorio irá evolucionando conforme se incorporen nuevos temas y ejercicios.

## 📝 Notas

Este proyecto tiene principalmente fines educativos. El código puede contener implementaciones experimentales, ejemplos simplificados y diferentes enfoques utilizados para comprender los conceptos del curso.

---

⭐ Proyecto creado como parte del aprendizaje de **FastAPI y desarrollo backend con Python**.