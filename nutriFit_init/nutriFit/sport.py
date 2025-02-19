import core
import eating
import event
import food
import schedule
import Searcher
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

class sport:
    #make it a class,in order to allow user Make new sports
    def __init__(self,sport_name,takeout=[]):
        self.sport_name=sport_name
        self.energy_lost=0
        self.fat_lost=0
        self.protein_lost=0
        self.vitaminA_lost=0
        self.vitaminB_lost=0
        self.vitaminC_lost=0
    #[name,energy,fat,protein,vitaminA,vitaminB,vitaminC]
    #the following are some default sports
    #according to given
    def play_basketball(self):
        self.sport_name="play_basketball"
        #in kj
        self.energy_lost=1000
        #in mg
        self.fat_lost=28
        self.protein_lost=17
        self.vitaminA_lost=5
        self.vitaminB_lost=6
        self.vitaminC_lost=0
    def play_socer(self):
        self.sport_name="play_basketball"
        self.energy_lost=0
        self.fat_lost=0
        self.protein_lost=0
        self.vitaminA_lost=0
        self.vitaminB_lost=0
        self.vitaminC_lost=0


    def swim_freestyle(self):
        self.sport_name = "swim_freestyle"
        self.energy_lost = 1500
        self.fat_lost = 40
        self.protein_lost = 22
        self.vitaminA_lost = 6
        self.vitaminB_lost = 8
        self.vitaminC_lost=0

    def cycle_road(self):
        self.sport_name = "cycle_road"
        self.energy_lost = 1800
        self.fat_lost = 55
        self.protein_lost = 30
        self.vitaminA_lost = 7
        self.vitaminB_lost = 10
        self.vitaminC_lost=0

    def lift_weights(self):
        self.sport_name = "lift_weights"
        self.energy_lost = 800
        self.fat_lost = 20
        self.protein_lost = 35
        self.vitaminA_lost = 4
        self.vitaminB_lost = 5
        self.vitaminC_lost=0

    def play_soccer(self):
        self.sport_name = "play_soccer"
        self.energy_lost = 1200
        self.fat_lost = 30
        self.protein_lost = 18
        self.vitaminA_lost = 5
        self.vitaminB_lost = 7
        self.vitaminC_lost=0

    def do_yoga(self):
        self.sport_name = "do_yoga"
        self.energy_lost = 500
        self.fat_lost = 10
        self.protein_lost = 5
        self.vitaminA_lost = 3
        self.vitaminB_lost = 4
        self.vitaminC_lost=0

    def play_tennis(self):
        self.sport_name = "play_tennis"
        self.energy_lost = 1100
        self.fat_lost = 32
        self.protein_lost = 20
        self.vitaminA_lost = 6
        self.vitaminB_lost = 7
        self.vitaminC_lost=0

    def jump_rope(self):
        self.sport_name = "jump_rope"
        self.energy_lost = 1300
        self.fat_lost = 35
        self.protein_lost = 15
        self.vitaminA_lost = 5
        self.vitaminB_lost = 9
        self.vitaminC_lost=0

    def hike_mountain(self):
        self.sport_name = "hike_mountain"
        self.energy_lost = 2000
        self.fat_lost = 60
        self.protein_lost = 25
        self.vitaminA_lost = 8
        self.vitaminB_lost = 12
    def rock_climbing(self):
        self.sport_name = "rock_climbing"
        self.energy_lost = 1700
        self.fat_lost = 50
        self.protein_lost = 40
        self.vitaminA_lost = 7
        self.vitaminB_lost = 10
        self.vitaminC_lost=0

    def skiing(self):
        self.sport_name = "skiing"
        self.energy_lost = 1600
        self.fat_lost = 45
        self.protein_lost = 20
        self.vitaminA_lost = 6
        self.vitaminB_lost = 8
        self.vitaminC_lost=0

    def rowing(self):
        self.sport_name = "rowing"
        self.energy_lost = 1400
        self.fat_lost = 38
        self.protein_lost = 28
        self.vitaminA_lost = 5
        self.vitaminB_lost = 9
        self.vitaminC_lost=0
    def boxing(self):
        self.sport_name = "boxing"
        self.energy_lost = 1800
        self.fat_lost = 60
        self.protein_lost = 35
        self.vitaminA_lost = 7
        self.vitaminB_lost = 12
        self.vitaminC_lost=0

    def skateboarding(self):
        self.sport_name = "skateboarding"
        self.energy_lost = 900
        self.fat_lost = 25
        self.protein_lost = 15
        self.vitaminA_lost = 4
        self.vitaminB_lost = 6
        self.vitaminC_lost=0

    def fencing(self):
        self.sport_name = "fencing"
        self.energy_lost = 1200
        self.fat_lost = 30
        self.protein_lost = 20
        self.vitaminA_lost = 5
        self.vitaminB_lost = 7
        self.vitaminC_lost=0

    def surfing(self):
        self.sport_name = "surfing"
        self.energy_lost = 1400
        self.fat_lost = 45
        self.protein_lost = 25
        self.vitaminA_lost = 6
        self.vitaminB_lost = 9
        self.vitaminC_lost=0

    def wrestling(self):
        self.sport_name = "wrestling"
        self.energy_lost = 1900
        self.fat_lost = 65
        self.protein_lost = 40
        self.vitaminA_lost = 8
        self.vitaminB_lost = 13
        self.vitaminC_lost=0

    def badminton(self):
        self.sport_name = "badminton"
        self.energy_lost = 1100
        self.fat_lost = 32
        self.protein_lost = 18
        self.vitaminA_lost = 5
        self.vitaminB_lost = 7
        self.vitaminC_lost=0

    def parkour(self):
        self.sport_name = "parkour"
        self.energy_lost = 2000
        self.fat_lost = 70
        self.protein_lost = 45
        self.vitaminA_lost = 9
        self.vitaminB_lost = 14

    def horse_riding(self):
        self.sport_name = "horse_riding"
        self.energy_lost = 950
        self.fat_lost = 27
        self.protein_lost = 14
        self.vitaminA_lost = 4
        self.vitaminB_lost = 6
        self.vitaminC_lost=0

    def kayaking(self):
        self.sport_name = "kayaking"
        self.energy_lost = 1250
        self.fat_lost = 37
        self.protein_lost = 22
        self.vitaminA_lost = 6
        self.vitaminB_lost = 8
        self.vitaminC_lost=0

    def table_tennis(self):
        self.sport_name = "table_tennis"
        self.energy_lost = 850
        self.fat_lost = 20
        self.protein_lost = 12
        self.vitaminA_lost = 3
        self.vitaminB_lost = 5
        self.vitaminC_lost=0

    #the following method are abonded
    def sporta(self):
        self.sport_name = "kayaking"
        self.energy_lost = 1250
        self.fat_lost = 37
        self.protein_lost = 22
        self.vitaminA_lost = 6
        self.vitaminB_lost = 8
        self.vitaminC_lost=0
    def sportb(self):
        self.sport_name = "kayaking"
        self.energy_lost = 1250
        self.fat_lost = 37
        self.protein_lost = 22
        self.vitaminA_lost = 6
        self.vitaminB_lost = 8
        self.vitaminC_lost=0
    def sportc(self):
        self.sport_name = "kayaking"
        self.energy_lost = 1250
        self.fat_lost = 37
        self.protein_lost = 22
        self.vitaminA_lost = 6
        self.vitaminB_lost = 8
        self.vitaminC_lost=0
    def sportd(self):
        self.sport_name = "kayaking"
        self.energy_lost = 1250
        self.fat_lost = 37
        self.protein_lost = 22
        self.vitaminA_lost = 6
        self.vitaminB_lost = 8
        self.vitaminC_lost=0
    def sporte(self):
        self.sport_name = "kayaking"
        self.energy_lost = 1250
        self.fat_lost = 37
        self.protein_lost = 22
        self.vitaminA_lost = 6
        self.vitaminB_lost = 8
        self.vitaminC_lost=0
