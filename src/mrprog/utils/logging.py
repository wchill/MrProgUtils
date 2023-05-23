import logging
import platform
from typing import Optional

from python_logging_rabbitmq import RabbitMQHandler


def install_logger(host: str, username: str, password: str, logger_name: Optional[str] = None) -> None:
    logging.getLogger().setLevel(logging.INFO)
    logging.basicConfig()

    hostname = platform.node()

    logger = logging.getLogger(logger_name)
    rabbit = RabbitMQHandler(
        level=logging.DEBUG,
        host=host,
        username=username,
        password=password,
        port=5672,
        exchange="log",
        declare_exchange=True,
        routing_key_formatter=lambda r: f"{hostname}.{r.name}.{r.levelname}",
    )
    # logger.addHandler(rabbit)
