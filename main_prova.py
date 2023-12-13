from utils.prova_load import *
from utils.load_function import *
from utils.plot_function import *


"""if __name__ == "__main__":
    from prova_load import get_data_from_local, get_data_from_url
else:
    from utils.prova_load import get_data_from_local, get_data_from_url"""

def main():
    dict = None
    while dict == None:
        scelta = input("Vuoi aprire un dataset da online o locale? (scrivi 'online' o 'locale'): ")
        if scelta.lower() == 'online' or scelta.lower() == 'o':
            # Codice per aprire un dataset online
            print("Hai scelto di aprire un dataset online.")
            try:
                dict = load_dict_from_url(input("inserisci url: "))
            except Exception as ex:
                print (f"we got an error: {ex}")
            # Inserisci qui il codice per aprire il dataset online

        elif scelta.lower() == 'locale' or scelta.lower() == 'l':
            # Codice per aprire un dataset locale
            print("Hai scelto di aprire un dataset locale.")
            try:
                dict = load_dict_from_file(input("inserisci file"))
            except Exception as ex:
                print (f"we got an error: {ex}")
            # Inserisci qui il codice per aprire il dataset locale

        else:
            print("Scelta non valida. Per favore, inserisci 'online' o 'locale'.")
            #apri_dataset()  # Richiama la funzione in modo ricorsivo in caso di input non valido
    print("Dizionario caricato correttamente")
    parks_list = generate_parks_list(dict)
    #print(parks_list[0].get_detections_list())
    plot_free_places(9,parks_list[0])

if __name__ == "__main__":
    main()
