
from src.personnelManagement.role.Role_dto import Role
from src.personnelManagement.role.role_service import RoleService
from .auth_service import AuthService

from fastapi import APIRouter
from fastapi import Depends, HTTPException
from fastapi.security import  OAuth2PasswordRequestForm
from pydantic import BaseModel
from src.personnelManagement.user.User_dto import User
from odmantic import Model

from .auth_service import *




auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)
class LoginUser(Model):
    email:str
    password:str

class GetToken(Model):
    username:str
    password:str

class Token(BaseModel):
    access_token: str
    token_type: str


@auth_router.post("/login")
async def login_for_access_token(loginUser: LoginUser):
    try:
        jwtToken, loginUserName, email , userid= await AuthService().authenticate_user(loginUser.email, loginUser.password)
    

        return {"access_token": jwtToken,"userName":loginUserName ,"email" : email,"token_type": "bearer", "id": str(userid)}
    except BaseException as e:
        raise HTTPException(status_code=401, detail=e)

@auth_router.post("/form/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    try:
        logger.info("form_data.username: " + form_data.username)
        logger.info("form_data.password: " + form_data.password)
        jwtToken, loginUserName, email, userid= await AuthService().authenticate_user(form_data.username, form_data.password)
    

        return {"access_token": jwtToken, "token_type": "bearer"}
    except BaseException as e:
        raise HTTPException(status_code=401, detail=e)


@auth_router.post("/sign-up")
async def signUp(current_user: User):
    """
    ! Need to test
    """
    try:
        gusetRole:Role = await RoleService().findRoleByName('guest')
        current_user.role = gusetRole.id
        await AuthService().signUp(current_user)
        return {
            "email": current_user.email,
            "fullName": current_user.fullName,
            "status": "create successful!",
        }    
    except BaseException as e:
        raise HTTPException(status_code=401, detail=e)