from django import forms
from .models import BookOnShelf


class BookOnShelfForm(forms.Form):
    def __init__(self, instance, *args, **kwargs):
        super(BookOnShelfForm, self).__init__(*args, **kwargs)
        self.fields["position"] = forms.ModelChoiceField(queryset=None)
        qs = BookOnShelf.objects.filter(shelf=instance.shelf).exclude(pk=instance.pk)
        self.fields["position"].queryset = qs
        self.object = instance

    def save(self, *args, **kwargs):
        selected_obj = self.cleaned_data["position"]
        self.object.change_position(selected_obj)
