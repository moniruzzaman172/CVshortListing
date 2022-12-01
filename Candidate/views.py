import os
from django.shortcuts import render, redirect
from pyresparser import ResumeParser
from Authority.models import Skill
from Candidate.models import Resume, Candidate
from . forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

def canRegistration(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        context = {
            'signform': form,
            'message': '',
            'msgtype': 'failed'

        }
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Candidate:login')
    else:
        form = NewUserForm()
    return render(request, 'Candidate/registration.html',
                  {'signform': form, 'usr': 'Candidate', 'login_var': 'Registration'})


def CanLogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('Candidate:submitCV')
    else:
        form = AuthenticationForm()
    return render(request, 'Candidate/login.html', {'form': form, 'usr': 'Candidate', 'login_var': 'Login'})


def CanLogout(request):
    logout(request)
    return redirect('Account:roll')

def personal(request):

    return render(request, 'Candidate/index.html', {})


def con(request):
    return render(request, 'Candidate/contactbase.html', {})


def contact(request):
    return render(request, 'Candidate/contact.html', {})


@login_required(login_url='Candidate:login')
def handleResume(request):

    if request.method == 'POST':
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print('post')
        resume = request.FILES.get('resume', None)
        print(resume)
        if resume:
            saving = Resume(resume=resume)
            saving.save()
            media_path = os.path.join(base_dir, 'Resumes')
            l_part = str(saving.resume).split('/')
            full_path = os.path.join(media_path, l_part[1])
            data = ResumeParser(str(full_path)).get_extracted_data()
            print(data.get('total_experience'))
            print(data.get('skills'))
            skills = data.get('skills')
            predefined_skill = Skill.objects.all()
            skills_score = 0
            for skill in skills:
                skill = skill.casefold()
                for pre_skill in predefined_skill:
                    if pre_skill.skill_name.casefold() == skill:
                        skills_score = skills_score + pre_skill.score

            print(skills_score)
            experiences_skills_combined_score = float(data.get('total_experience')) + skills_score
            print(experiences_skills_combined_score)
            candidate = Candidate(name=data.get('name'), email=data.get('email'),
                                  phone=data.get('mobile_number'),
                                  total_experiences=float(data.get('total_experience')),
                                  total_skills=len(data.get('skills')),
                                  designation="N/A" if data.get('designation') is None else data.get('designation'),
                                  company="N/A" if data.get('company_names') is None else data.get('company_names'),
                                  skills_score=skills_score,
                                  experiences_skills_combined_score=experiences_skills_combined_score)

            candidate.save()

            return render(request, "Authority/sorted_list.html", {})

    return render(request, "Candidate/cv_form.html", {})
