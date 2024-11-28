from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated
from app.models import User
from app.schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete
from slugify import slugify
from fastapi import APIRouter

user = APIRouter(prefix='/user', tags=['user'])

@user.get('/')
async def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User)).all()
    if users is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is no user'
        )
    return users

@user.get('/user_id')
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    cur_user = db.scalars(select(User).where(user_id == User.id))
    if cur_user is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found'
        )
    return cur_user

@user.post('/create')
async def create_user(db: Annotated[Session, Depends(get_db)], create_user: CreateUser):
    db.execute(insert(User).values(username=create_user.username,
                                   firstname=create_user.firstname,
                                   lastname=create_user.lastname,
                                   age=create_user.age,
                                   slug=slugify(create_user.username)))
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }

@user.put('/update')
async def update_user(db: Annotated[Session, Depends(get_db)], user_id: int, update_user: UpdateUser):
    cur_user = db.scalars(select(User).where(user_id == User.id))
    if cur_user is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='The user was not found'
        )
    db.execute(update(User).where(user_id == User.id).values(username=update_user.username,
                                                             firstname=update_user.firstname,
                                                             lastname=update_user.lastname,
                                                             age=update_user.age,
                                                             slug=slugify(update_user.username)))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Successful update'
    }

@user.delete('/delete')
async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
    cur_user = db.scalars(select(User).where(user_id == User.id))
    if cur_user is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='The user was not found'
        )
    db.execute(delete(User).where(user_id == User.id))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Successful delete'
    }