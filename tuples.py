# Define a function to collect and display group details
def collect_group_details():
    # Initialize an empty list to store group details
    groups = []

    # Loop to collect details for 5 groups
    for i in range(5):
        print(f"\nEntering details for Group {i + 1}:")
        
        # Collecting group details from user input
        group_name = input("Enter the group name: ")
        group_size = int(input("Enter the size of the group: "))
        competition_date = input("Enter the date of the competition (YYYY-MM-DD): ")
        venue = input("Enter the venue: ")
        medal_type = input("Enter the type of medal (gold, silver, bronze): ").lower()
        
        # Creating a tuple with the collected details
        group_details = (group_name, group_size, competition_date, venue, medal_type)
        
        # Adding the tuple to the list of groups
        groups.append(group_details)

    # Displaying all group records
    print("\n--- Group Records ---")
    for index, group in enumerate(groups):
        print(f"Group {index + 1}:")
        print(f"  Name: {group[0]}")
        print(f"  Size: {group[1]}")
        print(f"  Competition Date: {group[2]}")
        print(f"  Venue: {group[3]}")
        print(f"  Medal Type: {group[4]}")
        print()

# Call the function to execute the program
if __name__ == "__main__":
    collect_group_details()
