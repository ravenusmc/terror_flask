#This file will hold the class for the ideology information.

#Importing files that will be used for the project
import pandas as pd
import numpy as np

#This class will deal with all of the data for this project.
class Ideology():

    #The following method all deal with looking at ideology.
    def ideology_info(self, data_type):
        self.__data = pd.read_csv('plots.csv')
        total_deaths = len(self.__data)
        attacks = len(self.__data[self.__data.plot_ideology == data_type])
        return total_deaths, attacks

    #The following two methods allow the user to look at prevented and attacks
    #which were not prevented.
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
        self.__data = self.__data[self.__data.victims_killed >= number_deaths]
        plot = self.__data[[1]]
        plot = plot.values
        return plot

#This is only for draft/testing purposes to make sure that my code works how
#I want it to work.
# idea =  Ideology()
# plot = idea.deaths(45)
# print(plot)
