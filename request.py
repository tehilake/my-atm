import requests

# balance (GET)
response = requests.get("http://localhost:5000/accounts/12345/balance")
if response.status_code == 200:
    print(response.json())  # print the answer (account balance)
else:
    print("Error:", response.json())

# withdraw (POST)
withdraw_data = {"amount": 50}
response = requests.post("http://localhost:5000/accounts/12345/withdraw", json=withdraw_data)
if response.status_code == 200:
    print(response.json())  # print the answer (balance after withdraw)
else:
    print("Error:", response.json())

# deposit (POST)
deposit_data = {"amount": 200}
response = requests.post("http://localhost:5000/accounts/12345/deposit", json=deposit_data)
if response.status_code == 200:
    print(response.json())  # print the answer (balance after deposit)
else:
    print("Error:", response.json())
