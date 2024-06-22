from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from esi.routes.alliance import get_alliances_alliance_id
from esi.routes.character import get_characters_character_id
from esi.routes.corporation import get_corporations_corporation_id
from esi.routes.location import get_characters_character_id_location


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        character_id = self.request.user.id
        token = self.request.user.token

        character = get_characters_character_id(
            character_id=character_id,
        )
        corporation = get_corporations_corporation_id(
            corporation_id=character.corporation_id,
        )
        alliance = get_alliances_alliance_id(
            alliance_id=character.alliance_id,
        )
        location = get_characters_character_id_location(
            character_id=character_id,
            token=token,
        )

        context["character"] = character
        context["corporation"] = corporation
        context["alliance"] = alliance
        context["location"] = location
        return context
