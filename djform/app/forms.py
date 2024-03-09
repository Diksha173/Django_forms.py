from django import forms
g=[['MALE','Male'],['FEMALE','Female']]
w=[['PYTHON','Python'],['SQL','Sql'],['WEBTECH','Webtech']]
class StudentForm(forms.Form):
    sname=forms.CharField(max_length=50,required=False)
    sage=forms.IntegerField(required=False)
    saddress=forms.CharField(widget=forms.Textarea(attrs={'cols':25,'rows':5}))
    spassword=forms.CharField(widget=forms.PasswordInput)
    # gender=forms.CharField(choices=g)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    cource=forms.ChoiceField(choices=w,widget=forms.CheckboxSelectMultiple)


