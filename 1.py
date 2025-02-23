# from fastapi import FastAPI,Form,File,UploadFile

# from pydantic import BaseModel,Field
# from typing import Optional
# import aiofiles

# app = FastAPI()




# @app.get("/")
# async def root():
#     return {'message':"hello world"}

# class Item(BaseModel):
#     name:str
#     price:int 
#     in_stock:bool

    
# @app.post("/product")
# def create_item(item: Item):
#     return {"item": item}



# @app.post("/login")
# def login(username: str = Form(...),password: str = Form(...)):
#     return {"username":username}


# @app.post("/upload")
# def uplaod(file: UploadFile = File(...)):
#     return {"filename":file.filename}


# #query parameter for default value and type validation


# @app.get("/search")
# def user(name:str = None,
#          email:str = "email@gmail.com",
#          password:str="password"):
#     return{"username":name,"email":email,"password":password}

# class Address(BaseModel):
#     city:str
#     munacipility: str

# #... yesle field required garcha 
# class User(BaseModel):
#     name:str = File(...,min_length=10)
#     age:int = 12
#     email:str
#     address : Optional[Address]
    
    
# @app.post("/user")
# def user(user: User):
#     return{"user":user}   


# # @app.post("/file")
# # async def file(file: UploadFile= File(...)):
# #     content = await file.read()
# #     return{"file":file.filename,"size":len(content)}
    
    
    
# @app.post("/file")
# async def uplaodfile(file: UploadFile = File(...)):
#     file_path = f"uplaods/{file.filename}"
    
#     async with aiofiles.open(file_path,"wb") as buffer:
#         while chunk := await file.read(1024 * 1024):
#             await buffer.write(chunk)  
            
#     return {"filename":file.filename,"message":"file uploads"}