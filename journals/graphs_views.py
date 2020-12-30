from django.db.models import Max, Min
from django.shortcuts import render
from django.views.generic import TemplateView
from plotly.offline import plot
import plotly.graph_objs as go
from django_pandas.io import read_frame
from graphs.models import RankingPer5Year, University


# See https://resources.rescale.com/using-database-views-in-django-orm/
# See https://plotly.com/python/
# See https://style.ons.gov.uk/category/data-visualisation/chart-type/#ranking
# See http://qlikshow.com/creating-a-ranking-chart-over-time/
def get_graph(top_x, from_year, university):
    # university = 'Tilburg University' # id=15843
    if university.startswith('---'):
        top_x_universities = RankingPer5Year.objects.filter(year=from_year).filter(
            uni_rank__lte=top_x)
    else:
        top_x_universities = RankingPer5Year.objects.filter(year=from_year).filter(
            university__contains=university)

    # select delta years
    years = RankingPer5Year.objects.aggregate(Min('year'), Max('year'))
    delta = years['year__max'] - years['year__min'] + 1;

    if university.startswith('---'):
        graph_title = f"Ranking between {years['year__min']} and {years['year__max']} of top {top_x} universities in {from_year}"
    else:
        graph_title = f"Ranking between {years['year__min']} and {years['year__max']} of {university}"

    # Convert into list
    list_top_x_universities = list(
        top_x_universities.values_list('university_id', flat=True))
    if len(list_top_x_universities) == 0:
        return None

    # Get ranking of the top universities
    ranking = RankingPer5Year.objects.filter(
        university_id__in=list_top_x_universities).order_by('university_id', 'year')
    if ranking.count() == 0:
        return None

    # convert queryset to panda dataframe
    df = read_frame(ranking)

    # Prepare years for display on the x-axis
    x = df.year  # (0, 1990) (1, 1990) (2, 1990) ...

    # Initialize plot
    figure = go.Figure()

    # Loop over top universities
    i = 0
    for uni in list_top_x_universities:

        # Build y-axis
        y = df.uni_rank[round(delta * i):round(delta * (i + 1))]

        # Create and style traces
        name = f"{df.university[delta * i]}"
        marker = {'symbol': 'circle', 'size': 10}
        if not university.startswith('---') and df.university[delta * i] == university:
            marker.update({'color': 'black'})
        else:
            marker.update({'cauto': True})
        figure.add_trace(go.Scatter(x=x, y=y,
                                    marker=marker,
                                    mode="lines+markers", name=name,
                                    line={'width': 2},
                                    hovertemplate=None,
                                    hoverlabel={'namelength': -1}))
        i = i + 1

    # Edit layout and axes
    figure.update_layout(title=graph_title,
                         xaxis={'title': 'Years'},
                         yaxis={'title': 'Ranking', 'range': [100, 0], 'dtick': 10},
                         height=1000,
                         showlegend=True,
                         # hovermode="x unified"
                         )
    return plot(figure, auto_open=False, output_type='div')


def update_graph(request):
    try:
        top_x = request.GET['top_x']
    except:
        top_x = 10
    try:
        from_year = request.GET['from_year']
    except:
        from_year = 2000
    try:
        university = request.GET['university']
    except:
        university = 'Tilburg University'

    universities = RankingPer5Year.objects.filter(uni_rank__lte=100).values('university').order_by('university').distinct()

    context = {
        'top_x': top_x,
        'from_year': from_year,
        'university': university,
        'universities': universities,
        'graph': get_graph(top_x, from_year, university)
    }
    return render(request, 'graph.html', context)