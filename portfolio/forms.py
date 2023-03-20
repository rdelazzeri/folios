from django.forms import ModelForm, fields, Form
from .models import *




class FolioDetailForm(ModelForm):

    class Meta:
        model = Folio
        fields = '__all__'



class PictureDetailForm(ModelForm):

    class Meta:
        model = Picture
        fields = '__all__'