from .backend_suite import BackendSuite


class BackendTest(BackendSuite):

    ##issue: JSON is not standartisized, e.g. sometimes no "rain" in response, sometimes empty dict, sometimes null
    def test_city(self):
        """Test Case - Backend - City.
            Pre-Conditions:
            ---------------

            Steps:
            ------
            1. Send /weather request with city as a parameter
            -----------------
            200 status code received
            Next fields are returned in JSON:
            "weather", "coord", "base", "main", "visibility", "wind", "rain", "clouds", "dt", "sys", "timezone", "id",
            "name", "cod"
        """
        cities = ["Zaragoza", "London", "Paris", "Phoenix", "Barcelona", "Lviv", "San Francisco", "New York", "Ivano-Frankivsk"]
        for city in cities:
            response = self.client.make_request("weather", {"q":city})
            self.assertEqual(response['code'], 200, "Expected Status 200")
            self.assertCountEqual(
                ["weather", "coord", "base", "main", "visibility", "wind", "rain", "clouds", "dt", "sys", "timezone", "id",
                 "name", "cod"], response['body'])

    ##issue 5** errors and stack trace
    def test_city_invalid_cities_neg(self):
        """Test Case - Backend - City invalid Negative.
            Pre-Conditions:
            ---------------

            Steps:
            ------
            1. Send /weather request with invalid city as a parameter
            -----------------
            400/404 Bad request status code received
            Next fields are returned in JSON:

        """
        cities = ["Мяу Мяу Мяу!", "ME ?gusto", "?/more", "\/n", "san & fran>?}|",
                  "how ab = + $ , / ? % # [ ]out! this*", "Cat butt"*1024]
        for city in cities:
            response = self.client.make_request("weather", {"q":city})
            self.assertEqual(response['code'], 400, "Expected Status 200")


    def test_city_unexisting_cities_neg(self):
        """Test Case - Backend - City unexisting Negative.
            Pre-Conditions:
            ---------------

            Steps:
            ------
            1. Send /weather request with not existing city as a parameter
            -----------------
            400/404 Bad request status code received
            Next fields are returned in JSON:

        """
        cities = ["666666", "Zootropolis", "Silent hill", "Raccoon City", "Orgrimmar", "Gotham"]
        for city in cities:
            response = self.client.make_request("weather", {"q":city})
            self.assertEqual(response['code'], 404, "Expected Status 404")



    def test_city_country(self):
        """Test Case - Backend - City Country.
            Pre-Conditions:
            ---------------

            Steps:
            ------
            1. Send /weather request with city and it's country as parameters
            -----------------
            200 status code received

        """
        city_country = {"Warsaw":"Poland", "Glasgow": "United Kingdom of Great Britain and Northern Ireland (the)",
                        "Ottawa": "Canada", "Denver": "United States of America (the)", "Tokyo": "Japan" }
        for city, country in city_country.items():
            response = self.client.make_request("weather", {city:country})
            self.assertEqual(response['code'], 200, "Expected Status 200")

    def test_city_country_neg(self):
        """Test Case - Backend - City Country Negative.
            Pre-Conditions:
            ---------------

            Steps:
            ------
            1. Send /weather request with invalid city and it's country pairs as parameters
            -----------------
            200 status code received

        """
        city_country = {"Poland":"Warsaw", "Wonderland": "United Kingdom of Great Britain and Northern Ireland (the)",
                        "Ottawa": "Canada1", "Denver": "USA", "Tokyo": "666" }
        for city, country in city_country.items():
            response = self.client.make_request("weather", {city:country})
            self.assertEqual(response['code'], 404, "Expected Status 404")

    def test_city_id(self):
        """Test Case - Backend - City by ID as stated in http://bulk.openweathermap.org/sample/
            6362983 - Zaragoza
            6545108 - Las Tres Tores
            5159178 - Jerrys First Addition
            6534051 - Cruïlles, Monells i Sant Sadurní de l'Heura
            702550 - Lviv
            Pre-Conditions:
            ---------------

            Steps:
            ------
            1. Send /weather request with city ID as parameter

            -----------------
            200 status code received
            Next fields are returned in JSON:
            "weather", "coord", "base", "main", "visibility", "wind", "rain", "clouds", "dt", "sys", "timezone", "id",
            "name", "cod"
        """
        city_id = (6362983, 6545108, 5159178, 6534051, 702550)
        for cityid in  city_id:
            response = self.client.make_request("weather", {"id": cityid})
            self.assertEqual(response['code'], 200, "Expected Status 200")

    def test_city_id_neg(self):
        """Test Case - Backend - City by ID Negative
            6362983 - Zaragoza
            6545108 - Las Tres Tores
            5159178 - Jerrys First Addition
            6534051 - Cruïlles, Monells i Sant Sadurní de l'Heura
            702550 - Lviv
            Pre-Conditions:
            ---------------

            Steps:
            ------
            1. Send /weather request with city ID as parameter

            -----------------
            200 status code received
            Next fields are returned in JSON:
            "weather", "coord", "base", "main", "visibility", "wind", "rain", "clouds", "dt", "sys", "timezone", "id",
            "name", "cod"
        """
        city_id = (0, None, -50, 653.4051, pow(99, 99))
        for cityid in  city_id:
            response = self.client.make_request("weather", {"id": cityid})
            self.assertEqual(response['code'], 401, "Expected Status 401")
