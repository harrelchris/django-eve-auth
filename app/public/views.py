from django.views.generic import TemplateView

from public.mixins import LogoutRequiredMixin


class IndexView(LogoutRequiredMixin, TemplateView):
    template_name = "public/index.html"
