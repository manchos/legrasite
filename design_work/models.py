from django.db import models
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page, Collection
from home.blocks import ImageBlock, BaseStreamBlock
from design_work.aux import get_table_list


from pytils.translit import slugify

from wagtail.admin.edit_handlers import (
    FieldPanel, MultiFieldPanel, StreamFieldPanel
    )
from wagtail.images.edit_handlers import ImageChooserPanel
# Create your models here.
from wagtail.search import index
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class DesignWorkPage(Page):
    """
    Detail view for a specific DesignWork
    """
    description = RichTextField(
        help_text='Text to describe the page',
        blank=True,
        verbose_name="Описание",
    )
    # image = models.ForeignKey(
    #     'wagtailimages.Image',
    #     null=True,
    #     blank=True,
    #     on_delete=models.SET_NULL,
    #     related_name='+',
    #     verbose_name="Основное изображение",
    #     help_text='Landscape mode only; horizontal width between 1000px and 3000px.'
    # )

    sequence_number = models.PositiveSmallIntegerField(
        blank=True,
        verbose_name="Номер по порядку",
        null=True,
    )

    body = StreamField(
        [('image_block', ImageBlock())], verbose_name="Дополнительные изображения", blank=False,
    )
    # We include related_name='+' to avoid name collisions on relationships.
    # e.g. there are two FooPage models in two different apps,
    # and they both have a FK to bread_type, they'll both try to create a
    # relationship called `foopage_objects` that will throw a valueError on
    # collision.

    content_panels = Page.content_panels + [
        FieldPanel('description', classname="full"),
        FieldPanel('sequence_number'),
        # ImageChooserPanel('image'),
        StreamFieldPanel('body'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    parent_page_types = ['DesignWorkIndexPage']

    def get_context(self, request):
        context = super(DesignWorkPage, self).get_context(request)

        # designs = self.paginate(request, self.get_designs())
        # designs = self.get_designs()
        context['designs'] = get_table_list(self.body, columns=4, rows=3)
        return context

    def save(self, *args, **kwargs):
        if self.slug:
            self.slug = slugify(self.slug)
        else:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Дизайн страница'
        verbose_name_plural = 'Дизайн страницы'



class DesignWorkIndexPage(Page):
    menu_label = 'Страница с таблицей изображений без перехода'

    introduction = models.TextField(
        help_text='Text to describe the page',
        blank=True)

   # image = models.ForeignKey(
    #     'wagtailimages.Image',
    #     null=True,
    #     blank=True,
    #     on_delete=models.SET_NULL,
    #     related_name='+',
    #     help_text='Landscape mode only; horizontal width between 1000px and '
    #     '3000px.'
    # )

    content_panels = Page.content_panels + [
        FieldPanel('introduction', classname="full"),
        # ImageChooserPanel('image'),
    ]

    subpage_types = ['DesignWorkPage']

    # Returns a queryset of Page objects that are live, that are direct
    # descendants of this index page with most recent first
    def get_designs(self):
        # return DesignWorkPage.objects.live().descendant_of(
        #     self).order_by('-first_published_at')
        return DesignWorkPage.objects.live().descendant_of(self).order_by('sequence_number')

    # Allows child objects (e.g. DesignWorkPage objects) to be accessible via the
    # template. We use this on the HomePage to display child items of featured
    # content
    def children(self):
        return self.get_children().specific().live()

    # Pagination for the index page. We use the `django.core.paginator` as any
    # standard Django app would, but the difference here being we have it as a
    # method on the model rather than within a view function
    def paginate(self, request, *args):
        page = request.GET.get('page')
        paginator = Paginator(self.get_breads(), 12)
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)
        return pages

    # Returns the above to the get_context method that is used to populate the
    # template
    def get_context(self, request):
        context = super(DesignWorkIndexPage, self).get_context(request)

        # designs = self.paginate(request, self.get_designs())
        designs = self.get_designs()
        context['designs'] = get_table_list(designs, columns=4, rows=3)
        context['mount'] = len(designs)
        return context

    # class Meta:
        # verbose_name = 'Страница с таблицей изображений без перехода'
        # verbose_name_plural = 'Авторы'

