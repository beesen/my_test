from django.shortcuts import render

from my_test.utils_2 import search_username_in_ldap

# Create your views here.
def home_view(request):
    a = search_username_in_ldap('beesen')
    context = {}
    return render(request, template_name='pages/home.html', context=context)