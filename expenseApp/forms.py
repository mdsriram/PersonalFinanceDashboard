#forms.py
from django import forms
from .models import Income, Expense, Budget, Savings

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['source', 'amount', 'date'] #Exclude 'user' field

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields =['category','description','amount','date'] #Exclude user field

class BudgetForm(forms.ModelForm):
    class  Meta:
        model = Budget
        fields = ['category','amount', 'month']


class SavingsForm(forms.ModelForm):
    class Meta:
       model = Savings
       fields = ['name','target_amount','current_amount','deadline']
            

            