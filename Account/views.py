from django.shortcuts import render

# Create your views here.
def userRole(request):
    return render(request, 'Account/userRolePage.html')


def candidate(request):
    return render(request, 'Account/candidatePage.html')


def authority(request):
    return render(request, 'Account/authorityPage.html')