from django.conf.urls import url
from .views import  EducationList
urlpatterns = [

    url(r'^get-education', view=EducationList.as_view(), name='get_education'),

]