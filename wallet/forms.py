from django.forms import ModelForm
from wallet.models import Wallet 

#create form class
class Create(ModelForm):
    class Meta:
        model = Wallet

        

