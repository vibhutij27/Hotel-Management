import unittest

from src.hotel import hotel

class Test(unittest.TestCase):
    def test_date_validation(self):
        h = hotel()
        self.assertEquals(h.verify_date("22-07-2030","24-07-2030"),True)
    
    def test_date_validation1(self):
        h = hotel()
        self.assertEquals(h.verify_date("22-07-2030","24-07-2025"),False)

    def test_date_validation2(self):
        h = hotel()
        self.assertEquals(h.verify_date("22-07-2000","24-07-2030"),False)

   
    def test_get_room_status(self):
        h = hotel()
        self.assertEquals(h.get_room_status(101),0)
    
    def test_get_room_status1(self):
        h = hotel()
        self.assertEquals(h.get_room_status(203),1)