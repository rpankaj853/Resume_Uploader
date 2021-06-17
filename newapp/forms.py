from django import forms
from .models import newmodel


class newform(forms.ModelForm):
	class Meta:

		model = newmodel

		fields = ('name','Resume','tech')


