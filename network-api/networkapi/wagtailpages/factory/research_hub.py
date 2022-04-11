import random

import factory
import factory.fuzzy
import wagtail_factories

from networkapi.utility.faker import helpers as faker_helpers
from networkapi.wagtailpages import models as wagtailpage_models
from networkapi.wagtailpages.factory import documents as documents_factory
from networkapi.wagtailpages.factory import profiles as profiles_factory


class ResearchLandingPageFactory(wagtail_factories.PageFactory):
    class Meta:
        model = wagtailpage_models.ResearchLandingPage

    title = "Research"


class ResearchLibraryPageFactory(wagtail_factories.PageFactory):
    class Meta:
        model = wagtailpage_models.ResearchLibraryPage

    title = "Library"


class ResearchAuthorsIndexPageFactory(wagtail_factories.PageFactory):
    class Meta:
        model = wagtailpage_models.ResearchAuthorsIndexPage

    title = "Authors"


class ResearchDetailLinkFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = wagtailpage_models.ResearchDetailLink

    label = factory.Faker('text', max_nb_chars=30)
    url = ''
    document = None

    class Params:
        with_url = factory.Trait(
            url=factory.Faker('uri'),
        )
        with_document = factory.Trait(
            document=factory.SubFactory(documents_factory.DocumentFactory)
        )


class ResearchDetailPageFactory(wagtail_factories.PageFactory):
    class Meta:
        model = wagtailpage_models.ResearchDetailPage

    title = factory.Faker('text', max_nb_chars=50)
    research_links = factory.RelatedFactoryList(
        factory=ResearchDetailLinkFactory,
        factory_related_name='research_detail_page',
        size=lambda: random.randint(1, 2),
        with_url=True,
    )
    original_publication_date = factory.Faker('date_object')
    introduction = factory.Faker('text', max_nb_chars=300)

    @factory.lazy_attribute
    def overview(self):
        faker = faker_helpers.get_faker()
        return '\n\n'.join(faker.paragraphs(nb=3))

    @factory.lazy_attribute
    def collaborators(self):
        faker = faker_helpers.get_faker()
        names = []
        for _ in range(random.randint(1, 5)):
            names.append(faker.name())
        return "; ".join(names)


class ResearchRegionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = wagtailpage_models.ResearchRegion

    name = factory.Faker('country')


class ResearchTopicFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = wagtailpage_models.ResearchTopic

    name = factory.Faker('catch_phrase')
    description = factory.Faker('paragraph')


class ResearchAuthorRelationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = wagtailpage_models.ResearchAuthorRelation

    research_detail_page = factory.SubFactory(ResearchDetailPageFactory)
    author_profile = factory.SubFactory(profiles_factory.ProfileFactory)


class ResearchDetailPageResearchRegionRelationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = wagtailpage_models.ResearchDetailPageResearchRegionRelation

    research_detail_page = factory.SubFactory(ResearchDetailPageFactory)
    research_region = factory.SubFactory(ResearchRegionFactory)


class ResearchDetailPageResearchTopicRelationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = wagtailpage_models.ResearchDetailPageResearchTopicRelation

    research_detail_page = factory.SubFactory(ResearchDetailPageFactory)
    research_topic = factory.SubFactory(ResearchTopicFactory)


def generate(seed):
    faker_helpers.reseed(seed)
    home_page = faker_helpers.get_homepage()

    print("Generating research hub")

    # Only one landing page can exist
    research_landing_page = wagtailpage_models.ResearchLandingPage.objects.first()
    if not research_landing_page:
        research_landing_page = ResearchLandingPageFactory.create(parent=home_page)

    # Only one library page can exist
    research_library_page = wagtailpage_models.ResearchLibraryPage.objects.first()
    if not research_library_page:
        research_library_page = ResearchLibraryPageFactory.create(parent=research_landing_page)

    # Only one authors index page can exist
    research_authors_index_page = wagtailpage_models.ResearchAuthorsIndexPage.objects.first()
    if not research_authors_index_page:
        research_authors_index_page = ResearchAuthorsIndexPageFactory.create(parent=research_landing_page)

    for _ in range(4):
        ResearchRegionFactory.create()
        ResearchTopicFactory.create()

    for _ in range(6):
        research_detail_page = ResearchDetailPageFactory.create(parent=research_library_page)

        for profile in faker_helpers.get_random_objects(model=wagtailpage_models.Profile, max_count=3):
            ResearchAuthorRelationFactory.create(
                research_detail_page=research_detail_page,
                author_profile=profile,
            )

        for region in faker_helpers.get_random_objects(model=wagtailpage_models.ResearchRegion, max_count=2):
            ResearchDetailPageResearchRegionRelationFactory.create(
                research_detail_page=research_detail_page,
                research_region=region,
            )

        for topic in faker_helpers.get_random_objects(model=wagtailpage_models.ResearchTopic, max_count=2):
            ResearchDetailPageResearchTopicRelationFactory.create(
                research_detail_page=research_detail_page,
                research_topic=topic,
            )
