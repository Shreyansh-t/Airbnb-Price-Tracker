from django.shortcuts import redirect, render
from .forms import StayDetailForm
from home.scraper import *
from .models import Property, History, SearchParams
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def stay_detail_info(request):

    if request.method == "POST":
        form = StayDetailForm(request.POST)
        if form.is_valid():

            obj = Entry(
                form.cleaned_data["where"],
                form.cleaned_data["check_in"],
                form.cleaned_data["check_out"],
                form.cleaned_data["adults"],
                form.cleaned_data["children"],
                form.cleaned_data["infants"]
            )
            obj.add_details()
            # go_back()
            request.session['stay_detail_data'] = form.cleaned_data
            return redirect('properties:listings')
    

    else:
        form = StayDetailForm()
        

    return render(request, 'form.html', {'form': form})


def listings(request):
    titles, descs, prices = fetch_data()
    data = list(zip(titles, descs, prices))

    p = Paginator(data, 9)
    page_number = request.GET.get('page', 1)
    
    if request.method == "POST":

        stay_detail_data = request.session.get('stay_detail_data')
        search_params, created = SearchParams.objects.get_or_create(
            destination=stay_detail_data['where'],
            adults=stay_detail_data['adults'],
            children=stay_detail_data['children'],
            infants=stay_detail_data['infants'],
        )

        Property.objects.create(
            user = request.user,
            title = request.POST.get('title'),
            desc = request.POST.get('desc'),
            price = request.POST.get('price'),
            search_params=search_params,
        )

        return redirect('properties:confirmation')

    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {
        'page_obj':page_obj
    }
        
    return render(request, "listings.html", context)


def confirmation(request):
    return render(request, 'confirmation.html')