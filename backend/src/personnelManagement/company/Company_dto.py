from typing import Optional, List
from odmantic import Model, Field, ObjectId

# class Company(Model):
#     name: Optional[str] = Field("翔隆航太股份有限公司", example="翔隆航太股份有限公司")
#     address: Optional[str] = Field("111 Taipei City Taiwan", example="111 Taipei City Taiwan")
#     tel: Optional[str] = Field("0988888888", example="0988888888")
#     vat: Optional[str] = Field("24736311", example="24736311")
#     remarks: Optional[str] = Field("翔隆航太股份有限公司", example="翔隆航太股份有限公司")
#     imageUrl: Optional[str] = Field("https://static.accupass.com/eventintro/1911041001001992042421.jpg", example="https://static.accupass.com/eventintro/1911041001001992042421.jpg")
#     contacts: List[ObjectId] = Field([], example=[])

#     class Config:
#         collection = "Company"


class Company(Model):
    # * relation
    employees: List[ObjectId] = Field([], example=[])
    drones: List[ObjectId] = Field([], example=[])
    inspections: List[ObjectId] = Field([], example=[])
    parentCompanies: Optional[List[ObjectId]] = Field([], example=[])
    
    # * Metadata
    name: str = Field( example="翔隆航太股份有限公司")
    tel: str = Field( example="0988888888")
    address: str = Field( example="111 Taipei City Taiwan")
    
    vat: Optional[str] = Field("",example="24736311")
    remarks: Optional[str] = Field("",example="翔隆航太股份有限公司")
    imageUrl: Optional[str] = Field("",example="https://static.accupass.com/eventintro/1911041001001992042421.jpg")
    contacts: List[ObjectId] = Field([], example=[])
    
    # *  permission 
    blacklist: List[ObjectId] = Field([], example=[]) # * at least include self
    
    
    

    class Config:
        collection = "Company"
        
        
class CompanyPatchSchema(Model):
    # * relation
    employees: Optional[List[ObjectId]] = Field([], example=[])
    drones:  Optional[List[ObjectId]] = Field([], example=[])
    inspections:Optional[List[ObjectId]] = Field([], example=[])
    parentCompanies: Optional[List[ObjectId]] = Field([], example=[])
    
    # * Metadata
    name: Optional[str] = Field("航空股份有限公司", example="翔隆航太股份有限公司")
    tel: Optional[str] = Field( example="0988888888")
    address: Optional[str] = Field( example="111 Taipei City Taiwan")
    
    vat: Optional[str] = Field("",example="24736311")
    remarks: Optional[str] = Field("",example="翔隆航太股份有限公司")
    imageUrl: Optional[str] = Field("",example="https://static.accupass.com/eventintro/1911041001001992042421.jpg")
    contacts: Optional[List[ObjectId]] = Field([], example=[])
    
    # *  permission 
    blacklist: List[ObjectId] = Field([], example=[]) # * at least include self
    
    
