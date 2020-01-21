from django.urls import path
from django.views.generic import TemplateView


class HelloUniverseView(TemplateView):
    template_name = "misc/hello_universe.html"


urlpatterns = [
    path("", HelloUniverseView.as_view()),
]
