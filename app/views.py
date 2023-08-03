from typing import Any, Dict
from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView,FormView
from app.forms import *
from django.http import HttpResponse

class TempDataRender(TemplateView):
    template_name='TempDataRender.html'

    def get_context_data(self, **kwargs):
        ECDO=super().get_context_data(**kwargs)
        ECDO['name']='Harshad'
        return ECDO
    

class TempInsertData(TemplateView):
    template_name='TempInsertData.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        ECDO=super().get_context_data(**kwargs)
        SFO=StudentForm()
        ECDO['SFO']=SFO
        return ECDO

    def post(self,request):
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('DataInserted')




class StudentFormViewInsert(FormView):
    template_name='StudentFormViewInsert.html'
    form_class=StudentForm

    def form_valid(self, form):
        form.save()

        return HttpResponse('StudentFormViewInsert')









































