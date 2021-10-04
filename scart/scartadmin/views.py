from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, authenticate,logout as auth_logout
from django.contrib.auth.models import User
from shopping.forms import FormUser
# Create your views here.

def adminLoginview(request):
    if request.user.is_authenticated and request.session.has_key('admin'):
        return redirect('admin:home')
    if request.method  == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password = password)
        try:
            superuser = User.objects.get(username=username)
        except:
            pass
        if user is not None and superuser.is_superuser:
            print(user)       
            auth_login(request,user)
            request.session['admin'] = True
            return redirect('admin:home')
        else:
            messages.error(request, 'Invalid Username or Password')
            print('authentication fails')
            return redirect('admin:login')

    return render(request,'scartadmin/admin-login.html')
    
@login_required(login_url='login/')   
def adminHomeview(request):
    search = None
    try:
        search = request.GET['search']
    except:
        pass
    if search is not None:
        print(search)
        users = User.objects.all().filter(username__contains = search).order_by('id')
    else:
        users = User.objects.all().order_by('id')
    context = {'users' : users}
    if request.session.has_key('admin'):
        return render(request,'scartadmin/index.html',context)
    return redirect('admin:login')

@login_required(login_url='admin:login')
def detailView(request,user_id):
    if request.session.has_key('admin'):
        user_detail = User.objects.get(pk=user_id)
        print('detail view loaded')
        return render(request,'scartadmin/detail.html' ,{'user_detail':user_detail})
    return redirect('admin:login')


def userDetailUpdate(request,user_id):
    if request.session.has_key('admin'):
        if request.method == 'POST':
            for key, value in request.POST.items():
                # print('Key: %s' % (key) ) 
                print(f'Key: {key}')
                # print('Value %s' % (value) )
                print(f'Value: {value}')
            # print(request.POST.get('username'))
            selected_task = User.objects.get(id=user_id)
            form = FormUser(request.POST,instance=selected_task)
            print(form.is_valid())
            if form.is_valid():
                form.save()
                # selected_task.set_password(request.POST['password'])
                # selected_task.save()
                print('updated')
                
            return redirect('admin:detail',user_id)
        form = FormUser()
        user_detail = User.objects.get(pk=user_id)
        return render(request,'scartadmin/detail_edit.html',{'user_detail':user_detail})
    return redirect('admin:login')
def userDetaildelete(request, user_id):
    try:
        task = User.objects.get(id=user_id)
        task.delete()
    except:
        pass
    return redirect('admin:home') 

def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        if request.session.has_key('admin'):
            del request.session['admin']
        return redirect('admin:home')
    return redirect('admin:login')

# @method_decorator(login_required, name='dispatch')
# class adminHomeView(ListView):
#     template_name = 'scartadmin/index.html'
#     model = User

    
