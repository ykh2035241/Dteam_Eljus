from django import forms

from .models import ProblemManage # 1115

#1115
class ProblemCreateForm(forms.ModelForm):
  class Meta:
    model= ProblemManage

  def clean(self):
    problemstate = self.cleaned_data['problemstate']
    problemimage = self.cleaned_data['problemimage']
    if not (problemstate) and not (problemimage):
      raise forms.ValidationError('error')

  class Meta:
      model = ProblemManage
      fields = ('uselanguage', 'usesyntax', 'usesyntaxtext', 'problemstate', 'problemimage', 'difficulty','tips' )
      #↑モデルのフィールド書き出し

  def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      for field in self.fields.values():
          field.widget.attrs['class'] = 'form-control'