from django.views.generic import TemplateView

url(r'^static/', TemplateView.as_view(template_name="pdfExample.pdf"),
    name = "pdfExample"),