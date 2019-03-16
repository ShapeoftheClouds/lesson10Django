from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Stockspractice
import pygal
from pygal.style import BlueStyle
from .charts import StocksPie
from .forms import StockForm

# Create your views here.

def index(request):
    ownerObject = Stockspractice.objects.all()
    context = {'stocks': ownerObject}
    return render(request, 'stocksApp/index.html', context)

class IndexView(TemplateView):
    template_name = 'stocksApp/piepage.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        cht_stocks = StocksPie(
            height=600,
            width=800,
            explicit_size=True,
            style=BlueStyle
        )

        context['cht_stocks'] = cht_stocks.generate()
        return context

def new_stock(request):
    # Add a new stock.
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = StockForm()
    else:
        # POST data submitted; process data.
        form = StockForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('stocksApp:index'))
    context = {'form' : form}
    return render(request, 'stocksApp/new_stocks.html', context)
