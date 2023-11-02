from django.urls import path
from . import views

urlpatterns=[
  path('myform/',views.myform_view,name='myform'),
  path('pulpito/',views.pulpito_view,name='pulpito'),
  path('get_response/',views.get_response_from_flask, name='get_response'),
  path('get_response2/',views.get_response_from_flask2, name='get_response')
  
]