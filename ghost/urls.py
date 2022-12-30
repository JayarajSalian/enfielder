from django.urls import path
from ghost.views import *
app_name='Something1'

urlpatterns=[
    # path=('jinja_print/', jinja_print,name='jinja_print'),
    path('jinja_print/',jinja_print,name='jinja_print')
]