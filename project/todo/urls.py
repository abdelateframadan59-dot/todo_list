from django.urls import path
from . import views


urlpatterns=[

path('',views.index,name=''),


path('update/<str:pk>',views.Updatetask,name='update'),

path('delete/<str:pk>',views.deletetask,name='delete')
]


