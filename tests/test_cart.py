import requests
from utils.api_client import BASE_URL

def test_cart():

    
   

    payload = {
        "userId": 7,
        "date": "2026-12-17",
        "products": [ 
            {
                "productId": 1,
                "quantity":4
            
            },
           {
                "productId": 3,
                "quantity":3
                       
            }

        ]
    }

    """
    headers = {
        "Content-Type":
        "application/json",
        "Accept":"application/json"
    }
    
    """

    response=requests.post(f"{BASE_URL}/carts", json=payload)

    
    

    assert response.status_code in (200,201), f"Error: {response.status_code} Texto: {response.text}"

    cart = response.json()

    assert isinstance(cart,dict), f"Error: {response.status_code} Texto: {response.text}"


    assert "id" in cart, f"Error: {response.status_code} Texto: {response.text}"


    assert cart["userId"] == payload["userId"], f"Error: {response.status_code} Texto: {response.text}"


    assert isinstance(cart["products"],list), f"Error: {response.status_code} Texto: {response.text}"


    assert len(cart["products"]) == len(payload["products"]), f"Error: {response.status_code} Texto: {response.text}"