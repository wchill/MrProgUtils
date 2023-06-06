import asyncio
import pathlib
from typing import Optional

GIT_REPOS = ["BattleNetworkAutomation", "BattleNetworkData", "MrProgDiscordBot", "MrProgWorker", "MrProgUtils"]


async def run_shell(cmd: str, cwd: Optional[str] = None) -> str:
    proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, cwd=cwd)
    stdout, _ = await proc.communicate()
    return stdout.decode("utf-8")


async def get_git_versions() -> dict[str, str]:
    path = pathlib.Path(__file__)
    while not str(path).endswith("MrProgUtils"):
        path = path.parent

    common_dir = path.parent

    retval = {}
    for repo_name in GIT_REPOS:
        try:
            git_version = (await run_shell("git describe --always", cwd=str(common_dir / repo_name))).strip()
            retval[repo_name] = git_version
        except FileNotFoundError:
            pass

    return retval
