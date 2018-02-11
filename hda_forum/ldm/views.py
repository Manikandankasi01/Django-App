from django.shortcuts import render,redirect, get_object_or_404
import datetime
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from desg_t18 import dash
from ldm.ldm_form import LdmMeetingUpdateForm, LdmForumForm
from ldm.models import (
                            LdmMeetingUpdate,
                            LdmForum,
                            )
# Create your views here.

def ldm_team(request):

    return render(request, 'ldm/ldm_team.html')

def ldm_home(request,track=None):
    user=request.session['user']
    print ("im the logged user",user)
    return render(request,'ldm/ldmhome.html',{})

def ldm_workflow(request):

    return render(request, 'ldm/ldm_workflow.html')

def ldm_meeting_update(request,track=None):
    meeting_update=LdmMeetingUpdate.objects.all()
    query=request.GET.get('search')
    meeting_form=LdmMeetingUpdateForm(request.POST or None)
    if query:
        meeting_update=meeting_update.filter(
                                    Q(title__icontains=query)|
                                    Q(content__icontains=query)
                                    )
    if request.method =='POST':
        if meeting_form.is_valid():
            meeting=meeting_form.save(commit=False)
            meeting.updated_by=request.session['user']
            meeting.save()
            return redirect('/ldm/ldm_meeting_update')
    else:
        paginator = Paginator(meeting_update, 10) # Show 2 contacts per page
        page = request.GET.get('page')
        post = paginator.get_page(page)
        meeting={"meeting_form":meeting_form,
                "posted_data":post,
                }
        return render(request,'ldm/ldm_meetingupdates.html',meeting)

def edit_meeting_content(request,id=None):
    instance=get_object_or_404(LdmMeetingUpdate,id=id)
    meeting_form=LdmMeetingUpdateForm(request.POST or None, instance=instance)
    meeting={"meeting_form":meeting_form,
                "posted_data":instance,
                }
    if meeting_form.is_valid():
        meeting=meeting_form.save(commit=False)
        meeting.updated_by=request.session['user']
        meeting.save()
        return redirect('/ldm/ldm_meeting_update')
    else:
        return render(request,'ldm/editMeetingcontent.html',meeting)

def delete_meeting_content(request, id=None):
    instance=get_object_or_404(LdmMeetingUpdate,id=id)
    instance.delete()
    return redirect('/ldm/ldm_meeting_update')

def ldm_forum(request,track=None):
    posted_data=LdmForum.objects.all()
    query=request.GET.get('forum-search')
    forum_form=LdmForumForm(data=request.POST )
    if query:
        posted_data=posted_data.filter(
                                    Q(track__icontains=query)|
                                    Q(title__icontains=query)|
                                    Q(question__icontains=query)
                                    )
    if request.method =='POST':
        if forum_form.is_valid():
            forum_form=forum_form.save(commit=False)
            forum_form.updated_by=request.session['user']
            forum_form.save()
            return redirect('/ldm/ldm_forum')
    else:
        paginator = Paginator(posted_data, 10) # Show 25 contacts per page
        page = request.GET.get('page')
        post = paginator.get_page(page)
        forum={"forum_form":forum_form,
                "posted_data":post,
                }
    return render(request,'ldm/ldm_forum.html',forum)

def edit_forum_content(request,id=None):
    instance=get_object_or_404(LdmForum,id=id)
    meeting_form=LdmForumForm(request.POST or None, instance=instance)
    meeting={"meeting_form":meeting_form,
                "posted_data":instance,
                }
    if meeting_form.is_valid():
        meeting=meeting_form.save(commit=False)
        meeting.updated_by=request.session['user']
        meeting.save()
        return redirect('/ldm/ldm_forum')
    else:
        return render(request,'ldm/editForumcontent.html',meeting)

def delete_forum_content(request, id=None):
    instance=get_object_or_404(LdmForum,id=id)
    instance.delete()
    return redirect('/ldm/ldm_forum')

def ldm_dashboard(request):
    s_date=request.GET.get('from_date')
    e_date=request.GET.get('to_date')
    track=request.GET.get('track')
    today=datetime.datetime.now()
    default_e_date=today-datetime.timedelta(days=30)
    default_s_date=datetime.datetime.strftime(today, '%m-%d-%Y')
    default_e_date=datetime.datetime.strftime(default_e_date, '%m-%d-%Y')
    default_s_date=datetime.datetime.strptime(default_s_date, '%m-%d-%Y')
    default_e_date=datetime.datetime.strptime(default_e_date, '%m-%d-%Y')
    if s_date is not None:
        if len(s_date)>0 and len(e_date)>0:
            user_s_date=datetime.datetime.strptime(s_date, '%m/%d/%Y')
            user_e_date=datetime.datetime.strptime(e_date, '%m/%d/%Y')

        if len(s_date)>0 and len(e_date)>0 and track=='all':
            ldm=dash.ldm_report(user_s_date,user_e_date)

        else:
            ldm=dash.ldm_report(default_e_date,default_s_date)
    else:
        ldm=dash.ldm_report(default_e_date,default_s_date)
    reports={
       "ldm_report":ldm,
        }
    return render (request,'ldm/ldm_dashboard.html',reports)

def format_date(date):
    return datetime.datetime.strptime(date, '%m/%d/%Y')