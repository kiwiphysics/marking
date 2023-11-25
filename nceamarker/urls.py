"""
URL configuration for nceamarker project.

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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from marking import views as marking_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', marking_views.mark_menu, name='mark_menu'),
    path('start', marking_views.enter_school_id, name='enter_school_id'),
    path('login_user',marking_views.login_user, name='login_user'),
    path('logout', marking_views.logout_user, name='logout_user'),
    path('q<current_question>', marking_views.mark_current_question, name='mark_current_question'),
    path('total_marks', marking_views.total_marks, name='total_marks'),
    path('review_marks_<sort_type>_<the_marker>', marking_views.review_marks, name='review_marks'),
    path('confirm_void', marking_views.confirm_void, name='confirm_void'),
    path('edit_menu_<paper_id>', marking_views.edit_menu, name='edit_menu'),
    path('confirm_void_<paper_id>', marking_views.confirm_void_menu, name='confirm_void_menu'),
    path('confirm_delete_<paper_id>', marking_views.confirm_delete, name='confirm_delete'),
    path('edit_paper_<paper_id>_<question_number>', marking_views.edit_paper, name='edit_paper'),
    path('super_review_menu', marking_views.super_review_menu, name='super_review_menu'),
    path('statistics', marking_views.statistics, name='statistics'),
    path('change_cutscores', marking_views.change_cutscores, name='change_cutscores'),
    path('check_marking', marking_views.check_marking, name='check_marking'),
    path('review_check_marks', marking_views.review_check_marks, name='review_check_marks'),
    path('test_page', marking_views.test_page, name='test_page'),
]
