
import requests

BASE_URL = "http://localhost:8080"  
HEADERS = {"API-Key": "your-api-key"}  # Replace with correct API key

def fetch_clusters():
    url = f"/clusters"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def fetch_regions():
    url = f"/regions"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def fetch_stores():
    url = f"/stores"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def fetch_store_products(page=0):
    url = f"/stores/products?page={page}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def fetch_filter_values(filter_id, filters):
    url = f"/filters/{filter_id}"
    response = requests.post(url, json={"filters": filters}, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def fetch_stores_by_filters(filters):
    url = f"/stores"
    response = requests.post(url, json={"filters": filters}, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def update_store_name(store_name, new_name):
    url = f"/stores/{store_name}"
    response = requests.patch(url, json={"name": new_name}, headers=HEADERS)
    return response.status_code == 200
