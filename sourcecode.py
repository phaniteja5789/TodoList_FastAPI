from fastapi import FastAPI,Request,Form,status
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel,Field

class Task(BaseModel):
    taskName:str|None = Field( default=None,max_length=30)
    taskFlag:int=Field(default=0,le=2)

templates=Jinja2Templates(directory="templates")
app=FastAPI()
todoTaskList=[]

@app.get("/",response_class=HTMLResponse)
def StartUpScreen(request:Request):
    return templates.TemplateResponse("StartUpScreen.html",{"request":request,"todoTaskList":todoTaskList})

@app.post("/",response_class=HTMLResponse)
def postTaskData(request:Request,taskName:str=Form(...)):
    todoTaskList.append(Task(taskName=taskName,taskFlag=0))
    return templates.TemplateResponse("StartUpScreen.html",{"request":request,"todoTaskList":todoTaskList})

@app.post("/completedTask")
async def completedTask(request:Request):
    val=await request.json()
    todoTaskList[val["index"]].taskFlag=1
    redirect_url=request.url_for("StartUpScreen")
    print(val["index"])
    return RedirectResponse(redirect_url,status_code=status.HTTP_303_SEE_OTHER)
    
@app.post("/removeTask")
async def removeTask(request:Request):
    val=await request.json()
    del todoTaskList[val["index"]]
    return RedirectResponse("/",status_code=status.HTTP_303_SEE_OTHER)

if __name__=="__main__":
    app()