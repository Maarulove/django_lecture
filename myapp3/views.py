from typing import Any
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView


def hello(request):
    return HttpResponse('hello world')

class Hello(View):
    def get(self, request):
        return HttpResponse(" Helloo world class")
    
def year_post(request, year):
    text  = ''

    return HttpResponse(f"post from{year} <br> {text}")

def year_post(request,month, year):
    text  = ''

    return HttpResponse(f"post from{year}, {month} <br> {text}")

def post_details(request, year, month, slug):
    post = {
        "year": year,
        "months": month,
        "slug": slug,
        "title": "fdsadasdasdds",
        "content": "fdsadasdasddsdsdasdsad"
    }
    return JsonResponse(post, json_dumps_params={"ensure_ascii": False})

def my_views(request):
    context = {"name": "john"}
    return render(request, "myapp3/index.html", context)





class Temlif(TemplateView):
    temp_name = "myapp3/index.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context["message"] = "hellloo "
        return context

def view_for(request):
    my_list = ["dsd", "dasdas"]
    my_dict = {
        "dsad":'dasds',
        "dsadfds":'dasds',
        "dsadfa":'dasds',
        "dsaddsa":'dasds',
    }
    context = {"my_list": my_list, "my_dict":my_dict}
    return render(request, "myapp3/index.html", context)

def author_get(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author).ordered_by("-id")[:5]
    return render(request, "myapp3/dasd.html", {"post": posts})

def Posts(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "myapp3/dasd.html", {"post": posts})