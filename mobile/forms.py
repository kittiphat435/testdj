from django import forms
from .models import Askqa

class Askqaforms(forms.ModelForm):

	class Meta:
		model = Askqa
		fields = ('name','topic','detail')
		

