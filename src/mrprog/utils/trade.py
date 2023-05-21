import base64
from typing import Any, Optional

from .serializable import Serializable
from .types import TradeItem


class TradeRequest(Serializable):
    def __init__(
        self,
        user_name: str,
        user_id: int,
        channel_id: int,
        system: str,
        game: int,
        trade_id: int,
        trade_item: TradeItem,
        priority: Optional[int] = 0,
    ):
        self.user_name = user_name
        self.user_id = user_id
        self.channel_id = channel_id
        self.system = system
        self.game = game
        self.trade_id = trade_id
        self.trade_item = trade_item

        # TODO: Implement priority
        self.priority = priority


class TradeResponse(Serializable):
    SUCCESS = 0
    IN_PROGRESS = 1
    USER_TIMEOUT = 2
    RETRYING = 3
    FAILURE = 4
    CRITICAL_FAILURE = 5
    CANCELLED = 6

    def __init__(
        self,
        request: TradeRequest,
        worker_id: str,
        status: int,
        *,
        message: Optional[str] = None,
        embed: Optional[dict[str, Any]] = None,
        image: Optional[bytes] = None,
    ):
        self.request = request
        self.worker_id = worker_id
        self.status = status
        self.message = message
        self.embed = embed
        self.image = image

    @property
    def image(self) -> bytes:
        return base64.b85decode(self._image)

    @image.setter
    def image(self, data: bytes) -> None:
        self._image = base64.b85decode(data)
