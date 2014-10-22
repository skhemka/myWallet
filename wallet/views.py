from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404

from wallet.models import Wallet

# Create your views here.
def index(request):
    wallet_styles = Wallet.objects.all()
    context = {'wallet_styles': wallet_styles}
    return render(request, 'wallet/index.html', context)

def detail(request, style):
    wallet = get_object_or_404(Wallet, pk=style)
    return render(request, 'wallet/detail.html', {'wallet': wallet})

