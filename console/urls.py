from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.home, name='home'),
    path('dashboard/', views.home, name='dashboard'),  
    path('academics/internals/', views.internals, name='internals'),
    path('academics/semesters/', views.semesters, name='semesters'),
    path('academics/assigned_class/', views.assigned_class, name='assigned_class'),
    path('academics/assigned_sem/', views.assigned_sem, name='assigned_sem'),
    path('jobs/assign_int/', views.assign_int, name='assign_int'),
    path('jobs/assign_sem/', views.assign_sem, name='assign_sem'),
    path('jobs/add_subject/', views.add_subject, name='add_subject'),
    path('jobs/edit_grades/<pk>/', views.edit_grade_view, name='edit_grade_form'),
    path('jobs/edit_sub/', views.edit_sub, name='edit_sub'),
    path('jobs/edit_sub/<pk>/', views.edit_sub_view, name='edit_sub_form'),
    path('jobs/add_grade/', views.add_grade, name='add_grade'),
    path('jobs/edit_grades/', views.edit_grade, name='edit_grades'),
    path('jobs/delete_grade/', views.delete_grade, name='delete_grade'),
    path('jobs/delete_grade/<pk>/', views.delete_grade_view, name='delete_grade_form'),
    path('jobs/delete_sub/', views.delete_sub, name='delete_sub'),
    path('jobs/delete_sub/<pk>/', views.delete_sub_view, name='delete_sub_form'),
    path('profile/', views.profile, name='profile'),
    path('departments/',views.get_departments,name='get-departments'),
    path('staffs/',views.get_teachers)
]