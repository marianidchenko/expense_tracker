from django.shortcuts import render, redirect

from expense_tracker.web.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm, CreateExpenseForm, \
    DeleteExpenseForm, EditExpenseForm
from expense_tracker.web.helpers import get_profile, get_expenses, get_budget_left
from expense_tracker.web.models import Expense


def show_index(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')
    expenses = get_expenses()
    budget_left = get_budget_left()

    context = {
        'profile': profile,
        'expenses': expenses,
        'budget_left': budget_left,
    }
    return render(request, 'home-with-profile.html', context)


def create_expense(request):
    if request.method == 'POST':
        form = CreateExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateExpenseForm()

    context = {
        'form': form,
    }
    return render(request, 'expense-create.html', context)


def edit_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditExpenseForm(request.POST, instance=expense)
        if form.is_valid:
            form.save()
            return redirect('show index')
    else:
        form = EditExpenseForm(instance=expense)

    context = {
        'form': form,
        'expense': expense
    }
    return render(request, 'expense-edit.html', context)


def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = DeleteExpenseForm(instance=expense)
    context = {
        'form': form,
        'expense': expense,
    }
    return render(request, 'expense-delete.html', context)


def show_profile(request):
    profile = get_profile()
    budget_left = get_budget_left()
    expenses_count = len(get_expenses())

    context = {
        'profile': profile,
        'expenses_count': expenses_count,
        'budget_left': budget_left
    }
    return render(request, 'profile.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show profile')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'profile-edit.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'profile-delete.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show profile')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
        'no_profile': True,
    }

    return render(request, 'home-no-profile.html', context)
