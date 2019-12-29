from django.shortcuts import render, HttpResponse,redirect
# from django.http import HttpResponse
from django.views.generic import View
from .models import TypeDetail,Frame,Solution
#from .forms import TypeForm,FrameForm,SolutionForm


# Create your views here.
def testindex(request):
    return render(request,'testuu/index.html')

# 新增类型
class TypeAdd(View):
    def get(self, request):
        allType = TypeDetail.objects.filter(p_type_id=0)
        context = {}
        context['allType'] = allType
        return render(request, 'testuu/TypeAdd.html', context)
    def post(self, request):
        if request.POST.get("p_type_id") == '0':
            level =1
        else:
            level =2
        p_type_id = request.POST.get("p_type_id")
        name = request.POST.get("name")
        TypeDetailI = TypeDetail()
        TypeDetailI.level = level
        TypeDetailI.p_type_id = p_type_id
        TypeDetailI.name = name
        TypeDetailI.save()
        return redirect(to='typeList')

# 类型列表
def typeList(request):
    allType = TypeDetail.objects.all()
    context = {}
    context['allType'] = allType
    return render(request,'testuu/typelist.html',context)


#新增Frame
class FrameAdd(View):
    def get(self, request):
        type_id = TypeDetail.objects.filter(level=2)
        frame_union = Frame.objects.filter(title_content=0).count()
        context = {}
        context['frame_union'] = frame_union
        context['type_id'] = type_id
        return render(request, 'testuu/FrameAdd.html', context)
    def post(self, request):
        # p_type_id = request.POST.get("p_type_id")
        frame_union = request.POST.get("frame_union")
        Num = request.POST.get("Num") #问题个数
        name=request.POST.get("Tname")
        # title_content = 0
        type_id = request.POST.get("type_id")
        FrameI = Frame()
        FrameI.title_content = 0
        FrameI.frame_union = frame_union
        FrameI.name=name
        FrameI.type_id = type_id #type_id
        # CaseTitleInstance.user=request.user
        FrameI.save()
        t_id = FrameI.id
        for i in range(int(Num)):
            FrameI=Frame()
            FrameI.title_id = t_id
            FrameI.title_content = 1
            FrameI.frame_union = frame_union
            FrameI.type_id = type_id
            FrameI.name=request.POST.get("Cname"+str(i+1))
            FrameI.save()
        return  redirect(to='frameList')

# 框架列表
def frameList(request):
    allFrame = Frame.objects.all().filter(title_content=0)
    allType = TypeDetail.objects.all()
    context = {}
    context['allType'] = allType
    context['allFrame'] = allFrame
    return render(request,'testuu/frameList.html', context)

# 展示框架下所有方案列表
def framedetail(request,type_id,frame_union,):
    frame = Frame.objects.filter(frame_union=frame_union).filter(type_id=type_id).filter(title_content=0)
    solution = Solution.objects.filter(range_flage=frame_union)
    context = {}
    context['frame'] = frame
    context['solution'] = solution
    return render(request,'testuu/framedetail.html', context)


class SolutionAdd(View):
    def get(self, request,type_id, frame_union):
        frame = Frame.objects.filter(frame_union=frame_union).filter(type_id=type_id)
        solution_union = Solution.objects.filter(range_flage=frame_union).values('solution_union').distinct()
        context = {}
        context['solution_union'] = solution_union
        context['frame'] = frame
        return render(request, 'testuu/SolutionAdd.html', context)

    def post(self, request,type_id, frame_union):
        numb = request.POST.get("numb")
        for i in range(int(numb)):
            SolutionI = Solution()
            SolutionI.range_flage = frame_union
            SolutionI.frame_id = request.POST.get("frame"+str(i+1))
            SolutionI.name = request.POST.get("solution" + str(i + 1))
            SolutionI.solution_union = request.POST.get("solution_union")
            SolutionI.save()
        return redirect(to='frameList')
        # return render(request, 'testuu/index.html')

#
def solutiontail(request,type_id,frame_union,solution_union):
    frame = Frame.objects.filter(type_id=type_id).filter(frame_union=frame_union)
    solution = Solution.objects.filter(solution_union=solution_union)
    context = {}
    context['frame'] = frame
    context['solution'] = solution
    return render(request,'testuu/solutiontail.html', context)

