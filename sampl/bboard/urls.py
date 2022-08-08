from django.urls import path

from .views import *

urlpatterns = [
    # path('add/save/', add_save, name='add_save'),
    # path('add/', add, name='add'),
    # path('add/', add_and_save, name='add'),
    # path('add/', BbCreateView.as_view(), name='add'),
    # path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('<int:rubric_id>/', BbByRubricView.as_view(), name='by_rubric'),
    path('', index, name='index'),
    # Неполучается отобразить 205 стр
    # path('detail/<int:pk>/', BbDetailView.as_view(), name='detail'),
    path('add/', BbAddViews.as_view(), name='add'),
    # Неполучается отобразить 214 стр
    path('bb_form/<int:pk>/', BbEditView.as_view(), name='bb_form'),
]