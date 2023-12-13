from utils.prova_load import *


"""if __name__ == "__main__":
    from prova_load import get_data_from_local, get_data_from_url
else:
    from utils.prova_load import get_data_from_local, get_data_from_url"""

def main():
    scelta = input("Vuoi aprire un dataset da online o locale? (scrivi 'online' o 'locale'): ")
    if scelta.lower() == 'online':
        # Codice per aprire un dataset online
        print("Hai scelto di aprire un dataset online.")
        try:
            get_data_from_url(input("inserisci url"))
        except Exception as ex:
            print (f"we got an error: {ex}")
        # Inserisci qui il codice per aprire il dataset online

    elif scelta.lower() == 'locale':
        # Codice per aprire un dataset locale
        print("Hai scelto di aprire un dataset locale.")
        try:
            get_data_from_local(input("inserisci file"))
        except Exception as ex:
            print (f"we got an error: {ex}")
        # Inserisci qui il codice per aprire il dataset locale

    else:
        print("Scelta non valida. Per favore, inserisci 'online' o 'locale'.")
        #apri_dataset()  # Richiama la funzione in modo ricorsivo in caso di input non valido
if __name__ == "__main__":
    main()
