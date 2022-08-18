#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sathwik
"""
from fastapi import FastAPI,Body,Request,File,UploadFile,Form,Depends
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm

app=FastAPI()

list_of_usernames = list()
templates =Jinja2Templates(directory="htmldirectory")

oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/token")
async def token_generate(form_data:OAuth2PasswordRequestForm = Depends()):
    print(form_data)
    return {"access_token":form_data.username,"token_type":"bearer"}

@app.get("/user/pic")
async def pic(token:str = Depends(oauth_scheme)): 
    print(token)
    return {
        "user":"sathwik",
        "pic":"house"
   }

class NameValues(BaseModel):
    name:str 
    country:str 
    age:int 
    salary:float 
    
@app.get("/student/{student_name}",response_class=HTMLResponse)
def student(request: Request,student_name:str):
    return templates.TemplateResponse("student",{"request":request,"username":student_name})
