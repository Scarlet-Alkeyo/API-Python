
from django.urls import path
from .views import StudentListView, TeacherListView, CourseListView, ClassesListView, ClassPeriodListView

urlpatterns = [
    path('students/', StudentListView.as_view(), name='student-list'),
    path('teachers/', TeacherListView.as_view(), name='teacher-list'),
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('classes/', ClassesListView.as_view(), name='classes-list'),
    path('class-periods/', ClassPeriodListView.as_view(), name='class-period-list'),
]










