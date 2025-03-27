from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore
from .models import Member

def members(request):
    mymembers = Member.objects.all().values()
    context = {
        'mymembers': mymembers,
    }
    return render(request, 'index.html', context)