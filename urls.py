from django.urls import path
from . import views

urlpatterns = [

    path('',views.patient_list,name="patients"),

    path('patient/<uuid:patient_id>/',views.patient_trials,name="patient_trials"),

]
