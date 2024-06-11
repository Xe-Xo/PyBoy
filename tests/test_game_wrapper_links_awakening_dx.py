#
# License: See LICENSE.md file
# GitHub: https://github.com/Baekalfen/PyBoy
#

import os
import platform
import sys

import numpy as np
import pytest

from pyboy import PyBoy
from pyboy.plugins.game_wrapper_links_awakening_dx import GameWrapperLinksAwakeningDX
from pyboy.utils import WindowEvent

def test_links_awakening_dx_basics(links_awakening_dx_rom):
    pyboy = PyBoy(links_awakening_dx_rom, window="null")
    pyboy.set_emulation_speed(0)
    assert pyboy.cartridge_title == "THE LEGEND OF ZELDA: LINK'S AWAKENING DX"

    links_awakening_dx = pyboy.game_wrapper
    assert isinstance(links_awakening_dx, GameWrapperLinksAwakeningDX)

    assert links_awakening_dx.enabled()
    pyboy.stop(False)

def test_links_awakening_dx_advanced(links_awakening_dx_rom):
    pyboy = PyBoy(links_awakening_dx_rom, window="null")
    pyboy.set_emulation_speed(0)
    assert pyboy.cartridge_title == "THE LEGEND OF ZELDA: LINK'S AWAKENING DX"

    links_awakening_dx = pyboy.game_wrapper
    assert isinstance(links_awakening_dx, GameWrapperLinksAwakeningDX)

    assert links_awakening_dx.enabled()
    pyboy.stop(False)