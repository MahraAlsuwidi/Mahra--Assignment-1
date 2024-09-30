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

