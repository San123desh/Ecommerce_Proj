

from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from io import BytesIO
from django.contrib.auth.decorators import login_required
from .models import Cart
import datetime
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Profile
from products.models import *
from accounts.models import Cart, CartItems

def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username=email)

        if not user_obj.exists():
            messages.warning(request, 'Account not found.')
            return HttpResponseRedirect(request.path_info)

        user_obj = authenticate(username=email, password=password)
        if user_obj:
            login(request, user_obj)
            return redirect('/')

        messages.warning(request, 'Invalid credentials')
        return HttpResponseRedirect(request.path_info)

    return render(request, 'accounts/login.html')


def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user_obj = User.objects.filter(username=email)

        if user_obj.exists():
            messages.warning(request, 'Email is already taken.')
            return HttpResponseRedirect(request.path_info)

        user_obj = User.objects.create(first_name=first_name, last_name=last_name, email=email, username=email)
        user_obj.set_password(password)
        user_obj.save()

        user_obj = authenticate(username=email, password=password)
        if user_obj:
            login(request, user_obj)
            return redirect('/')

    return render(request, 'accounts/register.html')


@login_required
def add_to_cart(request, uid):
    variant = request.GET.get('variant')
    product = get_object_or_404(Product, uid=uid)
    user = request.user

    cart, created = Cart.objects.get_or_create(user=user, is_paid=False)
    cart_item = CartItems.objects.create(cart=cart, product=product)

    if variant:
        size_variant = get_object_or_404(SizeVariant, size_name=variant)
        cart_item.size_variant = size_variant
        cart_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove_cart(request, cart_item_uid):
    try:
        cart_item = CartItems.objects.get(uid=cart_item_uid)
        cart_item.delete()
    except Exception as e:
        print(e)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def cart(request):
    cart_obj = get_object_or_404(Cart, is_paid=False, user=request.user)
    
    if request.method == 'POST':
        coupon = request.POST.get('coupon')
        coupon_obj = Coupon.objects.filter(coupon_code__icontains=coupon)
        if not coupon_obj.exists():
            messages.warning(request, 'Invalid coupon code')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        if cart_obj.coupon:
            messages.warning(request, 'Coupon already exists.')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        if cart_obj.get_cart_total() < coupon_obj[0].minimum_amount:
            messages.warning(request, f'Minimum amount to apply coupon is {coupon_obj[0].minimum_amount}')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        if coupon_obj[0].is_expired:
            messages.warning(request, 'Coupon is expired.')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        cart_obj.coupon = coupon_obj[0]
        cart_obj.save()
        
        messages.success(request, 'Coupon applied.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    context = {'cart': cart_obj}
    return render(request, 'accounts/cart.html', context)


@login_required
def remove_coupon(request, cart_id):
    cart = get_object_or_404(Cart, uid=cart_id)
    cart.coupon = None
    cart.save()
    messages.success(request, 'Coupon Removed')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def checkout(request):
    return render(request, 'accounts/checkout.html')


@login_required
def generate_invoice(request):
    try:
        cart = Cart.objects.get(user=request.user, is_paid=False)
        cart_total = cart.get_cart_total()
    except Cart.DoesNotExist:
        return HttpResponse("No active cart found for this user.", status=404)

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []

    styles = getSampleStyleSheet()
    title_style = styles['Title']
    normal_style = styles['BodyText']
    bold_style = ParagraphStyle('Bold', parent=styles['BodyText'], fontName='Helvetica-Bold')

    elements.append(Paragraph("Invoice Receipt", title_style))
    elements.append(Spacer(1, 0.5 * inch))

    elements.append(Paragraph(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d')}", normal_style))
    elements.append(Spacer(1, 0.2 * inch))

    elements.append(Paragraph(f"Customer Name: {request.POST.get('full_name')}", normal_style))
    elements.append(Paragraph(f"Address: {request.POST.get('address')}", normal_style))
    elements.append(Paragraph(f"City: {request.POST.get('city')}", normal_style))
    elements.append(Paragraph(f"Landmark: {request.POST.get('landmark', '')}", normal_style))
    elements.append(Paragraph(f"Order Note: {request.POST.get('order_note', '')}", normal_style))
    elements.append(Spacer(1, 0.2 * inch))

    data = [
        ['Customer Name', request.POST.get('full_name')],
        ['Address', request.POST.get('address')],
        ['City', request.POST.get('city')],
        ['Landmark', request.POST.get('landmark', '')],
        ['Order Note', request.POST.get('order_note', '')],
        ['Amount', f'Rs {cart_total}'],
        ['Payment Method', request.POST.get('payment')],
    ]

    table = Table(data, colWidths=[2.5 * inch, 4 * inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(table)

    doc.build(elements)
    pdf = buffer.getvalue()
    buffer.close()

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'
    return response
