from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.utils import timezone
from .models import Internal, Semester, SubjectAssign, SemAssign, Subject, Grade, Department
from django.forms import modelformset_factory
from .forms import SubjectAssignForm, SemAssignForm, SubjectForm, GradeForm
from django.contrib import messages
import json
from django.views.decorators.csrf import csrf_exempt


def home(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return render(request, 'console/su-dashboard.html')
        elif request.user.is_staff:
            return render(request, 'console/dashboard.html')
        else:
            return render(request, 'student/dashboard.html')

    else:
        return render(request, 'console/home.html')


def assign_int(request):
    if request.user.is_staff:
        form = SubjectAssignForm(request.POST)
        if request.method == "GET":
            dept = request.GET.get('department')
            sem = request.GET.get('subject')
            form.fields['staff'].queryset = User.objects.filter(
                is_staff=True, profile__Department=dept)
            form.fields['subject'].queryset = Subject.objects.filter(sem=sem)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect('assign_int')
        return render(request, 'console/jobs/assign_int.html', {'form': form})
    else:
        return redirect('dashboard')


def assigned_class(request):
    if request.user.is_staff:
        context = {
            'classes': SubjectAssign.objects.filter(staff__username=request.user.username)
        }
        return render(request, 'console/academics/assigned_class.html', context)
    else:
        return redirect('internals')


def internals(request):
    if request.user.is_staff:
        formset = modelformset_factory(Internal, fields=(
            'student', 'marks1', 'marks2', 'marks3'), extra=0)
        search = request.GET.get('subject-query')
        if request.method == "POST":
            forms = formset(request.POST)
            if forms.is_valid():
                forms.save()
                return redirect('assigned_class')
        forms = formset(
            queryset=(Internal.objects.filter(subject__subcode=search)))
        return render(request, 'console/academics/internals.html', {'forms': forms})
    else:
        context = {
            'internals1': Internal.objects.filter(student__username=request.user.username).filter(subject__sem=1),
            'internals2': Internal.objects.filter(student__username=request.user.username).filter(subject__sem=2),
            'internals3': Internal.objects.filter(student__username=request.user.username).filter(subject__sem=3),
            'internals4': Internal.objects.filter(student__username=request.user.username).filter(subject__sem=4),
            'internals5': Internal.objects.filter(student__username=request.user.username).filter(subject__sem=5),
            'internals6': Internal.objects.filter(student__username=request.user.username).filter(subject__sem=6),
            'internals7': Internal.objects.filter(student__username=request.user.username).filter(subject__sem=7),
            'internals8': Internal.objects.filter(student__username=request.user.username).filter(subject__sem=8),
        }
        return render(request, 'student/academics/internals.html', context)


def assign_sem(request):
    if request.user.is_staff:
        form = SemAssignForm(request.POST)
        if request.method == "GET":
            dept = request.GET.get('department')
            sem = request.GET.get('subject')
            form.fields['staff'].queryset = User.objects.filter(
                is_staff=True, profile__Department=dept)
            form.fields['semester'].queryset = Subject.objects.filter(sem=sem)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect('assign_sem')
        return render(request, 'console/jobs/assign_sem.html', {'form': form})
    else:
        return redirect('dashboard')


def assigned_sem(request):
    if request.user.is_staff:
        context = {
            'classes': SemAssign.objects.filter(staff__username=request.user.username)
        }
        return render(request, 'console/academics/assigned_sem.html', context)
    else:
        return redirect('semesters')


def semesters(request):
    if request.user.is_staff:
        formset = modelformset_factory(Semester, fields=(
            'student', 'subject', 'grade', 'result'), extra=0)
        search = request.GET.get('subject-query')
        if request.method == "POST":
            forms = formset(request.POST)
            if forms.is_valid():
                forms.save()
                return redirect('assigned_sem')
        forms = formset(
            queryset=(Semester.objects.filter(subject__subcode=search)))
        return render(request, 'console/academics/semesters.html', {'forms': forms})
    else:
        context = {
            'semesters1': Semester.objects.filter(student__username=request.user.username).filter(subject__sem=1),
            'semesters2': Semester.objects.filter(student__username=request.user.username).filter(subject__sem=2),
            'semesters3': Semester.objects.filter(student__username=request.user.username).filter(subject__sem=3),
            'semesters4': Semester.objects.filter(student__username=request.user.username).filter(subject__sem=4),
            'semesters5': Semester.objects.filter(student__username=request.user.username).filter(subject__sem=5),
            'semesters6': Semester.objects.filter(student__username=request.user.username).filter(subject__sem=6),
            'semesters7': Semester.objects.filter(student__username=request.user.username).filter(subject__sem=7),
            'semesters8': Semester.objects.filter(student__username=request.user.username).filter(subject__sem=8),
        }
        return render(request, 'student/academics/semesters.html', context)


def profile(request):
    if request.user.is_staff:
        return render(request, 'console/profile.html',)
    else:
        return render(request, 'student/profile.html',)


class Login(View):
    template_name = "console/home.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        try:
            user = User.objects.get(email=request.POST.get('email'))
        except:
            return render(request, self.template_name, {'error': True})
        else:
            user = authenticate(request, username=user.username,
                                password=request.POST.get('password'))
            if user is None:
                return render(request, self.template_name, {'error': True})
            login(request, user)
            response = redirect('dashboard')
            response.set_cookie('role', 'user')
            return response
        return render(request, self.template_name)


class LogoutView(View, LoginRequiredMixin):
    def get(self, request):
        logout(request)
        response = redirect('home')
        response.delete_cookie('role')
        return response


def add_subject(request):
    if request.user.is_staff:
        form = SubjectForm(request.POST)
        if form.is_valid():
            Subject = form.save()
            return redirect('add_subject')
        return render(request, 'console/jobs/add_subject.html', {'form': form})
    else:
        return redirect('dashboard')


def edit_sub(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            context = {
                'subjects': Subject.objects.all()
            }
            return render(request, 'console/jobs/edit_sub.html', context)
        else:
            return redirect('dashboard')


def edit_sub_view(request, pk):
    if request.user.is_staff:
        obj = get_object_or_404(Subject, id=pk)
        form = SubjectForm(request.POST or None, instance=obj)
        context = {'form': form}
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context = {'form': form}
            return redirect('edit_sub_form')
        return render(request, 'console/jobs/edit_sub_form.html', context)
    else:
        return redirect('edit_sub')


def delete_sub(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            context = {
                'subjects': Subject.objects.all()
            }
            return render(request, 'console/jobs/delete_sub.html', context)
        else:
            return redirect('dashboard')


def delete_sub_view(request, pk):
    if request.user.is_authenticated:
        if request.user.is_staff:
            obj = Subject.objects.filter(id=pk)
            obj.delete()
            return redirect('delete_sub')
        return redirect('dashboard')


def add_grade(request):
    if request.user.is_staff:
        form = GradeForm(request.POST)
        if form.is_valid():
            Grade = form.save()
            return redirect('add_grade')
        return render(request, 'console/jobs/add_grade.html', {'form': form})
    else:
        return redirect('dashboard')


def edit_grade(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            context = {
                'grades': Grade.objects.all()
            }
            return render(request, 'console/jobs/edit_grade.html', context)
        else:
            return redirect('dashboard')


def edit_grade_view(request, pk):
    if request.user.is_staff:
        obj = get_object_or_404(Grade, id=pk)
        form = GradeForm(request.POST or None, instance=obj)
        context = {'form': form}
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context = {'form': form}
            return redirect('edit_grade_form')
        return render(request, 'console/jobs/edit_grade_form.html', context)
    else:
        return redirect('edit_grade')


def delete_grade(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            context = {
                'grades': Grade.objects.all()
            }
            return render(request, 'console/jobs/delete_grade.html', context)
        else:
            return redirect('dashboard')


def delete_grade_view(request, pk):
    if request.user.is_authenticated:
        if request.user.is_staff:
            obj = Grade.objects.filter(id=pk)
            obj.delete()
            return redirect('delete_grade')
        return redirect('dashboard')


def get_departments(request):
    if request.method == 'GET':
        dept = [dept.code for dept in Department.objects.all()]
        return JsonResponse(dept, safe=False)


@csrf_exempt
def get_teachers(request):
    print(request.body)
    dept = json.loads(request.body)['dept']
    sem = json.loads(request.body)['sem']
    staffs = [staff.username for staff in User.objects.filter(
        is_staff=True, profile__Department=dept)]
    subjects = [subject.subname for subject in Subject.objects.filter(sem=sem)]

    return JsonResponse({
        'staffs': staffs,
        'subjects': subjects
    })
