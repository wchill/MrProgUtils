import asyncio
import os
import pathlib
import subprocess
import sys
from typing import Optional

GIT_REPOS = ["BattleNetworkAutomation", "BattleNetworkData", "MrProgDiscordBot", "MrProgWorker", "MrProgUtils"]


async def run_shell_unix(cmd: str, cwd: Optional[str] = None) -> str:
    proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, cwd=cwd)
    stdout, _ = await proc.communicate()
    return stdout.decode("utf-8")


async def run_shell_windows(cmd: str, cwd: Optional[str] = None) -> str:
    proc = await asyncio.to_thread(lambda: subprocess.run(cmd, stdout=subprocess.PIPE, cwd=cwd))
    return proc.stdout.decode("utf-8")


RUN_SHELL_FUNC = run_shell_windows if sys.platform.lower() == "win32" or os.name.lower() == "nt" else run_shell_unix


async def get_git_versions() -> dict[str, str]:
    path = pathlib.Path(__file__)
    while not str(path).endswith("MrProgUtils"):
        path = path.parent

    common_dir = path.parent

    retval = {}
    for repo_name in GIT_REPOS:
        try:
            git_version = (await RUN_SHELL_FUNC("git describe --always", cwd=str(common_dir / repo_name))).strip()
            retval[repo_name] = git_version
        except FileNotFoundError:
            pass
        except NotADirectoryError:
            pass

    return retval
