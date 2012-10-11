from django.forms import ModelForm
from ventures.resources.models import Resource


class ResourceForm(ModelForm):
    class Meta:
        model = Resource
