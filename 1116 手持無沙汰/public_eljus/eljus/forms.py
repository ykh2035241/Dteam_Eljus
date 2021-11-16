from django import forms

from .models import ProblemManage # 1115

#1115
class ProblemrCeateForm(forms.ModelForm):
  class Meta:
    model= ProblemManage

  def clean(self):
    problemstate = self.cleaned_data['problemstate']
    problemimage = self.cleaned_data['problemimage']
    if not (problemstate) and not (problemimage):
      raise forms.ValidationError('errorrrrrrrrrr')