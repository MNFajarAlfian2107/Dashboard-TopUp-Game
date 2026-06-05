from django.shortcuts import render, redirect
from .payment import PaymentFactory
from django.contrib.auth.models import User
from .models import Transaction

def index(request):
    games = [
        {"name": "Mobile Legends", "image": "images/ml.jpg"},
        {"name": "Free Fire", "image": "images/ff.jpg"},
        {"name": "PUBG Mobile", "image": "images/pubg.jpg"},
        {"name": "FC Mobile", "image": "images/fc.jpg"},
        {"name": "Higgs Domino", "image": "images/higgs.jpg"},
    ]

    history = Transaction.objects.all().order_by('-id')
    success = request.session.pop("payment_success", False)

    for t in history:
        t.total_format = f"{t.total:,}".replace(",", ".")

    return render(request, "index.html", {
        "games": games,
        "history": history,
        "success": success
    })


def checkout(request):
    if request.method == "POST":
        user = request.user

        if not user.is_authenticated:
            user = User.objects.get_or_create(username="guest")[0]

        payment_method = request.POST['payment']
        amount = int(request.POST['total'])

        payment_obj = PaymentFactory.get_payment(payment_method)
        payment_status = payment_obj.process()

        Transaction.objects.create(
            user=user,
            game=request.POST['game'],
            nominal=request.POST['nominal'],
            payment=payment_status,
            total=amount
        )

        request.session['payment_success'] = True
        return redirect('/')