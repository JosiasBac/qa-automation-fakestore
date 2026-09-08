import requests, pytest
from utils.api_client import BASE_URL

MOD_URL = f"{BASE_URL}/products/category/"


def test_list_products():
    response=requests.get(f"{BASE_URL}/products?limit=5")

    

    assert response.status_code == 200, f"Error code: {response.status_code}. Text: {response.text}"

    products=response.json()

    assert isinstance(products,list)

    assert len(products) == 5



@pytest.mark.parametrize("category", [
    (f"{MOD_URL}electronics"), (f"{MOD_URL}jewelery"), 
    (f"{MOD_URL}men's clothing"), (f"{MOD_URL}women's clothing")
])


def test_category_products(category):
    response=requests.get(category)


    assert response.status_code == 200, f"Error code: {response.status_code} Text: {response.text}"