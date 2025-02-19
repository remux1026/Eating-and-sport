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
import ui
from database import database
class core:
    def __init__(self,id,user=None,database=None,ui=None):
        self.id=id
        self.user=user
        self.database=database
        self.ui=ui
    def set_user(self,user_id,name,age,weight,height,schedule=[],plan=[],menu=[]):
        new_user=user.user(user_id,name,age,weight,height,schedule,plan,menu)
        self.user=new_user
        return new_user
    def set_database(self,new_database):
        self.database=new_database
        return new_database
    def start(self):
        self.ui.print_welcome_page()
        new_user=user.user(-1,"default",0,0,0,[],[],[])
        new_database=database(0)
        new_database.standardlize_sport_database()
        new_database.standardlize_food_database()
        self.database=new_database
        self.user=new_user
        self.ui.display_main_menu()
        self.ui.get_user_choice()
