from django.shortcuts import render
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView,
                                  FormView)
from django.views import View
from .models import Category, Video
import pdb
# Create your views here.


class IndexView(View):

	def get(self,  *args, **kwargs):
		context={}
		context['politic_videos']=Video.objects.filter(category__name__icontains='polit')[:4]
		context['lifestyle_videos']=Video.objects.filter(category__name__icontains='lifest')
		context['entertainment_videos']=Video.objects.filter(category__name__icontains='entertain')
		context['latest_videos']=Video.objects.all().order_by('created_date')
		context['feature']=Video.objects.filter(feature=True)[:2]
		return render(self.request, 'main/index.html', context)


class CatView(DetailView):
	model=Category
	template_name='main/category_page.html'

	def get_context_data(self, **kwargs):
		context = super(CatView, self).get_context_data(**kwargs)
		category=self.get_object()
		context['videos']=category.video_set.all().order_by('-created_date')
		
		return context






