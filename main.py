from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from middelwars.error_handler import ErrorHandler
from config.database import  engine, Base
from routers.movie import movie_router
from routers.user import user_router

app = FastAPI()
app.title = "Mi aplicacion con fastAPI"
app.version = '0.0.1'

app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(user_router)

Base.metadata.create_all(bind=engine)

@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>hola</h1>')


