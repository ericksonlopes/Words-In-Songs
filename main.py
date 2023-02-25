from fastapi import FastAPI

from src.views.word_in_songs_view import wis_router

app = FastAPI()

app.include_router(wis_router, prefix="/api/v1", tags=["wis"])

if __name__ == '__main__':
    """ Executar localmente """
    import uvicorn
    from dotenv import load_dotenv

    load_dotenv()
    uvicorn.run(app, host="localhost", port=8001)
