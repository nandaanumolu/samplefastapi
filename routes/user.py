from fastapi import APIRouter

from models.user import User
from config.db import conn
from schemas.user import userEntity,usersEntity
from bson import ObjectId

user=APIRouter()


@user.get('/')
async def find_one_users():
    return usersEntity(conn.local.user.find())


@user.get('/{id}')
async def delete_user(id,user: User):
    
    return userEntity(conn.local.user.find_one({"_id":ObjectId(id)}))


@user.post('/')
async def create_user(user: User):
    conn.local.user.insert_one(dict(user))
    return "SuccessFully Created User"



@user.put('/{id}')
async def update_user(id,user: User):
    conn.local.user.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(user)
    })
    return "SuccessFully Updated User"


@user.delete('/{id}')
async def delete_user(id,user: User):
    conn.local.user.find_one_and_delete({"_id":ObjectId(id)})
    return "SuccessFully Updated User"