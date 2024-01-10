import json
datafile = "test_dataFRR.json"
'''
The program is a database of historical federal funds rate set my FOMC meetings. The user could search the change made to FFR by typing in the meeting date (Month Year).
'''
print("==================")
print("Welcome to Fed interest rate database.")
print("Please search for the changes to the federal funds rate (FFR) made after each FOMC meeting by the Month and Year of the meeting.")
print()
print("Type ", '''"Add data"''', " to contribute a data point to the database.")
print("Type ", '''"Exit search"''', " to end the search.")
print("==================")
counter = 1
searched_items = []
added_items = []
deleted_items = []
#add a delete function: ask user if they want ot delete a data being searched. Then add a deleted_items list.

def invalid_input (data_request, data):
    if data_request not in data and data_request != "Add data" and data_request != "Delete data":
     print ("Invalid input.")

while True:
  print("------------Search number {}------------".format(counter))
  data_request = input("Enter a Month and Year of FOMC Meeting: ")
  if data_request == "Exit search":
    print ("Search ended.")
    break
    
  with open(datafile) as json_file:
   data = json.load(json_file) #WITH automatically closes a statement.
    #json.load reads a json file and converts json file format to python. Turning json into a dictionary
  invalid_input(data_request, data)
  if data_request in data and data_request != "March 2020":
    searched_items.append(data_request)
    print("At {}, the following was the change from the previous FOMC meeting: {}. The final FFR after this FOMC meeting was {}.".format(data_request, data[data_request]["change"], data[data_request]["final FFR"]))
    #If the user types a meeting date that is in the database, the program will display the change made to FFR.
  if data_request == "March 2020":
    searched_items.append(data_request)
    march_2020_selection = int(input("Enter the number (1, 2, or 3) of the March 2020 FOMC meeting from which you wish to view the FFR decision:\n1 - March 03, 2020\n2 - March 15, 2020\n3 - March 23, 2020\n"))
    #Since there were three meetings in March 2020, the user selects which of the three to view.
    if march_2020_selection == 1:
      print("At March 03, 2020, the following was the change from the previous FOMC meeting: {}. The final FFR after this FOMC meeting was {}.".format(data["March 2020"]["March 03, 2020"]["change"], data["March 2020"]["March 03, 2020"]["final FFR"]))
    elif march_2020_selection == 2:
      print("At March 15, 2020 the following was the change from the previous FOMC meeting: {}. The final FFR after this FOMC meeting was {}.".format(data["March 2020"]["March 15, 2020"]["change"], data["March 2020"]["March 15, 2020"]["final FFR"]))
    elif march_2020_selection == 3:
      print("At March 23, 2020 the following was the change from the previous FOMC meeting: {}. The final FFR after this FOMC meeting was {}.".format(data["March 2020"]["March 23, 2020"]["change"], data["March 2020"]["March 23, 2020"]["final FFR"]))

  elif data_request == "Add data":
    add_data_key = input("What is the Month and Year of the FOMC Meeting that provides the new data? ")
    added_items.append(add_data_key)
    add_data_key_change = input("What is the new change? ")
    add_data_key_FFR = input ("What is the new final FFR? ")
    with open(datafile, "r") as file:
      new_data = json.load(file)
    print(add_data_key, " has been added to the database.")
      #-----------------------
      #new data template
    template = {"change":"unknown", "final FFR":"unknown"}
      #-----------------------
    new_data[add_data_key] = template.copy()
    new_data[add_data_key]["change"] = add_data_key_change 
      #[] is the key, and what's after "=" is the value.
    new_data[add_data_key]["final FFR"] = add_data_key_FFR
    with open(datafile, "w") as file:
      json.dump(new_data, file) #json.dump turn a python object into a json-acceptable data.
  elif data_request == "Delete data":
    #User could delete a data point in the base by typing "Delete data."
    with open(datafile, "r") as file:
      delete_this_data = json.load(file)
      ask_deleted_data = input("What data point do you wish to delete? ")
    if ask_deleted_data in delete_this_data:
      deleted_items.append(ask_deleted_data)
      del delete_this_data [ask_deleted_data]
      print("Data has been deleted.")
      with open(datafile, "w") as post_delete_file:
        json.dump(delete_this_data, post_delete_file)
    else:
     print ("Please enter a Month and Year of a FOMC meeting data existing in the database.")
  counter = counter + 1
    
print("----------------------------------")
print("Search Summary: Total {} Searches/Additions/Deletes to the database".format(counter))
print("Searched Items: ")
for i in searched_items:
  print("\t",i)
print("Added Data Points: ")
for i in added_items:
  print("\t", i)
print("Deleted Data Points: ")
for i in deleted_items:
  print("\t", i)
