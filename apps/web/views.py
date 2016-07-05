from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.views.generic import View

from apps.web import celery_task


class MainView(View):
  def get(self, request):
    return TemplateResponse(request, 'apps/web/index.html')


class AddHitView(View):
  def get(self, request):
    data = celery_task.mul.delay(100, 400)
    print('data : ', data)
    return HttpResponseRedirect(reverse('main'))
