from django.shortcuts import render,redirect, get_object_or_404
import datetime
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from desg_t18 import dash
from pdc.pdc_form import PdcMeetingUpdateForm, PdcForumForm
from pdc.models import (
                            PdcMeetingUpdate,
                            PdcForum,
                            )
# Create your views here.

def pdc_team(request):

    return render(request, 'pdc/pdc_team.html')

def pdc_home(request,track=None):

    return render(request,'pdc/pdchome.html',{})

def pdc_workflow(request):

    return render(request, 'pdc/pdc_workflow.html')
def meeting_update(request,track=None):
    meeting_update=PdcMeetingUpdate.objects.all()
    query=request.GET.get('search')
    meeting_form=PdcMeetingUpdateForm(request.POST or None)
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
            return redirect('/pdc/pdc_meeting_update')
    else:
        paginator = Paginator(meeting_update, 10) # Show 2 contacts per page
        page = request.GET.get('page')
        post = paginator.get_page(page)
        meeting={"meeting_form":meeting_form,
                "posted_data":post,
                }
        return render(request,'pdc/pdc_meetingupdates.html',meeting)

def edit_meeting_content(request,id=None):
    instance=get_object_or_404(PdcMeetingUpdate,id=id)
    meeting_form=PdcMeetingUpdateForm(request.POST or None, instance=instance)
    meeting={"meeting_form":meeting_form,
                "posted_data":instance,
                }
    if meeting_form.is_valid():
        meeting=meeting_form.save(commit=False)
        meeting.updated_by=request.session['user']
        meeting.save()
        return redirect('/pdc/pdc_meeting_update')
    else:
        return render(request,'pdc/editMeetingcontent.html',meeting)

def delete_meeting_content(request, id=None):
    instance=get_object_or_404(PdcMeetingUpdate,id=id)
    instance.delete()
    return redirect('/pdc/pdc_meeting_update')

def pdc_forum(request,track=None):
    posted_data=PdcForum.objects.all()
    query=request.GET.get('forum-search')
    forum_form=PdcForumForm(data=request.POST )
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
            return redirect('/pdc/pdc_forum')
    else:
        paginator = Paginator(posted_data, 10) # Show 25 contacts per page
        page = request.GET.get('page')
        post = paginator.get_page(page)
        forum={"forum_form":forum_form,
                "posted_data":post,
                }
    return render(request,'pdc/pdc_forum.html',forum)

def edit_forum_content(request,id=None):
    instance=get_object_or_404(PdcForum,id=id)
    meeting_form=PdcForumForm(request.POST or None, instance=instance)
    meeting={"meeting_form":meeting_form,
                "posted_data":instance,
                }
    if meeting_form.is_valid():
        meeting=meeting_form.save(commit=False)
        meeting.updated_by=request.session['user']
        meeting.save()
        return redirect('/pdc/pdc_forum')
    else:
        return render(request,'pdc/editForumcontent.html',meeting)

def delete_forum_content(request, id=None):
    instance=get_object_or_404(PdcForum,id=id)
    instance.delete()
    return redirect('/pdc/pdc_forum')

def pdc_dashboard(request):
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
            pdc,delta=dash.pdc_report(user_s_date,user_e_date)

        elif len(s_date)>0 and len(e_date)>0 and track=='transit':
            pdc,delta=dash.pdc_report(default_e_date,default_s_date)

        else:
            pdc,delta=dash.pdc_report(default_e_date,default_s_date)
    else:
        pdc,delta=dash.pdc_report(default_e_date,default_s_date)
    reports={
       "pdc_report":pdc,
       "pdc_delta_report":delta,
        }
    return render (request,'pdc/pdc_dashboard.html',reports)

def format_date(date):
    return datetime.datetime.strptime(date, '%m/%d/%Y')