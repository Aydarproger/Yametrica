import grpc.aio as aiogrpc
import pb2.users.users_pb2_grpc as users_pb2_grpc
import pb2.users.users_pb2 as users_pb2
from typing import Any, AsyncGenerator

import data.config as config


class UsersService:
    """
    Class provide interface for working with users service
    """
    def __init__(self, token: str='') -> None:
        self.metadata = (
            ('api-key', config.API_KEY),
            ('access-token', token),
        )

    
    async def add_quiz_answer(self, question: str, answer: str) -> None:
        """
        Add substring to quiz_answers
        """
        async with aiogrpc.insecure_channel(config.USERS_GRPC_URL) as channel:
            stub = users_pb2_grpc.UsersStub(channel)
            request = users_pb2.QuizRequest(field=question, value=answer)
            await stub.QuizAnswer(request,
                                  metadata=self.metadata)
    

    async def update_field(self, 
                           field: str, 
                           value: str | int) -> str:
        """
        Обновляет одно из полей пользователя
        """
        async with aiogrpc.insecure_channel(config.USERS_GRPC_URL) as channel:
            stub = users_pb2_grpc.UsersStub(channel)
            request = users_pb2.UpdateFieldRequest(field=field)
            if isinstance(value, int):
                request.value.number_value = value 
            else:
                request.value.string_value = value
            response: users_pb2.BaseResponse = await stub.UpdateField(request,
                                                                      metadata=self.metadata)
            return response.message
        
        
    async def get_ban_ids(self) -> AsyncGenerator[Any, users_pb2.UserId]:
        """
        Возвращает лист айди забаненых пользователей
        """
        async with aiogrpc.insecure_channel(config.USERS_GRPC_URL) as channel:
            stub = users_pb2_grpc.UsersStub(channel)
            request = users_pb2.BlackListRequest()
            response = stub.GetBlackList(request,
                                         metadata=self.metadata)
            async for user_id in response:
                yield user_id
    
    
    async def get_users(self, limit: int=10, offset: int=0) -> AsyncGenerator[Any, users_pb2.UserResponse]:
        """
        Возвращает список пользователей

        Args:
            limit (int, optional): сколько вернуть
            offset (int, optional): отступ от начала списка
        """
        async with aiogrpc.insecure_channel(config.USERS_GRPC_URL) as channel:
            stub = users_pb2_grpc.UsersStub(channel)
            request = users_pb2.UsersRequest(limit=limit, offset=offset)
            response = stub.GetUsers(request,
                                     metadata=self.metadata)
            async for user in response:
                yield user