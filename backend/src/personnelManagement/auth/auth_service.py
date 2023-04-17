
from src.general.errorCode import ErrorCodeException, ErrorCodeLevel, ErrorCodeModule
from fastapi.exceptions import HTTPException
from fastapi.params import Depends
from fastapi.security.oauth2 import OAuth2PasswordBearer
from src.personnelManagement.user.user_service import UserService
from src.personnelManagement.role.role_service import RoleService
from mongodb_controller.mongodb_controller import engine
from datetime import datetime, timedelta
from typing import Optional
import os
from src.personnelManagement.user.User_dto import User
import bcrypt
from jose import JWTError, jwt

from main import logger

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/form/token",auto_error=False)

async def get_current_user(token: str = Depends(oauth2_scheme)):
        credentials_exception = HTTPException(
            status_code=401,
            detail="Could not validate credentials, maybe token expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            logger.info("token: %s", token)
            payload = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=os.getenv('JWTALGORITHM'))
            email: str = payload.get("email")
            if email is None:
                raise credentials_exception
            logger.info("email: %s", email)
            logger.info("payload: %s", payload)
        except JWTError:
            raise credentials_exception
            
        loginUser: User = await engine.find_one(User, User.email==email)

        if loginUser is None:
            raise credentials_exception
        
        return loginUser
    
async def get_current_active_user(current_user: User = Depends(get_current_user)):
        logger.info("current_user")
        logger.info("current_user: %s", current_user)
        if not current_user.enable:
            raise HTTPException(status_code=400, detail="Inactive user")
        return current_user
class AuthService():
    
    def create_access_token(self, data: dict, expires_delta: Optional[timedelta] = None) -> str:
        """[summary]

        Args:
            data (dict): to_encode data
            expires_delta (Optional[timedelta], optional): the time jwt token expires. Defaults to None.

        Returns:
            str: jwt token
        """
        to_encode = data.copy()
        
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=600)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, os.getenv('SECRET_KEY'), algorithm=os.getenv('JWTALGORITHM'))
        return encoded_jwt
    
    
    
    

    async def signUp(self, userDto:User):
        """[summary]
        # TODO test env variable 

        Args:
            userDto (User): the user data

        Raises:
            ErrorCodeException: Can not find the user =>  Email

        Returns:
            User: new User Info
        """
        isExist = await UserService().findUserByEmail(userDto.email)
        if isExist:
            
            raise ErrorCodeException(error_message="User email already exists!" ,error_code=ErrorCodeLevel.System + ErrorCodeModule.Auth + "0004")
        else:
            userDto.password = bcrypt.hashpw(userDto.password.encode('utf-8'), bcrypt.gensalt())
            domain = os.getenv('DOMAINNAME')
            userDto.avatarUrl = domain + str(userDto.id)
            users = await engine.save(userDto)
            return users
        
    async def authenticate_user(self, email:str, password:str):
        """[summary]

        Args:
            email (str): 
            password (str): 

        Raises:
            ErrorCodeException: Can not find the user =>  Email
            ErrorCodeException: password is not consistent

        Returns:
           token, user.fullName, email, user.id
        """
        user = await UserService().findUserByEmail(email)
        if user is None:
            raise ErrorCodeException(error_message="Can not find the user =>  Email: " + email ,error_code= ErrorCodeLevel.System + ErrorCodeModule.Auth + "0002")
        else:
            if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                currentUserRole = await RoleService().findRoleById(user.role)
                access_token_expires = timedelta(minutes=int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')))
                token = self.create_access_token({"Role": currentUserRole.name, "userName": user.fullName, "email":user.email},access_token_expires)                   
                return token, user.fullName, email, user.id
            else :
                
                raise ErrorCodeException(error_message="password is not consistent!" ,error_code=ErrorCodeLevel.System + ErrorCodeModule.Auth + "0003")
            
    async def checkPasswordIsConsistent(self, email:str, oldPassword:str):
        """[summary]

        Args:
            email (str): [description]
            oldPassword (str): [description]

        Raises:
            ErrorCodeException: Can not find the user =>  Email:

        Returns:
            bool : is password consistent?
        """
        user = await UserService().findUserByEmail(email)
        if user is None:
            raise ErrorCodeException(error_message="Can not find the user =>  Email: " + email ,error_code=ErrorCodeLevel.System + ErrorCodeModule.Auth + "0002")
        else:
            res =  bcrypt.checkpw(oldPassword.encode('utf-8'), user.password.encode('utf-8'))
            return res
                
    
