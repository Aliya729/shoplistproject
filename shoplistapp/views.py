from urllib import request

from django.http import HttpResponseRedirect
from django.shortcuts import render


def shoplistappVew(request):
    return render(request, 'shoplist.html')


from .models import ShoplistItem


def shoplistappView(request):
    all_shoplist_items = ShoplistItem.objects.all()
    return (render(request, 'shoplist.html', {'all_items': all_shoplist_items}))


def addShoplistView(request):
    x = request.POST['content']
    new_item = ShoplistItem(content=x)
    new_item.save()
    return HttpResponseRedirect('/shoplistapp/')


def deleteShoplistView(request, i):
    y = ShoplistItem.objects.get(id=i)
    y.delete()
    return HttpResponseRedirect('/shoplistapp/')

# Create your views here.
