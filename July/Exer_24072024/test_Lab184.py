import allure
import requests

#URL -> https://restful-booker.herokuapp.com/booking
#auth
#payload
#content-type - or Header
#Query parameter
#Path parameter


@allure.title("Test Get Request - Restful Booker project#1")
@allure.description ("TC#1 -> Verify that Get request with ID works")
@allure.tag("regression","p0","smoke")
def test_get_single_request_by_id():
    url = "https://restful-booker.herokuapp.com/booking/1"
    responseData = requests.get(url)
    print(responseData.json())
    assert responseData.status_code == 200

