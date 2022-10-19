import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from .models import User, Post
from django.views.generic import ListView
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

def show_post(request):
    return render(
        request,
        'post/index.html'
    )

class PostList(ListView):
    model = Post

def show_post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(
        request,
        'post/post_detail.html',
        {
            'post':post,
        }
    )


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, user_name=username, password=password)
        # print(username,password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return redirect('/'), {'error': 'username or password is incorrect'}
    else:
        return render(request, 'post/login.html')


@csrf_exempt
def register(request):
    data = request.POST
    template_name = "login.html"
    if User.objects.filter(id=data.get('username')).exists():
        context = {
            "result": "이미 존재하는 아이디입니다."
        }
        return redirect('post/register.html')
    elif data.get('password1') != data.get('password2') :
        context = {
            "result": "비밀번호가 다릅니다."
        }
    else:
        User.objects.create(
            username=data.get('username'),
            password=data.get('password1'),
        )
        context = {
            "result": "회원가입 성공"
        }
        return redirect('post/index.html')


@csrf_exempt
def loginCheck(request):
    template_name = 'login.html'
    request.session['loginOk'] = False
    inputId == ''
    inputPassword == ''
    
    try:
        data = request.POST
        inputId = data['username']
        inputPassword = data['password']

    except (KeyError):
        context = {
            "uid": "empty",
            "upass": "empty",
        }
        return render(request, template_name, context)
    else:
        if User.objects.filter(username=inputId).exists():
            getUser = User.objects.get(username=inputId)
            if getUser.password == inputPassword:
                request.session['loginOk'] = True
                context = {
                    "result": "로그인 성공"
                }
            else:
                request.session['loginOk'] = False
                context = {
                    "result": "비밀번호가 틀렸습니다"
                }
        else:
            request.session['loginOk'] = False
            context = {
                "result": "존재하지 않는 id입니다"
            }
        return HttpResponse(json.dumps(context), content_type="application/json")

# pip install djangorestframework
class Uploadfile(APIView):
    # @csrf_exempt
    def get(self,request):
        post=Post.objects.all()
        return render(request,"post/upload.html",context=dict(post=post)) 
    @csrf_exempt
    def post(self,request):
        title=request.data.get('title')
        content=request.data.get('content')
        user_id=request.data.get('user_id')
        file_org=request.FILES.getlist('file_org')
        # 닉네임에 따른 이미지
        post=Post()
        post.title=title
        post.content=content
        # post.save()
        for images in file_org:
            # post.author=nickname
            post.head_image=images
            post.save()
        # post.head_image=file_org
        # post.save()


        # print(user_id)
        return Response(status=200)

