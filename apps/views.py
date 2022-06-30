from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from apps.models import Organization


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        groups = self.request.user.rolegroup_set.all()
        orgs = [group.org for group in groups]
        context['orgs'] = orgs
        return context


class OrganizationHomeView(LoginRequiredMixin, TemplateView):
    template_name = "org_home.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        org = Organization.objects.get(id=kwargs["org_id"])
        context['org'] = org

        groups = org.rolegroup_set.all()
        for group in groups:
            if group.user.filter(id=self.request.user.id).exists():
                context['role'] = group.role
        return context
