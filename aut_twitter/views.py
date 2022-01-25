from django.shortcuts import render, redirect
from django.contrib.auth.models import User
#from django.contrib.auth import login, authenticate, logout
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
<<<<<<< HEAD
from .models import login_table
=======
>>>>>>> b28e892e132bbf547a3bf56658d604d1bd197493
from django.views.decorators.csrf import csrf_exempt,csrf_protect #Add this

#user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

# At this point, user is a User object that has already been saved
# to the database. You can continue to change its attributes
# if you want to change other fields.
#user.last_name = 'Lennon'
#user.save()

"""class UserViewSet(viewsets.ModelViewSet):
    
    #API endpoint that allows users to be viewed or edited.
    
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    
    API endpoint that allows groups to be viewed or edited.
    
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
"""
@csrf_exempt
def show(request):
    return render(request, 'base.html', {'error': 'salap'})

def signup(request):
    if request.method == "POST":
        if (request.POST['pass'] == request.POST['repeat-pass']) and (request.POST['pass'] != ''):
            try:
                User.objects.get(username = request.POST['username'])
                return render (request,'sign-up.html', {'error':'Username is already taken!'})
            except User.DoesNotExist:
<<<<<<< HEAD
                username_to_sign=request.POST['username']
                user = User.objects.create_user(username_to_sign, password=request.POST['pass'])
                user.first_name = request.POST['name']
                user.email = request.POST['email']
                user.save()
                #insert logged in user into login_table
                userlogged = login_table(username=username_to_sign)
                userlogged.save()
=======
                user = User.objects.create_user(request.POST['username'], password=request.POST['pass'])
                user.first_name = request.POST['name']
                user.email = request.POST['email']
                user.save()
>>>>>>> b28e892e132bbf547a3bf56658d604d1bd197493
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request,'sign-up.html', {'error':'Password does not match!'})
    else:
        return render(request,'sign-up.html')

def login(request):
    if request.method == 'POST':
<<<<<<< HEAD
        username_=request.POST['username']
        user = auth.authenticate(username=username_,password = request.POST['pass'])
        if (user is not None) and (not request.user.is_authenticated) and (username_ not in login_table):
            auth.login(request, user)
            userlogged = login_table(username=username_)
            userlogged.save()
=======
        user = auth.authenticate(username=request.POST['username'],password = request.POST['pass'])
        if (user is not None) and (not request.user.is_authenticated):
            auth.login(request,user)
>>>>>>> b28e892e132bbf547a3bf56658d604d1bd197493
            return redirect('home')
        else:
            return render (request,'login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'login.html')

def logout(request):
<<<<<<< HEAD
    #for username in login_table:
        #if (username is not None):
            #return render(request, 'sign-up.html')
    if (request.method == 'POST'):
        auth.logout(request)
        login_table.objects.delete()
=======
    if request.method == 'POST':
        auth.logout(request)
>>>>>>> b28e892e132bbf547a3bf56658d604d1bd197493
    return redirect('home')
