from fastapi import APIRouter
from fastapi import Path, Query
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from fastapi.encoders import jsonable_encoder
from services.movie import MovieService
from schemas.movie import Movie


movie_router = APIRouter()


@movie_router.get('/movies', tags=['movies'], response_model=List[Movie], status_code=200)
def get_movies() -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies()
    return JSONResponse(content=jsonable_encoder(result))



@movie_router.get('/movies/{id}', tags=['movies'], response_model=Movie)
def get_movie(id: int = Path(ge=1, le=2000)) -> Movie:
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404 ,content={'message': 'Elemento no encontrado'})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))



@movie_router.get('/movies/', tags=['movies'], response_model=List[Movie])
def get_movies_by_category(category: str = Query(min_length=5, max_length=15)) -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movie_by_cateegory(category)
    if not result:
        return JSONResponse(status_code=404 ,content={'message': 'Elemento no encontrado'})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))



@movie_router.post('/movies', tags=["movies"], response_model=dict, status_code=201)
def create_movies(movie: Movie) -> dict:
    db = Session()
    MovieService(db).create_movie(movie)
    return JSONResponse(status_code=201 ,content={'message': 'Se ha registrado la pelicula'})



@movie_router.put('/movies/{id}', tags=["movies"], response_model=dict, status_code=201)
def update_movie(id: int, movie: Movie) -> dict:
    db = Session()
    result = MovieService(db).get_movie(id)

    if not result:
        return JSONResponse(status_code=404 ,content={'message': 'Elemento no encontrado'})
    
    MovieService(db).update_movie(movie)
    return JSONResponse(status_code=201, content={'message': 'Se ha modificado la pelicula'})



@movie_router.delete('/movies/delete/{id}', tags=["movies"], response_model=dict, status_code=201)
def delete_movie(id: int) -> dict:
    db = Session()
    result = MovieService(db).get_movie(id)

    if not result:
        return JSONResponse(status_code=404 ,content={'message': 'Elemento no encontrado'})
    
    MovieService(db).delete_movie(id)
    return JSONResponse(status_code=201, content={'message': 'Se ha eliminado la pelicula'})
