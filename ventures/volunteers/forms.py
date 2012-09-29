from django.forms import ModelForm
from ventures.volunteers.models import Volunteer
from ventures.volunteers import ROLE_OPTIONS


class InfoForm(ModelForm):
    class Meta:
        model = Volunteer
