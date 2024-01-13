from django.shortcuts import render, HttpResponse, redirect
from .forms import BudgetForm, TransactionForm
from .models import Envelope, Transaction
from django.contrib.auth.models import User
def index(request):
	budgets = Envelope.objects.filter(user=request.user.id)
	return render(request, "budgets/budgets.html",{"budgets":budgets})

def create_budget(request):
	if request.method == "POST":
		form = BudgetForm(request.POST)
		if form.is_valid():
			new_envelope = form.save(commit=False)
			new_envelope.user = User.objects.get(id=request.user.id)
			new_envelope.save()
		return redirect("budgets")
	else:
		return render(request, 
					"budgets/create_budget.html", 
					{'form':BudgetForm()})

def budget(request):
	if request.method == "POST":
		envelope = Envelope.objects.get(id=int(request.POST['b_id']))
		request.session['envelope_id'] = envelope.id
		return redirect("budget_render")
	del request.session['envelope_id']
	return redirect("budgets")

def budget_render(request):
	context = {
		"budget": Envelope.objects.get(id=request.session['envelope_id']),
		"transactions":Transaction.objects.filter(envelope=request.session['envelope_id'])
	}
	return render(request, "budgets/budget.html", context)

def transaction_form(request):
	context = {
		'form':TransactionForm(),
	}
	return render(request, "budgets/create_transaction.html", context)


def create_transaction(request):
	form = TransactionForm(request.POST)
	b_id = request.session['envelope_id']
	form_valid = form.is_valid()
	for f in form.errors:
		print("errros"+f)
	if form_valid:
		envelope = Envelope.objects.get(id=b_id)
		new_transaction = form.save(commit=False)
		new_transaction.envelope = envelope
		new_transaction.save()
		envelope.total -= new_transaction.total
		envelope.save()
		return redirect("budget_render")
	return redirect("transaction_form")