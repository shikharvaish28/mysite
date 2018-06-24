# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
from .models import PostModel

def post_model_detail_view(request, id=None):
    obj = PostModel.objects.get(id=id)
    template="blog/detail_view.html"
    host = request.build_absolute_uri()
    print ("this "+host)
    context = {
    "object": obj,
    "host"  : host
    }
    return render(request , template, context)

def post_model_list_view(request):
    qs = PostModel.objects.all() #query set
    recent_post = PostModel.objects.all().order_by('-timestamp')
    page = request.GET.get('page' , 1)
    paginator = Paginator(qs, 4)
    try:
        qs = paginator.page(page)
    except PageNotAnInteger:
        qs = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)



    recent_page = request.GET.get('recent_page' , 1)
    recent_paginator = Paginator(recent_post, 4)
    try:
        recent_post = recent_paginator.page(page)
    except PageNotAnInteger:
        recent_post = recent_paginator.page(1)
    except EmptyPage:
        users = recent_paginator.page(recent_paginator.num_pages)

    template_path="blog/list_view.html"
    context = {
    "object_list": qs,
    "recent_post_list" : recent_post
    }
    return render(request , template_path , context)
