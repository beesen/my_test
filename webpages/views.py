from django.db import connection
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from .models import Webpage
from my_test.utils import get_default_db, get_default_vendor


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

    def get_database_info(self):
        tables = []
        vendor = get_default_vendor()
        db = get_default_db()
        s = f'Vendor: <b>{vendor}</b><br>'
        if vendor == 'sqlite':
            s = s + f"Name: <b>{db['NAME']}</b><br>"
            query = 'select upper(tbl_name) from sqlite_master where type="table" and tbl_name not like "sqlite%" order by upper(tbl_name)'
        elif vendor == 'oracle':
            s = s + f"Host: <b>{db['HOST']}</b><br>"
            s = s + f"User: <b>{db['USER']}</b><br>"
            query = 'select upper(table_name) from user_tables order by upper(table_name)'
        else:
            s = s + 'not yet implemented<br>'
            return s

        # open default database
        with connection.cursor() as cursor:
            # get table names
            cursor.execute(query)
            # for each table:
            for row in cursor.fetchall():
                tables.append(row[0])

            s = s + f'<br>'
            s = s + f'Database contains {len(tables)} tables<br>'
            s = s + f'<table>'
            s = s + f'<tr><th>Table</th><th>Nr of records</th></tr>'
            for table in tables:
                # get nr of records in table
                sql = f'select count(*) from {table}'
                cursor.execute(sql)
                for row in cursor.fetchall():
                    i = 1
                # row = cursor.fetchone()
                s = s + f'<tr><td>{table}</td><td>{row[0]}</td></tr>'
            s = s + f'</table>'
            cursor.close()

        return s

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if context['webpage'].pageid == 'CHECK':
            pagetext = context['webpage'].pagetext + self.get_database_info()
            # Methodology consist of two parts!
        elif context['webpage'].pageid == 'METHODOLOGY_1':
            webpage = Webpage.objects.get(pageid='METHODOLOGY_2')
            pagetext = context['webpage'].pagetext + webpage.pagetext
        else:
            pagetext = context['webpage'].pagetext
        context['webpage'].pagetext = pagetext
        return context
