import datetime

def main():
    # Printing
    print("Hello, world!")
 
    # Input
    name = input("Enter your name: ")
    print("Hello,", name)

    # Birthdate input
    birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
    birthdate = datetime.datetime.strptime(birthdate_str, "%Y-%m-%d")
    current_date = datetime.datetime.now()
    age = current_date.year - birthdate.year
    
    
    # Calculate age
    print("You are", age, "years old.")
    
    # Variables
    variable_name = age
    variable_name = variable_name + 1
    print("Your age in the upcoming year:", variable_name)

   

if __name__ == '__main__':
    main()

