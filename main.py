from fastapi import FastAPI

from config import PROJECT_NAME
from src.views.word_in_songs_view import wis_router

app = FastAPI(title=PROJECT_NAME)

app.include_router(wis_router, prefix="/api/v1", tags=["wis"])

if __name__ == '__main__':
    """ Executar localmente """
    import uvicorn
    from dotenv import load_dotenv

    load_dotenv()
    uvicorn.run(app, host="localhost", port=8001)
