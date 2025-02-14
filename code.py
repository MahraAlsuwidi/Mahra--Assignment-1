# Hotel Reservation System

class Reservation:
    """Reservation class to manage reservations"""

    def __init__(self, reservation_id, check_in_date, check_out_date, room_number, customer_name, email):
        """Constructor will initialize a Reservation object."""
        self._reservation_id = reservation_id
        self._check_in_date = check_in_date
        self._check_out_date = check_out_date
        self._room_number = room_number
        self._customer_name = customer_name
        self._status = "confirmed"
        self._email = email

    # Getters and Setters for attributes
    def get_reservation_id(self):
        return self._reservation_id

    def set_reservation_id(self, reservation_id):
        self._reservation_id = reservation_id

    def get_check_in_date(self):
        return self._check_in_date

    def set_check_in_date(self, check_in_date):
        self._check_in_date = check_in_date

    def get_check_out_date(self):
        return self._check_out_date

    def set_check_out_date(self, check_out_date):
        self._check_out_date = check_out_date

    def get_room_number(self):
        return self._room_number

    def set_room_number(self, room_number):
        self._room_number = room_number

    def get_customer_name(self):
        return self._customer_name

    def set_customer_name(self, customer_name):
        self._customer_name = customer_name

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status

    # Methods of Reservation class
    def make_reservation(self):
        pass

    def cancel_reservation(self):
        pass

    def modify_reservation(self):
        pass



class Customer:
    """ Class representing a customers in the system """

    def __init__(self, customer_id, name, email, phone_number, payment_details):
        """Constructor will initialize a Customer object."""
        self._customer_id = customer_id
        self._name = name
        self._email = email
        self._phone_number = phone_number
        self._payment_details = payment_details

    # Getters and Setters of attributes
    def get_customer_id(self):
        return self._customer_id

    def set_customer_id(self, customer_id):
        self._customer_id = customer_id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def get_phone_number(self):
        return self._phone_number

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

    def get_payment_details(self):
        return self._payment_details

    def set_payment_details(self, payment_details):
        self._payment_details = payment_details

    def view_reservation(self):
        pass

    def make_payment(self):
        pass


class Room:
    """ Class represent a hotel room in the system"""

    def __init__(self, room_number, room_type, rate_per_night, additional_features):
        """Constructor will initialize a Room object."""
        self._room_number = room_number
        self._room_type = room_type
        self._rate_per_night = rate_per_night
        self._is_available = True
        self._additional_features = additional_features

    # Getters and Setters for private attributes
    def get_room_number(self):
        return self._room_number

    def set_room_number(self, room_number):
        self._room_number = room_number

    def get_room_type(self):
        return self._room_type

    def set_room_type(self, room_type):
        self._room_type = room_type

    def get_rate_per_night(self):
        return self._rate_per_night

    def set_rate_per_night(self, rate_per_night):
        self._rate_per_night = rate_per_night

    def is_room_available(self):
        return self._is_available

    def set_room_availability(self, is_available):
        self._is_available = is_available

    def get_additional_features(self):
        return self._additional_features

    def set_additional_features(self, additional_features):
        self._additional_features = additional_features

    def check_availability(self):
        pass


class Bill:
    """Class represents a bill for a reservation in the system"""

    def __init__(self, bill_id, reservation_id, total_amount, taxes):
        """Constructor will initialize a Bill object."""
        self._bill_id = bill_id
        self._reservation_id = reservation_id
        self._total_amount = total_amount
        self._taxes = taxes
        self._payment_status = "unpaid"

    # Getters and Setters of the private members
    def get_bill_id(self):
        return self._bill_id

    def set_bill_id(self, bill_id):
        self._bill_id = bill_id

    def get_reservation_id(self):
        return self._reservation_id

    def set_reservation_id(self, reservation_id):
        self._reservation_id = reservation_id

    def get_total_amount(self):
        return self._total_amount

    def set_total_amount(self, total_amount):
        self._total_amount = total_amount

    def get_taxes(self):
        return self._taxes

    def set_taxes(self, taxes):
        self._taxes = taxes

    def get_payment_status(self):
        return self._payment_status

    def set_payment_status(self, payment_status):
        self._payment_status = payment_status

    def generate_bill(self):
        pass

    def make_payment(self):
        pass


# Creating a customer object
customer = Customer(1,"Ted Vera","tedvera@mac.com","123-456-7890","Mastercard (ending in 9904)")

# Creating a room object
room = Room(101,"2 Queen Beds",89.95,"No Smoking, Desk, Safe, Coffee Maker, Hair Dryer")

# Creating a reservation object
reservation = Reservation(52523687,"Sun, Aug 22, 2010 - 03:00 PM","Tue, Aug 24, 2010 - 12:00 PM",room.get_room_number(),customer.get_name(),customer.get_email())

# Creating a bill object
bill = Bill(15549850358,reservation.get_reservation_id(),179.90,21.58)

# Displaying reservation and billing details
print("Your Reservation Is Confirmed")
print("Thank you for your reservation. Please print your hotel receipt and sho it at check in.")
print(f"Customer Name: {reservation.get_customer_name()}")
print(f"Email: {reservation.get_email()}")
print("Comfort Inn & Suites Los Alamos")
print(f"Reservation ID: {reservation.get_reservation_id()}")
print(f"Hotel Confirmation Number: {reservation.get_reservation_id()}")
print(f"Check-In: {reservation.get_check_in_date()}")
print(f"Check-Out: {reservation.get_check_out_date()}")
print(f"Room Type: {room.get_room_type()} {room.get_additional_features()}")

print("\nSummary of Charges")
print(f"Room Cost (avg. per room, per night): ${room.get_rate_per_night()}")
print(f"Number of Nights: 2")
print(f"Room Subtotal: ${bill.get_total_amount()}")
print(f"Taxes and Fees: ${bill.get_taxes()}")
print(f"Total Charges: ${bill.get_total_amount() + bill.get_taxes()}")
