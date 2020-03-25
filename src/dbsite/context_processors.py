
from django.db.models import Count, Q

from journal.models import Category, Tag


def common(request):
    context = {
        'categories': Category.objects.annotate(
            num_journals=Count('journal', filter=Q(journal__is_public=True))),
        'tags': Tag.objects.annotate(
            num_journals=Count('journal', filter=Q(journal__is_public=True))),
    }
    return context





