from django.urls import path

from . import views
urlpatterns = [
     path('',views.index.as_view(),name='prediction'),
     path('modelinfo/',views.modelinfo.as_view(),name='modelinfo')
]
