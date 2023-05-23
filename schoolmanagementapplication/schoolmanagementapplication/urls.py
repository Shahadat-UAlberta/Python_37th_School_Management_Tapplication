
from django.urls import path

from schools import views

urlpatterns = [
    path("add", views.add),
    path("list/", views.list),
    path("edit/<int:id>", views.edit),
    path("update/<int:id>",views.update),
    path("delete/<int:id>", views.delete),

]
