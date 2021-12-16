from django.shortcuts import render, redirect
from django.contrib.auth.models import User
#from django.contrib.auth import login, authenticate, logout
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
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
                user = User.objects.create_user(request.POST['username'], password=request.POST['pass'])
                user.first_name = request.POST['name']
                user.email = request.POST['email']
                user.save()
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request,'sign-up.html', {'error':'Password does not match!'})
    else:
        return render(request,'sign-up.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['pass'])
        if (user is not None) and (not request.user.is_authenticated):
            auth.login(request,user)
            return redirect('home')
        else:
            return render (request,'login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('home')
