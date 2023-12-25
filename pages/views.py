from django.shortcuts import render, redirect

from pages.models import RESERVATIONModel, CaruselModel, LeftMenuModel, RightMenuModel, GalleryModel


def home_page(request):
    return render(request, 'index.html')


def reservation_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        name = request.POST.get('name')
        date = request.POST.get('date')
        time = request.POST.get('time')
        message = request.POST.get('message')
        user_email = RESERVATIONModel.objects.filter(email=email).first()
        if user_email:
            return redirect('home')
        new_user = RESERVATIONModel.objects.create(
            email=email,
            name=name,
            phone=phone,
            date=date,
            time=time,
            message=message
        )
        new_user.save()
        return redirect('home')


def Foods_image(request):
    carusel = CaruselModel.objects.all().order_by("-pk")[:5]
    foods_menu = LeftMenuModel.objects.all().order_by("-created_at")[:8]
    gallery = GalleryModel.objects.all().order_by('-created_at')[:8]
    context = {
        "carusel_list": carusel,
        "food_menu": foods_menu,
        "gallery": gallery
    }
    return render(request, 'index.html', context)

