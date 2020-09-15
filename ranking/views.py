from django.shortcuts import render

# Create your views here.
def ranking_view(request):
    context = {}
    return render(request, template_name='ranking/ranking.html', context=context)