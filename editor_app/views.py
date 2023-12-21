from django.shortcuts import render
from PIL import Image
from rembg import remove
from django.http import HttpResponse
import base64
from django.http import HttpResponse
from io import BytesIO

def process_image(request):
    if request.method == 'POST':
        input_image = request.FILES['input_image']
        input_image = Image.open(input_image)

        output_image = remove(input_image)

        
        output_image_base64 = None
        with BytesIO() as output_buffer:
            output_image.save(output_buffer, format='PNG')
            output_image_base64 = base64.b64encode(output_buffer.getvalue()).decode('utf-8')

        return render(request, 'process_image.html', {'output_image_base64': output_image_base64})

    return render(request, 'process_image.html')


def download_image(request):
    
    output_image = None 

    if output_image:
        response = HttpResponse(content_type='image/png')
        response['Content-Disposition'] = 'attachment; filename=output.png'
        output_image.save(response, format='PNG')
        return response

    return HttpResponse("Error: No processed image available.")
