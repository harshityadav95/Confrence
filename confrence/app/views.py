from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import *
from app.models import Sessions
from django.core.urlresolvers import reverse_lazy



# Create your views here.

def index(request):
    return render(request,'index.html')

class SessionList(ListView):
    model=Sessions
    # lot of scope for filtering and display

class SessionDetail(DetailView):
    model=Sessions

class SessionCreate(CreateView):
   model=Sessions
   fields=['title','abstract','track','speaker']


class SessionUpdate(UpdateView):
    model=Sessions
    fields=['title','abstracts','track','speaker']

class SessionDelete(DeleteView):
    model=Sessions
    success_url=reverse_lazy('sessions_list')

   


#@login_required
#def submit_session(request):
#    return render(request,'app/submit_session.html')
