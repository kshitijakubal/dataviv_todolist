from django import forms
from todo.models import TodoList
from bootstrap_datepicker_plus import DatePickerInput

class DateInput(forms.DateInput,forms.TimeInput):
    input_type='date'
    


class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['task','task_image','priority','deadline']
        widgets = {
        
        'deadline': DateInput(),
        
    }
class ImageForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['task_image']