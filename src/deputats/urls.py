from django.urls import include, path
from . import views

app_name = 'deputats'
urlpatterns = [
    path('surname/<str:surname>/', views.DeputatList.as_view()),
    path('', views.DeputatList.as_view(), name='deputat_list'),
    path('deputat/<int:id>/',
        views.DeputatRetrieveUpdateDestroy.as_view(),
        name='deputat_detail'),

]