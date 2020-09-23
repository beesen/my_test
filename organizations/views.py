from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from .models import Organization


# Create your views here.
class OrganizationListView(generic.ListView):
    model = Organization


class OrganizationCreateView(SuccessMessageMixin, generic.CreateView):
    model = Organization
    fields = '__all__'
    success_url = reverse_lazy("organizations:list")
    success_message = "Organization created..."


class OrganizationUpdateView(SuccessMessageMixin, generic.UpdateView):
    model = Organization
    fields = '__all__'
    success_url = reverse_lazy("organizations:list")
    success_message = "Organization updated..."



class OrganizationDeleteView(SuccessMessageMixin, generic.DeleteView):
    model = Organization
    success_url = reverse_lazy("organizations:list")
    success_message = "Organization deleted..."

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(OrganizationDeleteView, self).delete(request, *args, **kwargs)
