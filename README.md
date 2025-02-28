# Project Name: ATM Server

### Description:

The ATM Server is a simple API that simulates ATM operations. The server allows users to:  
- Check their account balance  
- Withdraw money  
- Deposit money  

### Technologies:

- Python  
- Flask  
- JSON (for database)  
- Heroku (for deployment)  

### Endpoints:

GET / : Main page- returns a welcome message.
POST /accounts : Checks if an account exists in the database.  
GET /accounts/<account_number> : Retrieves basic account information.  
GET /accounts/<account_number>/balance : Retrieve account balance.  
POST /accounts/<account_number>/withdraw : Withdraw cash from an account.  
POST /accounts/<account_number>/deposit :  Deposit Money to an account.  

### Usage Examples:

- GET / – Returns a welcome message.  
Example: A user accesses the homepage and sees a simple welcome text.  

- POST /accounts – Checks if an account exists in the database.  
Request Body (JSON):  
```json
{  
  "account_number": "12345"  
}
```
Example: A user submits an account number, and the server responds with a success message if the account exists or an error message if it does not.  

- GET /accounts/<account_number> – Retrieves basic account information.  
Example: A user requests account details and receives the account number if it is found in the database.  

- GET /accounts/<account_number>/balance – Retrieves the account balance.  
Example: A user queries the balance of an account and receives the current balance in response.
```json
{
    "account_number": "12345",
    "balance": 1897.0
}
```  

- POST /accounts/<account_number>/withdraw – Withdraws cash from an account.  
Request Body (JSON):  
```json
{  
  "amount": 100  
}
```
Example: A user sends a withdrawal request with a specified amount, and if sufficient funds are available, the balance is updated, and a success message is returned. Otherwise, an error message is displayed. 
```json
{
    "message": "Withdraw successful",
    "new_balance": 1897.0
}
```
  
- POST /accounts/<account_number>/deposit – Deposits money into an account.  
Request Body (JSON):  
```json
{
  "amount": 200
}
```
Example: A user deposits a specified amount into their account, and the updated balance is returned as confirmation.

### Design Approach

My approach to designing this ATM server centered around creating a simple and scalable solution that ensures seamless functionality.

**Why Flask?**  
I chose Flask because it is a lightweight yet powerful web framework that allows for rapid development. Since the ATM server is a relatively simple REST API, Flask provides all the necessary functionality without unnecessary complexity. Key benefits include:
- Minimal setup, allowing quick API implementation.
- Built-in support for request handling and routing.
- Easy integration with JSON-based responses.

**Why JSON for Data Storage?** 
I chose JSON files for storing account data because:  
- There's no need for a full database server in a small-scale project.
- JSON is readable and easy to modify, making it convenient for this type of project.
- Reading and writing small JSON files provides sufficient performance.

**How I Implemented the API**
The API ensures that each endpoint serves a clear purpose. Here's how I built it:
- Request Handling: Each path processes requests and returns JSON responses.
- Data Validation: Before processing requests, input data is validated to prevent errors. If there is an error, a meaningful message is returned to the user.
- Transaction Logic: For withdrawals, the system checks if there are enough funds before proceeding.

### Challenges I faced:

- Understanding Flask Usage and Integration with Other Technologies
Since this is my first time building a project using Flask, I initially faced challenges in fully understanding how Flask interacts with other technologies, such as JSON. It took some time to figure out the best approach to integrate everything smoothly.

Solution:
Through hands-on experience with Flask, I experimented with GET and POST requests to better understand how each request affects the usage of JSON. I also focused on organizing and structuring the code more effectively, ensuring that each part of the application worked cohesively. This process helped me gain a deeper understanding of how to manage requests and responses in a Flask-based application.

- Challenges with Deploying to the Cloud (Heroku)
The main challenge was moving from running the app locally to deploying it on Heroku. Since the server was configured for localhost, I had to make some adjustments for the cloud environment.

Solution:
I modified the Procfile to specify the correct command for Heroku and ensured the app listened to the dynamic port provided by Heroku (using the PORT environment variable). After these changes, I successfully deployed the app, making it accessible remotely.


