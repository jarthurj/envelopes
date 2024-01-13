from django.forms import ModelForm
from .models import Envelope, Transaction

class BudgetForm(ModelForm):

	class Meta:
		model = Envelope
		fields = ["name", "total"]

	def __init__(self, *args, **kwargs):
		super(BudgetForm, self).__init__(*args, **kwargs)

		self.fields['name'].widget.attrs['class'] = 'form-control my-2'
		self.fields['name'].widget.attrs['placeholder'] = 'Name'
		self.fields['name'].label = ''

		self.fields['total'].widget.attrs['class'] = 'form-control my-2'
		self.fields['total'].widget.attrs['placeholder'] = 'Total'
		self.fields['total'].label = ''
		self.fields['total'].help_text = '<ul class="form-text text-muted small"><li>Please enter the total amount for this envelope.</li></ul>'



class TransactionForm(ModelForm):

	class Meta:
		model = Transaction
		fields = ["name", "total"]

	def __init__(self, *args, **kwargs):
		super(TransactionForm, self).__init__(*args, **kwargs)

		self.fields['name'].widget.attrs['class'] = 'form-control my-2'
		self.fields['name'].widget.attrs['placeholder'] = 'Name'
		self.fields['name'].label = ''

		self.fields['total'].widget.attrs['class'] = 'form-control my-2'
		self.fields['total'].widget.attrs['placeholder'] = 'Total'
		self.fields['total'].label = ''
		self.fields['total'].help_text = '<ul class="form-text text-muted small"><li>Please enter the total amount for this transaction.</li></ul>'
