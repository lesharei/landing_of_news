from django.shortcuts import render, render_to_response
# Create your views here.
from django.views.generic import TemplateView, ListView

from landing.models import News, RfplSeazon


class LandingView(ListView):
    template_name = 'landing/index.html'
    model = News
    context_object_name = "news"

    def get_context_data(self, **kwargs):
        context = super(LandingView, self).get_context_data(**kwargs)
        context['ord_news'] = News.objects.filter(type_of_news=False).all()
        context['tours'] = RfplSeazon.objects.all()
        return context

    def get_queryset(self):
        return News.objects.filter(type_of_news=True).all()
