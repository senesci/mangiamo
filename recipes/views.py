from datetime import timezone

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .forms import SearchForm, RecipeForm

from .models import Recipe, Author
from django.db.models import Q

import markdown
import json
def index(request):
    recipes = Recipe.objects.all().filter(visible=True).order_by('-published')
    template = loader.get_template('recipes/index.html')
    context = {"recipes": recipes}
    return HttpResponse(template.render(context, request))

def display_about_page(request):
    template = loader.get_template('recipes/about.html')
    return HttpResponse(template.render({}, request))

def search_page(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search_term = form.cleaned_data['query']

            recipes = Recipe.objects.filter(
                Q(title__icontains=search_term) | Q(body__icontains=search_term) | Q(author__name__icontains=search_term),
                visible=True
            )

            template = loader.get_template('recipes/search-results.html')
            return HttpResponse(template.render({"results": recipes, "search_term": search_term}, request))

    template = loader.get_template('recipes/search.html')
    return HttpResponse(template.render({}, request))


def display_recipe(request, recipe_id):
    try:
        recipe = Recipe.objects.get(pk=recipe_id, visible=True)
    except Recipe.DoesNotExist:
        return HttpResponse("Recipe not found")
    template = loader.get_template('recipes/recipe.html')
    context = {"recipe": recipe, "markdown": markdown.markdown(recipe.body)}
    return HttpResponse(template.render(context, request))

def display_author(request, author_id):
    try:
        author = Author.objects.get(pk=author_id)
    except Author.DoesNotExist:
        return HttpResponse("Author not found")

    try:
        recipes = Recipe.objects.filter(author=author, visible=True)
    except Recipe.DoesNotExist:
        return HttpResponse("Author has no recipes")

    template = loader.get_template('recipes/author.html')
    context = {"author": author, "recipes": recipes}
    return HttpResponse(template.render(context, request))

def display_authors_page(request):
    authors = Author.objects.all().order_by('name')
    template = loader.get_template('recipes/authors.html')
    context = {"authors": authors}
    return HttpResponse(template.render(context, request))

def create_page(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            body = form.cleaned_data['body']

            recipe = Recipe.objects.create(title=title, author=Author.objects.get(pk=author), body=body, visible=False)
            recipe.save()

            return HttpResponseRedirect("/create/thanks")
        else:
            return HttpResponse("Invalid form data.")
    else:
        template = loader.get_template('recipes/create.html')
        form = RecipeForm()
        context = {"form": form}
        return HttpResponse(template.render(context, request))

def create_thanks(request):
    template = loader.get_template('recipes/create-thanks.html')
    context = {}
    return HttpResponse(template.render(context, request))