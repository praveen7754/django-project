from django.urls import path
from .views import * 

urlpatterns=[
    path("func/",func),
    # path("display/",display),
    # path("greet/",greet),
    # path("check/",ifelse),
    path("add/",add_data),
    path("view/",view_data),
    path("update/<int:id>/",update_date,name="up_date"),
    path("delete/<int:id>/",delete_data,name="del_data"),
    path("about/",about),
    path("base/",base),
    path("contact/",contact),
    path("service/",service),


]