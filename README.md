# PersonalFinanceDashboard
## Overview

The Finance Dashboard is a web application designed to help users manage their finances by tracking income, expenses, budget, and savings. The dashboard provides visualizations to give users insights into their financial health.
## Features

- **Income Tracking:** Add, update, view, and delete income sources.
- **Expense Management:** Add, update, view, and delete expenses. View monthly totals and breakdowns.
- **Budget Overview:**Create, update, view, and delete budgets. Monitor budget usage.
- **Savings Goals:** Set, update, and track savings goals.
- **Data Visualization:** Charts and graphs powered by Chart.js for clear financial insights.

## Technology Stack

- **Backend:** Django
- **Frontend:** HTML, CSS, Chart.js
- **Database:** SQLite (default with Django)
## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)
- Install all the dependencies necessary (pip install -r requirements.txt)

### Set Up Environment Variables:

Create a .env file in the root directory of the project and add your environment-specific settings. Refer to the .env.example for guidance
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_NAME=your-database-name
DATABASE_USER=your-database-user
DATABASE_PASSWORD=your-database-password
DATABASE_HOST=localhost
DATABASE_PORT=5432

### Run migrations

python manage.py migrate

### Create a Superuser(for accessing the admin interface)

python manage.py createsuperuser

### Start the Development Server

python manage.py runserver
Visit http://127.0.0.1:8000/ in your web browser to access the dashboard.

## Usage

### Access Dashboard

Navigate to Dashboard: Open http://127.0.0.1:8000/ in your web browser to access the Personal Finance Dashboard.

### User Authentication

- Register: Create a new account via the "Register" page.
- Log In: Access your account through the "Login" page.
- Log Out: Log out of your account via the "Logout" link.

### Log In

Log In: Use your registered credentials to log in. If you don’t have an account, you can register through the sign-up page.

### Manage Income

- View Income: Go to the "Income List" page to view all your recorded incomes.
- Add Income: Click on "Add Income" and fill out the form with:
   -  Source: The source of income (e.g., Salary).
   -  Amount: The amount received.
   -  Date: The date of income.
- Update Income: Edit existing income details as needed.
- Delete Income: Remove any income records that are no longer needed.

### Track Expenses

- Add Expense: Navigate to the "Add Expense" page to log a new expense:
    - Category: Select or create a category for the expense.
    - Description: Provide a brief description of the expense.
    - Amount: Enter the expense amount.
    - Date: Select the date of the expense.
- Monthly Expenses: View the total expenses for the current month on the "Monthly Expenses" page.
- Top Expenses: View the top 5 highest expenses for the current month on the "Top Expenses" page.
- Expense Breakdown: Get a breakdown of expenses by category on the "Expense Breakdown" page.
 
### Manage Budgets

- View Budgets: Go to the "Budget List" page to view all your budgets.
- Add Budget: Click on "Add Budget" to set a new budget:
    - Category: Choose a category.
    - Amount: Set the budget amount.
    - Month: Select the month for the budget.
- Update Budget: Modify existing budget details as needed.
- Delete Budget: Remove any budgets that are no longer applicable.
  
### Manage Savings Goals
- View Savings Goals: Navigate to the "Savings List" page to view all your savings goals.
- Add Savings Goal: Click on "Add Savings Goal" to set a new goal:
    - Name: Name of the savings goal.
    - Target Amount: The target amount for the goal.
    - Current Amount: The current amount saved towards the goal.
    - Deadline: The deadline for achieving the goal.
- Update Savings Goal: Edit details of existing savings goals.
- Delete Savings Goal: Remove any savings goals that are no longer needed.

### Profile
- View Profile: The "Profile" page displays a summary of your income, expenses, budgets, and savings goals, including charts and graphs to visualize your financial data.

### Screenshots
- Dashboard Overview
  
![image](https://github.com/user-attachments/assets/0181371f-8780-4c85-bcd8-61ee3913cd44)

- Income Mangament/add/update/delete

  ![image](https://github.com/user-attachments/assets/c6c364b1-73cf-49e3-9f58-84cf3a8e5046)

- Expense
  
![image](https://github.com/user-attachments/assets/1e407a40-1199-47fa-baa4-0d1b6ea11686)

- Budget
  
![image](https://github.com/user-attachments/assets/49ce3743-ec3c-40b9-8fb1-6044e1ea3ca5)

- Savings
  
![image](https://github.com/user-attachments/assets/5b1d4c6c-88db-4666-b3fe-d4420c6c212f)
 
- Profile
  
![image](https://github.com/user-attachments/assets/ef64d49c-b490-49bb-8d20-221212cfb940)

## Configuration

- Settings: Modify settings.py to adjust application settings such as debugging, allowed hosts, or other configurations.
- Database: Configure the database settings in .env if using a database other than SQLite.

## Acknowledgments

- Django: For the web framework.
- Chart.js: For data visualization.
- python-decouple: For managing environment variables.

## License

This project is licensed under the MIT License
