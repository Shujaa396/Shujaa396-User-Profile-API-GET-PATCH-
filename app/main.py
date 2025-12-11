from fastapi import FastAPI
from app.routes import product, auth

app = FastAPI()

# Include routers
app.include_router(product.router)
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"message": "Nexus Backend Week 3"}
from app.database import Base, engine
from app.models import product_model, user_model

Base.metadata.create_all(bind=engine)
