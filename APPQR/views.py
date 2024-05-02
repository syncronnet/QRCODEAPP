# views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
import qrcode
import os

from .forms import QRCodeForm

# QRCODEAPP/views.py

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse(request, 'qr.html')


def gerar_qrcode(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            link = form.cleaned_data['link']
            salvar_nome = form.cleaned_data['salvar_nome'] + ".png"  # Corrigido aqui
            
            # Create QR Code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(link)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")

            # Save QR Code to 'imagens' folder
            save_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'imagensQR')
            os.makedirs(save_dir, exist_ok=True)
            img_path = os.path.join(save_dir, salvar_nome)
            img.save(img_path)

            return redirect('gerar_qrcode')
    else:
        form = QRCodeForm()
    return render(request, 'qr.html', {'form': form})

# Create your views here.


# Create your views here.
