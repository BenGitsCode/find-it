from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View

from .search import get_query, normalize_query
from .models import Item, Place, Room
from .forms import RoomForm

class ItemList(View):
  def get(self, request):
    return render(
      request,
      'item/item_list.html',
      {'item_list': Item.objects.all() })

def item_detail(request, slug):
  item = get_object_or_404(Item, slug__iexact=slug)
  return render(request,
    'item/item_detail.html',
    { 'item': item })

class PlaceList(View):
  def get(self, request):
    return render(
      request,
      'item/place_list.html',
      {'place_list': Place.objects.all() })

def place_detail(request, slug):
  place = get_object_or_404(Place, slug__iexact=slug)
  return render(request,
    'item/place_detail.html',
    { 'place': place })


class RoomCreate(View):
  form_class = RoomForm
  template_name = 'item/room_form.html'

  def get(self, request):
    return render(
      request,
      self.template_name,
      {'form': self.form_class() })

  def post(self, request):
    bound_form = self.form_class(request.POST)
    if bound_form.is_valid():
        new_room = bound_form.save()
        return redirect(new_room)
    else:
      return render(
        request,
        self.template_name,
        { 'form': bound_form  })

class RoomList(View):
  def get(self, request):
    return render(
      request,
      'item/room_list.html',
      {'room_list': Room.objects.all() })

def room_detail(request, slug):
  room = get_object_or_404(Room, slug__iexact=slug)
  return render(request,
    'item/room_detail.html',
    { 'room': room })


# search

def search(request):
    query_string = ''
    found_items = None
    print 'got here'
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        print query_string

        entry_query = get_query(query_string, ['name'])

        found_items = Item.objects.filter(entry_query)

    return render(request,
                  'item/item_search.html',
                  { 'query_string': query_string, 'found_items': found_items },
                )


