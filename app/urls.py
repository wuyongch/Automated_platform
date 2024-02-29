from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("register/", views.register, name="register"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("project/", views.project, name="project"),
    path('project/<int:project_id>', views.project_config, name="project_config"),
    path('page/', views.page, name="page"),
    path('element/', views.element, name="element"),
    path('keyword/', views.keyword, name="keyword"),
    path('keyword/create', views.keyword_create, name="keyword_create"),
    path('keyword/edit/<int:keyword_id>', views.keyword_edit, name="keyword_edit"),
    path('testcase/', views.testcase, name="testcase"),
    path('testcase/create', views.testcase_create, name="testcase_create"),
    path('testcase/<int:testcase_id>', views.testcase_edit, name="testcase_edit"),
    path('result/', views.result, name="result"),
    path('result/<int:result_id>', views.result_see, name="result_see"),
    path('loginConfig', views.loginConfig, name="loginConfig"),
    path('loginConfig/create', views.loginConfig_create, name="loginConfig_create"),
    path('loginConfig/edit/<int:login_id>', views.loginConfig_edit, name="loginConfig_edit"),
    path('task/', views.task, name="task"),


]
