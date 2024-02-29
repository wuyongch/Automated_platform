from django.urls import path

from Product import views

urlpatterns = [
    # project
    path("project/create", views.Project.create),
    path("project/delete/<int:project_id>", views.Project.delete),
    path("project/edit/<int:project_id>", views.Project.edit),
    path("project", views.Project.find),
    path("project/<int:project_id>", views.Project.get),

    # environment
    path('environment/create', views.Environment.create),
    path('environment/delete/<int:environment_id>', views.Environment.delete),
    path('environment/edit/<int:environment_id>', views.Environment.edit),
    path('environment', views.Environment.find),
    path('environment/<int:environment_id>', views.Environment.get),

    # page
    path('page/create', views.Page.create),
    path('page/delete/<int:page_id>', views.Page.delete),
    path('page/edit/<int:page_id>', views.Page.edit),
    path('page', views.Page.find),
    path('page/<int:page_id>', views.Page.get),

    # element
    path('element/create', views.Element.create),
    path('element/delete/<int:element_id>', views.Element.delete),
    path('element/edit/<int:element_id>', views.Element.edit),
    path('element', views.Element.find),
    path('element/<int:element_id>', views.Element.get),

    # keyword
    path('keyword/create', views.Keyword.create),
    path('keyword/delete/<int:keyword_id>', views.Keyword.delete),
    path('keyword/edit/<int:keyword_id>', views.Keyword.edit),
    path('keyword', views.Keyword.find),
    path('keyword/<int:keyword_id>', views.Keyword.get),

    # testcase
    path('testcase/create', views.TestCase.create),
    path('testcase/delete/<int:testcase_id>', views.TestCase.delete),
    path('testcase/edit/<int:testcase_id>', views.TestCase.edit),
    path('testcase', views.TestCase.find),
    path('testcase/<int:testcase_id>', views.TestCase.get),
    path('testcase/copy/<int:testcase_id>', views.TestCase.copy),

    path('testcase/running/<int:testcase_id>', views.TestCase.test),
    path('result', views.TestResult.find),
    path('result/delete/<int:result_id>', views.TestResult.delete),
    path('result/<int:result_id>', views.TestResult.get),
    path('browser', views.Public.data),
    path('projectSummary', views.Public.index),
    path('barChar', views.Public.bar_char),
    path('lineChar', views.Public.line_char),

    # Login
    path('login/create', views.Login.create),
    path('login/delete/<int:login_id>', views.Login.delete),
    path('login/edit/<int:login_id>', views.Login.edit),
    path('login', views.Login.find),
    path('login/<int:login_id>', views.Login.get),
    path('login/bind/<int:login_id>', views.Login.bind),
    path('login/unbind/<int:EnvironmentLogin_id>', views.Login.unbind),
    path('login/bind/edit/<int:EnvironmentLogin_id>', views.Login.edit_bind),


    # tasks
    path('task/create', views.TestTasks.create),
    path('task/delete/<int:task_id>', views.TestTasks.delete),
    path('task/edit/<int:task_id>', views.TestTasks.edit),
    path('task', views.TestTasks.find),
    path('task/<int:task_id>', views.TestTasks.get),
    path('task/running/<int:task_id>', views.TestTasks.test),
]
