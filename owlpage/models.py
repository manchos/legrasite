from __future__ import unicode_literals

from wagtail.core.fields import StreamField
from wagtail.core.models import Page

from wagtail.admin.edit_handlers import StreamFieldPanel

from wagtail.core.blocks import RichTextBlock


class OwlPage(Page):
    body = StreamField(
        [('owl_paragraph', RichTextBlock(icon="fa-paragraph"))],
        verbose_name="Параграф-описание", blank=True, null=True,
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    def get_context(self, request):
        context = super(OwlPage, self).get_context(request)
        context['current_url'] = self.get_url()
        return context

    class Meta:
        verbose_name = "Страница по составу проекта"






