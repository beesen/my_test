from django.views import generic
from django.db import DatabaseError
from journals.models import Journal
from my_test.utils import get_default_vendor


# Create your views here.
class JournalListView(generic.ListView):
    model = Journal
    context_object_name = 'journals'

    class Meta:
        ordering = ['name']

    def get_context_data(self, *, object_list=None, **kwargs):
        try:
            context = super().get_context_data(**kwargs)
            context['vendor'] = get_default_vendor()
        except DatabaseError as E:
            context = {}
        return context
