from django import forms


class UploadForm(forms.Form):
    """
    Форма для загрузки файла
    """

    file = forms.FileField()