from django.shortcuts import render, redirect
from .models import Topic, Choice
# Create your views here.

def create(request):
    if request.method == "POST":
        s = request.POST.get("sub")
        c = request.POST.get("con")
        t = Topic(subject=s, content=c, maker=request.user)
        t.save()

        cho = request.POST.getlist("cho")
        com = request.POST.getlist("com")
        for n, c in zip(cho, com):
            Choice(topic=t, name=n, comment=c).save()
        return redirect("vote:index")
    return render(request, "vote/create.html")


def cancel(request, tpk):
    u = request.user
    t = Topic.objects.get(id=tpk)
    t.voter.remove(u)
    u.choice_set.get(topic=t).choicer.remove(u)
    return redirect("vote:detail", tpk)

    

def vote(request, tpk):
    t = Topic.objects.get(id=tpk)
    if not request.user in t.voter.all():
        t.voter.add(request.user)
        cpk = request.POST.get("cho")
        c = Choice.objects.get(id=cpk)
        c.choicer.add(request.user)
    return redirect("vote:detail", tpk)

def detail(request, tpk):
    t = Topic.objects.get(id=tpk)
    c = t.choice_set.all()
    context = {
        "t" : t,
        "cset" : c
    }
    return render(request, "vote/detail.html", context)

def index(request):
    t = Topic.objects.all()
    context = {
        "tset" : t
    }
    return render(request, "vote/index.html", context)