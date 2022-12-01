from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import authority_account_form, authority_login_raw_form
from Authority.models import TopCandidates
from Candidate.models import Candidate, Resume
from .models import authority_account
from django.contrib.auth.hashers import check_password
from django.urls import reverse


def authLogin(request):
    if request.method == "POST":
        user_id = request.POST['signin-user']
        user_password = request.POST['signin-password']
        print(f"{user_id} and {user_password}")
        login_id = authority_account.objects.filter(auth_userid=user_id)
        print((login_id))
        if login_id:
            is_login_id = authority_account.objects.filter(auth_userid=user_id, auth_pass=user_password)
            # login_pass = is_login_id.auth_pass
            # check_hash = check_password(user_password, login_pass)
            if is_login_id:
                request.session['auth_userid'] = user_id
                print('login successful')
                ses = request.session['auth_userid']

                # return render(request, 'manager/manager_dashboard.html', context)
                return HttpResponseRedirect(reverse('Authority:sorted_list'))
            else:
                print('login failed')
                context = {
                    'msg': 'failed and try again'
                }
                return render(request, 'Authority/login.html', context)
    elif request.session.has_key('auth_userid'):
        print('already has a keyy')
        return render(request, 'Authority/sorted_list.html')
    else:
        context = {
            'msg': 'failed and try again'
        }
        return render(request, 'Authority/login.html', context)


def authRegistration(request):
    form = authority_account_form()
    context = {
        'regForm': form,
        'msgtype': 'failed',
        'message': ''
    }
    if request.method == 'POST':
        form = authority_account_form(request.POST, request.FILES)
        if form.is_valid():
            # user = form.cleaned_data.get('man_userid')
            password1 = form.data['auth_pass']
            password2 = request.POST['man_pass2']
            print(f"{password1} and {password2}")
            if password1 == password2:
                form.save()
                form = authority_account_form()
                context.update({
                    'message': 'Registration is successful',
                    'msgtype': 'successful'
                })
            else:
                form = authority_account_form()
                context.update({
                    'message': ',Password Must be same',
                    'msgtype': 'failed'
                })
            # formuser = form.data['auth_userid']
            # print(formuser)
            # print(user)

        else:
            context.update({
                'message': 'Try Again',
                'msgtype': 'failed'
            })

    return render(request, 'Authority/registration.html', context)


def authLogout(request):
    if request.session.has_key('auth_userid'):
        print('key is deleted')
        del request.session['auth_userid']

    return HttpResponseRedirect(reverse('Authority:auth_login'))


def sorted_list_3(request):
    ses = request.session.has_key('auth_userid')
    if ses:
        candidates = Candidate.objects.all()
        candidates = list(candidates)
        candidates.sort(key=lambda c: c.experiences_skills_combined_score, reverse=True)
        return render(request, "Authority/sorted_list.html", {'candidates': candidates})
    else:
        return HttpResponseRedirect(reverse('Authority:auth_login'))


def sorted_list_2(request):
    ses = request.session.has_key('auth_userid')
    if ses:
        candidates = Candidate.objects.all()
        candidates = list(candidates)
        candidates.sort(key=lambda c: c.skills_score, reverse=True)

        return render(request, "Authority/sorted_list.html", {'candidates': candidates})
    else:
        return HttpResponseRedirect(reverse('Authority:auth_login'))


def sorted_list_1(request):
    ses = request.session.has_key('auth_userid')
    if ses:
        candidates = Candidate.objects.all()
        candidates = list(candidates)
        candidates.sort(key=lambda c: c.total_experiences, reverse=True)

        return render(request, "Authority/sorted_list.html", {'candidates': candidates})
    else:
        return HttpResponseRedirect(reverse('Authority:auth_login'))



def home(request):
    ses = request.session.has_key('auth_userid')
    if ses:
        return render(request, "Authority/sorted_list.html", {})
    else:
        return HttpResponseRedirect(reverse('Authority:auth_login'))



def sendEmail1(request):
    ses = request.session.has_key('auth_userid')
    if ses:
        top_candidates = TopCandidates.objects.all()
        candidates = Candidate.objects.all()
        candidates = list(candidates)
        candidates.sort(key=lambda c: c.total_experiences, reverse=True)
        mailPart(top_candidates, candidates)
        return render(request, "Authority/sorted_list.html", {'candidates': candidates})
    else:
        return HttpResponseRedirect(reverse('Authority:auth_login'))



def sendEmail2(request):
    ses = request.session.has_key('auth_userid')
    if ses:
        top_candidates = TopCandidates.objects.all()
        candidates = Candidate.objects.all()
        candidates = list(candidates)
        candidates.sort(key=lambda c: c.skills_score, reverse=True)
        mailPart(top_candidates, candidates)
        return render(request, "Authority/sorted_list.html", {'candidates': candidates})
    else:
        return HttpResponseRedirect(reverse('Authority:auth_login'))



def sendEmail3(request):
    ses = request.session.has_key('auth_userid')
    if ses:
        top_candidates = TopCandidates.objects.all()
        candidates = Candidate.objects.all()
        candidates = list(candidates)
        candidates.sort(key=lambda c: c.experiences_skills_combined_score, reverse=True)
        mailPart(top_candidates, candidates)
        return render(request, "Authority/sorted_list.html", {'candidates': candidates})
    else:
        return HttpResponseRedirect(reverse('Authority:auth_login'))



def mailPart(top_candidates, candidates):
    count = 1
    for max_can in top_candidates:
        max_candidates = max_can.number_of_selection
        date = max_can.date
        print(max_candidates)
    for can in candidates:
        if count <= max_candidates:
            send_mail(
                'Django Developer Interview',
                'You submitted your CV to Antor Productions. You are cordially invited for the interview. Your score: ' +
                str(can.experiences_skills_combined_score) + '. Position: ' + str(count) + '. Interview Date: ' + str(
                    date) + '.',
                settings.EMAIL_HOST_USER,
                [can.email],
                fail_silently=False,
            )
            count = count + 1

