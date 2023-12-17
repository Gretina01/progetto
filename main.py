""""""
from utils.load_convert_function import get_data_from_url, get_data_from_local, generate_parks_list
from utils.plot_function import plot_free_places

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
    plot_free_places(10,parks_list[0])

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
