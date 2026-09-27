from django.shortcuts import render, redirect, get_object_or_404
from .models import Member, Trainer, Attendance, Payment
from datetime import date

# Create your views here.
def home(request):
    return render(request, "index.html")

def add_member(request):
    if request.method == "POST":
        member = Member(
            name = request.POST.get("name"),
            age=request.POST.get("age"),
            gender=request.POST.get("gender"),
            phone=request.POST.get("phone"),
            email=request.POST.get("email"),
            address=request.POST.get("address"),
            join_date=request.POST.get("join_date"),
        )
        member.save()
        return redirect("/add-member/")
    
    today = date.today().isoformat()

    return render(request, "add_member.html", {"today":today})

def member_list(request):
    members = Member.objects.all()
    return render(request, "member_list.html", {"members":members})

def update_member(request, id):
    
    member = get_object_or_404(Member, id=id)

    if request.method == "POST":
        member.name = request.POST.get("name")
        member.age = request.POST.get("age")
        member.gender = request.POST.get("gender")
        member.phone = request.POST.get("phone")
        member.email = request.POST.get("email")
        member.address = request.POST.get("address")
        member.join_date = request.POST.get("join_date")

        member.save()

        return redirect("/member/")
    
    return render(request, "update_member.html", {"member":member})

def delete_member(request, id):
    member = get_object_or_404(Member, id=id)

    member.delete()

    return redirect("/member/")


def add_trainer(request):

    if request.method == "POST":

        trainer = Trainer(
            name=request.POST.get("name"),
            trainer_id=request.POST.get("trainer_id"),
            phone=request.POST.get("phone"),
            email=request.POST.get("email"),
            specialization=request.POST.get("specialization"),
        )

        trainer.save()

        return redirect("/trainers/")

    return render(request, "add_trainer.html")

def trainer_list(request):
    trainers = Trainer.objects.all()

    return render(request, "trainer_list.html", {"trainers": trainers})


def delete_trainer(request, id):
    trainer = Trainer.objects.get(id=id)
    trainer.delete()
    return redirect("/trainers/")

def add_attendance(request):

    members = Member.objects.all()
    trainers = Trainer.objects.all()

    if request.method == "POST":

        attendance = Attendance(
            member_id=request.POST.get("member"),
            trainer_id=request.POST.get("trainer"),
            date=request.POST.get("date"),
            status=request.POST.get("status"),
        )

        attendance.save()

        return redirect("/attendance-list/")

    return render(request, "add_attendance.html", {
        "members": members,
        "trainers": trainers,
        "today": date.today().isoformat()
    })

def attendance_list(request):

    attendance = Attendance.objects.all()

    return render(request, "attendance_list.html", {
        "attendance": attendance,
    })


def add_payment(request):

    members = Member.objects.all()

    if request.method == "POST":

        payment = Payment(
            member_id=request.POST.get("member"),
            amount=request.POST.get("amount"),
            payment_date=request.POST.get("payment_date"),
            status=request.POST.get("status"),
        )

        payment.save()

        return redirect("/payment-list/")

    return render(request, "add_payment.html", {"members": members, "today": date.today().isoformat()})

def payment_list(request):

    payments = Payment.objects.all()

    return render(request, "payment_list.html", {"payments": payments})

def home(request):

    total_members = Member.objects.count()
    total_trainers = Trainer.objects.count()
    total_attendance = Attendance.objects.count()
    total_payments = Payment.objects.count()

    context = {
        "total_members": total_members,
        "total_trainers": total_trainers,
        "total_attendance": total_attendance,
        "total_payments": total_payments,
    }

    return render(request, "index.html", context)


def member_list(request):

    search = request.GET.get("search")

    if search:
        members = Member.objects.filter(name__icontains=search)
    else:
        members = Member.objects.all()

    return render(request, "member_list.html", {"members": members})
