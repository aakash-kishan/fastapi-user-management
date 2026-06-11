from fastapi import FastAPI
from app.database import Base
from app.database import engine
from app.routes.user import router as user_router
from mangum import Mangum
#Base.metadata.create_all(bind=engine)

app = FastAPI(title="User Management API")

handler = Mangum(app)

app.include_router(user_router)


@app.get("/")
def home():
    return {
        "message": "User Management API Running"
    }