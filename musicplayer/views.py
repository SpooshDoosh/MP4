from django.shortcuts import render
from django.views.generic import TemplateView
from .models import MusicPlayer

# Create your views here.


class RenderHTMLPlayer(TemplateView):
    template_name = 'music_player.html'
    model = MusicPlayer

    def get(self, request, *args, **kwargs):
        id = self.kwargs.get('id')
        song = MusicPlayer.objects.filter(id=id).first()
        song_uri = '/media' + \
            request.build_absolute_uri(podcast.file.url).split('media')[1]

        context = {'track_url': track_uri}
        return render(request, self.template_name, context)
