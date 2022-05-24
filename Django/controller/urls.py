from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('forward/',forward,name='forward'),
    path('back/',back,name='back'),
    path('left/',left,name='left'),
    path('right/',right,name='right'),
    path('stop/',stop,name='stop')

]