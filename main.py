from fastapi import FastAPI,Request,Form
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from sqlalchemy.orm import  Session
from database import engine,Base,get_db
from models import User_Model



app=FastAPI()
templates=Jinja2Templates(directory="templates")
Base.metadata.create_all(bind=engine)

@app.get("/")
def home(request:Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html"

    )
@app.get("/register")
def register(request:Request):
    return templates.TemplateResponse(
        request=request,
        name="registration.html"
    )






@app.get("/login")
def login(request:Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html"
    )





