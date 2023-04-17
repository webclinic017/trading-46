from typing import (
    Any,
    AsyncGenerator,
    AsyncIterable,
    Awaitable,
    Dict,
    Generator,
    Generic,
    List,
    Optional,
    Sequence,
    Tuple,
    Type,
    TypeVar,
    Union,
    cast,
)
from odmantic import ObjectId
from odmantic.engine import ModelType
from odmantic.exceptions import DocumentNotFoundError
from odmantic.query import QueryExpression
class DeleteByIdObject:
    __collection__= ""
    id = ObjectId()
    __primary_field__ = ""
    
    def __init__(self, collection, primary_key, id):
        self.__collection__ = collection
        self.__primary_field__ = primary_key
        self.id = id
        
        

# ref: https://github.com/art049/odmantic/pull/147/commits/8bf86af870d0bf7cb1d8123c933b8ea643b2ae4b
# ! odmantic not yet implement! 
async def delete_many(
        engine,
        model: Type[ModelType],
        *queries: Union[
            QueryExpression, Dict, bool
        ],  # bool: allow using binary operators with mypy
    ) -> int:
        """Delete Model instances matching the query filter provided
        Args:
            model: model to perform the operation on
            queries: query filter to apply
        Raises:
            DocumentsNotFoundError: the instance(s) that have not been persisted to
            the database
        Returns:
            int: the number of instances deleted from the database.
        """
        delete_count = 0
        not_found_instances: List[ModelType] = []
        motor_cursor = engine.find(model, *queries)
        async for instance in motor_cursor:
            try:
                await engine.delete(instance)
            except DocumentNotFoundError:
                not_found_instances.append(instance)
            else:
                delete_count += 1
        if not_found_instances:
            raise DocumentNotFoundError(not_found_instances)
        return delete_count