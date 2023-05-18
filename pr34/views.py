import io
import os

from PyPDF2 import PdfFileMerger, PdfMerger
from django.core.files.base import ContentFile
from django.http import FileResponse, HttpResponse
from django.shortcuts import render
from django.views import View
import reportlab
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus.para import Paragraph


class GenPdf(View):

    def get(self, request):
        return render(request, "pr34/pdfgen.html")

    def post(self, request):
        text = request.POST.get('text')

        merger = PdfMerger()
        path_to_pdfs = r"pdfs/"
        count = 0
        for root, dirs, file_names in os.walk(path_to_pdfs):
            for file_name in file_names:
                merger.append(path_to_pdfs + file_name)
                count = count + 1
        newname = f"oleg123{count}.pdf"
        pdf_buffer = io.BytesIO()
        pdf = canvas.Canvas(filename=f"pdfs/{newname}")
        pdf2 = canvas.Canvas(pdf_buffer)
        pdf.drawString(200, 700, text)
        pdf2.drawString(200, 700, text)
        pdf2.showPage()
        pdf.save()
        merger.append(f"pdfs/{newname}")
        merger.write("merged_all_pdfs.pdf")
        merger.close()
        pdf2.save()
        pdf_buffer.seek(0)
        pdf_to_return = open("merged_all_pdfs.pdf", 'r')
        pdf_content = pdf_to_return.read()
        pdf_to_return.close()
        return HttpResponse(pdf_content, content_type="application/pdf")
        #return FileResponse(pdf_buffer, as_attachment=True, filename="mypdf.pdf")

