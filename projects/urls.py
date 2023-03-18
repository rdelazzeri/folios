from django.urls import path

from . import views as v

app_name = 'projects'

urlpatterns = [
    path('', v.cover, name = 'cover'),

]