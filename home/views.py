from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

#View del Home y  lógica del formulario de contacto.
def home(request):
    """Atiende la petición GET /"""

    if request.method == "POST":
        subject = request.POST["asunto"]
        message = request.POST["mensaje"] + "\n\n" + request.POST["nombre"] + "\n" + request.POST["correo"] + "\n" + request.POST["phone"]
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ["s.mabell.lopez@gmail.com"]
        send_mail(
            subject,
            message,
            from_email,
            recipient_list,
            fail_silently=False
        )

        return render(request, 'home/thankyou.html')

    return render(request, "home/home.html")

# view de la Thank You page.
def thankyou(request):

    return render(request, 'home/thanyou.html')