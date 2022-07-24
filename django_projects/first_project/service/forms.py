from django import forms
from service.models import User

class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'