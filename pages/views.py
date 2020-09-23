from django.shortcuts import render
# import cx_Oracle
import os

# Create your views here.
def home_view(request):
    # try connecting to the cloud
    # See http://www.dominicgiles.com/blog/files/13ab9bba7c8831f42af87a01a150f3ce-172.html
    # os.environ['TNS_ADMIN'] = 'C:\Program Files\Oracle'
    # connection = cx_Oracle.connect('BEESEN', 'beesen', 'BAKPHOON_ORA12PDB_2')
    # cursor = connection.cursor()
    # rs = cursor.execute("select 'Hello for ADB' from dual")
    # rs.fetchall()
    context = {}
    return render(request, template_name='pages/home.html', context=context)