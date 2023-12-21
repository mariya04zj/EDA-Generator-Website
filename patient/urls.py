"""
URL configuration for patient project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from patient import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',                     views.home_page,      name='webpage1'),
    path('survey-questions/', views.survey_ques, name='webpage2'),
    path('analysis-procedure/', views.analysis_procedure, name='webpage3'),
    path('login/',           views.start_process, name='webpage4'),
    path('login/post-login/', views.post_login,      name='webpage5'),
    path('login/post-login/enter-csv/', views.enter_csv,      name='webpage6'),
    path('login/post-login/enter-csv/view-report/', views.view_report , name='webpage7')
]

