from django.shortcuts import render ,redirect
from .models import Enrollment

# Create your views here.


def home(request):
    return render(request, 'index.html')


def enroll(request):

    if request.method == 'POST':

        Enrollment.objects.create(
            full_name=request.POST.get('full_name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            education=request.POST.get('education'),
            course=request.POST.get('course'),
            message=request.POST.get('message'),
        )

        return render(
            request,
            'webapp/index.html',
            {
                'success': 'Enrollment submitted successfully! Our team will contact you soon.'
            }
        )
    return redirect('/')
    return redirect('/')