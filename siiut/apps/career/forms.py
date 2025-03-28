from django import forms
from .models import Quarter, Level, Career, Subject

input_tail = 'border-gray-300 p-2 rounded-xl focus:shadow-xl'

class QuarterForm(forms.ModelForm):
    class Meta:
        model = Quarter
        fields = ['quarter', 'quarter_name']
        widgets = {
            'quarter': forms.TextInput(attrs={'type':'number','class': input_tail}),
            'quarter_name': forms.TextInput(attrs={'class':input_tail})
        }
        
class LevelForm(forms.ModelForm):
    class Meta:
        model = Level
        fields = ['name', 'short_name']
        widgets = {
            'name': forms.TextInput(attrs={
                "class": input_tail
                }),
            'short_name': forms.TextInput(attrs={
                "class": input_tail
                })
        }
        
class CareerForm(forms.ModelForm):
    class Meta:
        model = Career
        fields = ['name', 'short_name', 'level', 'is_active', 'principal', 'year']
        widgets = {
            'name': forms.TextInput(attrs={'class': input_tail}),
            'short_name': forms.TextInput(attrs={'class': input_tail}),
            'is_active': forms.CheckboxInput(attrs={'class':input_tail}),
            'principal': forms.TextInput(attrs={'class': input_tail}),
            'year': forms.TextInput(attrs={'class': input_tail}),
        }

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['quarter', 'name', 'total_hours', 'weekly_hours']
        widgets = {
            'quarter': forms.Select(attrs={'class': 'input_tail'}),
            'name': forms.TextInput(attrs={'class': 'inoit_tail'}),
            'total_hours': forms.NumberInput(attrs={'class': 'input_tail'}),
            'weekly_hours': forms.NumberInput(attrs={'class': 'input_tail'}),
        }