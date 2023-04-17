
from mongodb_controller.mongodb_controller import engine

from odmantic import ObjectId
from .User_dto import  User, UserPatchSchema

from src.personnelManagement.role.role_service import RoleService

class UserService():
    async def findAllUsers(self):
        """
        TODO: should to implement with Pagination

        Args:
            None

        Returns:
            all users in database

        Raises:
            None
        """

        users = await engine.find(User)
        return users

    async def findAllManagers(self):
        """
        TODO: should to implement with Pagination

        Args:
            None

        Returns:
            all managers in database

        Raises:
            None
        """
        managerRole = await RoleService().findRoleByName("manager")
        users = await engine.find(User, User.role == managerRole.id)
        return users
    
    async def findUserByEmail(self, email: str):
        """


        Args:
            email: str

        Returns:
            specific user 

        Raises:
            None
        """

        user = await engine.find_one(User, User.email == email)
        return user

    async def findUserById(self, id: str):
        """


        Args:
            id: str

        Returns:
            specific user 

        Raises:
            None
        """
        user = await engine.find_one(User, User.id == ObjectId(id))
        return user



    

    async def updateUserPatch(self, userPatch:UserPatchSchema, oldUser:User) :
        """[summary]

        Args:
            userPatch (UserPatchSchema): [description]
            oldUser (User): [description]

        Returns:
            [type]: [description]
        """
        userPatch_dict = userPatch.dict(exclude_unset=True)
        for name, value in userPatch_dict.items():
            if type(value) == type({}):
                dictVal = getattr(oldUser, name)
                for name, value in value.items():
                    setattr(dictVal, name, value)
            else:
                if hasattr(oldUser, name) :
                    setattr(oldUser, name, value)
        newUser = await engine.save(oldUser)
        return newUser
    
    async def updateUser(self, userDto:User) :
        """[summary]

        Args:
            user (User): [description]

        Returns:
            [type]: [description]
        """
        user = await engine.save(userDto)
        return user
    
    async def deleteUser(self, user: User):
        """
        Args:
            id: str
        Returns:
            success or fail

        Raises:
            None
        """
        await engine.delete(user)
        return "success"
