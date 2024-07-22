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
    
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class StudentDetailView(APIView):
    def get(self,request,id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    def put(self,request,id):
        student = Student.objects.get(id = id)
        serializer = StudentSerializer(student, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        student = Student.objects.get(id = id)
        student.delete()
        return Response(status = status.HTTP_202_ACCEPTED)
    



class TeacherListView(APIView):
    def get(self,request):
        teacher=Teacher.objects.all()
        serializer=TeacherSerializer(teacher, many=True)
        return Response(serializer.data)
    def post(self , request):
        serializer = TeacherSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
        
class TeacherDetailView(APIView):
    def get(self, request, id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)
    
    def put(self, request, id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(classroom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CourseListView(APIView):
    def get(self,request):
        courses=Course.objects.all()
        serializer=CourseSerializer(courses, many=True)
        return Response(serializer.data)
    
    def post(self , request):
        serializer = CourseSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
        
class CourseDetailView(APIView):
    def get(self,request,id):
        course = Course.objects.get(id=id)
        serializer = CourseSerializer(student)
        return Response(serializer.data)
    
    def put(self,request,id):
        courses = Course.objects.get(id = id)
        serializer = CourseSerializer(courses, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
        course = Student.objects.get(id = id)
        course.delete()
        return Response(status = status.HTTP_202_ACCEPTED)
    

class ClassesListView(APIView):
    def get(self,request):
        classes=Classroom.objects.all()
        serializer=ClassroomSerializer(classes, many=True)
        return Response(serializer.data)
    
    def post(self , request):
        serializer = ClassroomSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
        
        
class ClassesDetailView(APIView):
    def get(self, request, id):
        classess = Classes.objects.get(id=id)
        serializer = ClassesSerializer(classperiod)
        return Response(serializer.data)
    def put(self, request, id):
        classroom = Classes.objects.get(id=id)
        serializer = ClassPeriodSerializer(classes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        classroom = Classes.objects.get(id=id)
        classperiod.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    

    
class ClassPeriodListView(APIView):
    def get(self,request):
        classPeriod=ClassPeriod.objects.all()
        serializer=ClassPeriodSerializer(classPeriod, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ClassPeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ClassPeriodDetailView(APIView):
    def get(self, request, id):
        classperiod = ClassPeriod.objects.get(id=id)
        serializer = ClassPeriodSerializer(classperiod)
        return Response(serializer.data)
    def put(self, request, id):
        classperiod = ClassPeriod.objects.get(id=id)
        serializer = ClassPeriodSerializer(classperiod, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        classperiod = ClassPeriod.objects.get(id=id)
        classperiod.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

