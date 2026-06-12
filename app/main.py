from fastapi import FastAPI
from app.database import Base
from app.database import engine
from app.routes.user import router as user_router
from mangum import Mangum
#Base.metadata.create_all(bind=engine)
from fastapi import Request

app = FastAPI(title="User Management API")

app.include_router(user_router)

@app.get("/")
def home():
    return {
        "message": "User Management API Running"
    }

@app.middleware("http")
async def log_request(request: Request, call_next):
    print("PATH RECEIVED:", request.url.path)

    response = await call_next(request)

    print("STATUS:", response.status_code)

    return response



print("ROUTES:")
for route in app.routes:
    print(route.path)

handler = Mangum(app)