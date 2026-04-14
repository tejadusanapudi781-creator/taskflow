from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user


class TaskForm(forms.ModelForm):
    due_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-input'})
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'status', 'due_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Task title...'}),
            'description': forms.Textarea(attrs={'class': 'form-input', 'rows': 3, 'placeholder': 'Description (optional)...'}),
            'priority': forms.Select(attrs={'class': 'form-input'}),
            'status': forms.Select(attrs={'class': 'form-input'}),
        }
