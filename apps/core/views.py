from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .utils import send_telegram_message

from apps.services.models import Service
from apps.news.models import News


def home(request):
    services = Service.objects.filter(is_active=True)[:6]

    # So'nggi 3 ta yangilik
    latest_news = News.objects.filter(is_active=True)[:3]

    context = {
        'services': services,
        'latest_news': latest_news,
    }
    return render(request, 'core/home.html', context)


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()

            # Telegram xabar
            tg_message = f"""
<b>📩 Yangi xabar!</b>

<b>Ism:</b> {contact_message.name}
<b>Telefon:</b> {contact_message.phone}
<b>Email:</b> {contact_message.email or 'Kiritilmagan'}

<b>Xabar:</b>
{contact_message.message}
"""
            send_telegram_message(tg_message)

            messages.success(request, 'Xabaringiz muvaffaqiyatli yuborildi!')
            return redirect('core:contact')
    else:
        form = ContactForm()

    context = {
        'form': form
    }
    return render(request, 'core/contact.html', context)


def certification_body(request):
    """Sertifikatlashtirish organi sahifasi"""
    return render(request, 'core/certification-body.html')


def testing_laboratory(request):
    """Sinov laboratoriyasi sahifasi"""
    return render(request, 'core/testing-laboratory.html')