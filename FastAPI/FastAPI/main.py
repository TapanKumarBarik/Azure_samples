from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root()->dict:
    return {"message":"Hello World"}


#PATH PARAM
@app.get("/greet/{name}")
async def greet_user(name:str)->dict:
    return {"message": f"Hello {name}"}


#QUERY PARAM
@app.get("/greet/")
async def greet_user(name:str)->dict:
    return {"message": f"Hello {name}"}


#BOTH , PATH VARIABLE + QUERY PARAM
@app.get("/greets/{name}")
async def greet_user(name:str,age:int)->dict:
    return {"message": f"Hello  {name}","age":age}