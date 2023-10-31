from abc import ABC, abstractmethod
from datetime import datetime

class Ride_Sharng:
    def __init__(self, company_name) -> None:
        self.company_name = company_name
        self.riders = []
        self.drivers = []
        self.rides = []

    def add_rider(self, rider):
        self.riders.append(rider)

    def add_driver(self, driver):
        self.drivers.append(driver)

    def __repr__(self) -> str:
        return (f'{self.company_name} with riders : {len(self.riders)} and driverse {len(self.drivers)}')
    
class User(ABC):
    def __init__(self, name, email, nid) -> None:
        self.name = name
        self.email = email 
        # TODO: set user id dynamically 
        self.__id = 0
        self.__nid = nid
        self.wallet = 0

    @abstractmethod
    def display_profile(self):
        raise NotImplementedError


class Rider(User):
    def  __init__(self, name, email, nid, current_location, initial_amount) -> None:
        self.current_ride = None 
        self.wallet = initial_amount
        self.current_location = current_location
        super().__init__(name, email, nid)

    def display_profile(self):
        print(f'Rider: with name {self.name}: {self.email}')

    def load_cash(self, amount):
        if(amount>0):
            self.wallet+=amount

    def update_location(self, current_location):
        self.current_location = current_location

    def request_ride(self, destination):
        if not self.current_ride:
            # TODO: set ride properly 
            # TODO: set current ride via ride match 
            ride_request = Ride_Request(self, destination)
            ride_request = Ride_Matching()
            self.current_ride = None

    def show_current_ride(self):
        print(self.current_ride)

class Driver(User):
    def __init__(self, name, email, nid, current_location) -> None:
        super().__init__(name, email, nid)
        self.current_location = current_location
        self.wallet = 0

    def display_profile(self):
        print (f'Driver with name: {self.name} and eamil: {self.email}')

    def accept_ride(self, ride):
        ride.set_driver(self)



class Ride:
    def __init__(self, start_location, end_location) -> None:
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = None

    def set_driver(self, driver):
        self.driver = driver 
    
    def start_ride(self):
        self.start_time = datetime.now()

    def end_ride(self, rider, amount):
        self.end_time = datetime()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet +=self.estimated_fare

    
    def __repr__(self) -> str:
        return f'Ride details. started: {self.start_location} to {self.end_location}'


class Ride_Request:
    def __init__(self, rider, end_location) -> None:
        self.rider = rider 
        self.end_location = end_location


class Ride_Matching:
    def __init__(self) -> None:
        self.available_drivers = []

    def find_driver(self, ride_request):
        if len(self.available_drivers) > 0:
            #TODO: find the closest driver of the rider 
            driver = self.available_drivers[0]
            ride = Ride(ride_request.rider, ride_request.end_location)
            driver.accept_ride(ride)
            return ride
        

class Vehicle(ABC):

    speed = {
        'car' : 50,
        'bike' : 60,
        'cng': 15
    }

    def __init__(self, vehicle_type, license_plate, rate) -> None:
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate
        self.rate = rate
        self.status = 'available'

    @abstractmethod
    def start_drive(self):
        pass 



class Car(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)

    def start_drive(self):
        self.status = 'Unavailable'


class Bike(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)


    def start_drive(self):
        self.status = 'Unavailable'


# check the class Integration 

niye_jao = Ride_Sharng('Niye Jao')
sakib = Rider('Sakib Khan', 'Sakib@gmail.com', 1235, 'Mohakhali', 1200)
niye_jao.add_rider(sakib)
kala_pakhi = Driver('Kala Paki', 'Kala@dada.com', 5465, 'Gulshan-1')
niye_jao.add_driver(kala_pakhi)

print(niye_jao)

sakib.request_ride('Uttara')
