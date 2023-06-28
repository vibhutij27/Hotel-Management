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
    
    def test_get_room_status2(self):
        h = hotel()
        h.update_room_status(203)
        self.assertEquals(h.get_room_status(203),0)
    
    def test_get_available_room(self):
        h = hotel()
        self.assertEquals(h.get_available_room(3),203)
    
    def test_get_available_room1(self):
        h = hotel()
        h.update_room_status(103)
        self.assertEquals(h.get_available_room(2),0)
    
    def test_gen_bill(self):
        h = hotel()
        self.assertEquals(h.gen_bill(203,'20-09-2000','22-09-2020'),'Invalid Date')
    
    def test_gen_bill1(self):
        h = hotel()
        self.assertEquals(h.gen_bill(203,'20-09-2030','22-09-2030'),8720.0)