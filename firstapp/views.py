from django.shortcuts import render, redirect
from fastai.vision import *
from pathlib import Path
from django.conf import settings
import os
from .forms import PostForm
from .models import Post



defaults.device = torch.device('cpu')
#pkl_path = Path("C:\\Users\\KIMSUI\Documents\\17_ai_project\\export-model-3")
pkl_path = os.path.join(settings.MEDIA_ROOT, "pkl")
learn = load_learner(pkl_path)

def classify(filename):
    #img_trash_file = Path("C:\\Users\\KIMSUI\Documents\\10_IITP-AI-Challenge\\nara\\train\\1000\\26536211_1.jpg")
    img_trash_file = os.path.join(settings.MEDIA_ROOT,'train',filename)
    print('----------------------')
    print(img_trash_file)
    print('----------------------')

    img_trash = open_image(img_trash_file)
    pred_class,pred_idx,outputs = learn.predict(img_trash)

    return pred_class.obj

# Create your views here.
def index(request):
    context = {
        'posts' : 'test'
    }
    return render(request, 'firstapp/index.html', context)

def upload(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            # post.image.url -> /media/26536209_1.jpg
            # url = post.image.url
            post.save()
            
            print('----------------------')
            print(post.image.url.split("/")[3])
            print('----------------------')
            
            result_list = classify(post.image.url.split("/")[3])
            
            trash_class = ['일반쓰레기', '종이', '캔류', '유리병', '플라스틱', '비닐', '스티로폼', '음식물']

            for n, i in enumerate(result_list):
                result_list[n] = trash_class[int(i)-1]

            result_str = ''
            for data in result_list:
                result_str = result_str + '#' + data + ' '

            context = {
                'result' : result_str,
                'result_list' : result_list,
                'url' : post.image.url
            }
            
            return render(request, 'firstapp/classify.html', context)
    else:
        form = PostForm()
    context = {
        'form' : form
    }
    return render(request, 'firstapp/form.html', context)

# def save_class(request, result_list):

