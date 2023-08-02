from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def start():
    return {'message: Hello, World!'}


if __name__ == '__main__':
    pass