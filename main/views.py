from django.shortcuts import render
from .models import Item
# Create your views here.

def item_list(request):
    items = Item.objects.all()
    return render(request, 'index.html', {'items': items})