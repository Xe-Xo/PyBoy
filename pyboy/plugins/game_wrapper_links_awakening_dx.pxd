#
# License: See LICENSE.md file
# GitHub: https://github.com/Baekalfen/PyBoy
#

cimport cython
from libc.stdint cimport uint8_t

from pyboy.logging cimport Logger

cimport pyboy.plugins.window_sdl2
from pyboy.plugins.base_plugin cimport PyBoyGameWrapper
from pyboy.plugins.base_plugin cimport PyBoyWindowPlugin


cdef Logger logger

cdef class GameWrapperLinksAwakeningDX(PyBoyGameWrapper):
    pass

cdef class LinkAwakeningDebugWindow(PyBoyWindowPlugin):
    cdef int width
    cdef int height
    cdef object _window
    cdef object _sdlrenderer
    cdef object _sdltexturebuffer


    @cython.locals(event=WindowEvent)
    cef list handle_events(self, list) noexcept





