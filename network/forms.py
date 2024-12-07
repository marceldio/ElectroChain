from dal import autocomplete
from django import forms
from .models import NetworkNode, Product

class NetworkNodeAdminForm(forms.ModelForm):
    class Meta:
        model = NetworkNode
        fields = ['supplier', 'products', 'contact', 'debt', 'name']
        field_order = ['supplier', 'products', 'contact', 'debt', 'name']
        list_filter = ('supplier', 'contact',)

    products = forms.ModelMultipleChoiceField(
        queryset=Product.objects.none(),
        widget=autocomplete.ModelSelect2Multiple(
            url='network:product-autocomplete',
            forward=['supplier']
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Если есть instance, заполняем доступные продукты
        if self.instance and self.instance.supplier:
            self.fields['products'].queryset = Product.objects.filter(network_nodes=self.instance.supplier)
        else:
            self.fields['products'].queryset = Product.objects.all()
