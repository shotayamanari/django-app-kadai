from django.shortcuts import render
from django.views import View

from.models import Restaurant

class IndexView(View):
    def get(self, request, *args, **kwargs):
    
        context = {}

        context["restaurants"] = Restaurant.objects.all()

        return render(request, "nagoyameshiapp/index.html", context)

# urls.pyから呼び出ししやすいようにする
index = IndexView.as_view()