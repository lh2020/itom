from django.shortcuts import render, redirect, HttpResponse
from containerManage.models import *


# Create your views here.
def index(request):
    all_container_list = Container.objects.all()
    all_host_list = Host.objects.all()
    all_user_list = User.objects.all()

    # host_name=Host.objects.filter(id=Container.host_id)
    # if request.method == 'POST':
    #     name = request.POST.get('name')
    #     image = request.POST.get('image')
    #     host = request.POST.get('hostname')
    #     tag = request.POST.get('tag')
    #     host=request.POST.get('host')
    #     # Container.objects.create(name=name, image=image, , tag=tag, )
    #     return redirect('/index/')
    return render(request, 'index.html', locals())


def add(request):
    # Container.objects.create(name='lzyy-bt', image='lzyy-bt', status='running', tag='lzyy', host_id=3)
    return HttpResponse('ok')


def delete(request):
    pass


def edit(request):
    pass


def query(request):
    pass
