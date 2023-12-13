"""This module contains graphic functions."""

import matplotlib.pyplot as plt
from classes.detection_class import Detection
def plot_free_places(self):
        detections = []
        free_spaces = []
        for detection in self._detections_list:
            detections.append(detection.get_datetime())
            free_spaces.append(detection.get_free_spaces())
        
        fig = plt.figure(figsize = (10, 5))
        
        # creating the bar plot
        plt.bar(detections, free_spaces, color ='maroon', 
                width = 0.4)
        
        plt.title("Parcheggi liberi in ogni rilevazione")
        plt.ylabel("Numero di parcheggi liberi")
        plt.xlabel("Singole rilevazioni")
        plt.show()