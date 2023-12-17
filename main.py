""""""
from utils.load_convert_function import get_data_from_url, get_data_from_local, generate_parks_list
from utils.plot_function import *
from utils.export_function import export_csv


def main():
    """Function that provides information on parking in Bologna"""
    dictionary = None
    while dictionary is None:
        user_choice = input("Do you want to open a dataset from online or local? ")
        # Code to open dataset from url (online)
        if user_choice.lower() == 'online' or user_choice.lower() =="o":
            print("You have chosen to open an online dataset.")
            try:
                dictionary = get_data_from_url(input("Input url: "))
            except ValueError as value:
                print (f"There is an error: {value}")
        # Code to open dataset from file (local)
        elif user_choice.lower() == 'local' or user_choice.lower() =="l":
            print("You have chosen to open an offline dataset.")
            try:
                dictionary = get_data_from_local(input("Input file path: "))
            except ValueError as value:
                print (f"There is an error: {value}")
        # If the user choice is not valid, an error is raised.
        else:
            print("Invalid choice. Please enter 'online' or 'local'.")
    print("Dictionary loaded successfully.")

    parks_list = generate_parks_list(dictionary)
    #print(parks_list[0].get_detections_list())
    mese_scelto = input("Indica il mese di cui vuoi vedere la disponibilità dei parcheggi: ")
    for i, park in enumerate(parks_list):
        print(f"Scrivi {i} per il parcheggio {park.get_name()}")
    park_choice = input("Scegli un parcheggio: ")
    mese_scelto = int(mese_scelto)
    park_choice = int(park_choice)
    free_parks = generate_free_parks_in_hours(mese_scelto, parks_list[park_choice])
    fig = generate_figure(free_parks, mese_scelto)
    show_plot(fig)
    img_output_name_file = input("Scegli il nome del file immagine: ")
    img_format = input("Scegli il formato del file immagine: ")
    save_plot(fig, img_output_name_file, img_format)
    csv_output_name_file = input("Scegli il nome del file di CSV: ")
    delimiter = input("Scegli il delimitatore del CSV: ")
    export_csv(free_parks, csv_output_name_file, parks_list[park_choice], mese_scelto, delimiter)

    """#  Save file in a .csv
    filename = input("To save the results in a .csv file, choose the name: ")
    while True:
        try:
            geo.save_csv(filename, )
            break
        # If file name contains format error (examples: <, >, :, "", ?, !, |, \, *)
        except:
            filename = input("The chosen name is not allowed. Please input a new name: ")"""

    """with open("data.csv", "w") as my_file:
        #salvataggio dell'heather...
        my_file.write("lat;lon\n")
        my_file.write(f"{my_lat};{my_lon}\n")"""
    
    

    """if format_image.lower() == 'jpg' or format_image.lower() == 'jpeg':
        image.save(f"{file_name}.jpg", "JPEG")
    elif format_image.lower() == 'png':
        image.save(f"{file_name}.png", "PNG")
    elif format_image.lower() == 'svg':
        with open(f"{file_name}.svg", "w") as f:
            f.write(image.tostring())
    elif format_image.lower() == 'pdf':
        image.save(f"{file_name}.pdf", "PDF", resolution=100.0)"""

if __name__ == "__main__":
    main()
