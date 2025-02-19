import core
import eating
import food
import schedule
import Searcher
import sport
import user
import sys
import os
import shutil
import pathlib
import glob
import logging
import argparse
import configparser
import platform
from ui import ui
import database

#self,id,user,database,ui

def main():
    A_ui=ui()
    core_0 = core.core(id=0, user=None, database=None, ui=A_ui)

    core_0.start()

if __name__ == "__main__":
    main()
