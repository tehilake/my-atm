from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the ATM app!"

def load_accounts():
    """
    Loads the accounts from the 'accounts.json' file.

    :return:
        dict: A dictionary where each key is an account number (string),
              and the value is another dictionary containing account details (balance).
    """
    try:
        with open("accounts.json", "r") as file:
            accounts = json.load(file)
            return accounts
    except FileNotFoundError:
        return {} # If the file doesn't exist, return an empty dictionary


def save_accounts(accounts):
    """
    Saves the provided accounts dictionary to the 'accounts.json' file.
    This function is typically used to persist changes made to existing accounts.

     :arg
        dictionary of accounts.
        """
    with open('accounts.json', 'w') as f:
        json.dump(accounts, f, indent=4)


@app.route('/accounts', methods=["POST"])
def accounts():
    """
      Handles the POST request to check if an account exists.
      If the account exists, it returns a success message and a redirect URL.
      If the account does not exist, it returns an error message.

      :return: JSON response
      """
    #Get the account number from the request's JSON
    account_number = request.json.get("account_number")
    accounts = load_accounts()

    if account_number in accounts:
        # If account exists, return a success masssage, and URL to the account page
        return jsonify({
            "message": "Account found",
            "redirect_url": f"/accounts/{account_number}"
         }), 200
    else:
        ## If account not exists, return error masssage
        return jsonify({"error": "Account not found"}), 404


@app.route('/accounts/<account_number>', methods=["GET"])
def account_page(account_number):
    """
    Retrieves the account details for the specified account number.
    If the account exists, it returns the account number.
    If the account is not found, it returns an error message.

    :param account_number: The unique identifier for the account to retrieve
    :return: A JSON response with the account details or an error message
    """
    # Load the current accounts from the file
    accounts = load_accounts()
    # Try to get the account data for the specified account number
    account = accounts.get(account_number)

    # If account was found return the account number
    if account:
        return jsonify({"account_number": account_number}), 200
    else:
        # Return an error message if the account was not found
        return jsonify({"error": "Account not found"}), 404


@app.route('/accounts/<account_number>/balance', methods=['GET'])
def balance(account_number):
    """
    Handles the GET request for checking the balance of a specific account.

    :arg:
        account_number (str): The account number provided in the URL.

    :return:
        JSON response with the account balance or an error message if the account is not found.
    """
    # Load all accounts from the JSON file
    accounts = load_accounts()
    # Try to find the account with the provided account_number
    account = accounts.get(account_number)

    # If the account is found, return the account balance
    if account:
        return jsonify({"account_number": account_number, "balance": account["balance"]}), 200
    else:
        # If the account is not found, return an error message
        return jsonify({"error": "Account not found"}), 404


@app.route('/accounts/<account_number>/withdraw', methods=['POST'])
def withdraw(account_number):
    """
       Handles the withdrawal of a specified amount from an account.
       If the account exists and has enough balance, the withdrawal is successful and the balance is updated.
       If the amount is invalid or insufficient balance exists, an error message is returned.

       :param account_number: The unique identifier for the account from which to withdraw
       :return: A JSON response with either a success message and updated balance or an error message
       """
    # Load all accounts from the JSON file
    accounts = load_accounts()
    # Try to find the account with the provided account_number
    account = accounts.get(account_number)

    # # If the account exists withdraw the amount
    if account:
        try:
            # Get the withdrawal amount from the JSON data
            amount = float(request.json.get('amount'))
            if amount <= 0:
                return jsonify({"error": "Amount must be greater than zero"}), 400
        except (ValueError, TypeError):
            # Return an error if the amount is not valid
            return jsonify({"error": "Invalid amount"}), 400

        balance = account["balance"]
        # Check if there are sufficient funds in the account for the withdrawal
        if amount <= balance:
            # Update the balance after the withdrawal
            account["balance"] = balance - amount
            save_accounts(accounts)
            # Return a success message with the new balance
            return jsonify({"message": "Withdraw successful", "new_balance": account["balance"]}), 200
        else:
            # Return an error if the balance is too low for the withdrawal
            return jsonify({"error": "Low balance for this withdrawal"}), 400
    else:
        # Return an error if the account is not found
        return jsonify({"error": "Account not found"}), 404


@app.route('/accounts/<account_number>/deposit', methods=['POST'])
def deposit(account_number):
    """
       Handles the deposit of a specified amount into an account.
       If the account exists, the deposit is successful and the balance is updated.
       If the amount is invalid, an error message is returned.

       :param account_number: The unique identifier for the account into which to deposit
       :return: A JSON response with either a success message and updated balance or an error message
       """
    # Load all accounts from the JSON file
    accounts = load_accounts()
    # Try to find the account with the provided account_number
    account = accounts.get(account_number)

    # If the account exists deposit the amount
    if account:
        try:
            # Get the deposit amount from the JSON data
            amount = float(request.json.get('amount'))
            if amount <= 0:
                return jsonify({"error": "Amount must be greater than zero"}), 400
        except (ValueError, TypeError):
            # Return an error if the amount is not valid
            return jsonify({"error": "Invalid amount"}), 400

        # Update the balance after the withdrawal
        balance = account["balance"]
        account["balance"] = balance + amount
        save_accounts(accounts)
        # Return a success message with the new balance
        return jsonify({"message": "Deposit successful", "new_balance": account["balance"]}), 200
    else:
        # Return an error if the account is not found
        return jsonify({"error": "Account not found"}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
    #app.run(debug=True)
