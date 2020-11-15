from django import forms
from core.models import packagemodel
class package_form(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(package_form,self).__init__(*args,**kwargs)
        self.label_suffix=' '
    class Meta:
        model=packagemodel
        fields="__all__"
        labels={
            'pname':'Package Name','pdesc':'Package Description','pduration':'Package Duration','pprice':'Package Price'
        }
        widgets={
            'pname':forms.TextInput(attrs={'class':'form-control','placeholder':'Package Name'}),
            'pdesc':forms.Textarea(attrs={'class':'form-control','placeholder':'Package Description','rows':2}),
            'pduration':forms.NumberInput(attrs={'class':'form-control','placeholder':'Package Duration'}),
            'pprice':forms.NumberInput(attrs={'class':'form-control','placeholder':'Package Price'}),
        }