from django import forms
from.models import Beer, Brewery


class BeerForm(forms.ModelForm):

    class Meta:
        model = Beer
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            breweries = Brewery.objects.all()
            friendly_names = [(brewery.id, brewery.get_friendly_name())
                              for brewery in breweries]

            self.fields['brewery'].choices = friendly_names
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'red darken-4'
