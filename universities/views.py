from django.views import generic
from django.shortcuts import render

from universities.models import University

# Create your views here.
class UniversityListView(generic.ListView):
    model = University


def university_view(request):
    context = {}
    return render(request, template_name='universities/university.html',
                  context=context)
