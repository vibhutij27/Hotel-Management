class hotel():
    def __init__(self, room_no = 0, from_date = '', to_date = '', room_cat = 0):
        self.from_date = from_date
        self.to_date = to_date
        self.room_no = room_no
        self.room_cat = room_cat
        #Struct {room_no:[room_cat,availability,price_per_day]}
        self.room = {101:[1,0,6000],102:[1,0,6000],103:[2,1,5000],
            104:[2,0,5000],105:[4,1,3000],201:[1,1,6000],
            202:[1,1,6000],203:[3,1,4000],204:[3,1,4000],
            205:[4,1,3000]}
        #struct {room_cat:[room_no]}
        self.room_type = {1:[101,102,201,202],2:[103,104],3:[203,204],4:[105,205]}
    
    def room_catalog(self):
        """
        Return the room details in the following structure:
        """
        """
        We have the following types of rooms:
        S.no.   |Class      |Price PN (USD)
        1.      |A          |6000
        2.      |A premium  |5000
        3.      |Premium    |4000
        4.      |Gold       |3000
        """
        return None
    
    def verify_date(self, from_date, to_date):
        """
        If today >= checkinDate >= checkoutDate, then return true. Otherwise return false.
        """
        return None
    
    def update_room_status(self, room_no):
        """
        If a particular room was available and it was used for a booking, then the status of that room must be changed to unavailable or vice-versa. 
        """
        return None
    
    def get_room_status(self, room_no):
        """
        Return the room status for the provided room number, that is, room_no.
        """
        return None
    
    def get_available_room(self, room_cat):
        """
        Return the available room number for the provided category.
        Note: If no rooms in a specific category are available, then the function must return 0.
        """
        return None
    
    def gen_bill(self, room_no, from_date,to_date):
        """
        The bill must be generated only if the checkin and checkout dates are valid.
        If the provided dates are valid, then perform the following:
            1. Generate the bill for the duration of the stay. Thus, you can calculate the bill using the following formula:
               bill = (room_rent * number of days stayed) + 9% tax
            2. The bill generated must be rounded off to two decimal points. For example, if the bill generated is 189.1034, then you must return 189.10.
        If the provided dates are invalid, then you must return 'Invalid Date'.
        """
        return None