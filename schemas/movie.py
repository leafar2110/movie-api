from pydantic import BaseModel, Field
from typing import Optional


class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=15)
    overview: str =  Field(min_length=15, max_length=50)
    year: int =  Field(le=2022, default=2022)
    rating: float = Field(ge=1, default=10)
    category: str = Field(min_length=5, max_length=15)

    class Config:
        schema_extra = {
            "example": {
                'title': 'Mi pelicula',
                'overview': "Descripcion de la pelicula",
                'year': 2022,
                'rating': 7.8,
                'category': 'Acción' 
            }
        }