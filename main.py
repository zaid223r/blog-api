from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
from sqlalchemy.orm import Session

import models
from database import engine, local_session

app = FastAPI()
models.base.metadata.create_all(bind=engine)

class PostBase(BaseModel):
    title:str
    content:str
    user_id:int
    
class UserBase(BaseModel):
    username:str
    
def get_db():
    db = local_session()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserBase, db: db_dependency):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    
@app.post("/posts/", status_code=status.HTTP_201_CREATED)
async def create_post(post: PostBase, db: db_dependency):
    db_post = models.Posts(**post.dict())
    db.add(db_post)
    db.commit()
    
@app.get("/posts/{post_id}", status_code=status.HTTP_200_OK)
async def read_post(post_id: int, db: db_dependency):
    post = db.query(models.Posts).filter(models.Posts.id == post_id).first()
    if post: 
        return post
    raise HTTPException(status_code=404, detail="Post not found")

@app.get("/users/{user_id}", status_code=status.HTTP_200_OK)
async def read_user(user_id: int, db: db_dependency):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user: 
        return user
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/posts/{post_id}",status_code=status.HTTP_200_OK)
async def delete_post(post_id: int, db: db_dependency):
    post = db.query(models.Posts).filter(models.Posts.id == post_id).first()
    if post:
        db.delete(post)
        db.commit()
        return
    raise HTTPException(status_code=404, detail="Post Not Found")