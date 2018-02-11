from django.shortcuts import render,redirect, get_object_or_404
import datetime
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from desg_t18 import dash
from desg_t18.registration import UserRegistration, LoginForm, ResetForm
from desg_t18.models import (
                            OverView,
                            UserInformation,
                            TriageNote,
                            MeetingUpdate,
                            KnowledgeSharing,
                            DesgPcUpdate,
                            DesgGmlUpdate,
                            )
from desg_t18.desgForm import (
                                TriageForm,
                                MeetingForm,
                                KnowledgeSharingForm,
                                PcUpdateForm,
                                GmlUpdateForm,
                                )
from pdc.models import PdcMeetingUpdate
from pdc.pdc_form import PdcMeetingUpdateForm
# Create your views here.

def test(request):
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
            return redirect('/desg/test')
    else:
        paginator = Paginator(meeting_update, 10) # Show 2 contacts per page
        page = request.GET.get('page')
        post = paginator.get_page(page)
        meeting={"meeting_form":meeting_form,
            "posted_data":post,
            }
        return render(request,'test.html',meeting)
def desg_team(request):

    return render(request, 'desg/desg_team.html')
def index(request):
    return render(request, 'index.html')

#Validating user
def login(request):
    login_form= LoginForm(request.POST or None)
    login={
            'login_form':login_form,
          }
    if request.method=='POST':
        if login_form.is_valid():
            user=request.session['user'] = request.POST['user_name']
            #print ("im the user",request.session['user'] )
            return redirect('/desg/home')
        else:
            return render(request, 'login.html',login)
    else:
        return render(request, 'login.html',login)

# Register New user
def register(request):
    new_user= UserRegistration(request.POST or None)
    user={'new_user':new_user}
    if request.method=='POST':
        if new_user.is_valid():
            register=new_user.save()
            register.save()
            return redirect('/desg/login')
        else:
            return render(request, 'registration.html',user)
    else:
        return render(request, 'registration.html',user)

#Reset Password
def reset_pass(request):
    reset_form= ResetForm(request.POST or None)
    reset={'reset_form':reset_form}
    if request.method=='POST':
        if reset_form.is_valid():
            reset_form=reset_form.save()
            reset_form.save()
            return redirect('/desg/login')
        else:
            return render(request, 'reset_pass.html',reset)
    else:
        return render(request, 'reset_pass.html',reset)

def hda_home(request):
    nbn=OverView.get_data()
    content ={'content':nbn}
    return render(request, 'home.html', content)

def desg_home(request,track=None):
    return render(request,'desg/desghome.html',{})

def team_view(request):
    return render(request, 'hda_team.html', {})

def hda_dashboard(request):
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
            desg_pc,desg_gml=dash.desg_report(user_s_date,user_e_date)
            ldm_report=dash.ldm_report(user_s_date,user_e_date)
            dsg_report=dash.dsg_iab_report(user_s_date,user_e_date)
            pdc,pdc_delta=dash.pdc_report(user_s_date,user_e_date)

        elif len(s_date)>0 and len(e_date)>0 and track=='pdc':
            desg_pc,desg_gml=dash.desg_report(default_e_date,default_s_date)
            ldm_report=dash.ldm_report(default_e_date,default_s_date)
            dsg_report=dash.dsg_iab_report(default_e_date,default_s_date)
            pdc,pdc_delta=dash.pdc_report(user_s_date,user_e_date)

        elif len(s_date)>0 and len(e_date)>0 and track=='desg':
            desg_pc,desg_gml=dash.desg_report(user_s_date,user_e_date)
            ldm_report=dash.ldm_report(default_e_date,default_s_date)
            dsg_report=dash.dsg_iab_report(default_e_date,default_s_date)
            pdc,pdc_delta=dash.pdc_report(default_e_date,default_s_date)

        elif len(s_date)>0 and len(e_date)>0 and track=='ldm':
            desg_pc,desg_gml=dash.desg_report(default_e_date,default_s_date)
            ldm_report=dash.ldm_report(user_s_date,user_e_date)
            dsg_report=dash.dsg_iab_report(default_e_date,default_s_date)
            pdc,pdc_delta=dash.pdc_report(default_e_date,default_s_date)

        elif len(s_date)>0 and len(e_date)>0 and track=='dsg':
            desg_pc,desg_gml=dash.desg_report(default_e_date,default_s_date)
            ldm_report=dash.ldm_report(default_e_date,default_s_date)
            dsg_report=dash.dsg_iab_report(user_s_date,user_e_date)
            pdc,pdc_delta=dash.pdc_report(default_e_date,default_s_date)

        elif len(s_date)>0 and len(e_date)>0 and track=='ndq':
            desg_pc,desg_gml=dash.desg_report(default_e_date,default_s_date)
            ldm_report=dash.ldm_report(default_e_date,default_s_date)
            dsg_report=dash.dsg_iab_report(default_e_date,default_s_date)
            pdc,pdc_delta=dash.pdc_report(default_e_date,default_s_date)

        else:
            desg_pc,desg_gml=dash.desg_report(default_e_date,default_s_date)
            ldm_report=dash.ldm_report(default_e_date,default_s_date)
            dsg_report=dash.dsg_iab_report(default_e_date,default_s_date)
            pdc,pdc_delta=dash.pdc_report(default_e_date,default_s_date)
    else:
        desg_pc,desg_gml=dash.desg_report(default_e_date,default_s_date)
        ldm_report=dash.ldm_report(default_e_date,default_s_date)
        dsg_report=dash.dsg_iab_report(default_e_date,default_s_date)
        pdc,pdc_delta=dash.pdc_report(default_e_date,default_s_date)
    reports={
        "monthly_desg_pc_report":desg_pc,
        "monthly_desg_gml_report":desg_gml,
        "monthly_ldm_report":ldm_report,
        "monthly_dsg_iab_report":dsg_report,
        "pdc_report":pdc,
        "pdc_delta_report":pdc_delta,
        }

    return render(request, "dashboard.html",reports)

def triage_update(request,id=None):
    posted_data=TriageNote.objects.all()
    query=request.GET.get('search')
    triage_form=TriageForm(request.POST or None)
    if query:
        posted_data=posted_data.filter(
                                    Q(sam_name__icontains=query)|
                                    Q(title__icontains=query)|
                                    Q(content__icontains=query)
                                    )
    if request.method =='POST':
        if triage_form.is_valid():
            triage=triage_form.save(commit=False)
            triage.updated_by=request.session['user']
            triage.save()
            return redirect('/desg/triage_update')
    else:
        paginator = Paginator(posted_data, 10) # Show 25 contacts per page
        page = request.GET.get('page')
        post = paginator.get_page(page)
        triage={"triage_form":triage_form,
                "posted_data":post,
                }
        return render(request,'desg/triagenote.html',triage)

def edit_triage_content(request,id=None):
    instance=get_object_or_404(TriageNote,id=id)
    meeting_form=TriageForm(request.POST or None, instance=instance)
    meeting={"meeting_form":meeting_form,
                "posted_data":instance,
                }
    if meeting_form.is_valid():
        meeting=meeting_form.save(commit=False)
        meeting.updated_by=request.session['user']
        meeting.save()
        return redirect('/desg/triage_update')
    else:
        return render(request,'desg/editTriagecontent.html',meeting)

def delete_triage_content(request, id=None):
    instance=get_object_or_404(TriageNote,id=id)
    instance.delete()
    return redirect('/desg/triage_update')

def perform_check(request,track=None):

    return render(request,'desg/performcheck.html',{})

def pc_update(request,track=None):
    pc_update=DesgPcUpdate.objects.all()
    query=request.GET.get('search')
    pc_update_form=PcUpdateForm(request.POST or None)
    if query:
        pc_update=pc_update.filter(
                                    Q(title__icontains=query)|
                                    Q(content__icontains=query)
                                    )
    if request.method =='POST':
        if pc_update_form.is_valid():
            meeting=pc_update_form.save(commit=False)
            meeting.updated_by=request.session['user']
            meeting.save()
            return redirect('/desg/pc_update')
    else:
        paginator = Paginator(pc_update, 10) # Show 2 contacts per page
        page = request.GET.get('page')
        post = paginator.get_page(page)
        pc_update_content={"pc_update_form":pc_update_form,
                "posted_data":post,
                }
    return render(request,'desg/pc_update.html',pc_update_content)

def edit_pc_update(request,id=None):
    instance=get_object_or_404(DesgPcUpdate,id=id)
    pc_update_form=PcUpdateForm(request.POST or None, instance=instance)
    meeting={"pc_update_form":pc_update_form,
                "posted_data":instance,
                }
    if pc_update_form.is_valid():
        meeting=pc_update_form.save(commit=False)
        meeting.updated_by=request.session['user']
        meeting.save()
        return redirect('/desg/pc_update')
    else:
        return render(request,'desg/edit_pc_update.html',meeting)

def delete_pc_update(request, id=None):
    instance=get_object_or_404(DesgPcUpdate,id=id)
    instance.delete()
    return redirect('/desg/pc_update')


def gml_creation(request,track=None):

    return render(request,'desg/gmlcreation.html',{})

def gml_update(request,track=None):
    gml_update=DesgGmlUpdate.objects.all()
    query=request.GET.get('search')
    gml_update_form=GmlUpdateForm(request.POST or None)
    if query:
        gml_update=gml_update.filter(
                                    Q(title__icontains=query)|
                                    Q(content__icontains=query)
                                    )
    if request.method =='POST':
        if gml_update_form.is_valid():
            meeting=gml_update_form.save(commit=False)
            meeting.updated_by=request.session['user']
            meeting.save()
            return redirect('/desg/gml_update')
    else:
        paginator = Paginator(gml_update, 10) # Show 2 contacts per page
        page = request.GET.get('page')
        post = paginator.get_page(page)
        gml_update_content={"gml_update_form":gml_update_form,
                "posted_data":post,
                }
    return render(request,'desg/gml_update.html',gml_update_content)

def edit_gml_update(request,id=None):
    instance=get_object_or_404(DesgGmlUpdate,id=id)
    gml_update_form=GmlUpdateForm(request.POST or None, instance=instance)
    meeting={"gml_update_form":gml_update_form,
                "posted_data":instance,
                }
    if gml_update_form.is_valid():
        meeting=gml_update_form.save(commit=False)
        meeting.updated_by=request.session['user']
        meeting.save()
        return redirect('/desg/gml_update')
    else:
        return render(request,'desg/edit_gml_update.html',meeting)

def delete_gml_update(request, id=None):
    instance=get_object_or_404(DesgGmlUpdate,id=id)
    instance.delete()
    return redirect('/desg/gml_update')

def meeting_update(request,track=None):
    meeting_update=MeetingUpdate.objects.all()
    query=request.GET.get('search')
    meeting_form=MeetingForm(request.POST or None)
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
            return redirect('/desg/meeting_update')
    else:
        paginator = Paginator(meeting_update, 10) # Show 2 contacts per page
        page = request.GET.get('page')
        post = paginator.get_page(page)
        meeting={"meeting_form":meeting_form,
                "posted_data":post,
                }
        return render(request,'desg/meetingupdates.html',meeting)

def edit_meeting_content(request,id=None):
    instance=get_object_or_404(MeetingUpdate,id=id)
    meeting_form=MeetingForm(request.POST or None, instance=instance)
    meeting={"meeting_form":meeting_form,
                "posted_data":instance,
                }
    if meeting_form.is_valid():
        meeting=meeting_form.save(commit=False)
        meeting.updated_by=request.session['user']
        meeting.save()
        return redirect('/desg/meeting_update')
    else:
        return render(request,'desg/editMeetingcontent.html',meeting)

def delete_meeting_content(request, id=None):
    instance=get_object_or_404(MeetingUpdate,id=id)
    instance.delete()
    return redirect('/desg/meeting_update')

def forum(request,track=None):
    posted_data=KnowledgeSharing.objects.all()
    query=request.GET.get('forum-search')
    forum_form=KnowledgeSharingForm(data=request.POST )
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
            return redirect('/desg/forum')
    else:
        paginator = Paginator(posted_data, 10) # Show 25 contacts per page
        page = request.GET.get('page')
        post = paginator.get_page(page)
        forum={"forum_form":forum_form,
                "posted_data":post,
                }
    return render(request,'desg/forum.html',forum)

def edit_forum_content(request,id=None):
    instance=get_object_or_404(KnowledgeSharing,id=id)
    meeting_form=KnowledgeSharingForm(request.POST or None, instance=instance)
    meeting={"meeting_form":meeting_form,
                "posted_data":instance,
                }
    if meeting_form.is_valid():
        meeting=meeting_form.save(commit=False)
        meeting.updated_by=request.session['user']
        meeting.save()
        return redirect('/desg/forum')
    else:
        return render(request,'desg/editForumcontent.html',meeting)

def delete_forum_content(request, id=None):
    instance=get_object_or_404(KnowledgeSharing,id=id)
    instance.delete()
    return redirect('/desg/forum')

def desg_dashboard(request):
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
            desg_pc,desg_gml=dash.desg_report(user_s_date,user_e_date)

        elif len(s_date)>0 and len(e_date)>0 and track=='transit':
            desg_pc,desg_gml=dash.desg_report(default_e_date,default_s_date)

        else:
            desg_pc,desg_gml=dash.desg_report(default_e_date,default_s_date)
    else:
        desg_pc,desg_gml=dash.desg_report(default_e_date,default_s_date)

    reports={
       "monthly_desg_pc_report":desg_pc,
       "monthly_desg_gml_report":desg_gml,
        }
    return render (request,'desg/desg_dashboard.html',reports)

def format_date(date):
    return datetime.datetime.strptime(date, '%m/%d/%Y')