from django.shortcuts import render
from django.http import HttpResponse, Http404

from wallet.models import Wallet

# Create your views here.
def index(request):
    wallet_styles = Wallet.objects.all()
    print(wallet_styles)
    context = {'wallet_styles': wallet_styles}
    return render(request, 'wallet/index.html', context)

def detail(request, style):
    try:
        wallet = Wallet.objects.get(pk=style)
    except Wallet.DoesNotExist:
        raise Http404
    return render(request, 'wallet/detail.html', {'wallet': wallet})
    
