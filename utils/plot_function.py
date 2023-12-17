"""This module contains graphic functions."""

import datetime
import matplotlib.pyplot as plt # Library used to create plot.
from classes.parking_class import Parking
from utils.validations import validate_free_spaces_by_time_slot
from constants.months import Month
from utils.validations import validate_file_name, validate_format_image


# Define a function that creates a bar graph based on the average number of free spaces
# in % and the time slots in a month of your choice.
def generate_free_parks_in_hours(month: int, parking: Parking):
        mesi = [data.month for data in [datetime.datetime.strptime(coppia[0], "%Y-%m-%d %H:%M:%S") for coppia in parking.get_detections_list()]]
        # Selezioniamo le coppie del mese di dicembre
        coppie_mese = [coppia for coppia, mese in zip(parking.get_detections_list(), mesi) if mese == month]
        ore = [data.hour for data in [datetime.datetime.strptime(coppia[0], "%Y-%m-%d %H:%M:%S") for coppia in coppie_mese]]

        occupati_per_fasce_orarie = [[] for _ in range(24)]

        for coppia, ora in zip(coppie_mese, ore):
                occupati_per_fasce_orarie[ora].append(coppia)

        avg_free_spaces_by_time_slot = []
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
                avg_free_spaces_by_time_slot.append((avg/parking.get_total_spaces())*100)
        
        return avg_free_spaces_by_time_slot

def generate_figure(avg_free_spaces_by_time_slot: list, month: int, output_name_file: str, format_image: str):
        try:
                validate_free_spaces_by_time_slot(avg_free_spaces_by_time_slot)
        except ValueError as value:
                print(value)
        except TypeError as value:
                print(value)
        else:
                plt.figure(figsize = (10, 5))
                plt.bar(range(24), avg_free_spaces_by_time_slot, color ='maroon', 
                        width = 0.4)
                
                for i, valore in enumerate(avg_free_spaces_by_time_slot):
                        plt.text(i, valore, f"{valore:.2f}%", ha='center', va='bottom')
                        plt.title(f"Parcheggi liberi per fascia oraria nel mese di {Month(month).name}")
                        plt.ylabel("Numero di parcheggi liberi")
                        plt.xlabel("Orario")
                #return fig
                        

#def save_plot(fig: plt.figure, output_name_file: str, format_image: str):
                try:
                        validate_file_name(output_name_file)
                        validate_format_image(format_image)
                except ValueError as value:
                        print(value)
                except TypeError as value:
                        print(value)
                else:
                        plt.savefig(f"outputs/{output_name_file}.{format_image}", format=format_image)
        

# def show_plot(fig: plt.figure):
                plt.show()         
         


