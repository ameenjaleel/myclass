from django.shortcuts import render,get_object_or_404
from django.shortcuts import render
from .models import Classroom,Student
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
#form accounts.views import
#from django.contrib.auth.models import User
from django.db.models import Q
# Create your views here.

@login_required
def index(request):
    classrooms = Classroom.objects.filter(user=request.user.id)
    student_results = Student.objects.all()
    query = request.GET.get("q")
    if query:
        classrooms = classrooms.filter(
            Q(classroom_title__icontains=query)
        ).distinct()
        student_results = student_results.filter(
            Q(student_name__icontains=query)
        ).distinct()
        return render(request, 'home/index.html', {
            'classrooms': classrooms,
            #'students': student_results
        })
    else:
        return render(request,'home/index.html',{'classrooms':classrooms})

@login_required
def myclass(request,classroom_id):
        #user = request.user
        classroom = Classroom.objects.get(id=classroom_id)
        students = Student.objects.filter(classroom_id=classroom_id)
        #student_list = Student.objects.all()
        query = request.GET.get("q")
        if query:
            student_results = student_results.filter(
                Q(student_name__icontains=query)
            ).distinct()
        return render(request, 'home/myclass.html',{'students':students,'classroom':classroom})

@login_required
def classroom_create(request):
    data = dict()
    if request.method == 'POST':
        #jsondata = JSONParser().parse(request)
        #classroom_title = jsondata.get('classroom_title', None)
        classroom_title = request.POST.get('classroom_title')
        print classroom_title
        user1=request.user.id
        user = User(user1)
        classroom = Classroom.objects.create(user=user,classroom_title=classroom_title)
        data['form_is_valid'] = True
    else:
            data['form_is_valid'] = False

    data['html_form'] = render_to_string('home/partial_classroom_create.html',
            request=request
    )
    return JsonResponse(data)

def create_student(request, pk):
        data = dict()
        classroom = get_object_or_404(Classroom, pk=pk)
        classroom_id=pk
        print "GET request"
        if request.method == 'POST':
            print "POST request"
            student_name = request.POST.get('student_name')
            mark = request.POST.get('mark')
            student = Student.objects.create(classroom_id=classroom_id,student_name=student_name,mark=mark)
            data['form_is_valid'] = True
            students = Student.objects.filter(classroom_id=pk)
            data['html_student_list'] = render_to_string('home/partial_student_list.html',{"students":students})
        else:
            print "form request"
            data['form_is_valid'] = False
            context={"classroom":classroom}
            data['html_form'] = render_to_string('home/partial_student_create.html',
                context,
                request=request
        )
        return JsonResponse(data)

def delete_classroom(request, pk):
    classroom = get_object_or_404(Classroom,pk=pk)
    students= Student.objects.filter(classroom_id=pk)
    print classroom.id
    data=dict()
    if request.method =='POST':
        print"POST delete"
        classroom.delete()
        data['form_is_valid'] = True
    else:
        context = {'classroom': classroom}
        data['html_form'] = render_to_string('home/partial_delete_classroom.html',
            context,
            request=request,
        )
    return JsonResponse(data)

def delete_student(request, pk):
    students = get_object_or_404(Student, pk=pk)
    data=dict()
    print students.student_name

    if request.method =='POST':
        print"DEL STUDENT POST"
        students.delete()
        data['form_is_valid']= True
        #data['html_student_list'] = render_to_string('home/partial_student_list.html',{"student_list":student_list})
        #classrooms = Classroom.objects.filter(user=request.user)
        #return render(request, 'mysite/index.html', {'classrooms': classrooms})
    else:
        print "STUDENT DEL GET REQuest"
        context = {'students': students}
        data['html_form'] = render_to_string('home/partial_delete_student.html',
            context,
            request=request,
        )
    return JsonResponse(data)
