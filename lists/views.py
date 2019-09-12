from django.shortcuts import render, redirect

from lists.models import Item, List


def home_page(request):
    return render(request, 'home.html')

    # Django's render function takes the request as its first param
    # and the name of the template to render

    # This will automatically search folders called "templates" inside any of
    # your apps' directories. Then it builds an HttpResponse for you, based on the
    # content of the template


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)

    # Django's render function takes the request as its first param
    # and the name of the template to render

    # This will automatically search folders called "templates" inside any of
    # your apps' directories. Then it builds an HttpResponse for you, based on the
    # content of the template
    return render(request, 'list.html', {'list': list_})


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')


def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')
