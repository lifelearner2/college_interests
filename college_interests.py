"""
This code is designed to help High School Seniors keep track of the 
colleges that they are interested in attending along with a few of 
their attributes. The code utilizes lists, dictionaries, for loops,
if statements and while loops.
"""


def main():
   college_dictionary()

#helper function
def college_dictionary():
    #creating a list to store college info
    colleges = []
    
    #This will continue (infinite loop) to ask user if they want to enter in another college until user types q, at which point "break" will stop it.
    while True:
        college_name = input("Enter the college name or 'q' to quit: ")
        if college_name == 'q':
            break
        
        print()
        college_chance_category =  input("Is this is a Safety, Target or Reach school? ")
        college_majors = input("List some majors that they have that you are interested in? ")
        college_interest_level = input("How interested are you in this school on a scale of 1-5 (5 being very interested)? ")
        print()
        
        #storing user input for each college in a dictionary called colleges
        college_info = {
            "college_name": college_name,
            "college_chance_category": college_chance_category,
            "college_majors": college_majors,
            "college_interest_level": college_interest_level
        }
        
        
        colleges.append(college_info)
        
   
    #iterate over dictionary and print contents for each college
    for college in colleges:
        print()
        print(f"College: {college['college_name']}")
        print(f"Chance Category: {college['college_chance_category']}")
        print(f"Majors of interest: {college['college_majors']}")
        print(f"Your interest level: {college['college_interest_level']}")
        print()



if __name__ == "__main__":
    main()