import unittest
import api
import get_weather_api
import cache_data

class UnitTest(unittest.TestCase): #TODO:
    def test_redis(self):
        self.assertEqual(api.ping_test(api.r), True)
    def test_key(self):
        self.assertEqual(get_weather_api.weather_test("New York", api.api_key), True)

if __name__ == '__main__':
    unittest.main()


