from django.shortcuts import render
from home.models import *


# Create your views here.
def index(request):
    
    try:
        if request.method=='POST': 
            title = (request.POST.get('title'))
            author = (request.POST.get('author'))
            contentBox = (request.POST.get('contentBox'))
            imageBox = (request.POST.get('imageBox'))
        
        # if len(title)>10 and len(author)>5 and len(contentBox)>50:
        modelDataFill = recentlyAdded(title=title,author=author,contentBox=contentBox, imageBox=imageBox)
        modelDataFill.save()
    except:
        pass
    
    PopularBlogs = popularblog.objects.all()
    
    return render(request, 'htmls/index.html', {'titles':'IIMT Blogs','PopularBlog':PopularBlogs})

def contact(request):
    
    try:
        if request.method=='POST': 
            name = (request.POST.get('fname'))
            email = (request.POST.get('email'))
            phoneNo = (request.POST.get('phoneNo'))
            subject = (request.POST.get('subject'))
            messageBox = (request.POST.get('messageBox'))
        
        if len(name)>2 and len(email)>11 and len(phoneNo)==10 and len(subject)>10 and   len(messageBox)>20:
            modelDataFill = contactForm(fname=name,emailId=email,phoneNo=phoneNo,subject=subject,messageContent=messageBox)
            modelDataFill.save()
    except:
        pass
    
    return render(request, 'htmls/contact.html', {'titles':'Contact Us - IIMT Blogs'})

def about(request):
    return render(request, 'htmls/about.html', {'titles':'About Us - IIMT Blogs'})

def blog(request):
    WebBlogs = WebBlog.objects.all()
    AppBlogs = AppBlog.objects.all()
    RecentBlogs = recentlyAdded.objects.all()
    return render(request, 'htmls/blog.html', {'titles':'Blogs - IIMT Blogs', 'WebBlog':WebBlogs, 'AppBlog':AppBlogs, 'RecentBlog':RecentBlogs})


def webBlog(request):
    WebBlogs = WebBlog.objects.all()
    return render(request, 'htmls/webBlog.html', {'WebBlog':WebBlogs, 'titles':'Web Development Blogs - IIMT Blogs'})



def appBlog(request):
    AppBlogs = AppBlog.objects.all()
    return render(request, 'htmls/appBlog.html', {'AppBlog':AppBlogs, 'titles':'App Development Blogs - IIMT Blogs'})


def view_blog(request, pk):
    
    viewBlog = WebBlog.objects.get(pk=pk)
    return render(request, 'htmls/viewBlog.html', {'viewBlog':viewBlog})