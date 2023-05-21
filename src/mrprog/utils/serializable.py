from typing import Type

import jsonpickle as jsonpickle


class Serializable:
    def to_json(self) -> str:
        return jsonpickle.dumps(self.__dict__)

    @classmethod
    def from_json(cls: Type["Serializable"], data: str) -> "Serializable":
        request = cls.__new__(cls)
        request.__dict__ = jsonpickle.loads(data)
        return request

    def to_bytes(self) -> bytes:
        return self.to_json().encode("utf-8")

    @classmethod
    def from_bytes(cls: Type["Serializable"], data: bytes) -> "Serializable":
        return cls.from_json(data.decode("utf-8"))
