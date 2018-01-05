from pyse import TestCase, TestRunner

class zhywAtuo(TestCase):

    def home(self):
        self.driver.open("http://192.168.0.123:7779/ioms/index.jsp")
