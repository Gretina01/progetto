"""This module contains graphic functions."""

import matplotlib.pyplot as plt
import datetime
from classes.parking_class import Parking

def plot_free_places(month:int,park:Parking):

        date = [datetime.datetime.strptime(coppia[0], "%Y-%m-%d %H:%M:%S") for coppia in park.get_detections_list()]

        # Otteniamo il mese da ogni data
        mesi = [data.month for data in date]
        ore = [data.hour for data in date]
        # Selezioniamo le coppie del mese di dicembre
        coppie_mese = [coppia for coppia, mese in zip(park.get_detections_list(), mesi) if mese == month]

        liberi_per_fasce_orarie = []
        
        for i in range (0,23):
                liberi_per_fasce_orarie.append([coppia for coppia, ora in zip(coppie_mese, ore) if ora == i])

        print(liberi_per_fasce_orarie[0])

        """detections = []
        free_spaces = []
        for detection in park.get_detections_list():
            detections.append()
            free_spaces.append(detection.get_free_spaces())
        
        fig = plt.figure(figsize = (10, 5))
        
        # creating the bar plot
        plt.bar(detections, free_spaces, color ='maroon', 
                width = 0.4)
        
        plt.title("Parcheggi liberi in ogni rilevazione")
        plt.ylabel("Numero di parcheggi liberi")
        plt.xlabel("Singole rilevazioni")
        plt.show()"""