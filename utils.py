import requests

def make_api_request(url, headers=None, params=None, data=None, method='GET'):
    try:
        response = requests.request(method, url, headers=headers, params=params, json=data)
        response.raise_for_status()  
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API request error: {e}")
        return None
