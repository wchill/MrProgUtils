import socket
import time
from typing import Optional


def wait_port(
    host: str = "localhost", port: int = 3000, timeout: Optional[int] = None, attempt_every: int = 100
) -> None:
    """
    wait until a port would be open, for example the port 5432 for postgresql
    before going further

    >>> fixtup.helper.wait_port(5432, timeout=5000)

    :param host: host on which the port has to be open. It will be localhost by default
    :param port: port that has to be open
    :param timeout: timeout in ms before raising TimeoutError.
    :param attempt_every: time in ms between each attempt to check if the port is responding
    """
    start = time.monotonic()
    connected = False
    while not connected:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.connect((host, port))
                connected = True
            except ConnectionRefusedError:
                if timeout is not None and time.monotonic() - start > (timeout / 1000):
                    raise TimeoutError()
            except socket.gaierror:
                if timeout is not None and time.monotonic() - start > (timeout / 1000):
                    raise TimeoutError()

        time.sleep(attempt_every / 1000)
