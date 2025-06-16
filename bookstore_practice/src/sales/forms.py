from django import forms

CHART_CHOICES = (
    # Specify choices as a tuple
    ('#1', 'Bar chart'),
    ('#2', 'Pie chart'),
    ('#3', 'Line chart')
)
# Define class-based Form imported from Django forms
class SalesSearchForm(forms.Form):
    book_title = forms.CharField(max_length=120)
    chart_type = forms.ChoiceField(choices=CHART_CHOICES)