from django.urls import path
from .views import persons_list
from .views import persons_new
from .views import persons_update
from .views import persons_delete

from .views import PersonList, PersonDetail


urlpatterns = [
    path('list/', persons_list, name="person_list"),
    path('new/', persons_new, name="person_new"),
    path('update/<int:id>/', persons_update, name="persons_update"),
    path('delete/<int:id>/', persons_delete, name="persons_delete"),

    path('person/', PersonList.as_view()),
    path('person_detail/<int:pk>', PersonDetail.as_view(), name='url_person_detail'),
]