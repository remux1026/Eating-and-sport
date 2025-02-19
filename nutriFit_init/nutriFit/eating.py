import core
import event
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
class eating:
    #man event
    def __init__(self,food,weight):
        self.food_name=food.food_name
        self.energy_gain=food.energy_gain*weight
        self.fat_gain=food.fat_gain*weight
        self.protein_gain=food.protein_gain*weight
        self.vitaminA_gain=food.vitaminA_gain*weight
        self.vitaminB_gain=food.vitaminB_gain*weight
        self.vitaminC_gain=food.vitaminC_gain*weight
