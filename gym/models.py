from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    join_date = models.DateField()

    def __str__(self):
        return self.name

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    trainer_id = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MembershipPlan(models.Model):
    plan_name = models.CharField(max_length=50)
    duration = models.IntegerField()
    fees = models.IntegerField()

    def __str__(self):
        return self.plan_name

class Attendance(models.Model):
    STATUS_CHOICE = [
        ("Present", "Present"),
        ("Absent", "Absent")
    ]

    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)

    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)

    def __str__(self):
        return f"{self.member.name} - {self.date}"

class Payment(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    amount = models.IntegerField()
    payment_date = models.DateField()

    status = models.CharField(max_length=20)

    def __str__(self):
        return self.member.name