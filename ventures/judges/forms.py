from django.forms import ModelForm
from ventures.judges.models import Judge


class InfoForm(ModelForm):
    class Meta:
        model = Judge
