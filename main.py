from fastapi import FastAPI
import uvicorn
from app.routes import routes
app = FastAPI()

app.include_router(routes.router)

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
