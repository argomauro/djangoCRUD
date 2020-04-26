from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import (View, TemplateView, ListView, DetailView,
                                    CreateView, UpdateView, DeleteView)
from django.http import HttpResponse
from . import models


class SchoolListView(ListView):
    model = models.School
    # school_list


class SchoolDetailView(DetailView):
    model = models.School
    template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('basic_app:listScuola')

'''
METTIAMO QUI IL CODICE DEL CRUD STUDENTE
'''
class StudentDetailView(DetailView):
    model = models.Student
    template_name = 'basic_app/student_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class StudentCreateView(CreateView):
    fields = ('name','age','school')
    model = models.Student

class StudentUpdateView(UpdateView):
    fields = ('name','age','school')
    model = models.Student

class StudentDeleteView(DeleteView):
    model = models.Student

    def get_success_url(self):
        school = self.object.school
        return reverse_lazy( 'basic_app:detailScuola', kwargs={'pk': school.pk})

'''
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION'
        return context
'''



#class CBView(View):
#    def get(self, request):
#        return HttpResponse('CLASS BASED VIEW')

# Create your views here.
def indexApp(request):
    return render(request,'basic_app/basic_app_index.html')
def indexHome(request):
    return render(request,'index.html')
