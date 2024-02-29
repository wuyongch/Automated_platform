from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
# from Autotest_platform import settings
from django.conf import settings
# 设置环境变量

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Automated_platform.settings')

# 注册Celery的APP
app = Celery('Automated_platform')
# app = Celery('Automated_platform', backend='redis://localhost:6379/1', broker='redis://localhost:6379/0')
# 绑定配置文件
app.config_from_object('django.conf:settings')

# 自动发现各个app下的tasks.py文件
app.autodiscover_tasks(['Product'], force=True)

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)



