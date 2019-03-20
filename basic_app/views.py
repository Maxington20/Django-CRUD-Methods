from django.shortcuts import render, reverse
from django.views.generic import (View, TemplateView, 
                                ListView, DetailView,
                                CreateView, UpdateView,
                                DeleteView)
from django.http import HttpResponse
from basic_app import models
from django.urls import reverse_lazy

# Create your views here.
# def index(request):
#     return render(request,'index.html')

# basic class based view
# class CBView(View):
#     def get(self,request):
#         return HttpResponse("Class based views are cool")

class IndexView(TemplateView):
    template_name = 'index.html' # 'app_name/index.html' if there was a template subdirectory

    # *args: arguments can pass in multiple
    # **kwargs: key word arguments, gives you dictionaries 
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'Basic Injection'
        return context

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    # school_list

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
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

    success_url = reverse_lazy("basic_app:list")