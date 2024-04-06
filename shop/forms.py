from django import forms

from shop.models import Contact


class ContactForm(forms.Form):
    ContactChoice = (
        ("buy", "Buy"),
        ("sell", "Sell"),
        ("promotion", "Promotion"),
        ("order", "Order")
    )
    reason = forms.CharField(max_length=34, choices=ContactChoice)

    class Meta:
        model = Contact
        fields = ['name', 'phone', 'reason', 'subject']
