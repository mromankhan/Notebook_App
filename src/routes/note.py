from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from models.note import Note
from config.db import conn
from schemas.note import noteEntity, notesEntity
from fastapi.templating import Jinja2Templates

note = APIRouter()
templates = Jinja2Templates(directory="templates")

@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    cursor = conn.notes.notes.find({})  
    docs = cursor.to_list(length=100) 
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id": str(doc["_id"]),
            "title": doc.get("title", "N/A"),
            "desc": doc.get("desc", "N/A"),
            "important": doc.get("important", False),
        })
    # print(newDocs)
    return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})




@note.post("/") 
async def create_item(request: Request):
    form = await request.form()
    # print("complete form:", form)    
    formDict = dict(form)
    formDict["important"] = True if formDict.get("important") == "on" else False
    note =  conn.notes.notes.insert_one(formDict)
    return{"Sucess": True}