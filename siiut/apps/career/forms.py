from django import forms
from .models import Quarter, Level, Career

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
            'name': forms.TextInput(attrs={'class':'border border-gray-400 p-1 rounded-xl'}),
            'short_name': forms.TextInput(attrs={'class':'border border-gray-400 p-1 rounded-xl'}),
            'level': forms.Select(attrs={'class':'border border-gray-400 p-1 rounded-xl'}),
            'is_active': forms.CheckboxInput(attrs={'class':'border border-gray-400 p-1 rounded-xl'}),
            'principal': forms.TextInput(attrs={'class':'border border-gray-400 p-1 rounded-xl'}),
            'year': forms.TextInput(attrs={'class':'border border-gray-400 p-1 rounded-xl'})
        }