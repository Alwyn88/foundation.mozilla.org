from django import http, shortcuts
from django.utils import text as text_utils
from wagtail.core import models as wagtail_models
from wagtail.contrib.routable_page import models as routable_models

from networkapi.wagtailpages.pagemodels.mixin import foundation_metadata
from networkapi.wagtailpages.pagemodels import profiles


class ResearchAuthorsIndexPage(
    routable_models.RoutablePageMixin,
    foundation_metadata.FoundationMetadataPageMixin,
    wagtail_models.Page,
):
    max_count = 1
    parent_page_types = ['ResearchLandingPage']


    def get_context(self, request):
        context = super().get_context(request)
        context["author_profiles"] = profiles.Profile.objects.all()
        return context

    @routable_models.route(r'^(?P<profile_id>[0-9]+)/(?P<profile_slug>[-a-z]+)/$')
    def author_detail(self, request: http.HttpRequest, profile_id: str, profile_slug: str):
        author_profile = shortcuts.get_object_or_404(
            profiles.Profile,
            id=int(profile_id),
        )
        if not text_utils.slugify(author_profile.name) == profile_slug:
            raise http.Http404('Slug does not match id')

        return self.render(
            request=request,
            template='wagtailpages/research_author_detail_page.html',
            context_overrides={'author_profile': author_profile},
        )

