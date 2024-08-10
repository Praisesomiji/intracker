from django import forms
from .models import Document
from django.core.exceptions import ValidationError

class DocumentForm(forms.ModelForm):
    def clean_file(self):
        file = self.cleaned_data.get('file', False)
        if file:
            if not file.name.endswith('.pdf'):
                raise ValidationError('Only PDF files are allowed.')
            if file.size > 2 * 1024 * 1024:  # 2 MB limit
                raise ValidationError('File size must be under 2 MB.')
        return file

    class Meta:
        model = Document
        fields = '__all__'

