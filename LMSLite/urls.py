"""LMSLite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from django.conf.urls import include

from courses import views as courseView
from accounts import views as accountView
from LMSLite import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    path('auth/', include('django.contrib.auth.urls')),
    path('profile/', accountView.profile_view, name='profile'),
    path('courses/<int:id>/', courseView.course_view, name='course_page'),
    path('courses/<int:cid>/quizzes/',courseView.quiz_list_view, name='quiz_list'),
    path('courses/<int:cid>/quizzes/<int:id>/start/', courseView.quiz_view, name='quiz_page'),
    path('courses/<int:cid>/surveys/<int:id>/start/', courseView.take_survey_view, name='survey_page'),
    path('courses/<int:cid>/quizzes/<int:id>/', courseView.pre_quiz_view, name='quiz_start'),
    path('courses/<int:cid>/surveys/<int:id>/', courseView.pre_survey_view, name='pre_survey'),
    path('courses/<int:cid>/surveys/',courseView.survey_list_view, name='survey_list'),
    path('courses/Assignments/files/<int:id>/', views.download, name='download'),
    path('courses/<int:id>/Homework/', courseView.homework_view, name='homework_list'),
    path('courses/<int:cid>/Homework/<int:id>/', courseView.homework_submit_view, name='submit_assign'),
    path('courses/<int:cid>/grades/', courseView.grade_view, name='assignment_list'),
    path('courses/<int:cid>/grades/<int:id>/submission', courseView.submission_view, name='submission_view'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)