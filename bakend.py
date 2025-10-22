

from fastapi import FastAPI
import uvicorn 

app = FastAPI()


from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(
    title="API REST Cliente-Servidor",
    description="API base desarrollada con FastAPI, Docker y pruebas automáticas",
    version="1.0.0"
 )
class Usuario(BaseModel):
    id: int
    nombre: str
    correo: str

usuarios = [
    {"id": 1, "nombre": "Lisa", "correo": "lisa@example.com"},
    {"id": 2, "nombre": "Juan", "correo": "juan@example.com"},
]

@app.get("/")
def inicio():
    print("Servidor FastAPI funcionando correctamente ")
    return {"mensaje": "Bienvenido a la API REST Cliente-Servidor"}

@app.get("/usuarios")
def listar_usuarios():
    return {"usuarios": usuarios}

@app.post("/usuarios")
def crear_usuario(usuario: Usuario):
    usuarios.append(usuario.dict())
    print(f"Usuario agregado: {usuario.nombre}")
    return {"mensaje": "Usuario agregado correctamente", "usuario": usuario }
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    canst responde = await fetch ( Url 
                              method: "GET",
                              const url = https://railway.com/project/4038e7da-7a10-4200-95ba-08157e1da8dd/service/edba3143-a5a6-4d69-9bfa-6a822eb971cd?environmentId=8cae78a2-b24c-481d-a90c-de2c3e6df51f

                            headers : { 
                                "Content-Type": "application/json"
                                }
                                if (response.ok) {
                                  const data = await response.json();
                                  console.log("Datos de usuarios:", data);
                                } else {
                                  console.error("Error http: " + response.status);
                                }  console.log("Datos de usuarios:", data);
                                const url = "http://localhost:8000/usuarios";
    } 
         console.log("Rosana chaguendo  trabajando en el proyecto individual");lo intente catch (error) 


     

