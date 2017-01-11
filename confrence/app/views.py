from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect
from django.views.generic import *
from app.models import Sessions
from django.core.urlresolvers import reverse_lazy
from app.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404



# Create your views here.

def index(request):
    return render(request,'index.html')

class SessionList(ListView):
    model=Sessions
    # lot of scope for filtering and display

class SessionDetail(DetailView):
    model=Sessions



#class SessionCreate(CreateView):
#   model=Sessions
#   fields=['title','abstract','track','speaker']
#  URL redirect issue  after filling the  form and resuming back 

def sessioncreate(request):
    if request.method=="GET":
        form=SessionForm();
        return  render(request,'app/sessions_form.html',{'form':form});
    elif request.method=="POST":
        form=SessionForm(request.POST);
        form.save();
        return HttpResponseRedirect('/sessions');



def SessionUpdate(request,pk):
    post = get_object_or_404(Sessions, pk=pk)
    if request.method == "post":
        form = SessionForm()
        form.save()
        return HttpResponseRedirect('/sessions');
    else:
        form = SessionForm(instance=post)
    

    
    return  render(request,'app/sessions_form.html',{'form':form});




#class SessionUpdate(LoginRequiredMixin,UpdateView):
#    model=Sessions
#    fields=['title','abstracts','track','speaker']
  

class SessionDelete(LoginRequiredMixin,DeleteView):
    model=Sessions
    success_url=reverse_lazy('sessions_list')
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

   


#@login_required
#def submit_session(request):
#    return render(request,'app/submit_session.html')
