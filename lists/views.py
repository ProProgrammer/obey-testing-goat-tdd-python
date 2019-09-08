from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_page(request):

    # if request.method == 'POST':
    return render(request, 'home.html', {
        'new_item_text': request.POST.get('item_text', ''),
    })

    # Django's render function takes the request as its first param
    # and the name of the template to render

    # This will automatically search folders called "templates" inside any of
    # your apps' directories. Then it builds an HttpResponse for you, based on the
    # content of the template
