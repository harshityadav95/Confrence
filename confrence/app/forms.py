from django.forms import ModelForm
from app.models import Sessions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class SesionsForm(ModelForm):

    class Meta:
            model=Sessions
            fields=['title','abstract','track','speaker']
    def __init__(self, *args, **kwargs):
        super(SessionForm, self).__init__(*args, **kwargs)
        self.helper=FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-offset-1 col-sm-2'
        self.helper.field_class = 'col-sm-8'
    #    self.helper.add_input(Submit('submit', 'Submit'))

                       

