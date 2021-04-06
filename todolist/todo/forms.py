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
    def clean(self):
        task = self.cleaned_data.get('task')
        task_image = self.cleaned_data.get('task_image')
        if not task and not task_image:
            raise forms.ValidationError('One of fields is required')
        return self.cleaned_data