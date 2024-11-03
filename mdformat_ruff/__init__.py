import subprocess

from ruff.__main__ import find_ruff_bin

__version__ = (
    "0.1.3"  # DO NOT EDIT THIS LINE MANUALLY. LET bump2version UTILITY DO IT
)


def format_python(unformatted: str, _info_str: str) -> str:
    r"""Format python.

    :param unformatted:
    :type unformatted: str
    :param _info_str:
    :type _info_str: str
    :rtype: str
    """
    return subprocess.check_output(
        [find_ruff_bin(), "format", "-"],
        input=unformatted.encode(),
        stderr=subprocess.DEVNULL,
    ).decode()
