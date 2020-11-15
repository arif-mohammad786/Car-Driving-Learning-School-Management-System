from .models import applicants_model
from django import forms
class applicants_form(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(applicants_form,self).__init__(*args,**kwargs)
        self.label_suffix=' '
    class Meta:
        model=applicants_model
        exclude=['status']
        labels={
            'package':'Select Package','start_date':'Select Training Start Date','timing':'Select Timing','name':'Enter Your Name',
            'email':'Enter Your Email','phone':'Enter Your Phone Number','gender':'Your Gender','age':'Your Age','locenseno':'Your License Number',
            'licensepic':'Upload Your License Photo','address':'Your Full Address'
        }
        widgets={
            'package':forms.Select(attrs={'class':'form-control'}),
            'start_date':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'timing':forms.Select(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),
            'gender':forms.Select(attrs={'class':'form-control'}),
            'age':forms.NumberInput(attrs={'class':'form-control'}),
            'licenseno':forms.NumberInput(attrs={'class':'form-control'}),
            'licensepic':forms.FileInput(attrs={'class':'form-control-file'}),
            'address':forms.Textarea(attrs={'class':'form-control','rows':3}),

        }