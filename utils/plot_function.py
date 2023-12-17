"""This module contains graphic functions."""

import datetime
import matplotlib.pyplot as plt # Library used to create plot.
from classes.parking_class import Parking

# Define a function that creates a bar graph based on the average number of free spaces
# in % and the time slots in a month of your choice.
def plot_free_places(month: int, parking: Parking):
        """Function that create a plot for each month."""
        mese = [data.month for data in [datetime.datetime.strptime(coppia[0], "%Y-%m-%d %H:%M:%S") for coppia in parking.get_detections_list()]]
        # Selezioniamo le coppie del mese di dicembre
        coppie_mese = [coppia for coppia, mese in zip(parking.get_detections_list(), month) if mese == month]
        ore = [data.hour for data in [datetime.datetime.strptime(coppia[0], "%Y-%m-%d %H:%M:%S") for coppia in coppie_mese]]

        occupati_per_fasce_orarie = [[] for _ in range(24)]

        for coppia, ora in zip(coppie_mese, ore):
                occupati_per_fasce_orarie[ora].append(coppia)

        media_posti_libera_ora = []
        for ora in range(24):
                count = 0
                sum = 0
                for rilevazione in occupati_per_fasce_orarie[ora]:
                        sum += (parking.get_total_spaces() - rilevazione[1])
                        count += 1
                if count == 0:
                        avg = 0
                else:
                        avg = sum / count
                #print (f" media è {avg} in percentuale è {(avg/park.get_total_spaces())*100} data da {count} rilevazioni \n")
                media_posti_libera_ora.append((avg/parking.get_total_spaces())*100)
        
        fig = plt.figure(figsize = (10, 5))
        
        # creating the bar plot
        plt.bar(range(24), media_posti_libera_ora, color ='maroon', 
                width = 0.4)
        
        for i, valore in enumerate(media_posti_libera_ora):
                plt.text(i, valore, f"{valore:.2f}%", ha='center', va='bottom')

        nomi_mesi = ["Gennaio", "Febbraio", "Marzo", "Aprile",
                     "Maggio", "Giugno", "Luglio", "Agosto",
                     "Settembre", "Ottobre", "Novembre", "Dicembre"]
        
        plt.title(f"Parcheggi liberi per fascia oraria nel mese di {nomi_mesi[month]}")
        plt.ylabel("Numero di parcheggi liberi")
        plt.xlabel("Orario")
        plt.show()