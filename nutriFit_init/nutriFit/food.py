import core
import eating
import event
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

class food:
    #food database class
    def __init__(self,food_name):
        #nutrion data in per pound
        self.food_name=food_name
        self.energy_gain=0
        self.fat_gain=0
        self.protein_gain=0
        self.vitaminA_gain=0
        self.vitaminB_gain=0
        self.vitaminC_gain=0
    def change_data_to_kg(self,food_name):
        #nutrion data in per pound
        self.food_name=food_name
        self.energy_gain=self.energy_gain/453.59*1000.0
        self.fat_gain=self.fat_gain/453.59*1000.0
        self.protein_gain=self.protein_gain/453.59*1000.0
        self.vitaminA_gain=self.vitaminA_gain/453.59*1000.0
        self.vitaminB_gain=self.vitaminB_gain/453.59*1000.0
        self.vitaminC_gain=self.vitaminB_gain/453.59*1000.0
    def change_data_to_g(self,food_name):
        #nutrion data in per pound
        self.food_name=food_name
        self.energy_gain=self.energy_gain/453.59
        self.fat_gain=self.fat_gain/453.59
        self.protein_gain=self.protein_gain/453.59
        self.vitaminA_gain=self.vitaminA_gain/453.59
        self.vitaminB_gain=self.vitaminB_gain/453.59
        self.vitaminC_gain=self.vitaminB_gain/453.59
