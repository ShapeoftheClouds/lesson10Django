from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Stockspractice
import pygal
from pygal.style import BlueStyle
from .charts import StocksPie

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
