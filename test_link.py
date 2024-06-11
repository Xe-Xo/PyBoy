from pyboy import PyBoy


pyboy = PyBoy("test_roms/ladx.gbc", links_awakening_dx_debug=True)


while pyboy.tick():
    pass


pyboy.stop()