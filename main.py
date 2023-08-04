from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List, Optional, Union

app = FastAPI()
templates = Jinja2Templates(directory='templates')


class Movie(BaseModel):
    id: Union[int, None] = None
    title: str
    description: str
    year: int
    genre: List[str] = None
    watched: Optional[bool] = True
    # title: Field(..., )
    # description: Field(None, )


movies = [
    Movie(id=1, title='title1', description='description1',
          year=1990, genre=['Drama', 'Comedy'], watched=True),
    Movie(id=2, title='title2', description='description2',
          year=1991, genre=['Drama', 'Thriller'], watched=False)
]


@app.get('/', response_class=HTMLResponse)
async def html_movies(request: Request):
    return templates.TemplateResponse('index.html',
                                      {'request': request, 'movies': movies})


@app.get('/movies', response_model=List[Movie])
async def get_movies():
    return movies


@app.get('/movies/{id}', response_model=Movie)
async def get_movie():
    for movie in movies:
        if id == movie.id:
            return movie
    raise HTTPException(status_code=404, detail='Movie not found')


@app.post('/movies/', response_model=Movie)
async def add_movie(movie: Movie):
    max_id = 1
    for element in movies:
        max_id = max(max_id, element.id) + 1
    movie.id = max_id
    movies.append(movie)
    return movie


@app.put('/movies/{movie_id}', response_model=Movie)
async def update_movie(movie_id: int, movie: Movie):
    for i, movie_ in enumerate(movies):
        if movie_id == movie_.id:
            movies[i] = movie
            return movie
    raise HTTPException(status_code=404, detail='Movie not found')


@app.delete('/movies/{movie_id}')
async def delete_movie(movie_id: int):
    for i, movie in enumerate(movies):
        if movie_id == movie.id:
            id = i
            break
    try:
        movies.pop(id)
        return {"message": "Delete successful"}
    except:
        raise HTTPException(status_code=404, detail='Movie not found')


if __name__ == '__main__':
    pass
