from django.shortcuts import render
from rest_framework.views import APIView
from student.models import Student
from teacher.models import Teacher
from course.models import Course
from classroom.models import Classroom
from classperiod.models import ClassPeriod
from rest_framework.response import Response

from .serializer import StudentSerializer
from .serializer import TeacherSerializer
from .serializer import CourseSerializer
from .serializer import ClassPeriodSerializer  
from .serializer import ClassroomSerializer

class StudentListView(APIView):
    def get(self,request):
        students=Student.objects.all()
        serializer=StudentSerializer(students, many=True)
        return Response(serializer.data)

class TeacherListView(APIView):
    def get(self,request):
        teacher=Teacher.objects.all()
        serializer=TeacherSerializer(teacher, many=True)
        return Response(serializer.data)


class CourseListView(APIView):
    def get(self,request):
        courses=Course.objects.all()
        serializer=CourseSerializer(courses, many=True)
        return Response(serializer.data)

class ClassesListView(APIView):
    def get(self,request):
        classes=Classroom.objects.all()
        serializer=ClassroomSerializer(classes, many=True)
        return Response(serializer.data)
    
class ClassPeriodListView(APIView):
    def get(self,request):
        classPeriod=ClassPeriod.objects.all()
        serializer=ClassPeriodSerializer(classPeriod, many=True)
        return Response(serializer.data)

