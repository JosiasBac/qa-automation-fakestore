import requests, pytest




def test_list_products():
    response=requests.get("https://fakestoreapi.com/products?limit=5")

    

    assert response.status_code == 200, f"Error code: {response.status_code}. Text: {response.text}"

    products=response.json()

    assert isinstance(products,list)

    assert len(products) == 5


@pytest.mark.parametrize("category", [
    ("https://fakestoreapi.com/products/category/electronics"), ("https://fakestoreapi.com/products/category/jewelery"), 
    ("https://fakestoreapi.com/products/category/men's clothing"), ("https://fakestoreapi.com/products/category/women's clothing")
])


def test_category_products(category):
    response=requests.get(category)


    assert response.status_code == 200, f"Error code: {response.status_code} Text: {response.text}"