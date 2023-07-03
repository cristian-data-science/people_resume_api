from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from dotenv import load_dotenv
import openai
import os
import secrets
import json

# Cargamos las variables de entorno y establecemos la clave de la API de OpenAI
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

# Inicializamos la autenticación básica HTTP
security = HTTPBasic()

function_descriptions = [
    {
        "name": "extract_info_from_cv",
        "description": "categorizar y extraer información clave de los candidatos, como su experiencia relevante, estudios, etc.",
        "parameters": {
            "type": "object",
            "properties": {
                "experiencia_total": {
                    "type": "string",
                    "description": "determina el total de años de experiencia laboral que el candidato ha mencionado en su currículum"
                },
                "experiencia_relevante": {
                    "type": "string",
                    "description": "Identifica la experiencia laboral que está directamente relacionada con el puesto que estamos interesados"
                },
                "educacion": {
                    "type": "string",
                    "description": "Busca el nivel más alto de educación que el candidato ha logrado y proporciona detalles de las instituciones educativas y fechas de graduación"
                },                                                
                "habilidades_tecnicas": {
                    "type": "string",
                    "description": "Busca y enumera todas las habilidades técnicas que el candidato ha mencionado en su currículum"
                },
                "habilidades_blandas": {
                    "type": "string",
                    "description": "Identifica y enumera todas las habilidades blandas o interpersonales mencionadas por el candidato en su currículum"
                },
                "industria": {
                    "type": "string",
                    "description": "Identifica las industrias en las que el candidato ha trabajado anteriormente"
                },
                "idiomas": {
                    "type": "string",
                    "description": "Identifica las industrias en las que el candidato ha trabajado anteriormente"
                }
            },
            "required": ["experiencia_total","experiencia_relevante","educacion", "habilidades_tecnicas", "habilidades_blandas", "industria", "Idiomas"]
        }
    }
]



# Definimos el modelo de email
class Email(BaseModel):
    #from_email: str
    content: str

# Función para validar las credenciales del usuario
def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, os.getenv('user_api'))
    correct_password = secrets.compare_digest(credentials.password, os.getenv('pass_api'))
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/")
def analyse_email(email: Email, username: str = Depends(get_current_username)):
    try:
        content = email.content
        #from_email = email.from_email
        query = f"Extrae la información de este candidato: {content} "
        messages = [{"role": "user", "content": query}]

        response = openai.ChatCompletion.create(
            #model="gpt-4-0613",
            model = "gpt-3.5-turbo-0613",
            messages=messages,
            functions = function_descriptions,
            function_call="auto"
        )

        arguments = json.loads(response.choices[0]["message"]["function_call"]["arguments"])
        experiencia_total = arguments.get("experiencia_total")
        experiencia_relevante = arguments.get("experiencia_relevante")
        educacion = arguments.get("educacion")
        habilidades_tecnicas = arguments.get("habilidades_tecnicas")
        habilidades_blandas = arguments.get("habilidades_blandas")
        industria = arguments.get("industria")
        idiomas = arguments.get("idiomas")
       

        return {
            "experiencia_total": experiencia_total,
            "experiencia_relevante": experiencia_relevante,
            "educacion": educacion,
            "habilidades_tecnicas": habilidades_tecnicas,
            "habilidades_blandas": habilidades_blandas,
            "industria": industria,
            "idiomas": idiomas

        }
    except Exception as e:
        return {"error": str(e)}