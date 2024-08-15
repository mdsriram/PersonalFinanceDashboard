#admin.py
from django.contrib import admin
from .models import Income, Expense, Category, Budget, Savings

# Register your models here.

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('source', 'amount','date','user')
    list_filter = ('date', 'user')
    search_fields = ('source', 'amount')


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('description', 'amount', 'category', 'date', 'user')
    list_filter = ('category', 'date')
    search_fields = ('description', 'user__username')
    ordering = ('-date',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display =('user','category','amount','month')
    list_filter =('month','user','category')
    search_fields =('user__username','category__name')

@admin.register(Savings)
class CategoryAdmin(admin.ModelAdmin):
    list_display =('name','user','target_amount', 'current_amount','progress_percentage','deadline')
    list_filter = ('user', 'deadline')
    search_fields = ('name',)