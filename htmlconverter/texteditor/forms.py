from .models import Editor
from django import forms
from ckeditor.widgets import CKEditorWidget

class Formeditor(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget(),label='Text editor')
    class Meta:
        model = Editor
        fields = "__all__"




