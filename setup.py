#!/usr/bin/env python
from cx_Freeze import setup,  Executable

setup(
    version = "0.1",
    description = "GUI for pinging continuously",
    name = "PingMe",

    # targets to build
    executables = [Executable(script="pingme.py", icon="world.ico", base="Win32GUI")],
    )

