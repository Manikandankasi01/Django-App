from django.shortcuts import render,redirect, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from automation.models import (
                            DesgAutomationRelease,
                            DesgAutomationUpdate,
                            PdcAutomationUpdate,
                            PdcAutomationRelease,
                            LdmAutomationUpdate,
                            LdmAutomationRelease,
                            )
from automation.automationForm import (
                                DesgAutomationUpdateForm,
                                DesgAutomationReleaseNoteForm,
                                PdcAutomationUpdateForm,
                                PdcAutomationReleaseNoteForm,
                                LdmAutomationUpdateForm,
                                LdmAutomationReleaseNoteForm,
                                )
'''
DESG Autoamtion view
'''
def desg_automation(request):
    desg_automation_content=DesgAutomationRelease.objects.all()
    query=request.GET.get('search')
    desg_automation_form=DesgAutomationReleaseNoteForm(request.POST or None)
    if query:
        desg_automation_content=desg_automation_content.filter(
                                    Q(title__icontains=query)|
                                    Q(content__icontains=query)
                                    )
    if request.method =='POST':
        if desg_automation_form.is_valid():
            meeting=desg_automation_form.save(commit=False)
            meeting.updated_by=request.session['user']
            meeting.save()
            return redirect('/automation/desg_automation')
    else:
        paginator = Paginator(desg_automation_content, 10) # Show 2 contacts per page
        page = request.GET.get('page')
        post = paginator.get_page(page)
        automation_content={"desg_automation_form":desg_automation_form,
                "posted_data":post,
                }
    return render(request,'automation/desg/desg_Automation.html',automation_content)

def desg_automation_update(request):
    desg_automation_update=DesgAutomationUpdate.objects.all()
    query=request.GET.get('search')
    desg_automation_update_form=DesgAutomationUpdateForm(request.POST or None)
    if query:
        desg_automation_update=desg_automation_update.filter(
                                    Q(title__icontains=query)|
                                    Q(content__icontains=query)
                                    )
    if request.method =='POST':
        if desg_automation_update_form.is_valid():
            meeting=desg_automation_update_form.save(commit=False)
            meeting.updated_by=request.session['user']
            meeting.save()
            return redirect('/automation/desg_automation_update')
    else:
        paginator = Paginator(desg_automation_update, 10) # Show 2 contacts per page
        page = request.GET.get('page')
        post = paginator.get_page(page)
        desg_automation_content={"desg_automation_update_form":desg_automation_update_form,
                "posted_data":post,
                }
    return render(request,'automation/desg/desg_automation_update.html',desg_automation_content)

def edit_desg_automation_content(request,id=None):
    instance=get_object_or_404(DesgAutomationRelease,id=id)
    meeting_form=DesgAutomationReleaseNoteForm(request.POST or None, instance=instance)
    meeting={"meeting_form":meeting_form,
                "posted_data":instance,
                }
    if meeting_form.is_valid():
        meeting=meeting_form.save(commit=False)
        meeting.updated_by=request.session['user']
        meeting.save()
        return redirect('/automation/desg_automation')
    else:
        return render(request,'automation/desg/edit_desg_automation.html',meeting)

def delete_desg_automation_content(request, id=None):
    instance=get_object_or_404(DesgAutomationRelease,id=id)
    instance.delete()
    return redirect('/automation/desg_automation')

def edit_desg_automation_update(request,id=None):
    instance=get_object_or_404(DesgAutomationUpdate,id=id)
    meeting_form=DesgAutomationUpdateForm(request.POST or None, instance=instance)
    meeting={"meeting_form":meeting_form,
                "posted_data":instance,
                }
    if meeting_form.is_valid():
        meeting=meeting_form.save(commit=False)
        meeting.updated_by=request.session['user']
        meeting.save()
        return redirect('/automation/desg_automation_update')
    else:
        return render(request,'automation/desg/edit_desg_automation_update.html',meeting)

def delete_desg_automation_update(request, id=None):
    instance=get_object_or_404(DesgAutomationUpdate,id=id)
    instance.delete()
    return redirect('/automation/desg_automation_update')

'''
PDC Automation View
'''

def pdc_automation(request):
    pdc_automation_content=PdcAutomationRelease.objects.all()
    query=request.GET.get('search')
    pdc_automation_form=PdcAutomationReleaseNoteForm(request.POST or None)
    if query:
        pdc_automation_content=pdc_automation_content.filter(
                                    Q(title__icontains=query)|
                                    Q(content__icontains=query)
                                    )
    if request.method =='POST':
        if pdc_automation_form.is_valid():
            meeting=pdc_automation_form.save(commit=False)
            meeting.updated_by=request.session['user']
            meeting.save()
            return redirect('/automation/pdc_automation')
    else:
        paginator = Paginator(pdc_automation_content, 10) # Show 2 contacts per page
        page = request.GET.get('page')
        post = paginator.get_page(page)
        automation_content={"pdc_automation_form":pdc_automation_form,
                "posted_data":post,
                }
    return render(request,'automation/pdc/pdc_Automation.html',automation_content)

def pdc_automation_update(request):
    pdc_automation_update=PdcAutomationUpdate.objects.all()
    query=request.GET.get('search')
    pdc_automation_update_form=PdcAutomationUpdateForm(request.POST or None)
    if query:
        pdc_automation_update=pdc_automation_update.filter(
                                    Q(title__icontains=query)|
                                    Q(content__icontains=query)
                                    )
    if request.method =='POST':
        if pdc_automation_update_form.is_valid():
            meeting=pdc_automation_update_form.save(commit=False)
            meeting.updated_by=request.session['user']
            meeting.save()
            return redirect('/automation/pdc_automation_update')
    else:
        paginator = Paginator(pdc_automation_update, 10) # Show 2 contacts per page
        page = request.GET.get('page')
        post = paginator.get_page(page)
        pdc_automation_content={"pdc_automation_update_form":pdc_automation_update_form,
                "posted_data":post,
                }
    return render(request,'automation/pdc/pdc_automation_update.html',pdc_automation_content)

def edit_pdc_automation_content(request,id=None):
    instance=get_object_or_404(PdcAutomationRelease,id=id)
    meeting_form=PdcAutomationReleaseNoteForm(request.POST or None, instance=instance)
    meeting={"meeting_form":meeting_form,
                "posted_data":instance,
                }
    if meeting_form.is_valid():
        meeting=meeting_form.save(commit=False)
        meeting.updated_by=request.session['user']
        meeting.save()
        return redirect('/automation/pdc_automation')
    else:
        return render(request,'automation/pdc/edit_pdc_automation.html',meeting)

def delete_pdc_automation_content(request, id=None):
    instance=get_object_or_404(PdcAutomationRelease,id=id)
    instance.delete()
    return redirect('/automation/pdc_automation')

def edit_pdc_automation_update(request,id=None):
    instance=get_object_or_404(PdcAutomationUpdate,id=id)
    meeting_form=PdcAutomationUpdateForm(request.POST or None, instance=instance)
    meeting={"meeting_form":meeting_form,
                "posted_data":instance,
                }
    if meeting_form.is_valid():
        meeting=meeting_form.save(commit=False)
        meeting.updated_by=request.session['user']
        meeting.save()
        return redirect('/automation/pdc_automation_update')
    else:
        return render(request,'automation/pdc/edit_pdc_automation_update.html',meeting)

def delete_pdc_automation_update(request, id=None):
    instance=get_object_or_404(PdcAutomationUpdate,id=id)
    instance.delete()
    return redirect('/automation/pdc_automation_update')



'''
LDM Automation View
'''

def ldm_automation(request):
    ldm_automation_content=LdmAutomationRelease.objects.all()
    query=request.GET.get('search')
    ldm_automation_form=LdmAutomationReleaseNoteForm(request.POST or None)
    if query:
        ldm_automation_content=ldm_automation_content.filter(
                                    Q(title__icontains=query)|
                                    Q(content__icontains=query)
                                    )
    if request.method =='POST':
        if ldm_automation_form.is_valid():
            meeting=ldm_automation_form.save(commit=False)
            meeting.updated_by=request.session['user']
            meeting.save()
            return redirect('/automation/ldm_automation')
    else:
        paginator = Paginator(ldm_automation_content, 10) # Show 2 contacts per page
        page = request.GET.get('page')
        post = paginator.get_page(page)
        automation_content={"ldm_automation_form":ldm_automation_form,
                "posted_data":post,
                }
    return render(request,'automation/ldm/ldm_Automation.html',automation_content)

def ldm_automation_update(request):
    ldm_automation_update=LdmAutomationUpdate.objects.all()
    query=request.GET.get('search')
    ldm_automation_update_form=LdmAutomationUpdateForm(request.POST or None)
    if query:
        ldm_automation_update=ldm_automation_update.filter(
                                    Q(title__icontains=query)|
                                    Q(content__icontains=query)
                                    )
    if request.method =='POST':
        if ldm_automation_update_form.is_valid():
            meeting=ldm_automation_update_form.save(commit=False)
            meeting.updated_by=request.session['user']
            meeting.save()
            return redirect('/automation/ldm_automation_update')
    else:
        paginator = Paginator(ldm_automation_update, 10) # Show 2 contacts per page
        page = request.GET.get('page')
        post = paginator.get_page(page)
        pdc_automation_content={"ldm_automation_update_form":ldm_automation_update_form,
                "posted_data":post,
                }
    return render(request,'automation/ldm/ldm_automation_update.html',pdc_automation_content)

def edit_ldm_automation_content(request,id=None):
    instance=get_object_or_404(LdmAutomationRelease,id=id)
    meeting_form=LdmAutomationReleaseNoteForm(request.POST or None, instance=instance)
    meeting={"meeting_form":meeting_form,
                "posted_data":instance,
                }
    if meeting_form.is_valid():
        meeting=meeting_form.save(commit=False)
        meeting.updated_by=request.session['user']
        meeting.save()
        return redirect('/automation/ldm_automation')
    else:
        return render(request,'automation/ldm/edit_ldm_automation.html',meeting)

def delete_ldm_automation_content(request, id=None):
    instance=get_object_or_404(LdmAutomationRelease,id=id)
    instance.delete()
    return redirect('/automation/ldm_automation')

def edit_ldm_automation_update(request,id=None):
    instance=get_object_or_404(LdmAutomationUpdate,id=id)
    meeting_form=LdmAutomationUpdateForm(request.POST or None, instance=instance)
    meeting={"meeting_form":meeting_form,
                "posted_data":instance,
                }
    if meeting_form.is_valid():
        meeting=meeting_form.save(commit=False)
        meeting.updated_by=request.session['user']
        meeting.save()
        return redirect('/automation/ldm_automation_update')
    else:
        return render(request,'automation/ldm/edit_ldm_automation_update.html',meeting)

def delete_ldm_automation_update(request, id=None):
    instance=get_object_or_404(LdmAutomationUpdate,id=id)
    instance.delete()
    return redirect('/automation/ldm_automation_update')