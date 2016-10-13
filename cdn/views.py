from django.shortcuts import render
import requests, json
from .models import Member, Event, Place, Presence
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.

API_BASE = "https://api.meetup.com/"
API_KEY = "?&key=56554e2c242d6b1d61424d7e65106d0"
URLNAME = "caf%C3%A9s-d%C3%A9bats-nantais/"

@login_required	
def index(request):
    
    members = Member.objects.all()
    # for member in members:
        # firstevent = Presence.objects.filter(member = member).order_by('event.time')[0]
        # member.presenceCount = Presence.objects.filter(member = member).count()
        # member.save()
    members =  members.order_by('-presenceCount') 
    events = Event.objects.filter(status = 'past').order_by('time')
    presences = Presence.objects.all()
    counts = {}
    
    for x in range(1, 100):
        count =  Member.objects.filter(presenceCount = x).count()
        if count != 0:
            counts[x] = Member.objects.filter(presenceCount = x).count()
           
    return render(request,'cdn/index.html',{
        'members': members,
        'events':events,
        'presences':presences,
        'counts':counts});
@login_required	    
def memberView(request, idmember):
    member = Member.objects.get(id = idmember)
    events = Event.objects.filter(status = 'past').order_by('time')
    
    presences = Presence.objects.filter(member = member)
    
    for event in events:
        event.presence = 0
    
    for presence in presences:
        for event in events:
            if event == presence.event:
                event.presence = 1
                        
    return render(request,'cdn/memberview.html',{
                'member': member,
                'events': events, 
                'presences': presences});
@login_required	    
def getEvent(request, idEvent):
    r = requests.get(API_BASE+URLNAME+'events/'+idEvent+API_KEY)
    data = json.loads(r.text)
    return render(request,'cdn/index.html',{'data': data});
@login_required	        
def getAllEvents(request):
    r = requests.get(API_BASE+URLNAME+'events'+API_KEY+'&status=past')
    data = json.loads(r.text)
    return render(request,'cdn/index.html',{'data': data});
@login_required	   
def updateMembers(request):
    r = requests.get(API_BASE+URLNAME+'members'+API_KEY)
    data = json.loads(r.text)
    for member in data:
        
        if 'role' in member['group_profile'] :
            role = member['group_profile']['role']
        else:
            role = 'no role'
    
        updated_values = {
            'name' : member['name'],
            'role' : role,
            'status' : member['group_profile']['status']    
        }
    
        obj, created = Member.objects.update_or_create(
            idmeetup = member['id'],
            defaults = updated_values   
        )   
    return render(request,'cdn/index.html',{'data': data});
@login_required	    
def updatePastEvents(request):
    r = requests.get(API_BASE+URLNAME+'events'+API_KEY+'&status=past')
    data = json.loads(r.text)
    
    r2 = requests.get(API_BASE+URLNAME+'events'+API_KEY+'&status=upcoming')
    data.extend(json.loads(r2.text))
    
    for event in data:
        
        eventTime = datetime.fromtimestamp(int(event['time'])/1000)
        
        updated_values = {
            'name' : event['name'],
            'status' : event['status'],
            'organisator_id' : 1,
            'time': eventTime
        }
    
        obj, created = Event.objects.update_or_create(
            idmeetup = event['id'],
            defaults = updated_values
        )       
    
    
    return render(request,'cdn/index.html',{'data': data});
@login_required	    
def updatePresence(idEvent):
    event = Event.objects.get(idmeetup = idEvent)

    r = requests.get(API_BASE+URLNAME+'events/'+idEvent+'/attendance'+API_KEY)
    data = json.loads(r.text)
    
    for presence in data:
        updated_values = {
            'guest': False
        }
        
        try:
            memb = Member.objects.get(idmeetup = presence['member']['id'])
        except:
            memb = Member.objects.get(idmeetup = 201199341 )
        
        obj, created = Presence.objects.update_or_create(
            member = memb,
            event = event,
            defaults = updated_values   
        )
    
    return;
@login_required	        
def updatePresences(request):
    
    r = requests.get(API_BASE+URLNAME+'events'+API_KEY+'&status=past')
    data = json.loads(r.text)
    
    for event in data:
        updatePresence( event['id'] )
            
    return render(request,'cdn/index.html',{'data': data});
    
