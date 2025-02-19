import core
import eating
import event
import food
import schedule
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

class Searcher:
    #food=[name,energy,fat,protein,vitaminA,vitaminB,vitaminC]
    #search food by food name
    def fname_search(self,arr,tar):
        length=len(arr)
        index=-1
        while(index<length-1):
            index+=1
            temp=arr[index][0]
            if(temp==tar):
                return index
    def fenergy_search(self,arr,tar):
        for index in range(len(arr)):
            energy=arr[index][1]
            if energy==tar:
                return index
    def ffat_search(self,arr,tar):
        for index in range(len(arr)):
            fat=arr[index][2]
            if fat==tar:
                return index
    def fprotein_search(self,arr,tar):
        index=0
        while(index<len(arr)):
            protein=arr[index][3]
            if protein==tar:
                return index
            index+=1
        return -1
    def fvitaminA_search(self,arr,tar):
        index=0
        while(index<len(arr)):
            protein=arr[index][4]
            if protein==tar:
                return index
            index+=1
        return -1
    def fvitaminB_search(self,arr,tar):
        index=0
        while(index<len(arr)):
            protein=arr[index][5]
            if protein==tar:
                return index
            index+=1
        return -1
    def fvitaminC_search(self,arr,tar):
        index=0
        while(index<len(arr)):
            protein=arr[index][6]
            if protein==tar:
                return index
            index+=1
        return -1
    #abonded methods,jut keep it here in case needed
    def linear_search(self,arr,tar):
        length=len(arr)
        index=-1
        while(index<length-1):
            index+=1
            temp=arr[index]
            if(temp==tar):
                return index
    # def binary_search_food_by_energy(self,foodlist, target_energy):
    #     left, right= 0, len(foodlist) - 1
    #     while left <= right:
    #         mid=(left+right)//2
    #         if foodlist[mid][1]==target_energy:
    #             return foodlist[mid]
    #         elif foodlist[mid][1]<target_energy:
    #             left=mid+1
    #         else:
    #             right=mid-1

    # def binary_search_food_by_protein(self,foodlist, target_protein):
    #     left,right=0,len(foodlist) - 1
    #     while left<=right:
    #         mid=(left+right)//2
    #         if foodlist[mid][3]==target_protein:
    #             return foodlist[mid]
    #         elif foodlist[mid][3]<target_protein:
    #             left=mid+1
    #         else:
    #             right=mid-1
    #
    # def binary_search_food_by_vitaminA(self,foodlist, target_vitaminA):
    #     left, right = 0, len(foodlist) - 1
    #     while left <= right:
    #         mid = (left + right) // 2
    #         if foodlist[mid][4] == target_vitaminA:
    #             return foodlist[mid]
    #         elif foodlist[mid][4] < target_vitaminA:
    #             left = mid + 1
    #         else:
    #             right = mid - 1
    #
    # def binary_search_food_by_vitaminB(self,foodlist, target_vitaminA):
    #     left, right = 0, len(foodlist) - 1
    #     while left <= right:
    #         mid = (left + right) // 2
    #         if foodlist[mid][5] == target_vitaminA:
    #             return foodlist[mid]
    #         elif foodlist[mid][5] < target_vitaminA:
    #             left = mid + 1
    #         else:
    #             right = mid - 1
    #
    # def binary_search_food_by_vitaminC(self,foodlist, target_vitaminA):
    #     left, right = 0, len(foodlist) - 1
    #     while left <= right:
    #         mid = (left + right) // 2
    #         if foodlist[mid][6] == target_vitaminA:
    #             return foodlist[mid]
    #         elif foodlist[mid][6] < target_vitaminA:
    #             left = mid + 1
    #         else:
    #             right = mid - 1
