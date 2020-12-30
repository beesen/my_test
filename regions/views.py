import json
from django.shortcuts import render
from django.http import JsonResponse

from .models import Region, Country
from my_test.utils import regions_as_select, countries_as_select

# Create your views here.
def regions_simple_view(request):
    template_name = 'regions/region_simple.html'
    regions = Region.objects.all()
    context = {
        'user': request.user,
        'regions_as_select': regions_as_select(regions),
        'countries_as_select': None
    }
    return render(request=request, template_name=template_name, context=context)


def regions_selected_view(request):
    if request.is_ajax and request.method == "POST":
        region_id = request.POST["region_id"]
        countries = Country.objects.filter(region_id=region_id)
        data = {
            "countries": countries_as_select(countries)
        }
        return JsonResponse(data=data, status=200)
    else:
        return JsonResponse(data={}, status=400)
