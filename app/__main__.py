import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.common.json_logging import logger
from app.parsers.google_parser import GoogleSearch

app = FastAPI(
        title="API Google Searcher"
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/google_issue/", status_code=200)
def get_google_issue(search_query: str):
    """
    Ручка для получения данных из поисковой выдачи\n
    :param search_query: текст запроса в виде строки\n
    :return: результат сбора данных в виде строки\n
    """
    logger.info('start google issue')
    google = GoogleSearch()
    result = google.search(search_query)
    logger.info('end google issue')
    return result


if __name__ == "__main__":
    uvicorn.run(app="__main__:app", port=9992, host='0.0.0.0')
