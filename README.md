#Project Name: ATM Server

Description:

The ATM Server is a simple API that simulates ATM operations. The server allows users to:
Check their account balance
Withdraw money
Deposit money

Technologies:

Python
Flask
JSON (for database)
Heroku (for deployment)

Endpoints:

GET /: Main page- returns a welcome message.
POST /accounts - Checks if an account exists in the database.
GET /accounts/<acccount_number> Retrieves basic account information.
GET /accounts/<account_number>/balance: Retrieve account balance.
POST /accounts/<account_number>/withdraw: Withdraw cash from an account.
POST /accounts/<account_number>/deposit:  Deposit Money to an account.

Usage Examples:

GET / – Returns a welcome message.
Example: A user accesses the homepage and sees a simple welcome text.

POST /accounts – Checks if an account exists in the database.
Request Body (JSON):
{
  "account_number": "12345"
}
Example: A user submits an account number, and the server responds with a success message if the account exists or an error message if it does not.

GET /accounts/<account_number> – Retrieves basic account information.
Example: A user requests account details and receives the account number if it is found in the database.

GET /accounts/<account_number>/balance – Retrieves the account balance.
Example: A user queries the balance of an account and receives the current balance in response.

POST /accounts/<account_number>/withdraw – Withdraws cash from an account.
Request Body (JSON):
{
  "amount": 100
}
Example: A user sends a withdrawal request with a specified amount, and if sufficient funds are available, the balance is updated, and a success message is returned. Otherwise, an error message is displayed.

  
POST /accounts/<account_number>/deposit – Deposits money into an account.  
Request Body (JSON):  
{
  "amount": 200
}
Example: A user deposits a specified amount into their account, and the updated balance is returned as confirmation.
