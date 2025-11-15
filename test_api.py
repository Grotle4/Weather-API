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



"""
Unit Tests to be implemented:
validate location
weather api url is valid
cache is storing keys properly
cache will return none properly on expired cache
cache returns a cache result on a cache hit
check to see if weather api is called on cache miss
check for external error apis to be handled correctly
"""