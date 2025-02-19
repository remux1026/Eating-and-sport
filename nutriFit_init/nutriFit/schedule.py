import core
import eating
import event
import food
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
class schedule:
    def __init__(self,start_date,end_date,event_list=[]):
        self.start_date=start_date
        self.end_date=end_date
        if event_list!=[]:
            #if not empty,then copy the list
            self.event_list=event_list
        else:
            #if empty then create empty list
            self.event_list=[]
    def add_event_simple(self,event):
        self.event_list.append(event)
    def add_event_in_date_oreder(self,date,event):
        index=date-self.start_date
        if self.event_list==[]:
            for i in range(index):
                self.event_list.append(None)
            self.event_list.append(event)
        elif index>len(self.event_list):
            for i in range(index-len(self.event_list)):
                self.event_list.append(None)
            self.event_list.append(event)
        else:
            self.event_list.append(event)
    def get_date_fat_change(self,date):
        fat_change=0
        for event in self.event_list:
            if isinstance(event,sport):
                fat_change-=event.fat_lost
            if isinstance(event,eating):
                fat_change-=event.fat_gain
        return fat_change
    def get_date_weight_change(self,date):
        energy_change=0
        for event in self.event_list:
            if isinstance(event,sport):
                if event.date==date:
                    energy_change-=event.energy_lost
            if isinstance(event,eating):
                if event.date==date:
                    energy_change-=event.energy_gain
        weight_change=energy_change/9
        return weight_change

    def get_date_fat_change(self,date):
        fat_change=0
        for event in self.event_list:
            if isinstance(event,sport):
                if event.date==date:
                    fat_change-=event.fat_lost
            if isinstance(event,eating):
                if event.date==date:
                    fat_change-=event.fat_gain
        return fat_change
    def get_date_vitaminA_change(self,date):
        vitaminA_change=0
        for event in self.event_list:
            if isinstance(event,sport):
                if event.date==date:
                    vitaminA_change-=event.vitaminA_lost
            if isinstance(event,eating):
                if event.date==date:
                    vitaminA_change-=event.vitaminA_gain
        return vitaminA_change
    def get_date_vitaminB_change(self,date):
        vitaminB_change=0
        for event in self.event_list:
            if isinstance(event,sport):
                if event.date==date:
                    vitaminB_change-=event.vitaminB_lost
            if isinstance(event,eating):
                if event.date==date:
                    vitaminB_change-=event.vitaminB_gain
        return vitaminB_change
    def get_date_vitaminC_change(self,date):
        vitaminC_change=0
        for event in self.event_list:
            if isinstance(event,sport):
                if event.date==date:
                    vitaminC_change-=event.vitaminC_lost
            if isinstance(event,eating):
                if event.date==date:
                    vitaminC_change-=event.vitaminC_gain
        return vitaminC_change
    def get_date_energy_change(self,date):
        energy_change=0
        for event in self.event_list:
            if isinstance(event,sport):
                if event.date==date:
                    energy_change-=event.energy_lost
            if isinstance(event,eating):
                if event.date==date:
                    energy_change-=event.energy_gain
        return energy_change
    def get_events_on_date(self, date):
        events_on_date = []
        for event in self.event_list:
            if hasattr(event, 'date'):
                if event.date == date:
                    events_on_date.append(event)
        return events_on_date
    def clean_event_list(self):
        cleaned_list = []
        for event in self.event_list:
            if event is not None:
                cleaned_list.append(event)
        self.event_list = cleaned_list
