from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Items, Category, Group, Set, Colour, Photo
from django.core import serializers
import urllib.parse
import json
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm

def index(request):
    json_items = serializers.serialize("json",Items.objects.all())   
    json_categories = serializers.serialize("json",Category.objects.all())    
    json_groups = serializers.serialize("json",Group.objects.all())
    json_sets = serializers.serialize("json",Set.objects.all())
    json_colours = serializers.serialize("json",Colour.objects.all())
    json_photos = serializers.serialize("json",Photo.objects.all())


    context = {
        "items": Items.objects.all(),
        "categories": Category.objects.all(),
        "groups": Group.objects.all(),
        "sets": Set.objects.all(),
        "colours": Colour.objects.all(),
        "photos": Photo.objects.all(),
        "json_items": json_items,
        "json_categories": json_categories,
        "json_groups": json_groups,
        "json_sets": json_sets,
        "json_colours": json_colours,
        "json_photos": json_photos,
    }
    return render(request, "web_app/home.html", context)

def home(request):
    json_items = serializers.serialize("json",Items.objects.all())   
    json_categories = serializers.serialize("json",Category.objects.all())    
    json_groups = serializers.serialize("json",Group.objects.all())
    json_sets = serializers.serialize("json",Set.objects.all())
    json_colours = serializers.serialize("json",Colour.objects.all())
    json_photos = serializers.serialize("json",Photo.objects.all())


    context = {
        "items": Items.objects.all(),
        "categories": Category.objects.all(),
        "groups": Group.objects.all(),
        "sets": Set.objects.all(),
        "colours": Colour.objects.all(),
        "photos": Photo.objects.all(),
        "json_items": json_items,
        "json_categories": json_categories,
        "json_groups": json_groups,
        "json_sets": json_sets,
        "json_colours": json_colours,
        "json_photos": json_photos,
    }
    return render(request, "web_app/home.html", context)


def collection(request):
    json_items = serializers.serialize("json",Items.objects.all())   
    json_categories = serializers.serialize("json",Category.objects.all())    
    json_groups = serializers.serialize("json",Group.objects.all())
    json_sets = serializers.serialize("json",Set.objects.all())
    json_colours = serializers.serialize("json",Colour.objects.all())
    json_photos = serializers.serialize("json",Photo.objects.all())


    context = {
        "items": Items.objects.all(),
        "categories": Category.objects.all(),
        "groups": Group.objects.all(),
        "sets": Set.objects.all(),
        "colours": Colour.objects.all(),
        "photos": Photo.objects.all(),
        "json_items": json_items,
        "json_categories": json_categories,
        "json_groups": json_groups,
        "json_sets": json_sets,
        "json_colours": json_colours,
        "json_photos": json_photos,
    }
    return render(request, "web_app/collection.html", context)

def about(request):
    json_items = serializers.serialize("json",Items.objects.all())   
    json_categories = serializers.serialize("json",Category.objects.all())    
    json_groups = serializers.serialize("json",Group.objects.all())
    json_sets = serializers.serialize("json",Set.objects.all())
    json_colours = serializers.serialize("json",Colour.objects.all())
    json_photos = serializers.serialize("json",Photo.objects.all())


    context = {
        "items": Items.objects.all(),
        "categories": Category.objects.all(),
        "groups": Group.objects.all(),
        "sets": Set.objects.all(),
        "colours": Colour.objects.all(),
        "photos": Photo.objects.all(),
        "json_items": json_items,
        "json_categories": json_categories,
        "json_groups": json_groups,
        "json_sets": json_sets,
        "json_colours": json_colours,
        "json_photos": json_photos,
    }
    return render(request, "web_app/about.html", context)

def category(request, category_name):
    json_items = serializers.serialize("json",Items.objects.all())   
    json_categories = serializers.serialize("json",Category.objects.all())    
    json_groups = serializers.serialize("json",Group.objects.all())
    json_sets = serializers.serialize("json",Set.objects.all())
    json_colours = serializers.serialize("json",Colour.objects.all())
    json_photos = serializers.serialize("json",Photo.objects.all())


    context = {
        "items": Items.objects.all(),
        "categories": Category.objects.all(),
        "groups": Group.objects.all(),
        "sets": Set.objects.all(),
        "colours": Colour.objects.all(),
        "photos": Photo.objects.all(),
        "category_name": category_name,
        "json_items": json_items,
        "json_categories": json_categories,
        "json_groups": json_groups,
        "json_sets": json_sets,
        "json_colours": json_colours,
        "json_photos": json_photos,
    }
    return render(request, "web_app/category.html", context)

def item(request, item_name, item_type, item_id):
    json_items = serializers.serialize("json",Items.objects.all())   
    json_categories = serializers.serialize("json",Category.objects.all())    
    json_groups = serializers.serialize("json",Group.objects.all())
    json_sets = serializers.serialize("json",Set.objects.all())
    json_colours = serializers.serialize("json",Colour.objects.all())
    json_photos = serializers.serialize("json",Photo.objects.all())

    context = {
        "items": Items.objects.all(),
        "categories": Category.objects.all(),
        "groups": Group.objects.all(),
        "sets": Set.objects.all(),
        "colours": Colour.objects.all(),
        "photos": Photo.objects.all(),
        "item_name": item_name,
        "item_id": item_id,
        "item_type": item_type,
        "json_items": json_items,
        "json_categories": json_categories,
        "json_groups": json_groups,
        "json_sets": json_sets,
        "json_colours": json_colours,
        "json_photos": json_photos,
    }
    return render(request, "web_app/item.html", context)

def contact(request):
    json_items = serializers.serialize("json",Items.objects.all())   
    json_categories = serializers.serialize("json",Category.objects.all())    
    json_groups = serializers.serialize("json",Group.objects.all())
    json_sets = serializers.serialize("json",Set.objects.all())
    json_colours = serializers.serialize("json",Colour.objects.all())
    json_photos = serializers.serialize("json",Photo.objects.all())

    context = {
        "items": Items.objects.all(),
        "categories": Category.objects.all(),
        "groups": Group.objects.all(),
        "sets": Set.objects.all(),
        "colours": Colour.objects.all(),
        "photos": Photo.objects.all(),
        "json_items": json_items,
        "json_categories": json_categories,
        "json_groups": json_groups,
        "json_sets": json_sets,
        "json_colours": json_colours,
        "json_photos": json_photos,
    }

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            user_email = form.cleaned_data['user_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, user_email, ["testharvardproject4@gmail.com"])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "web_app/contact.html", {'form': form}, context)

def search(request):
    search_input = request.POST.get('search', False)

    filter_items = Items.objects.filter(
        Q(item_name__icontains=search_input)
        | Q(description__icontains=search_input)
        | Q(category__category_name__icontains=search_input)
        | Q(group__group_name__icontains=search_input)
        | Q(sets__set_name__icontains=search_input)
        | Q(colour__colour_name__icontains=search_input)
    ).all().distinct()

    filter_sets = Set.objects.filter( Q(set_name__icontains=search_input)
        | Q(set_colour__colour_name__icontains=search_input)
        | Q(set_description__icontains=search_input)
    ).all().distinct()

    json_items = serializers.serialize("json",Items.objects.all())   
    json_categories = serializers.serialize("json",Category.objects.all())    
    json_groups = serializers.serialize("json",Group.objects.all())
    json_sets = serializers.serialize("json",Set.objects.all())
    json_colours = serializers.serialize("json",Colour.objects.all())
    json_photos = serializers.serialize("json",Photo.objects.all())
    json_search_items = serializers.serialize("json",filter_items)
    json_search_sets = serializers.serialize("json",filter_sets)
    
    context = {
        "items": Items.objects.all(),
        "categories": Category.objects.all(),
        "groups": Group.objects.all(),
        "sets": Set.objects.all(),
        "colours": Colour.objects.all(),
        "photos": Photo.objects.all(),
        "search_items": filter_items,
        "search_sets": filter_sets,
        "json_items": json_items,
        "json_categories": json_categories,
        "json_groups": json_groups,
        "json_sets": json_sets,
        "json_colours": json_colours,
        "json_photos": json_photos,
        "json_search_items": json_search_items,
        "json_search_sets": json_search_sets,
    }

    return render(request, "web_app/search.html", context)


def success(request):
    json_items = serializers.serialize("json",Items.objects.all())   
    json_categories = serializers.serialize("json",Category.objects.all())    
    json_groups = serializers.serialize("json",Group.objects.all())
    json_sets = serializers.serialize("json",Set.objects.all())
    json_colours = serializers.serialize("json",Colour.objects.all())
    json_photos = serializers.serialize("json",Photo.objects.all())


    context = {
        "items": Items.objects.all(),
        "categories": Category.objects.all(),
        "groups": Group.objects.all(),
        "sets": Set.objects.all(),
        "colours": Colour.objects.all(),
        "photos": Photo.objects.all(),
        "json_items": json_items,
        "json_categories": json_categories,
        "json_groups": json_groups,
        "json_sets": json_sets,
        "json_colours": json_colours,
        "json_photos": json_photos,
    }
    return render(request, "web_app/success.html", context)