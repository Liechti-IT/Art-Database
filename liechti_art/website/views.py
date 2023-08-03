from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from .models import Record
from .forms import AddRecordForm
from django.db.models import Q
from django.shortcuts import render, redirect
from .forms import ChangeRecordForm

def home(request):
    letzte_drei_eintraege = Record.objects.all().order_by('-created_at')[:3]
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        #Authenticate
        user = authenticate(request, username=username,  password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return redirect("home")
    else:
        return render(request, "home.html", {'records':letzte_drei_eintraege, 'active_view': 'home'})
    

def kunstverzeichnis(request):
    records_list = Record.objects.all()
    paginator = Paginator(records_list, 10)  # 10 Datensätze pro Seite
    page = request.GET.get('page')
    records = paginator.get_page(page)
    return render(request, "kunstverzeichnis.html", {'records': records, 'active_view': 'kunstverzeichnis'})



def add_record(request):
    if request.method == "POST":
        form = AddRecordForm(request.POST, request.FILES)
        if form.is_valid():
            record = form.save(commit=False)
            record.save()
            return redirect('home')  # Du kannst hier zu einer anderen Seite weiterleiten, z.B. zur Liste der Kunstwerke
    else:
        form = AddRecordForm()
    return render(request, "add_record.html", {'form': form, 'active_view': 'add_record'})


def update_record(request, pk):
    current_record = Record.objects.get(id=pk)
    form = ChangeRecordForm(request.POST or None, instance=current_record)
    if form.is_valid():
        record = form.save(commit=False)
        record.save()
        return redirect('home')
    else:
        return render(request, "update_record.html", {'form': form,'current_record': current_record})



def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        records = Record.objects.filter(
            Q(artist_name__contains=searched) |
            Q(img_title__contains=searched) |
            Q(bild_art__contains=searched)  |
            Q(bild_standort__contains=searched)  |
            Q(Jahrgang__contains=searched) |
            Q(comment__contains=searched)
        )
        return render(request, "search.html", {'records': records, 'searched': searched})
    else:
        return render(request, "search.html", {})


def login_user(request):
    pass

def logout_user(request):
    logout(request)
    return redirect("home")


