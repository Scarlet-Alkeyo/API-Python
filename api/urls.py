
from django.urls import path
from .views import StudentListView, TeacherListView, CourseListView, ClassesListView, ClassPeriodListView
from django.contrib import admin
from .views import StudentDetailView
from .views import ClassPeriodDetailView
from .views import ClassesDetailView
from .views import TeacherDetailView
from .views import CourseDetailView

urlpatterns = [
    path('students/', StudentListView.as_view(), name='student-list'),
    path('teachers/', TeacherListView.as_view(), name='teacher-list'),
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('classes/', ClassesListView.as_view(), name='classes-list'),
    path('class-periods/', ClassPeriodListView.as_view(), name='class-period-list'),
    path("students/<int:id>/", StudentDetailView.as_view(), name = "student_detail_view"),
    path("classperiod/<int:id>/", ClassPeriodListView.as_view(), name = "class_period_list_view"),
    path("classroom/<int:id>/", ClassesDetailView.as_view(), name = "classroom_list_view"),
    path("teacher/<int:id>/", TeacherDetailView.as_view(), name = "teacher_list_view"),
    path("course/<int:id>/", CourseDetailView.as_view(), name = "course_list_view"),

]














