""""""
import json
import datetime

def main():
    """"""
    while True:
        bologna_parking = input("percorso ????")
        try:
            with open(bologna_parking) as my_file:
                my_data = json.load(my_file)
                break
        except Exception as ex:
            print(f"we got an error. {ex}")

    
if __name__ == "__main__":
    main()