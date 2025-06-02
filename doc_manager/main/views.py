from django.shortcuts import render, redirect
from django.http import JsonResponse
from main.forms import UploadForm
from .models import Album, Customer, Object
import openpyxl
import re


def extract_inventory_number(filename):
    match = re.search(r'М-\d{6}', filename)
    return match.group(0) if match else None


def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            wb = openpyxl.load_workbook(request.FILES['file'])
            ws = wb.active
            for row in ws.iter_rows(min_row=2, values_only=True):
                (customer_name, object_name, doc_type_str,
                 volume, album_name, filename) = row
                try:
                    volume_str = str(volume).replace(',', '.')
                    volume = float(volume_str)
                except (ValueError, TypeError):
                    volume = None
                customer, _ = Customer.objects.get_or_create(
                    name=customer_name
                )
                obj, _ = Object.objects.get_or_create(
                    name=object_name
                )
                doc_type_map = {'КЖ': 1, 'КМ': 2, 'АР': 3}
                try:
                    doc_type = doc_type_map.get(doc_type_str)
                except ValueError:
                    doc_type = None
                inventory_number = filename
                Album.objects.create(
                    customer=customer,
                    object=obj,
                    name=album_name,
                    doc_type=doc_type,
                    volume=volume,
                    filename=filename,
                    inventory_number=extract_inventory_number(inventory_number)
                )
            return redirect('album_list')
    else:
        form = UploadForm()
    return render(request, 'main/upload.html', {'form': form})


def album_list(request):
    customers = Customer.objects.all()
    objects = Object.objects.all()
    return render(request, 'main/album_list.html', {
        'customers': customers,
        'objects': objects,
    })


def album_data(request):
    customer_id = request.GET.get('customer')
    object_id = request.GET.get('object')
    doc_type = request.GET.get('doc_type')

    albums = Album.objects.select_related('customer', 'object').all()

    if customer_id:
        albums = albums.filter(customer_id=customer_id)
    if object_id:
        albums = albums.filter(object_id=object_id)
    if doc_type:
        albums = albums.filter(doc_type=doc_type)

    data = list(albums.values(
        'customer__name', 'object__name', 'name',
        'doc_type', 'volume', 'filename', 'inventory_number'
    ))

    data = [
        {
            'customer__name': album.customer.name,
            'object__name': album.object.name,
            'name': album.name,
            'doc_type': album.get_doc_type_display(),
            'volume': album.volume,
            'filename': album.filename,
            'inventory_number': album.inventory_number,
        } for album in albums
    ]
    return JsonResponse(data, safe=False)
