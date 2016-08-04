# -*- encoding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .models import Post
from .forms import PostForm, CommentForm
from django.contrib import messages
from django.utils.text import slugify

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator




class ListView(View):
	def get(self, request):
		template_name = 'posts/lista.html'
		posts = Post.objects.all()
		context = {'posts':posts}
		return render(request,template_name,context)

class DetailView(View):
	def get(self,request,slug):
		template_name = 'posts/detalle.html'
		# post = Post.objects.get(slug=slug)
		post = get_object_or_404(Post,slug=slug)
		comment_form = CommentForm()
		context = {
		'post':post,
		'comment_form':comment_form,
		}
		return render(request,template_name,context)

class FormView(View):
	@method_decorator(login_required)
	def get(self,request):
		template_name = 'posts/formulario.html'
		form = PostForm()
		context = {'form':form}
		return render(request,template_name,context)

	def post(self,request):
		form = PostForm(request.POST,request.FILES)
		if form.is_valid():
			nuevo_post = form.save(commit=False)
			nuevo_post.slug = slugify(nuevo_post.titulo)
			nuevo_post.autor = request.user
			nuevo_post.save()
			messages.success(request,'Tu post se ha guardado con éxito! ')
			return redirect('posts:lista')
		else:
			messages.error(request,'No se guardo')
			return redirect('posts:nuevo')






