from fastapi import FastAPI, HTTPException, Depends, status
from contextlib import asynccontextmanager
from fastapi import Request
from app.db_setup import init_db, get_db
from sqlalchemy.orm import Session, joinedload, selectinload
from sqlalchemy import select, update, delete, insert
from app.api.v1.core.models import Company

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("starting Application")
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/company", status_code=200)
def list_companies(db: Session = Depends(get_db)):
    programs = db.scalars(select(Company)).all()
    if not programs:
        raise HTTPException(status_code=404, detail="No companies found")
    return programs