from django.shortcuts import render

# Create your views here.
def sandbox_view(request):
    context = {}
    return render(request, template_name='sandbox/sandbox.html', context=context)