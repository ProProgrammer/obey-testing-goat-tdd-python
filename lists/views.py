from django.shortcuts import render, redirect

from lists.models import Item


def home_page(request):
    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text)
        return redirect('/')

    items = Item.objects.all()

    # Django's render function takes the request as its first param
    # and the name of the template to render

    # This will automatically search folders called "templates" inside any of
    # your apps' directories. Then it builds an HttpResponse for you, based on the
    # content of the template
    return render(request, 'home.html', {'items': items})
