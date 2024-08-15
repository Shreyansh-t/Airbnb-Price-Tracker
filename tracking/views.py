from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from properties.models import *

# Create your views here.

@login_required
def selections(request):
    
    data = Property.objects.filter(user=request.user)

    context = {
        'data': data
    }
    return render(request, "selections.html", context)


def property_history(request, prop_id):
    data = History.objects.filter(property=prop_id)

    context = {
        'data': data
    }

    return render(request, 'history.html', context)

