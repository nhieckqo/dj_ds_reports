from typing import List
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Sale
from .forms import SalesSearchForm
import pandas as pd
# Create your views here.


def home_view(request):
    sales_df = None
    positions_df = None
    form = SalesSearchForm(request.POST or None)
    
    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')
        print(date_from, date_to, chart_type)

        sale_qs = Sale.objects.filter(created__date__lte=date_to, created__date__gte=date_from)
        if len(sale_qs) > 0:
            sales_df = pd.DataFrame(sale_qs.values())
            positions_data = []
            for sale in sale_qs:
                for pos in sale.get_positions():
                    obj = {
                        'postition_id': pos.id,
                        'product': pos.product.name,
                        'quantity': pos.quantity,
                        'price': pos.price

                    }
                    positions_data.append(obj)
            
            positions_df = pd.DataFrame(positions_data)
            print('position df')
            print(positions_df)

            sales_df = sales_df.to_html()
            positions_df = positions_df.to_html()

        else:
            print('no data')

        # obj = Sale.objects.get(id=1)
        # print(qs)
        # print(obj)
        # print('###########')
        # df1 = pd.DataFrame(qs.values())
        # print(df1)
        # print('##########')
        # df2 = pd.DataFrame(qs.values_list())
        # print(df2)

    context = {
        
        'form': form,
        'sales_df':sales_df,
        'positions_df': positions_df,
    }
    return render(request, 'sales/home.html', context)

# def sales_list_view(request):
#     qs = Sale.objects.all()
#     return render(request, 'sales/main.html', {'object_list':qs})

# def sales_detail_view(request, **kwargs):
#     pk = kwargs.get('pk')
#     obj = Sale.objects.get(pk=pk)
#     #or
#     #obj = get_object_or_404(Sale, pk=pk)
#     return render(request, 'sales/detail.html', {'object':obj})


class SalesListView(ListView):
    model = Sale
    template_name = 'sales/main.html'


class SalesDetailView(DetailView):
    model = Sale
    template_name = 'sales/detail.html'

