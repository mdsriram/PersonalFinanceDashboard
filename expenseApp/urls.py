#expenseApp_urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .expense_views import IncomeListView, IncomeCreateView, IncomeUpdateView, IncomeDeleteView, ExpenseCreateView, MonthlyExpensesView, TopExpensesView, ExpenseBreakdownView, BudgetCreateView, BudgetListView,BudgetUpdateView, BudgetDeleteView, SavingsCreateView, SavingsListView, SavingsUpdateView, SavingsDeleteView
urlpatterns = [
    path('', views.home_view, name='home'),  # Maps root URL to home_view
    path('register/',views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    # Other URL patterns
    path('incomes/', IncomeListView.as_view(), name='income_list'),
    path('incomes/create/', IncomeCreateView.as_view(), name='income_create'),
    path('incomes/<int:pk>/update/', IncomeUpdateView.as_view(), name='income_update'),
    path('incomes/<int:pk>/delete/', IncomeDeleteView.as_view(), name='income_delete'),
    #expense urls
    path('expense/add/', ExpenseCreateView.as_view(), name='expense_add'),  
    path('expenses/monthly/', MonthlyExpensesView.as_view(), name='monthly_expenses'),
    path('expenses/top/', TopExpensesView.as_view(), name='top_expenses'),
    path('expenses/breakdown/', ExpenseBreakdownView.as_view(), name='expense_breakdown'),
    #budgeturls
    path('budgets/', BudgetListView.as_view(), name='budget_list'),
    path('budgets/new/', BudgetCreateView.as_view(), name='budget_create'),
    path('budgets/<int:pk>/edit/', BudgetUpdateView.as_view(), name='budget_update'),
    path('budgets/<int:pk>/delete/', BudgetDeleteView.as_view(), name='budget_delete'),
    #savingsurl
    path('savings/', SavingsListView.as_view(), name='savings-list'),
    path('savings/new/', SavingsCreateView.as_view(), name='savings-create'),
    path('savings/<int:pk>/edit/', SavingsUpdateView.as_view(), name='savings-update'),
    path('savings/<int:pk>/delete/', SavingsDeleteView.as_view(), name='savings-delete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

