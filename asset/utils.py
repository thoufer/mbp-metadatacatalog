from django_tables2 import SingleTableView, RequestConfig
from django.core.paginator import Paginator

class PagedFilteredTableView(SingleTableView):
    """
    Generic class from http://kuttler.eu/post/using-django-tables2-filters-crispy-forms-together/
    """
    filter_class = None
    formhelper_class = None
    context_filter_name = 'filter'

    def get_queryset(self, **kwargs):
        qs = super(PagedFilteredTableView, self).get_queryset()
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        self.filter.form.helper = self.formhelper_class()
        return self.filter.qs

    def get_table(self, **kwargs):
        table = super(PagedFilteredTableView, self).get_table()
        RequestConfig(self.request, paginate={'page': self.request.GET.get('page'),
                        'per_page': self.paginate_by}).configure(table)
        return table

    def get_context_data(self, **kwargs):
        context = super(PagedFilteredTableView, self).get_context_data()
        context[self.context_filter_name] = self.filter

        page = self.request.GET.get('page')
        context['record_start'] = context['paginator'].get_page(page).start_index()
        context['record_end'] =  context['paginator'].get_page(page).end_index()
        context['rowcount'] = context['paginator'].count

        return context
