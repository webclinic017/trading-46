
from src.general.errorCode import ErrorCodeException, ErrorCodeLevel, ErrorCodeModule
from src.general.deleteByIdObject import *
import odmantic
from .Company_dto import Company, CompanyPatchSchema
from mongodb_controller.mongodb_controller import MongoEngine

from odmantic import  ObjectId


    
class CompanyService():
    async def findAllCompanyByUserCompanyId(self, userCompanyId:ObjectId, skip=0, limit=10):
        """[summary]
        # ! 0803 v1 done
        # ! 0818 v2 change white list to black list
        Args:
            userCompanyId (ObjectId): query blackList
            skip (int, optional): [description]. Defaults to 0.
            limit (int, optional): [description]. Defaults to 10.

        Returns:
            dict: all companies the user can query
        """
        
        companies = await MongoEngine.getEngine().find(Company, odmantic.query.not_in(Company.blacklist,  [userCompanyId]), skip= skip, limit =limit)
        userWhiteList = []
        for company in companies:
            companyTemp: dict = dict(company)
            
            companyTemp['id'] = str(companyTemp['id'])
            # * delete unrelational data
            del companyTemp['blacklist']
            del companyTemp['employees']
            del companyTemp['inspections']
            del companyTemp['drones']

            userWhiteList.append(companyTemp)
                
        return userWhiteList
    
    
    async def find_Company_By_CompanyId_And_UserCompanyId(self, userCompanyId:ObjectId, queryCompanyId:ObjectId):
        """[summary]
        # ! 0803 v1 done
        Args:
            userCompanyId (ObjectId): query blackList
            queryCompanyId (ObjectId): ObjectId

        Raises:
            ErrorCodeException: Not found!

        Returns:
            [type]: all companies the user can query
        """
        
        company= await MongoEngine.getEngine().find_one(Company, odmantic.query.and_(Company.id == queryCompanyId, odmantic.query.not_in(Company.blacklist,  [userCompanyId])))

        if company is None:
                raise ErrorCodeException(error_message="Not found!",error_code=ErrorCodeLevel.System + ErrorCodeModule.Company + "0001")

        companyTemp: dict = dict(company)
        # * delete unrelational data
        del companyTemp['id']
        del companyTemp['blacklist']
        del companyTemp['employees']
        del companyTemp['inspections']
        del companyTemp['drones']
        return companyTemp
    
    async def findCompanyByCompanyId(self, queryCompanyId:ObjectId):
        """[summary]

        Args:
            queryCompanyId (ObjectId): 
        Raises:
            ErrorCodeException: "Not found "

        Returns:
            Company: query company
        """
        company= await MongoEngine.getEngine().find_one(Company, Company.id == queryCompanyId)

        if company is None:
                raise ErrorCodeException(error_message="Not fount! ",error_code= ErrorCodeLevel.System + ErrorCodeModule.Company +  "0001")

        return company
    
    async def createCompany(self, company:Company):
        """[summary]

        Args:
            company (Company): company info

        Returns:
            Company: new company info
        """
        company= await MongoEngine.getEngine().save(company)

        return company
    
    async def updateCompany(self, companyPatch:CompanyPatchSchema, oldCompany:Company):
        """[summary]

        Args:
            companyPatch (CompanyPatchSchema): new change of company
            oldCompany (Company): old company info

        Returns:
            [type]: [description]
        """
        companyPatch_dict = companyPatch.dict(exclude_unset=True)
        # * max depth 2
        for name, value in companyPatch_dict.items():
            if type(value) == type({}):
                dictVal = getattr(oldCompany, name)
                for name, value in value.items():
                    setattr(dictVal, name, value)
            else:
                setattr(oldCompany, name, value)
        newCompany = await MongoEngine.getEngine().save(oldCompany)
        return newCompany
    
    async def deleteCompany(self, id:ObjectId):
        """[summary]

        Args:
            id (ObjectId): company id
        Returns:
            str: success
        """
        obj = DeleteByIdObject(id=id,collection="Company",primary_key="id")
        await MongoEngine.getEngine().delete(obj)
        return "success"
