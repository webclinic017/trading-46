
from src.general.errorCode import ErrorCodeException, ErrorCodeLevel, ErrorCodeModule
from src.personnelManagement.auth.Permission import Permission
from src.personnelManagement.role.Role_dto import Role, RolePatchSchema
from mongodb_controller.mongodb_controller import  engine

from odmantic import ObjectId



    
class RoleService():
    async def createManagerRole(self):
        managerRole = await engine.find_one(Role, Role.name == 'manager')
        if managerRole is None:
            managerPermissions = [Permission.CreateProject, Permission.UpdateBridge]
            managerRole =  Role(name="manager", permissions=managerPermissions, description="manager")
            await engine.save(managerRole)
        return managerRole 
            
        
    async def createRole(self, role:Role):
        """
        ! done 
        Args:
            role: the role data which user wants to create

        Returns:
            the role that user just created

        Raises:
            ValueError: if role name already exists
        """
        
        isExist = await engine.find(Role, Role.name == role.name)
        if isExist:
            raise ErrorCodeException(error_message="Role name already exists!",error_code= ErrorCodeLevel.System + ErrorCodeModule.Role +  "0002")
        else:
            newRole = await engine.save(role)
        return newRole
    
    async def findRoleByName(self, name:str):
        """
        ! done 
        Args:
            name: query name

        Returns:
            the role that has the query name

        Raises:
            None
        """
       
        
   
        role = await engine.find_one(Role, Role.name == name)
        # init guest Role 
        if name == "guest" and role is None:
            guestRole = Role(name = "guest", permissions=[Permission.View], description="guest Only view!")
            await self.createRole(guestRole)
        role = await engine.find_one(Role, Role.name == name)
        return role
    
    async def findRoleById(self, id:str):
        """
        ! done 
        Args:
            name: query ud

        Returns:
            the role that has the query name

        Raises:
            None
        """
        role = await engine.find_one(Role, Role.id == ObjectId(id))
        return role
    
    async def findAllRoles(self, skip=0, limit=10):
        """
        Args:
            skip: Int 
            limit: Int

        Returns:
            all roles with index [skip, skip+limit]

        Raises:
            None
        """
        role = await engine.find(Role, skip=skip, limit=limit)
        return role
    
    async def updateRole(self,rolePatch:RolePatchSchema, role:Role):
        """
        Args:
            role: the role data which user wants to update

        Returns:
            new role info

        Raises:
            None
        """
    
        rolePatch_dict = rolePatch.dict(exclude_unset=True)
        for name, value in rolePatch_dict.items():
            if type(value) == type({}):
                dictVal = getattr(role, name)
                for name, value in value.items():
                    setattr(dictVal, name, value)
            else:
                if hasattr(role, name) :
                    setattr(role, name, value)
        newRole = await engine.save(role)
        return newRole
    
    async def deleteRole(self, role:Role):
        """
        Args:
            role: Role
        Returns:
            success or fail

        Raises:
            None
        """
        await engine.delete(role)
        return "success"
