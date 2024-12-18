import grpc.aio as aiogrpc
import pb2.auth.auth_pb2 as auth_pb2
import pb2.auth.auth_pb2_grpc as auth_pb2_grpc

import data.config as config


class AuthService:
    def __init__(self) -> None:
        self.metadata = (
            ('api-key', config.API_KEY),
        )

    async def auth(self, id: int, username: str, utm_source: str='') -> auth_pb2.AuthResponse:
        """
        Авторизует или создаёт пользователя

        Проверить создание пользователя можно по полю status в объекте
        ответа
        """
        async with aiogrpc.insecure_channel(config.AUTH_GRPC_URL) as channel:
            stub = auth_pb2_grpc.AuthStub(channel)
            request = auth_pb2.AuthRequest(id=id, username=username, utm_source=utm_source)
            response: auth_pb2.AuthResponse = await stub.AuthOrCreate(request, 
                                                                      metadata=self.metadata)
            return response
    

    # async def auth(self, phone: str) -> str:
    #     """
    #     Отправляет код на телефон пользователя
    #     """
    #     async with aiogrpc.insecure_channel(config.auth_addr) as channel:
    #         stub = auth_pb2_grpc.AuthStub(channel)
    #         request = auth_pb2.AuthRequest(phone=phone)
    #         response: auth_pb2.BaseResponse = await stub.Auth(request, metadata=self.metadata)
    #         return response.message
    

    # async def check_auth(self, 
    #                      user_id: int, 
    #                      username: str, 
    #                      otp_code: int, 
    #                      phone: str) -> str:
    #     """
    #     Проверка кода
    #     """
    #     async with aiogrpc.insecure_channel(config.auth_addr) as channel:
    #         stub = auth_pb2_grpc.AuthStub(channel)
    #         request = auth_pb2.CheckAuthCodeRequest(
    #             phone=phone,
    #             otp_code=otp_code,
    #             username=username,
    #             id=user_id
    #         )
    #         response: auth_pb2.TokenResponse = await stub.CheckAuthCode(request, 
    #                                                                     metadata=self.metadata)
    #         return response.access_token
        