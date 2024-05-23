from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect                  #message
from django.contrib.auth.models import User
from .models import Message
from django.shortcuts import render, get_object_or_404
from .models import Post
from .models import Image

@login_required
def home(request):
    return render(request, "home.html", {})

def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None) 
        if form.is_valid():
            form.save()
    else: 
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

def compose_message(request, receiver_id):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver_id = receiver_id
            message.save()
            return redirect('inbox')
    else:
        form = MessageForm()
    return render(request, 'compose_message.html', {'form': form})

def inbox(request):
    received_messages = Message.objects.filter(receiver=request.user)
    return render(request, 'inbox.html', {'received_messages': received_messages})

def post_list(request):
    posts = Post.objects.all()  # Retrieve all posts from the database
    return render(request, 'post_list.html', {'posts': posts})

def send_message(request):
    if request.method == 'POST':
        # Process the form submission
        # Assuming you have a form for sending messages
        pass
    else:
        # Render the form for sending messages
        return render(request, 'send_message.html')
def send_message(request):
    # Your logic for sending messages goes here
    return render(request, 'send_message.html')

def inbox(request):
    # Retrieve messages sent to the logged-in user
    messages = Message.objects.filter(receiver=request.user)
    return render(request, 'inbox.html', {'messages': messages})

def create_post(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        author = request.user
        post = Post.objects.create(author=author, text=text)
        # Do something after creating the post
        return redirect('post_detail', post_id=post.id)
    return render(request, 'create_post.html')

def home(request):
    images = Image.objects.all()
    return render(request, 'home.html', {'images': images})  