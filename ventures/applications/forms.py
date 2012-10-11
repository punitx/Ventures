from django.forms import ModelForm
from ventures.applications.models import Application


class InfoForm(ModelForm):
    class Meta:
        model = Application
