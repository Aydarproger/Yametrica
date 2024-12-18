from typing import AsyncGenerator, Any

import grpc.aio as aiogrpc
import pb2.game.game_pb2 as game_pb2
import pb2.game.game_pb2_grpc as game_pb2_grpc

import data.config as config


class GameService:
    def __init__(self, token: str='') -> None:
        self.metadata = (
            ('api-key', config.API_KEY),
            ('access-token', token),
        )

    async def get_rating(self, limit: int=30) -> AsyncGenerator[Any, game_pb2.RatingResponse]:
        """
        Возвращает AsyncGenerator с пользователями (rank, username, score)
        """
        async with aiogrpc.insecure_channel(config.GAME_GRPC_URL) as channel:
            stub = game_pb2_grpc.GameStub(channel)
            request = game_pb2.RatingRequest(limit=limit)
            response = stub.GetRating(
                request,
                metadata=self.metadata
            )
            async for user in response:
                yield user
    