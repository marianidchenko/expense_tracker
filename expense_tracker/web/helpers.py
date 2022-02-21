from expense_tracker.web.models import Expense, Profile


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def get_expenses():
    expenses = Expense.objects.all()
    return expenses


def get_budget_left():
    profile = get_profile()
    expenses = Expense.objects.all()
    budget_left = profile.budget - sum(e.price for e in expenses)
    return budget_left