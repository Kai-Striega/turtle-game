import os
from pathlib import Path
import platform

if platform.system() == "Windows":
    import winsound

from bounding_box import SoundStrategy


class MacSoundStrategy:

    def __init__(self, sound_file_path: Path) -> None:
        self._sound_file_path = sound_file_path

    def play(self) -> None:
        os.system(f"afplay {self._sound_file_path}&")


class WindowsSoundStrategy:
    def __init__(self, sound_file_path: Path) -> None:
        self._sound_file_path = sound_file_path

    def play(self) -> None:
        winsound.PlaySound(str(self._sound_file_path), winsound.SND_ASYNC)


class LinuxSoundStrategy:

    def __init__(self, sound_file_path: Path) -> None:
        self._sound_file_path = sound_file_path

    def play(self) -> None:
        print("Sound for Linux systems is not implemented yet...")


def create_sound_strategy(sound_file_path: Path) -> SoundStrategy:

    match platform.system():
        case "Darwin":
            return MacSoundStrategy(sound_file_path)
        case "Windows":
            return WindowsSoundStrategy(sound_file_path)
        case "Linux":
            return LinuxSoundStrategy(sound_file_path)
        case _:
            raise ValueError("Working on unsupported OS.")


