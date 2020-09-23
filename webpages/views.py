from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from .models import Webpage


# Create your views here.
class WebpageListView(generic.ListView):
    model = Webpage


class WebpageCreateView(SuccessMessageMixin, generic.CreateView):
    model = Webpage
    fields = '__all__'
    success_url = reverse_lazy("webpages:list")
    success_message = "Webpage created..."


class WebpageUpdateView(SuccessMessageMixin, generic.UpdateView):
    model = Webpage
    fields = '__all__'
    success_url = reverse_lazy("webpages:list")
    success_message = "Webpage updated..."


class WebpageDeleteView(SuccessMessageMixin, generic.DeleteView):
    model = Webpage
    success_url = reverse_lazy("webpages:list")
    success_message = "Webpage deleted..."

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(WebpageDeleteView, self).delete(request, *args, **kwargs)


class WebpageDetailView(generic.DetailView):
    model = Webpage

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Methodology consist of two parts!
        if context['webpage'].pageid == 'METHODOLOGY_1':
            webpage = Webpage.objects.get(pageid='METHODOLOGY_2')
            pagetext = context['webpage'].pagetext + webpage.pagetext
        else:
            pagetext = context['webpage'].pagetext
        context['webpage'].pagetext = pagetext
        return context
