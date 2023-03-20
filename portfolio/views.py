from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from .models import Folio, Picture, Link

class WelcomeView(TemplateView):
  template_name = 'portfolio/welcome.html'

class PortfolioView(ListView):
  model = Folio
  template_name = 'portfolio/portfolio.html'

class FolioView(DetailView):
  model = Folio
  template_name = 'portfolio/folio.html'


@login_required
def folio_new(request):
  username = request.user.username
  return HttpResponse(username)

