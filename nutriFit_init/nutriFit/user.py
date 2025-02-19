import core
import eating
import event
import food
import schedule
import Searcher
import sport
import sys
import os
import shutil
import pathlib
import glob
import logging
import argparse
import configparser
import platform
class user:
    def __init__(self,user_id,name,age,weight,height,schedule=[],plan=[],menu=[]):
        self.id=user_id
        self.name=name
        self.age=age
        self.weight=weight
        self.height=height
        self.schedule= []
        self.sport_schedule= []
        self.eating_schedule= []
        self.plan=[]
        self.menu=[]
    def add_schedule(self,event):
        self.schedule.append(event)
    def remove_schedule(self, event):
        if event in self.schedule:
            self.schedule.remove(event)
    # def __str__(self):
    #     return (f"User(id={self.id}, name='{self.name}', age={self.age}, weight={self.weight}, height={self.height}, "
    #             f"schedule={self.schedule}, plan={self.plan})")
    def get_bmi(self):
        return self.weight/(self.height**2)
    #abonded method
    def add_plan(self, plan_item: str):
        self.plan.append(plan_item)
    def remove_plan(self, plan_item: str):
        if plan_item in self.plan:
            self.plan.remove(plan_item)
    #mbt
    def show_weight_in_kg(self):
        show_weight=self.weight/1000.0
        print(show_weight)
    def show_weight_in_pound(self):
        show_weight=self.weight/483.59
        print(show_weight)
    def show_height_in_meter(self):
        show_height=self.height/100.0
        print(show_height)
    def show_height_in_feet(self):
        show_height=self.height/30.48
        print(show_height)
    def show_height_in_inch(self):
        show_height=self.height/2.54
        print(show_height)
    def get_predict_weight(self):
        energy_lost=0
        for sport in self.sport_schedule:
            energy_lost+=sport.energy_lost
        energy_gain=0
        for eating in self.eating_schedule:
            energy_gain+=eating.energy_gain
        energy_change=energy_gain-energy_lost
        #accoringd to the given pdf 1g body weight=9000kj
        weight_change=energy_change/9
        self.weight+=weight_change
        predict_weight=self.weight
        return predict_weight
    def get_fat_change(self):
        fat_lost=0
        for sport in self.sport_schedule:
            fat_lost+=sport.fat_lost
        fat_gain=0
        for eating in self.eating_schedule:
            fat_gain+=eating.fat_gain
        fat_change=fat_gain-fat_lost
        return fat_change

    def get_vitaminA_change(self):
        vitaminB_lost=0
        for sport in self.sport_schedule:
            vitaminB_lost+=sport.vitaminB_lost
        vitaminB_gain=0
        for eating in self.eating_schedule:
            vitaminB_gain+=eating.vitaminB_gain
        vitaminB_change=vitaminB_gain-vitaminB_lost
        return vitaminB_change
