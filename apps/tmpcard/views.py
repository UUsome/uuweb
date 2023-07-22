from django.shortcuts import render,redirect
from django.views.generic import View
from .models import Tmpcard
# Create your views here.
class TmpcardView(View):
    def get(self, request):
        tmpcard = Tmpcard.objects.filter(sys_show=1)
        pcard = {} # dict()
        pcard['tmpcard'] = tmpcard
        return render(request,'tmpcard/tmpcard.html', pcard)
    def post(self, request):
        title = request.POST.get("mytitle")
        body = request.POST.get("mybody")
        TmpcardI = Tmpcard()
        TmpcardI.title = title
        TmpcardI.body = body
        TmpcardI.save()
        return redirect(to='caselist')
