from src.general.errorCode import ErrorCodeLevel, ErrorCodeModule
from src.personnelManagement.role.Role_dto import Role
from datetime import datetime, timedelta
from typing import Dict, Optional
from fastapi import APIRouter,FastAPI, File, Form, UploadFile
from fastapi import Depends
from starlette.responses import Response
from mongodb_controller.mongodb_controller import MongoEngine 

from src.personnelManagement.auth.auth_service import *
from src.personnelManagement.auth.auth_dto import UpdateUser, User
from odmantic import ObjectId
from .user_service import UserService
import bcrypt
from src.personnelManagement.auth.Permission import *

user_router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

# get all users
@user_router.get("/")
async def find_users(current_user:User = Depends(get_current_active_user)):
    """
        # TODO: implement with page!
    """
    try:
        
        role = await RoleService().findRoleById(current_user.role)
        
        if Permission.GetAllUser in role.permissions :
            users = await UserService().findAllUsers()
            partialUserInfos = []
            for user in users:
                role = await RoleService().findRoleById(user.role)
                partialUserInfos.append({"fullName": user.fullName,\
                                        "email": user.email,\
                                        "avatarUrl":user.avatarUrl,\
                                        "phoneNumber":user.phoneNumber,\
                                        "id": str(user.id),\
                                        "role":role.name    })
            return partialUserInfos
        else:
            raise ErrorCodeException(error_message="You dont have the permission",error_code= ErrorCodeLevel.System + ErrorCodeModule.Role +  "0001")
    except BaseException as e:
        raise HTTPException(status_code=401, detail=e)
    
@user_router.get("/manager")
async def find_users(current_user:User = Depends(get_current_active_user)):
    """
        # TODO: implement with page!
    """
    try:
        
        role = await RoleService().findRoleById(current_user.role)
        
        if Permission.GetAllUser in role.permissions :
            users = await UserService().findAllManagers()
            partialUserInfos = []
            for user in users:
                role = await RoleService().findRoleById(user.role)
                partialUserInfos.append({"fullName": user.fullName,\
                                        "email": user.email,\
                                        "avatarUrl":user.avatarUrl,\
                                        "phoneNumber":user.phoneNumber,\
                                        "id": str(user.id),\
                                        "role":role.name    })
            return partialUserInfos
        else:
            raise ErrorCodeException(error_message="You dont have the permission",error_code= ErrorCodeLevel.System + ErrorCodeModule.Role +  "0001")
    except BaseException as e:
        raise HTTPException(status_code=401, detail=e)
    
@user_router.get("/test/test")
async def find_userr_by_id( current_user: User = Depends(get_current_active_user)):
    """
        
    """
    try:

        ids = await UserService().findRelationalBridgesByUserId(current_user.id)
        return ids
    except BaseException as e:
        print(str(e))
        raise HTTPException(status_code=401, detail=e)
# get the user by ID
@user_router.get("/{id}")
async def find_user_by_id(id: str, current_user: User = Depends(get_current_active_user)):
    """
        
    """
    try:
        
        role = await RoleService().findRoleById(current_user.role)
        if Permission.GetAllUser in role.permissions  or current_user.id == id:
            user = await UserService().findUserById(id)
            return {"email": user.email, 
                    "fullName": user.fullName, 
                    "roleName": role.name, 
                    "phoneNumber": user.phoneNumber, 
                    "avatarUrl": user.avatarUrl}
        else:
            raise ErrorCodeException(error_message="You dont have the permission",error_code= ErrorCodeLevel.System + ErrorCodeModule.Role +  "0001")
    except BaseException as e:
        raise HTTPException(status_code=401, detail=e)


# update the user
# only admin can update others, otherwise only updating current user
@user_router.put("/{id}")
async def update_user(id:str, form: UpdateUser, current_user: User = Depends(get_current_active_user)):
    """[summary]

    Args:
        id (str): the User be updated
        form (UpdateUser): userPatchSchema
        current_user (User, optional): [description]. Defaults to Depends(get_current_active_user).

    Raises:
        ValueError: Old password is not consistent
        ValueError: You dont have the permission to change role
        ErrorCodeException: [description]
        HTTPException: [description]

    Returns:
        [type]: [description]
    """
    
    try:
        oldUserInfo = await UserService().findUserById(id)
        role = await RoleService().findRoleById(current_user.role)
        if Permission.ChangeUserInfo in role.permissions or current_user.id == ObjectId(id):
            if form.role is not None :
                if Permission.ChangeUserInfo not in role.permissions:
                    raise ErrorCodeException(error_message="You dont have the permission",error_code= ErrorCodeLevel.System + ErrorCodeModule.Role +  "0001")
            if form.newPassword is not None:
                if Permission.ChangeUserInfo in role.permissions:
                    form.newPassword = bcrypt.hashpw(form.newPassword.encode('utf-8'), bcrypt.gensalt())
                    form.password = form.newPassword
                else:    
                    res = await AuthService().checkPasswordIsConsistent(current_user.email, form.oldPassword)
                    if  res:
                        form.newPassword = bcrypt.hashpw(form.newPassword.encode('utf-8'), bcrypt.gensalt())
                        form.password = form.newPassword
                    else:
                        raise ErrorCodeException(error_message="Old password is not consistent",error_code= ErrorCodeLevel.System + ErrorCodeModule.Auth +  "0005")
            
            newUserInfo = await UserService().updateUserPatch(form,oldUserInfo)
            newRole = await RoleService().findRoleById(newUserInfo.role)
            return {"email": newUserInfo.email, 
                    "fullName": newUserInfo.fullName, 
                    "roleName": newRole.name, 
                    "phoneNumber": newUserInfo.phoneNumber, 
                    "avatarUrl": newUserInfo.avatarUrl}
        else:
            raise ErrorCodeException(error_message="You dont have the permission",error_code= ErrorCodeLevel.System + ErrorCodeModule.Role +  "0001")
    except BaseException as e:
        raise HTTPException(status_code=401, detail=e)

@user_router.put("/manager/{id}")
async def update_user(id: str, current_user: User = Depends(get_current_active_user)):
    """
    # TODO change to patch! 0819
    """
    
    try:
        
        role = await RoleService().findRoleById(current_user.role)
        if role.name=='ROOT':
            beChangedUser = await UserService().findUserById(id)
            managerRole = await RoleService().createManagerRole()
            beChangedUser.role = managerRole.id
            newUserInfo  = await UserService().updateUser(beChangedUser)
            return newUserInfo
        else:
            raise ErrorCodeException(error_message="You dont have the permission",error_code= ErrorCodeLevel.System + ErrorCodeModule.Role +  "0001")
    except BaseException as e:
        raise HTTPException(status_code=401, detail=e)
    
#create user
# only admin can create a new user
@user_router.post("/")
async def create_user(user: User, current_user: User = Depends(get_current_active_user)):
    """

    """
    try:
        
        role = await RoleService().findRoleById(current_user.role)
        if Permission.CreateUser in role.permissions :
            if user.role is None:
                gusetRole:Role = await RoleService().findRoleByName('guest')
                user.role = gusetRole.id
            await AuthService().signUp(user)
            return {
                "email": user.email,
                "fullName": user.fullName,
                "status": "create successful!",
            }
        else:
            raise ErrorCodeException(error_message="You dont have the permission",error_code= ErrorCodeLevel.System + ErrorCodeModule.Role +  "0001")        
    except BaseException as e:
        raise HTTPException(status_code=401, detail=e)

#delete user
#only admin can delete a user
@user_router.delete("/{id}")
async def delete_user_by_id(id: str, current_user: User = Depends(get_current_active_user)):
    """
       
    """
    try:
        role = await RoleService().findRoleById(current_user.role)
        user = await UserService().findUserById(id)
        if Permission.DeleteUser in role.permissions  or current_user.id == id:
            res = await UserService().deleteUser(user)
            return {"status": res}
        else:
            raise ErrorCodeException(error_message="You dont have the permission",error_code= ErrorCodeLevel.System + ErrorCodeModule.Role +  "0001")
    except BaseException as e:
        raise HTTPException(status_code=401, detail=e)



   