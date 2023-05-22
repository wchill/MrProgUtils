import logging
import platform
from typing import Optional

from python_logging_rabbitmq import RabbitMQHandler


def install_logger(host: str, username: str, password: str, logger_name: Optional[str] = None) -> None:
    hostname = platform.node()

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    rabbit = RabbitMQHandler(
        host=host,
        username=username,
        password=password,
        port=5672,
        exchange="log",
        declare_exchange=True,
        routing_key_formatter=lambda r: f"{hostname}.{r.name}.{r.levelname}",
    )
    logger.addHandler(rabbit)
