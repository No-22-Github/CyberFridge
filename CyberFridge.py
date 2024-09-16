import sys
import os
import toml
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from moudles.main.config_loader import *
from moudles.main.tray_icon import *

def main():
    checker()
    chara = path_mapper()
    tray_icon(*chara)

main()