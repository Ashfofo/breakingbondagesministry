from django.shortcuts import render
from .models import Video,Sermon,Deliverance
from django.core.paginator import Paginator


def video(request):
    videos_list = Video.objects.all()
    paginator = Paginator(videos_list,4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'videos': videos_list, #thi is the whole list so dont pass it as a whole it wll slow down thepage
        'page_obj':page_obj,
    }

    return render(request,'video.html',context=context)

def sermon_video(request):
    videos_list = Sermon.objects.all()
    paginator = Paginator(videos_list,4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'videos': videos_list, #thi is the whole list so dont pass it as a whole it wll slow down thepage
        'page_obj':page_obj,
    }

    return render(request,'sermon.html',context=context)

def deliverance_video(request):
    videos_list = Deliverance.objects.all()
    paginator = Paginator(videos_list,4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'videos': videos_list, #thi is the whole list so dont pass it as a whole it wll slow down thepage
        'page_obj':page_obj,
    }

    return render(request,'del.html',context=context)