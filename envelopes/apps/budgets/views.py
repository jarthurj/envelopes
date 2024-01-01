from django.shortcuts import render, HttpResponse
from .forms import BudgetForm
def index(request):
	return render(request, "budgets/budgets.html")

def create_budget(request):
	if request.method == "POST":
		pass
	else:
		return render(request, "budgets/create_budget.html", {'form':BudgetForm()})
