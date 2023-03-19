from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Folio, Picture, Link

class WelcomeView(TemplateView):
  template_name = 'portfolio/welcome.html'

class PortfolioView(ListView):
  model = Folio
  template_name = 'portfolio/portfolio.html'

class FolioView(DetailView):
  model = Folio
  template_name = 'portfolio/folio.html'