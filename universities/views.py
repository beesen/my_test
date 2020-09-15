from django.shortcuts import render


# Create your views here.
def university_view(request):
    context = {}
    return render(request, template_name='universities/university.html',
                  context=context)
