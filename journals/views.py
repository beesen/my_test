from json import dumps
from plotly.offline import plot
import plotly.graph_objs as go
from django_pandas.io import read_frame

from django.views import generic
from django.db import DatabaseError
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from journals.models import Journal, JournalYear, JournalYearIndicator


# Create your views here.
class JournalListView(generic.ListView):
    model = Journal
    context_object_name = 'journals'

    class Meta:
        ordering = ['name']


def get_graph(journal_id):
    # prefetch related data
    qs = JournalYearIndicator.objects.select_related('journal_year').filter(
        journal_year__journal_id=journal_id).order_by('journal_year__year', 'indicator')

    # convert queryset to panda dataframe
    df = read_frame(qs)

    # Initialize plot
    figure = go.Figure()

    # Prepare x-axis: years
    a = []
    b = []
    for q in qs:
        if q.indicator_id == 2:
            title = q.indicator.name
            a.append(q.journal_year.year)
            b.append(q.weight)
    x = a

    # Prepare y-axis: indicator weights
    y = b
    figure.update_yaxes(showgrid=True,
                        gridcolor='#bdbdbd')

    # Create and style traces
    name = 'indicator'
    #    marker = {'symbol': 'circle', 'size': 10}
    #    marker.update({'cauto': True})
    figure.add_trace(
        go.Scatter(x=x, y=y, mode="lines", name=name,
                   line={'width': 2,
                         'color': '#006094'}
                   ))

    config = {'displayModeBar': False}

    # Edit layout and axes
    figure.update_layout(title={
        'text': f"<b>{title}</b>",
        'x': 0.5,
        'y': 0.96},
        font_family='lato',

        #                         xaxis={'title': 'Years'},
        #                         yaxis={'title': 'Indicators', 'dtick': 10},
        height=300,
        width=350,
        #                         showlegend=True,
        plot_bgcolor='white',
        margin=dict(l=0, r=0, b=0, t=40)
    )

    return plot(figure, auto_open=False, output_type='div', config=config)


def journal_detail_view(request):
    journal_id = request.POST['journal_id']
    data = {
        'extra': get_graph(journal_id)
    }
    response = JsonResponse(data=data)
    # if something went wrong then
    # response.status_code = 500
    return response
#    return HttpResponse(dumps(data), content_type="application/json")
