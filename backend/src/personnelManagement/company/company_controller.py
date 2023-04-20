from src.general.errorCode import ErrorCodeException, ErrorCodeLevel, ErrorCodeModule
from src.personnelManagement.auth.Permission import Permission
from src.personnelManagement.role.role_service import RoleService
from .company_service import CompanyService
from .Company_dto import Company, CompanyPatchSchema

from fastapi import APIRouter
from fastapi import Depends, HTTPException
from mongodb_controller.mongodb_controller import MongoEngine
from src.personnelManagement.auth.auth_service import get_current_active_user
from src.personnelManagement.auth.auth_dto import User
from odmantic import ObjectId
from main import logger
company_router = APIRouter(
    prefix="/companies",
    tags=["companies"],
    responses={404: {"description": "Not found"}},
)



@company_router.get("/")
async def find_all_companies(skip:int = 0, limit:int = 10, current_user: User = Depends(get_current_active_user)):
    """
    ! 0803 v1 done
    Args:
        skip:int = 0, limit:int = 10,

    Returns:
        company list

    Raises:
        if user is not yet in any company
    """
    try:
        if current_user.company is  None:
            
            raise ErrorCodeException(error_message="You dont have the permission",error_code= ErrorCodeLevel.System + ErrorCodeModule.Role +  "0001")
            
        else: 
            logger.info("current_user.company: " + str(current_user.company))
            companies = await CompanyService().findAllCompanyByUserCompanyId(current_user.company, skip=skip, limit=limit)
            return companies
    except BaseException as e:
        raise HTTPException(status_code=401, detail=e)

@company_router.get("/{id}")
async def find_company_by_id(id: str, current_user: User = Depends(get_current_active_user)):
    """
    ! 0803 v1 done
    Args:
        id: company id

    Returns:
        company list

    Raises:
        if user is not yet in any company
        if not found any company return 404
    """
    try:
        if current_user.company is  None:
            
            raise ErrorCodeException(error_message="You dont have the permission",error_code= ErrorCodeLevel.System + ErrorCodeModule.Role +  "0001")
            
        else: 
            company = await CompanyService().find_Company_By_CompanyId_And_UserCompanyId(current_user.company, ObjectId(id))
            return company
    except BaseException as e:
        raise HTTPException(status_code=404, detail=e)



@company_router.put("/{id}")
async def update_company(id:str, companyPatch: CompanyPatchSchema, current_user: User = Depends(get_current_active_user)):
    """
    ! 0803 v1 done
    Args:
        id: company id
        company: CompanyPatchSchema

    Returns:
        updated company info

    Raises:
        user dont have the permission
    """
    try:
        role = await RoleService().findRoleById(current_user.role)
        company = await CompanyService().findCompanyByCompanyId(ObjectId(id))
        if Permission.UpdateCompany in role.permissions :    
            newCompany =  await CompanyService().updateCompany(companyPatch, company)
            return newCompany
        else:
                raise ErrorCodeException(error_message="You dont have the permission",error_code= ErrorCodeLevel.System + ErrorCodeModule.Role +  "0001")
    except BaseException as e:
        raise HTTPException(status_code=401, detail=e)

@company_router.post("/")
async def create_company(company: Company, current_user: User = Depends(get_current_active_user)):
    """
    ! 0803 v1 done
    Args:
        company: Company

    Returns:
        company info

    Raises:
        user dont have the permission
    """
    try:
        
        role = await RoleService().findRoleById(current_user.role)
        if Permission.CreateCompany in role.permissions :
            newCompany = await CompanyService().createCompany(company)
            return newCompany
        else:
                raise ErrorCodeException(error_message="You dont have the permission",error_code= ErrorCodeLevel.System + ErrorCodeModule.Role +  "0001")
    except BaseException as e:
        raise HTTPException(status_code=401, detail=e)


@company_router.delete("/{id}")
async def delete_company_by_id(id: str, current_user: User = Depends(get_current_active_user)):
    """
    ! 0803 v1 done
    Args:
        id: company id

    Returns:
        delete company info

    Raises:
        user dont have the permission
    """
    try:
        role = await RoleService().findRoleById(current_user.role)
        if Permission.DeleteCompany in role.permissions :    
            status =  await CompanyService().deleteCompany(ObjectId(id))
            return status
        else:
                raise ErrorCodeException(error_message="You dont have the permission",error_code= ErrorCodeLevel.System + ErrorCodeModule.Role +  "0001")
    except BaseException as e:
        raise HTTPException(status_code=401, detail=e)
