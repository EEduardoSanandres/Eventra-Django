import requests

def get_tokens(email, password):
    url = 'http://127.0.0.1:8000/api/token/'
    payload = {
        'email': email,
        'password': password
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception('Failed to obtain token', response.status_code, response.text)

def get_user_info(access_token):
    url = 'http://127.0.0.1:8000/api/users/'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception('Failed to get user info', response.status_code, response.text)

def main():
    email = 'xd@example.com'  # Replace with your email
    password = 'string'  # Replace with your password
    try:
        tokens = get_tokens(email, password)
        access_token = tokens['access']
        user_info = get_user_info(access_token)
        print(user_info)
    except Exception as e:
        print('Error:', e)

if __name__ == '__main__':
    main()
