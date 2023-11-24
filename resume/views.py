from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse



def base_view(request):
    return render(request, 'resume/index.html')


def blog_view(request):
    return render(request, 'resume/blog-single.html')
