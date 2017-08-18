from django import forms

COLORS_CHOICES = (
  ('1', 'Red'),
  ('2', 'Green'),
  ('3', 'Blue'),
)

BITS_CHOICES = (
  ('1', '1'),
  ('2', '2'),
  ('3', '3'),
  ('4', '4'),
  ('5', '5'),
  ('6', '6'),
  ('7', '7'),
  ('8', '8'),
)

PIXEL_CHOICES = (
  ('1', 'Impar'),
  ('2', 'Par'),
)

class MessageSettingsForm(forms.Form):
  colors = forms.MultipleChoiceField(
    required=False,
    widget=forms.CheckboxSelectMultiple,
    choices=COLORS_CHOICES,
  )

  bits = forms.MultipleChoiceField(
    required=False,
    widget=forms.CheckboxSelectMultiple,
    choices=BITS_CHOICES,
  )

  pixel = forms.MultipleChoiceField(
    required=False,
    widget=forms.CheckboxSelectMultiple,
    choices=PIXEL_CHOICES,
  )

  def save(self, commit=True):
    colors = self.cleaned_data['colors']
    bits = self.cleaned_data['bits']
    pixel = self.cleaned_data['pixel']

    # print(colors, bits, pixel)
