from src.general.errorCode import ErrorCodeException, ErrorCodeLevel, ErrorCodeModule
from src.personnelManagement.auth.Permission import Permission
from src.personnelManagement.auth.auth_service import get_current_active_user
from fastapi import APIRouter
from fastapi import Depends
from fastapi import  HTTPException


from .role_service import RoleService
from src.personnelManagement.user.User_dto import User
from .Role_dto import Role, RolePatchSchema

role_router = APIRouter(
    prefix="/roles",
    tags=["roles"],
    responses={404: {"description": "Not found"}},
)


@role_router.post("/")
async def create_new_role(role:Role, current_user: User = Depends(get_current_active_user)):
    """
    TODO: only ROOT can call this api!
    
    Args:
        role:  role Dto

    Returns:
        200 if success
        401 maybe same role name.

    Raises:
        ValueError: if role name already exists
    """
    try:
        userRole = await RoleService().findRoleById(current_user.role)
        if userRole.name == "ROOT":
            newRole = await RoleService().createRole(role)
            return newRole
        else: 
            raise ErrorCodeException(error_message="You dont have the permission",error_code= ErrorCodeLevel.System + ErrorCodeModule.Role +  "0001")
    except BaseException as e:
        raise HTTPException(status_code=401, detail=e)
    
    
@role_router.get("/")
async def find_all_roles(skip:int = 0, limit:int = 10, current_user: User = Depends(get_current_active_user)):
    """
    ! done
    Args:
        None

    Returns:
        200 if success
        401 maybe same role name.

    Raises:
        ValueError: if role name already exists
    """
    try:
        role = await RoleService().findRoleById(current_user.role)
        if role.name ==  "ROOT":
            roles = await RoleService().findAllRoles(skip,limit)
            return roles
        else: 
            raise ErrorCodeException(error_message="You dont have the permission",error_code= ErrorCodeLevel.System + ErrorCodeModule.Role +  "0001")
    except BaseException as e:
        raise HTTPException(status_code=401, detail=e)
    
    
@role_router.put("/{id}")
async def update_user(id:str, newRoleInfo:RolePatchSchema, current_user: User = Depends(get_current_active_user)):
    """[summary]

    Args:
        id (str): role id
        newRoleInfo (RolePatchSchema): 
        current_user (User, optional): [description]. Defaults to Depends(get_current_active_user).

    Raises:
        ErrorCodeException: You dont have the permission
        HTTPException: [description]

    Returns:
        [type]: [description]
    """
    
    try:
        
        role = await RoleService().findRoleById(current_user.role)
        if role.name ==  "ROOT":
            
            updatedRole = await RoleService().findRoleById(id)
            newRoleInfo = await RoleService().updateRole(newRoleInfo,updatedRole)
            
            return newRoleInfo
        else:
            raise ErrorCodeException(error_message="You dont have the permission",error_code= ErrorCodeLevel.System + ErrorCodeModule.Role +  "0001")
    except BaseException as e:
        raise HTTPException(status_code=401, detail=e)
    
@role_router.get("/ROOT")
async def create_ROOT_role():
    """
    ! just exist in development
    """
    try:
        permissions = []
        for permission in Permission:
            permissions.append(permission)
        
        role = Role(name="ROOT", permissions =permissions, description="ROOT")
        newRole = await RoleService().createRole(role)
    except BaseException as e:
        raise HTTPException(status_code=401, detail=e)
    

@role_router.delete("/{id}")
async def delete_role_by_id(id: str, current_user: User = Depends(get_current_active_user)):
    """
    ! done
    Args:
        None

    Returns:
        200 if success
        401 maybe same role name.

    Raises:
        ValueError: if role name already exists
    """
    try:
        role = await RoleService().findRoleById(current_user.role)
        if role.name ==  "ROOT":
            deleteRole = await RoleService().findRoleById(id)
            
            status = await RoleService().deleteRole(deleteRole)
            return status
        else: 
            raise ErrorCodeException(error_message="You dont have the permission",error_code= ErrorCodeLevel.System + ErrorCodeModule.Role +  "0001")
    except BaseException as e:
        raise HTTPException(status_code=401, detail=e)
    
