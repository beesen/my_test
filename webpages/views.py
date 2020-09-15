from django.views import generic
from urllib.parse import unquote

from .models import Webpage


# Create your views here.
class WebpageDetailView(generic.DetailView):
    model = Webpage

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Methodology consist of two parts!
        if self.object.id == 7:
            pageText = Webpage.objects.get(pk=8).pagetext
            self.object.pagetext = self.object.pagetext + pageText
        self.object.pagetext = unquote(self.object.pagetext)
        return context
