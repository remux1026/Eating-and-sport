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

#parent class of sport and eating
class event:
    def __init__(self,type,date):
        self.type=type
        self.date=date
