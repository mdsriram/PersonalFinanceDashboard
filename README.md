# PersonalFinanceDashboard
## Overview

The Finance Dashboard is a web application designed to help users manage their finances by tracking income, expenses, budget, and savings. The dashboard provides visualizations to give users insights into their financial health.
## Features

- **Income Tracking:** Add and visualize different income sources.
- **Expense Management:** Track and categorize expenses.
- **Budget Overview:** Set and monitor budgets for different categories.
- **Savings Goals:** Monitor savings goals over time.
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

Add a Usage section to explain how to use the application:
- Access Dashboard: Navigate to http://127.0.0.1:8000/ to view and manage your finances.
- Add Income: Go to the "Income" section to add and categorize new income sources.
- Track Expenses: Use the "Expenses" section to log and categorize your spending.
- Set Budgets: Define and monitor your budget limits in the "Budget" section.
- Monitor Savings: Track your progress towards savings goals in the "Savings" section.

## Configuration

Provide details on how to configure the application:
- Settings: Modify settings.py to adjust application settings such as debugging, allowed hosts, or other configurations.
- Database: Configure the database settings in .env if using a database other than SQLite.

## Acknowledgments

- Django: For the web framework.
- Chart.js: For data visualization.
- python-decouple: For managing environment variables.

## License

This project is licensed under the MIT License
