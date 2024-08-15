#class Based views #expense_views.py
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.db.models import Sum
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Income, Expense, Category, Budget, Savings
from .forms import IncomeForm, ExpenseForm, BudgetForm, SavingsForm# Assuming you have a form for Income

class IncomeListView(ListView):
    model = Income
    template_name = 'expense/income_list.html'
    context_object_name = 'incomes'


class IncomeCreateView(CreateView):
    model = Income
    form_class = IncomeForm
    template_name = 'expense/income_form.html'
    success_url = reverse_lazy('income_list')

    def form_valid(self, form):
        form.instance.user = self.request.user  # Set the user to the logged-in user
        return super().form_valid(form)


class IncomeUpdateView(UpdateView):
    model = Income
    form_class = IncomeForm
    template_name = 'expense/income_form.html'
    success_url = reverse_lazy('income_list')

    def form_valid(self, form):
        form.instance.user = self.request.user  # Set the user to the logged-in user
        return super().form_valid(form)


class IncomeDeleteView(DeleteView):
    model = Income
    template_name = 'expense/income_confirm_delete.html'
    success_url = reverse_lazy('income_list')

#add expenses
class ExpenseCreateView(CreateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'expense/add_expense.html'
    success_url = reverse_lazy('home')  # Redirect to dashboard after adding an expense

    def form_valid(self, form):
        form.instance.user = self.request.user  # Associate with logged-in user
        return super().form_valid(form)

class MonthlyExpensesView(TemplateView):
    template_name = 'expense/monthly_expenses.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_month = now().month
        current_year = now().year
        monthly_expense_total = Expense.objects.filter(user=self.request.user, date__month=current_month, date__year=current_year).aggregate(Sum('amount'))['amount__sum'] or 0
        context['monthly_expense_total'] = monthly_expense_total
        return context

class TopExpensesView(TemplateView):
    template_name = 'expense/top_expenses.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_month = now().month
        current_year = now().year
        top_expenses = Expense.objects.filter(user=self.request.user, date__month=current_month, date__year=current_year).order_by('-amount')[:5]
        context['top_expenses'] = top_expenses
        return context

class ExpenseBreakdownView(TemplateView):
    template_name = 'expense/expense_breakdown.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_month = now().month
        current_year = now().year
        expenses_by_category = Expense.objects.filter(user=self.request.user, date__month=current_month, date__year=current_year).values('category__name').annotate(total=Sum('amount')).order_by('-total')
        context['expenses_by_category'] = expenses_by_category
        return context
    
# List all budgets for the logged-in user
class BudgetListView(ListView):
    model = Budget
    template_name = 'expense/budget_list.html'
    context_object_name = 'budgets'

    def get_queryset(self):
        return Budget.objects.filter(user=self.request.user).order_by('-month')

# Create a new budget
class BudgetCreateView(CreateView):
    model = Budget
    template_name = 'expense/budget_form.html'
    fields = ['category', 'amount', 'month']
    success_url = reverse_lazy('budget_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# Update an existing budget
class BudgetUpdateView(UpdateView):
    model = Budget
    template_name = 'expense/budget_form.html'
    fields = ['category', 'amount', 'month']
    success_url = reverse_lazy('budget_list')

    def get_queryset(self):
        return Budget.objects.filter(user=self.request.user)

# Delete a budget
class BudgetDeleteView(DeleteView):
    model = Budget
    template_name = 'expense/budget_confirm_delete.html'
    success_url = reverse_lazy('budget_list')

    def get_queryset(self):
        return Budget.objects.filter(user=self.request.user)
    


# List view to display all savings goals
class SavingsListView(ListView):
    model = Savings
    template_name = 'expense/savings_list.html'
    context_object_name = 'savings'

    def get_queryset(self):
        return Savings.objects.filter(user=self.request.user)

# Create view to add a new savings goal
class SavingsCreateView(CreateView):
    model = Savings
    form_class = SavingsForm
    template_name = 'expense/savings_form.html'
    success_url = reverse_lazy('savings-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# Update view to edit an existing savings goal
class SavingsUpdateView(UpdateView):
    model = Savings
    form_class = SavingsForm
    template_name = 'expense/savings_form.html'
    success_url = reverse_lazy('savings-list')

# Delete view to delete a savings goal
class SavingsDeleteView(DeleteView):
    model = Savings
    template_name = 'expense/savings_confirm_delete.html'
    success_url = reverse_lazy('savings-list')