from pages.models import Page

def get_pages(requests):

    pages = Page.objects.filter(visible=True).order_by('order').values_list('id', 'title', 'slug')
    #pages = Page.objects.filter(visible=True).values_list('id', 'title', 'slug')
    #pages = Page.objects.values_list('title', flat=True)

    return {
        'pages': pages
    }