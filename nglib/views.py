from django.http import JsonResponse
from django.shortcuts import render
from .forms import AuthorForm, isStandardized
import requests
import json
from .models import SearchStats
from django.core.exceptions import ObjectDoesNotExist


"""
We are doing this to get only title and description from json
WARNING!
Not every entry on openlibrary has description
"""


def trim_json(data: json) -> json:
    newd = {}
    try:
        newd["title"] = data["title"]
    except KeyError:
        newd["title"] = "No title"
    try:
        newd["description"] = data["description"]
    except KeyError:
        newd["description"] = "Description not provided"
    return newd


def get_author_id(name: str, surname: str) -> str:

    full_name = " ".join([name.lower(), surname.lower()]).strip()
    url_friendly_name = full_name.replace(" ", " ")

    author_data = requests.get(
        f"https://openlibrary.org/search/authors.json?q={url_friendly_name}"
    )
    author_parsed = author_data.json()
    return author_parsed


def get_author_books(id: str) -> json:

    author_books = requests.get(
        f"https://openlibrary.org/authors/{id}/works.json?limit=50"
    )
    books_parsed = author_books.json()
    book_data = books_parsed["entries"]

    cleaned_data = [trim_json(x) for x in book_data[1:]]
    return cleaned_data


# we can also trigger it via signal
def add_search_entry(id: int, data: dict) -> None:
    # or do this with get_or_create
    try:
        author = SearchStats.objects.get(author_id=id)
        author.amount = author.amount + 1
        author.save()

    except ObjectDoesNotExist:

        data["amount"] = 1
        data["author_id"] = id
        form = AuthorForm(data)

        if form.is_valid():
            form.save()


def render_main(request):

    form = AuthorForm()
    context = {"form": form}

    if request.method == "POST":
        author_input = request.POST.copy()
        if isStandardized(author_input["name"]) and isStandardized(
            author_input["surname"]
        ):
            
            author_data = get_author_id(author_input["name"], author_input["surname"])

            author_id_value = author_data["docs"][0]["key"]
            author_books = get_author_books(author_id_value)

            add_search_entry(author_id_value, author_input)

            context = {"book_data": author_books, "author_data": author_data}

            return JsonResponse(context, status=200)
        else:
            return JsonResponse({"failed": "Author data is invalid"}, status=400)

    return render(request, "nglib/search.html", context)
