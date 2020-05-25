from django.http import HttpResponse
from django.shortcuts import render
from .models import Items, Category, Group, Set, Colour
from django.core import serializers
import urllib.parse
import json

def index(request):
    json_items = serializers.serialize("json",Items.objects.all())   
    json_categories = serializers.serialize("json",Category.objects.all())    
    json_groups = serializers.serialize("json",Group.objects.all())
    json_sets = serializers.serialize("json",Set.objects.all())
    json_colours = serializers.serialize("json",Colour.objects.all())


    context = {
        "items": Items.objects.all(),
        "categories": Category.objects.all(),
        "groups": Group.objects.all(),
        "sets": Set.objects.all(),
        "colours": Colour.objects.all(),
        "json_items": json_items,
        "json_categories": json_categories,
        "json_groups": json_groups,
        "json_sets": json_sets,
        "json_colours": json_colours,
    }
    return render(request, "web_app/home.html", context)

def home(request):
    json_items = serializers.serialize("json",Items.objects.all())   
    json_categories = serializers.serialize("json",Category.objects.all())    
    json_groups = serializers.serialize("json",Group.objects.all())
    json_sets = serializers.serialize("json",Set.objects.all())
    json_colours = serializers.serialize("json",Colour.objects.all())


    context = {
        "items": Items.objects.all(),
        "categories": Category.objects.all(),
        "groups": Group.objects.all(),
        "sets": Set.objects.all(),
        "colours": Colour.objects.all(),
        "json_items": json_items,
        "json_categories": json_categories,
        "json_groups": json_groups,
        "json_sets": json_sets,
        "json_colours": json_colours,
    }
    return render(request, "web_app/home.html", context)
def collection(request):
    json_items = serializers.serialize("json",Items.objects.all())   
    json_categories = serializers.serialize("json",Category.objects.all())    
    json_groups = serializers.serialize("json",Group.objects.all())
    json_sets = serializers.serialize("json",Set.objects.all())
    json_colours = serializers.serialize("json",Colour.objects.all())


    context = {
        "items": Items.objects.all(),
        "categories": Category.objects.all(),
        "groups": Group.objects.all(),
        "sets": Set.objects.all(),
        "colours": Colour.objects.all(),
        "json_items": json_items,
        "json_categories": json_categories,
        "json_groups": json_groups,
        "json_sets": json_sets,
        "json_colours": json_colours,
    }
    return render(request, "web_app/collection.html", context)

def about(request):
    json_items = serializers.serialize("json",Items.objects.all())   
    json_categories = serializers.serialize("json",Category.objects.all())    
    json_groups = serializers.serialize("json",Group.objects.all())
    json_sets = serializers.serialize("json",Set.objects.all())
    json_colours = serializers.serialize("json",Colour.objects.all())


    context = {
        "items": Items.objects.all(),
        "categories": Category.objects.all(),
        "groups": Group.objects.all(),
        "sets": Set.objects.all(),
        "colours": Colour.objects.all(),
        "json_items": json_items,
        "json_categories": json_categories,
        "json_groups": json_groups,
        "json_sets": json_sets,
        "json_colours": json_colours,
    }
    return render(request, "web_app/about.html", context)

def contact(request):
    json_items = serializers.serialize("json",Items.objects.all())   
    json_categories = serializers.serialize("json",Category.objects.all())    
    json_groups = serializers.serialize("json",Group.objects.all())
    json_sets = serializers.serialize("json",Set.objects.all())
    json_colours = serializers.serialize("json",Colour.objects.all())


    context = {
        "items": Items.objects.all(),
        "categories": Category.objects.all(),
        "groups": Group.objects.all(),
        "sets": Set.objects.all(),
        "colours": Colour.objects.all(),
        "json_items": json_items,
        "json_categories": json_categories,
        "json_groups": json_groups,
        "json_sets": json_sets,
        "json_colours": json_colours,
    }

    return render(request, "web_app/contact.html", context)

def category(request, category_name):
    json_items = serializers.serialize("json",Items.objects.all())   
    json_categories = serializers.serialize("json",Category.objects.all())    
    json_groups = serializers.serialize("json",Group.objects.all())
    json_sets = serializers.serialize("json",Set.objects.all())
    json_colours = serializers.serialize("json",Colour.objects.all())


    context = {
        "items": Items.objects.all(),
        "categories": Category.objects.all(),
        "groups": Group.objects.all(),
        "sets": Set.objects.all(),
        "colours": Colour.objects.all(),
        "category_name": category_name,
        "json_items": json_items,
        "json_categories": json_categories,
        "json_groups": json_groups,
        "json_sets": json_sets,
        "json_colours": json_colours,
    }
    return render(request, "web_app/category.html", context)

def item(request, item_name, item_type, item_id):
    json_items = serializers.serialize("json",Items.objects.all())   
    json_categories = serializers.serialize("json",Category.objects.all())    
    json_groups = serializers.serialize("json",Group.objects.all())
    json_sets = serializers.serialize("json",Set.objects.all())
    json_colours = serializers.serialize("json",Colour.objects.all())


    context = {
        "items": Items.objects.all(),
        "categories": Category.objects.all(),
        "groups": Group.objects.all(),
        "sets": Set.objects.all(),
        "colours": Colour.objects.all(),
        "item_name": item_name,
        "item_id": item_id,
        "item_type": item_type,
        "json_items": json_items,
        "json_categories": json_categories,
        "json_groups": json_groups,
        "json_sets": json_sets,
        "json_colours": json_colours,
    }
    return render(request, "web_app/item.html", context)

