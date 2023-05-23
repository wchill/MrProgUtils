from typing import Any, List, Literal, Optional, Type, Union

from mmbn.gamedata.bn3 import bn3_chip_list, bn3_ncp_list
from mmbn.gamedata.bn6 import bn6_chip_list, bn6_ncp_list
from mmbn.gamedata.chip import Code
from mmbn.gamedata.chip_list_utils import ChipT
from mmbn.gamedata.navicust_part import ColorT, NaviCustPart

SUPPORTED_GAMES = {"switch": [3, 6], "steam": [6]}
SupportedGameLiteral = Literal[3, 6]
SupportedPlatformLiteral = Literal["Switch"]

GAME_MODULES = {
    3: (bn3_chip_list, bn3_ncp_list, bn3_ncp_list.BN3NaviCustPartColor),
    6: (bn6_chip_list, bn6_ncp_list, bn6_ncp_list.BN6NaviCustPartColor),
}


class GameInfo:
    def __init__(self, game: int):
        self.game = game

    @property
    def chip_list(self) -> Any:
        return GAME_MODULES[self.game][0]

    @property
    def ncp_list(self) -> Any:
        return GAME_MODULES[self.game][1]

    @property
    def all_chips(self) -> List[ChipT]:
        return self.chip_list.ALL_CHIPS

    def get_chips_by_name(self, chip_name: str) -> List[ChipT]:
        return self.chip_list.get_chips_by_name(chip_name)

    def get_chip(self, chip_name: str, chip_code: Union[str, Code]) -> Optional[ChipT]:
        return self.chip_list.get_chip(chip_name, chip_code)

    def get_tradable_chip(self, chip_name: str, chip_code: Union[str, Code]) -> Optional[ChipT]:
        return self.chip_list.get_tradable_chip(chip_name, chip_code)

    @property
    def all_parts(self) -> List[NaviCustPart]:
        return self.ncp_list.ALL_PARTS

    def get_part(self, part_name: str, part_color: Union[str, ColorT]) -> Optional[NaviCustPart]:
        return self.ncp_list.get_ncp(part_name, part_color)

    def get_parts_by_name(self, part_name: str) -> List[NaviCustPart]:
        return self.ncp_list.get_parts_by_name(part_name)

    def get_color(self, color_name: str) -> ColorT:
        color_name = color_name.lower().capitalize()
        return self.get_color_class()[color_name]

    def get_color_class(self) -> Type[ColorT]:
        # noinspection PyTypeChecker
        return GAME_MODULES[self.game][2]


GAME_INFO = {3: GameInfo(3), 6: GameInfo(6)}
