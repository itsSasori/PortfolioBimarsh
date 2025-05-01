from django.shortcuts import render ,redirect
from .models import Project,WorkExperience,Contact

from django.core.paginator import Paginator
from django.contrib import messages



# Create your views here.
def home(request):
    projects = Project.objects.all().order_by('-created_at')
    paginator = Paginator(projects ,3)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    work_experience = WorkExperience.objects.all().order_by('-start_date')

    context= {
    'page_obj':page_obj,'work_experience':work_experience
    }
    return render(request, 'index.html',context)

def contact(request):
    if request.method == "POST":
        name=request.POST.get('userName')
        email=request.POST.get('userEmail')
        message=request.POST.get('userMessage')
        if not name:
            messages.error(request,'Please enter your name!')
            return render(request, 'contact.html')
        if not email:
            messages.error(request,'Please enter your email!')
            return render(request, 'contact.html')
        if not message:
            messages.error(request,'Please enter your message!')
            return render(request, 'contact.html')
        try:
            contact = Contact(name=name, email=email, message=message)
            contact.save()
            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
            messages.error(request, f"Failed to save message: {e}")
            print(f"Save error: {e}")
        messages.success(request,'Your message has been sent successfully!')
        return redirect('home')

    return render(request, 'contact.html')