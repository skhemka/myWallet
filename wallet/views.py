from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponse, Http404 
from django.core.urlresolvers import reverse
from django.views import generic

from wallet.models import Wallet
from wallet.forms import Create

#class IndexView(generic.ListView):
#    template_name = 'wallet/index.html'
#    context_object_name = 'wallet_styles'
#    
#    def get_queryset(self):
#        return Wallet.objects.all();
#
#class DetailView(generic.DetailView):
#    model = Wallet
#    template_name = 'wallet/detail.html'
#
#class CreateView(generic.edit.FormView):
#    form_class = Create
#    template_name = 'wallet/create.html'
#    success_url = reverse_lazy('wallet/index.html')

# Create your views here.
def index(request):
    wallet_styles = Wallet.objects.all()
    context = {'wallet_styles': wallet_styles}
    return render(request, 'wallet/index.html', context)

def detail(request, style):
    wallet = get_object_or_404(Wallet, pk=style)
    return render(request, 'wallet/detail.html', {'wallet': wallet})

def create(request):
    if request.method == 'POST':
        form = Create(data=request.POST)
        if form.is_valid():
            wallet = form.save()
            return redirect(reverse('index'))
    return render_to_response('wallet/create.html')

