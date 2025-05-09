from django.urls import path

from . import views as v

app_name = 'portfolio'

urlpatterns = [
    path('', v.WelcomeView.as_view(), name = 'welcome'),
    path('folios', v.PortfolioView.as_view(), name = 'portfolio'),
    path('folio/<slug:user>/<slug:slug>', v.FolioView.as_view(), name = 'folio'),
    path('folio/new', v.folio_new, name = 'folio_new'),

]