from django.shortcuts import render
from django.views.generic import TemplateView




class HomePegeView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class DasturchiPageView(TemplateView):
    template_name = 'creator.html'

class KitoblarPageView(TemplateView):
    template_name = 'kitoblar.html'







