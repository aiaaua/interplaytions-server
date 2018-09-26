from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view

import midi.api.generate
import midi.api.combine

app_name='midi'

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^api/doc', get_swagger_view(title='Rest API Document')),
    url(r'^api/v2/', midi.api.generate.generate_midi),
    url(r'^api/midi/(?P<seq>[0-9]+)/(?P<file_number>[0-9]+)/', midi.api.generate.generate_midi_one),
    url(r'^api/midi/combine/', midi.api.combine.combine_all),
    url(r'^api/test/(?P<seq>[0-9]+)/(?P<file_number>[0-9]+)/', midi.api.generate.request_test),
]