#This file will hold the class for the ideology information.

#Importing files that will be used for the project
import pandas as pd
import numpy as np

#This class will deal with all of the data for this project.
class Ideology():

    #The following methods all deal with looking at ideology. I will come out and
    #say it that at this point, this is bad code. I repeat myself over and over again!
    #I shall look to fix this.
    def right_wing_info(self):
        self.__data = pd.read_csv('plots.csv')
        data_type = 'Right Wing'
        total_deaths = len(self.__data)
        attacks = len(self.__data[self.__data.plot_ideology == data_type])
        return total_deaths, attacks

    def left_wing_info(self):
        self.__data = pd.read_csv('plots.csv')
        data_type = 'Left Wing'
        total_deaths = len(self.__data)
        attacks = len(self.__data[self.__data.plot_ideology == data_type])
        return total_deaths, attacks

    def islamic_info(self):
        self.__data = pd.read_csv('plots.csv')
        data_type = 'Jihadist'
        total_deaths = len(self.__data)
        attacks = len(self.__data[self.__data.plot_ideology == data_type])
        return total_deaths, attacks

    def prevented(self):
        self.__data = pd.read_csv('plots.csv')
        total_attacks = len(self.__data)
        prevented = len(self.__data[self.__data.plot_status == 'Prevented'])
        return total_attacks, prevented

    def not_prevented(self):
        self.__data = pd.read_csv('plots.csv')
        total_attacks = len(self.__data)
        not_prevented = len(self.__data[self.__data.plot_status == 'Not Prevented'])
        return total_attacks, not_prevented

    #This method will allow the user to see attacks were a certain number of
    #people were killed.
    def deaths(self, number_deaths):
        self.__data = pd.read_csv('plots.csv')
        information = self.__data[self.__data.victims_killed >= number_deaths]
        return information
