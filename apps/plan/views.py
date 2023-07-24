from django.shortcuts import render,redirect
from django.views.generic import View
from django.http import JsonResponse
from .models import DailySchedule



'''
def calendar(request):
    dailySchedules = DailySchedule.objects.all()
    context = {
        "dailySchedules":dailySchedules,
    }
    return render(request,'plan/calendar.html',context)

def all_events(request):                                                                                                 
    all_events = DailySchedule.objects.all()                                                                                    
    out = []                                                                                                             
    for event in all_events:                                                                                             
        out.append({                                                                                                     
            'title': event.content,                                                                                         
            'id': event.id,                                                                                              
            'start': event.start_time.strftime("%m/%d/%Y, %H:%M:%S"),                                                         
            'end': event.end_time.strftime("%m/%d/%Y, %H:%M:%S"),                                                             
        })                                                                                                               
                                                                                                                     
    return JsonResponse(out, safe=False)  

def add_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event = DailySchedule(content=str(title), start_time=start, end_time=end)
    event.save()
    data = {}
    return JsonResponse(data)


def update(request):
    start = request.GET.get("start_time", None)
    end = request.GET.get("end_time", None)
    title = request.GET.get("content", None)
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)


def remove(request):
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)
    
'''

class PlanScheduleView( View):

    def get(self, request):
        ret = dict()
        planSchedules = DailySchedule.objects.filter(sys_show=1)
        ret['planSchedules'] = planSchedules
        return render(request, 'plan/planshow.html', ret)

#### 
class AddPlanView(View):
    def get(self, request):
        categorys = [{'key': i[0], 'value': i[1]} for i in DailySchedule.cat_choices]
        context = {}
        context['categorys'] = categorys
        return render(request, 'plan/planadd.html', context)
    def post(self, request):
        DailyScheduleI = DailySchedule()
        DailyScheduleI.category = request.POST.get("category")
        DailyScheduleI.groupId = request.POST.get("groupId").replace('\n', '').replace('\r', '').strip()
        DailyScheduleI.title = request.POST.get("title").replace('\n', '').replace('\r', '').strip()
        DailyScheduleI.start = request.POST.get("start")
        DailyScheduleI.end = request.POST.get("end")
        DailyScheduleI.save()
        return  redirect(to='planschedule')





