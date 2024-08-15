from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Income, Expense, Budget, Savings
import json

def home_view(request):
    return render(request, 'registration/home.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in after registration
            return redirect('home')  # Redirect to home page or another page
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page or another page
        else:
            # Handle invalid login
            return render(request, 'registration/login.html', {'error': 'Invalid username or password'})
    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page or another page

@login_required
def profile_view(request):
    incomes = Income.objects.filter(user=request.user)  # Query Income entries for the logged-in user
    expenses = Expense.objects.filter(user=request.user)
    budgets = Budget.objects.filter(user=request.user)
    savings = Savings.objects.filter(user=request.user)  # Query Expense entries for the logged-in user
 
        # Prepare data for Income and Expense Chart
    income_labels = [income.source for income in incomes]
    income_data = [float(income.amount) for income in incomes]

    expense_labels = [expense.category.name for expense in expenses]
    expense_data = [float(expense.amount) for expense in expenses]

    # Prepare data for Budget Chart
    budget_labels = [budget.category.name for budget in budgets]
    budget_data = [float(budget.amount) for budget in budgets]
    remaining_budget_data = [budget.amount - sum(exp.amount for exp in expenses) for budget in budgets]
 
   #Calculate remaining budget per category
    remaining_budget_data = []
    for budget in budgets:
        # Sum expenses for each category
        total_expenses = sum(expense.amount for expense in expenses if expense.category == budget.category)
        remaining_budget_data.append(float(budget.amount - total_expenses))

    # Prepare data for Savings Goals
    savings_labels = [saving.name for saving in savings]
    savings_data = [float(saving.current_amount) for saving in savings]
    target_data = [float(saving.target_amount) for saving in savings]

    context = {
        'incomes': incomes,
        'expenses': expenses,
        'budget_data': budget_data,
        'savings': savings,
        'income_labels': json.dumps(income_labels),
        'income_data': json.dumps(income_data),
        'expense_labels': json.dumps(expense_labels),
        'expense_data': json.dumps(expense_data),
        'budget_labels': json.dumps(budget_labels),
        'budget_data': json.dumps(budget_data),
        'remaining_budget_data': json.dumps(remaining_budget_data),
        'savings_labels': json.dumps(savings_labels),
        'savings_data': json.dumps(savings_data),
        'target_data': json.dumps(target_data),
    }

    return render(request, 'registration/profile.html', context)
