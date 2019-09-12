from django.shortcuts import render, redirect

from lists.models import Item


def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/the-only-list-in-the-world/')
    return render(request, 'home.html')

    # Django's render function takes the request as its first param
    # and the name of the template to render

    # This will automatically search folders called "templates" inside any of
    # your apps' directories. Then it builds an HttpResponse for you, based on the
    # content of the template


def view_list(request):
    items = Item.objects.all()

    # Django's render function takes the request as its first param
    # and the name of the template to render

    # This will automatically search folders called "templates" inside any of
    # your apps' directories. Then it builds an HttpResponse for you, based on the
    # content of the template
    return render(request, 'list.html', {'items': items})
