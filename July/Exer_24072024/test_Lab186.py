import allure
import requests


#URL -> https://restful-booker.herokuapp.com/booking
#auth
#payload
#content-type - or Header
#Query parameter
#Path parameter


@allure.title("Create Booking CRUD")
@allure.description("TC#1 -> Verify the create booking")
def test_create_positive_booking():
    base_url = "https://restful-booker.herokuapp.com/"
    base_path = "booking/1"
    URL = base_url + base_path
    header = {"Content-Type", "application/json"}
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post(url=URL, headers = header,json=payload)
    responseData = response.json()
    print(responseData.json())
    assert responseData.status_code == 200
