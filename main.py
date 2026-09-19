from fastapi import FastApi
from config import APP_VERSION

app = FastApi(title="students-api", version=APP_VERSION)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/studenst")
def list_studenst():
    return[{"id":1, "name": "Ana"}, {"id": 2, "name": "Luis"}]