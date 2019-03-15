import pygal
from .models import Stockspractice

class StocksPie():

    def __init__(self, **kwargs):
        self.chart = pygal.Pie(**kwargs)
        self.chart.title= "Stock Shares"

    def get_data(self):
        data = {}
        for stock in Stockspractice.objects.all():
            data[str(stock.stockname)] = int(stock.shareno)
        return data

    def generate(self):
        chart_data = self.get_data()

        for key, value in chart_data.items():
            self.chart.add(key, value)

        return self.chart.render(is_unicode=True)
