class Traffic_System:

    def __init__(self, Places):
        self.Places = Places

    def displayAvailablePlaces(self):
        print("Recently Visited Places Available in System are: ")
        for Places in self.Places:
            print(" *"+Places)

    def TrafficStatus(self, place):
        if place in self.Places:
            print(
                f"$$You Have Been Provided The Information.$$")
            self.Places.remove(place)
            with open("PlacesList.txt", "a") as f:
                f.write(place+" ")
        else:
            print(
                "$$Sorry, currently place is already available.$$")

    def JourneyEnd(self, place):
        print(f"$$Thanks for Using Traffic System!.Hope you enjoyed the Ride.$$")
        self.Places.append(place)


class place:

    def Requestplace(self):
        self.place = input("Enter the name of place you want to add: ")
        return self.place

    def Places(self):
        self.place = input("Enter the name of place you want to visit: ")
        return self.place


if __name__ == "__main__":
    TrafficManagement = Traffic_System(
        ["Coimbatore", "Thanjavur", "Tirunelveli", "kodaikonal"])
    PlacesArg = place()
    while(True):
        print("\n")
        welcomeMsg = '''======= WELCOME TO TRAFFIC SYSTEM =======
        Please Enter Your Choice:
        1. Recently Visited Areas
        2. Tourist Ride
        3. Regular Ride
        4. Exiting The Traffic_System
        '''
        print(welcomeMsg)
        Choice = int(input("->> "))
        if(Choice == 1):
            TrafficManagement.displayAvailablePlaces()

        elif(Choice == 2):
            n = int(input('''
            1. Lists of Nearer Tourist Places
            2. Enter the Name Of Place You Want To Visit
            3. Make a List of Places You Want To Visit
            --> '''))
            if(n == 1):
                TrafficManagement.displayAvailablePlaces()
            elif(n == 2):
                place = input("Enter the Name of Place: ")
                print(f"best route for {place} is ")
            elif(n == 3):
                with open("PlacesToVist.txt", "w") as f:
                    num = int(
                        input("Enter The Number Of Places U Want To Visit: "))
                    for i in range(num):
                        pl = input(f"Enter The Place {i+1}: ")
                        f.write(pl+" ")
                   
        elif(Choice == 3):

            n = int(input('''
            1. Enter the Name Of Place You Want To Visit
            2. To Find Required Place Near to You
            3. Find The Distance Between Two Places
            --> '''))
            if(n == 1):
                place = input("Enter the Name of Place: ")
                print(f"Best route for {place} is ")
            elif(n == 2):
                place = input("Enter the Name of Place: ")
                print(f"{place} near to you are ")
            elif(n == 3):
                place1 = input(
                    "Enter The place from where you want to Start Journey ")
                place2 = input("Enter The place you want to Reach ")
                with open("places.txt", "r") as f:
                    places = f.read()
                    placeslist = places.split(" ")
                    if place1 in placeslist:
                        if place2 in placeslist:
                            pl1 = [1, 4]
                            pl2 = [3, 8]
                            dist = pow((pl2[0]-pl1[0]), 2) + \
                                pow((pl2[1]-pl1[1]), 2)
                            print(
                                f"The Distance Between {place1} & {place2} is: {dist}Km")
                    else:
                        print("Sorry!...The place is not Availaible in Our Dataset")

        elif(Choice == 4):
            print("******Thank you for using Traffic_System******")

            exit()
        else:
            print("You Entered wrong choice")
