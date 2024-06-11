#
# License: See LICENSE.md file
# GitHub: https://github.com/Baekalfen/PyBoy
#
__pdoc__ = {
    "GameWrapperLinksAwakeningDX.cartridge_title": False,
    "GameWrapperLinksAwakeningDX.post_tick": False,
}

import numpy
import pyboy

from pyboy import utils
from pyboy.api import Sprite, constants
import pyboy.logging
from pyboy.utils import WindowEvent
from pyboy.plugins.base_plugin import PyBoyGameWrapper, PyBoyWindowPlugin
from pyboy.plugins.debug import BaseDebugWindow


try:
    from cython import compiled
    cythonmode = compiled
except ImportError:
    cythonmode = False

try:
    import sdl2
except ImportError:
    sdl2 = None

import os
import re
import zlib
from array import array
from base64 import b64decode
from ctypes import c_void_p


logger = pyboy.logging.get_logger(__name__)

class GameWrapperLinksAwakeningDX(PyBoyGameWrapper):

    argv = [("-links_awakening_dx_debug", "--links_awakening_dx_debug", {"action": "store_true", "help": "Enable emulator debugging mode"})]

    cartridge_title = None

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        if not self.enabled():
            return
        
        print(args)
        print(kwargs)



        if self.pyboy_argv.get("links_awakening_dx_debug"):
            self.debug_window = LinksAwakeningDebugWindow(
                self.pyboy,
                self.mb,
                self.pyboy_argv
            )
        else:
            self.debug_window = None

    def enabled(self):
        return self.pyboy.cartridge_title == "ZELDA"
    
    def debug_window_enabled(self):
        return self.debug_window is not None

    def handle_events(self, events):
        #if self.sdl2_event_pump:
        #    events = sdl2_event_pump(events)
        if self.debug_window_enabled():
            events = self.debug_window.handle_events(events)
        return events

    def post_tick(self):
        if self.debug_window_enabled():
            self.debug_window.post_tick()
        pass

    def __repr__(self):
        # yapf: disable
        return (
            f"Links Awakening DX:\n" +
            super().__repr__()
        )
    
    def stop(self):
        #self.debug_window.stop()
        return super().stop()


class LinksAwakeningDebugWindow(BaseDebugWindow):
    
    def __init__(self, *args, **kwargs):
        

        super().__init__(
            *args          
            ,scale=2
            ,title="Window"
            ,width=256
            ,height=256
            ,pos_x=0
            ,pos_y=0      
            ,**kwargs
            )


        self.base_title = "Links Awakening DX Debug"
        self.update_title()

    
    def post_tick(self):
        self.draw_overlay()
        BaseDebugWindow.post_tick(self)

    def draw_overlay(self):
        pass

    def update_title(self):
        title = self.base_title
        title += " Links Awakening DX " 
        sdl2.SDL_SetWindowTitle(self._window, title.encode("utf8"))

