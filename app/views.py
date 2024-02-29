from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache


# Create your views here.

def login(request):
    if request.POST:
        username = password = ''
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)  # 认证给出的用户名和密码
        if user is not None and user.is_active:  # 判断用户名和密码是否有效
            auth.login(request, user)
            request.session['user'] = username  # 跨请求的保持user参数
            response = HttpResponseRedirect('/app/index/#//app/dashboard/')
            return response
        else:
            messages.add_message(request, messages.WARNING, '账户或者密码错误，请检查')
            return render(request, 'page/login.html')

    return render(request, 'page/login.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # 检查用户名是否已存在
            username = form.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                form.add_error('username', '用户名已存在')
                return render(request, 'page/register.html', {'form': form})

            # 检查密码是否一致
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password1 != password2:
                form.add_error('password2', '两次密码不一致,请检查')
                return render(request, 'page/register.html', {'form': form})

            form.save()
            return redirect('/app/login/')  # 注册成功后重定向到登录页面
    else:
        form = UserCreationForm()
    return render(request, 'page/register.html', {'form': form})


@login_required
def logout(request):
    auth.logout(request)
    return render(request, 'page/login.html')


@login_required
def index(request):
    return render(request, 'page/index.html')


@login_required
def dashboard(request):
    return render(request, 'page/dashboard.html')


@login_required
def project(request):
    return render(request, 'page/project.html')


@login_required
def project_config(request, project_id):
    from Product.models import Project
    from Automated_platform.helper.util import get_model
    p = get_model(Project, id=project_id)
    name = p.name if p else ""
    return render(request, "page/project_config.html", {"projectId": project_id, "projectName": name})


@login_required
def page(request):
    return render(request, "page/page.html")


@login_required
def element(request):
    return render(request, "page/page_element.html")


@login_required
def keyword(request):
    return render(request, "page/keyword.html")


@login_required
def keyword_create(request):
    return render(request, "page/keyword_create.html")


@login_required
def keyword_edit(request, keyword_id):
    from Product.models import Keyword, Project
    from Automated_platform.helper.util import get_model
    kw = get_model(Keyword, id=keyword_id)
    projectId = kw.projectId if kw else 0
    p = get_model(Project, id=projectId)
    projectName = p.name if projectId > 0 and p else "通用"
    keywordName = kw.name if kw else ""
    return render(request, "page/keyword_edit.html",
                  {"id": projectId, "projectName": projectName, "keywordId": keyword_id, "keywordName": keywordName})


@login_required
def testcase(request):
    return render(request, "page/testcase.html")


@login_required
def testcase_create(request):
    return render(request, "page/testcase_create.html")


@login_required
def testcase_edit(request, testcase_id):
    return render(request, "page/testcase_edit.html", {"testcaseId": testcase_id})


@login_required
def result(request):
    return render(request, "page/test_result.html")


@login_required
def result_see(request, result_id):
    return render(request, "page/test_report.html", {"id": result_id})


@login_required
def loginConfig(request):
    return render(request, "page/login_config.html")


@login_required
def loginConfig_create(request):
    return render(request, "page/login_config_create.html")


@login_required
def loginConfig_edit(request, login_id):
    return render(request, "page/login_config_edit.html", {"id": login_id})


@login_required
def task(request):
    return render(request, "page/task.html")
