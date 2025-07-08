from django.urls import path
from .views import (HomePegeView,AboutPageView,
                    DasturchiPageView,KitoblarPageView)

urlpatterns=[
    path('',HomePegeView.as_view(),name='home'),
    path('about/',AboutPageView.as_view(),name='about'),
    path('dasturchi/',DasturchiPageView.as_view(),name='creator'),
    path('books/',KitoblarPageView.as_view(),name='kitob'),
]