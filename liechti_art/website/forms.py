from django import forms
from .models import Record


# ADD Form

class AddRecordForm(forms.ModelForm):
    img_title = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Titel des Bildes", "class": "form-control bg-dark text-light"}), label="")
    img = forms.ImageField(required=True, widget=forms.FileInput(attrs={"class": "form-control bg-dark text-light"}), label="")
    artist_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Künstlername", "class": "form-control bg-dark text-light"}), label="")
    dimensions = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Dimensionen", "class": "form-control bg-dark text-light"}), label="")
    bild_art = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Art des Bildes", "class": "form-control bg-dark text-light"}), label="")
    bild_standort = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Standort des Bildes", "class": "form-control bg-dark text-light"}), label="")
    Jahrgang = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Jahrgang", "class": "form-control bg-dark text-light"}), label="")
    comment = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Bemerkung", "class": "form-control bg-dark text-light"}), label="")

    class Meta:
        model = Record
        exclude = ("user",)


# CHANGE Form

class ChangeRecordForm(forms.ModelForm):
    img_title = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Titel des Bildes", "class": "form-control bg-dark text-light"}), label="Titel des Bildes:")
    img = forms.ImageField(required=False, widget=forms.FileInput(attrs={"class": "form-control bg-dark text-light visually-hidden"}), label="")
    artist_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Künstlername", "class": "form-control bg-dark text-light"}), label="Künstlername:")
    dimensions = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Dimensionen", "class": "form-control bg-dark text-light"}), label="Dimensionen:")
    bild_art = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Art des Bildes", "class": "form-control bg-dark text-light"}), label="Art des Bildes:")
    bild_standort = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Standort des Bildes", "class": "form-control bg-dark text-light"}), label="Standort des Bildes:")
    Jahrgang = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Jahrgang", "class": "form-control bg-dark text-light"}), label="Jahrgang:")
    comment = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Bemerkung", "class": "form-control bg-dark text-light"}), label="Bemerkung:")

    class Meta:
        model = Record
        exclude = ("user",)
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Setze das img-Feld auf required=False
        self.fields['img'].required = False
        # Verstecke das img-Feld im Formular mit der "d-none" Bootstrap-Klasse
        self.fields['img'].widget.attrs['class'] = 'visually-hidden'