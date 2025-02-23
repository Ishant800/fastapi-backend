from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email: str
    age: int

class UserCreate(UserBase):
    pass

class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = True  

class BookCreate(BaseModel):
    bookname : str
    author : str
    title : str
    isbn : int

class BookResponse(BookCreate):
    id: int
    
    class Config:
        from_attributes = True
    