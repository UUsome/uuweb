from django.shortcuts import render,redirect
from django.views.generic import View
from .models import Case_title, Case_content, Solution
from django.db.models import Q
import uuid

def myindex(request):
    return render(request, 'index.html')

# 框架列表 全部
class CaseListView(View):
    def get(self, request):
        ret = dict()
        case_title = Case_title.objects.filter(sys_show=1)
        #case_content = Case_content.objects.filter(sys_show=1)
        ret['case_title'] = case_title
        #ret['case_content'] = case_content
        return render(request, 'casepoint/caselist.html', ret)

#### 框架 （增删改查）
class CaseAddView(View):
    def get(self, request):
        categorys = [{'key': i[0], 'value': i[1]} for i in Case_title.category_choices]
        context = {}
        context['categorys'] = categorys
        return render(request, 'casepoint/caseAdd.html', context)
    def post(self, request):
        Num = request.POST.get("Num") #问题个数
        casetitle = request.POST.get("casetitle")
        category = request.POST.get("category")
        Case_titleI = Case_title()
        Case_titleI.category = category
        Case_titleI.casetitle = casetitle
        Case_titleI.save()
        Case_title_id = Case_titleI.id
        for i in range(int(Num)):
            Case_contentI=Case_content()
            Case_contentI.casetitle_id = Case_title_id
            Case_contentI.casecontent=request.POST.get("Cname"+str(i+1))
            Case_contentI.sub_title = request.POST.get("sub_title"+str(i+1))
            Case_contentI.save()
        return  redirect(to='caseadd')


# 展示框架下所有方案列表(同时可增加Solution)

class CaseDetailView(View):

    def get(self, request,Case_title_id):
        case_title = Case_title.objects.get(pk=Case_title_id)
        case_contents = Case_content.objects.filter(casetitle_id=Case_title_id)
        # Solutions =  Solution.objects.filter(case_id__in=case_contents.values_list('id', flat=True))
        Solutions = Solution.objects.filter(case_id=case_title.id).filter(is_title=1)
        case_contents_count = Case_content.objects.filter(casetitle_id=Case_title_id).count()
        contt = {} # dict()
        contt['case_title'] = case_title
        contt['case_contents'] = case_contents
        contt['Solutions'] = Solutions
        contt['case_contents_count'] = case_contents_count
        return render(request,'casepoint/casedetail.html', contt)

    def post(self, request,Case_title_id):
        case_contents_count = request.POST.get("case_contents_count")
        unique_string = str(uuid.uuid4())
        SolutionI = Solution()
        SolutionI.uniqueid = unique_string
        SolutionI.case_id = Case_title_id
        SolutionI.is_title = 1
        SolutionI.solution = request.POST.get("solution0")
        SolutionI.save()
        for i in range(int(case_contents_count)):
            Case_id = request.POST.get("caseid" + str(i+1))
            #if Case_id > -1:  # 如果case_contents 对应此字段为子标题，caseid（N）值取-1
            SolutionI = Solution()
            SolutionI.uniqueid =unique_string
            SolutionI.case_id = Case_id
            SolutionI.is_title = 0
            SolutionI.solution = request.POST.get("solution" + str(i+1))
            SolutionI.save()
        return redirect(to='caselist')



class SolutionDetailView(View):
    def get(self, request,Case_title_id,uniqueid):
        Solutions =  Solution.objects.filter(uniqueid=uniqueid)
        case_title = Case_title.objects.get(pk=Case_title_id)
        case_contents = Case_content.objects.filter(casetitle_id=Case_title_id)
        context = {}
        context['Solutions'] = Solutions
        context['case_title'] = case_title
        context['case_contents'] = case_contents
        return render(request, 'casepoint/solutiondetail.html', context)



