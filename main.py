""""""
from utils.load_convert_function import get_data_from_url,get_data_from_local, generate_parks_list
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
                get_data_from_url(input("Input url: "))
                break
            except ValueError as value:
                print (f"There is an error: {value}")
        # Code to open dataset from file (local)
        elif user_choice.lower() == 'local' or user_choice.lower() =="l":
            print("You have chosen to open an offline dataset.")
            try:
                get_data_from_local(input("Input file path: "))
                break
            except ValueError as value:
                print (f"There is an error: {value}")
        # If the user choice is not valid, an error is raised.
        else:
            print("Invalid choice. Please enter 'online' or 'local'.")
    print("Dictionary loaded successfully.")

    parks_list = generate_parks_list(dict)
    #print(parks_list[0].get_detections_list())
    plot_free_places(9,parks_list[0])

   
    """with open("data.csv", "w") as my_file:
        #salvataggio dell'heather...
        my_file.write("lat;lon\n")
        my_file.write(f"{my_lat};{my_lon}\n")"""

if __name__ == "__main__":
    main()
