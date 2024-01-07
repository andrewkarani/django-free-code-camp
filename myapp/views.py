from django.shortcuts import render, redirect # redirect allows us to take the user to another page after registration
# importing an http response
from django.http import HttpResponse
# importing feature from models
from django.contrib.auth.models import User, auth # auth is the function that allows us to authenticate
from django.contrib import messages # used to send response if there is an error
from .models import Feature

# Create your views here.
def index(request):
  # we are soring in the variable called featuresall the objects of the Feature variable.
  # this variable is a list
  features = Feature.objects.all

  #feature1 = Feature()
  #feature1.id = 0
  #feature1.name = 'Fast'
  #feature1.is_true = True
  #feature1.details = 'our service is very quick'

  #feature2 = Feature()
  #feature2.id = 1
  #feature2.name = 'Reliable'
  #feature2.is_true = True
  #feature2.details = 'our service is very reliable'

  #feature3 = Feature()
  #feature3.id = 2
  #feature3.name = 'Affordable'
  #feature3.is_true = False
  #feature3.details = 'our service is very affordable'
  # the above is very repetitivewe cud just have a list

  #features = [feature1, feature2, feature3]
# so now in the html we can looop thru each of these lists and get all the attributes we need

  # lets return an http response with a simple html code
  # return HttpResponse('<h1>Hey, Welcome</h1>')
  #name = 'Patrick'
  #context = {
    #'name': 'patrick',
    #'age': 36,
    #'nationality': 'British',
 # }
  # new function called register for the user regitration
  def register(request):
    # we also need to checkif therequest methodis equal to POST
    if request.method == 'POST':
  # we also need to collect all the info in the register.html file. all this info is gotten and store in those variables    ``
      username = request.POST['username']
      email = request.POST['email']
      password = request.POST['password']
      password2 = request.POST['password2']
    # the above info shud be saved in the users database
    
      if  password == password2:
        if User.objects.filter(email=email).exists():
          messages.info(request, 'Email already used')
          return redirect('register')# we are returning the user back to register since email was already in use
        elif User.objects.filter(username=email).exists():
          messages.info(request, 'Username already used')
          return redirect('register')
        else:
          user = User.objects.create_user(username=username, email=email, password=password)
          user.save()
          return redirect('login') # redirecting to login for user to login
      else:
        messages.info(request, 'Password Not the same')
        return redirect('register')
    else:
      return render(request, 'register.html')# this else statement is for the POST method
  return render (request, 'index.html', {'features': features})#{'feature1': feature1, 'feature2': feature2, 'feature3': feature3})# we want to render the html file we have created

# function for the login
def Login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None: # this means the user is known and has already registerd, but if the user is None itmeans the user is  fake
      auth.login(request, user)
      return redirect('/')
    else:
      messages.info(request, 'Credentials Invalid')
      return redirect('login')
    
  else:
      return render(request, 'login.html')
def Logout(request):
  auth.logout(request)
  return redirect('/')

def counter(request):
  #text = request.POST['text']# we r setting a new variable and then passing a request to get whatever is being passed to this view ie text.
  # text is chosen  bcoz it is the name assigned to the text area in index.html
  # text.split()countsnumber of words
  #amount_of_words = len(text.split())

  posts = [1, 2, 3, 4, 5, 'tim', 'tom', 'john']
  return render(request, 'counter.html', {'posts':posts})#{'amount': amount_of_words})

def post(request, pk):
  return render(request, 'post.html', {'pk': pk})
# {'pk': pk}) here we r sending whatever value is in that html to that html
