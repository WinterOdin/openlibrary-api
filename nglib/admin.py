from django.contrib import admin
from .models import SearchStats
from django.contrib.admin import ModelAdmin, SimpleListFilter


class RangeFilter(SimpleListFilter):
    title = 'amount filter'
    parameter_name = 'amount'

    def lookups(self, request, model_admin):    
        return ('1', '0-5'),('2', '5-10'), ('3', '10-15'), ('4', '15-20'), ('5', '20-35'), ('6', '35-55')

    def queryset(self, request, queryset):
        filt_amount = request.GET.get('amount')
        amount_dict = dict(self.lookups(None, None))
        if amount_dict.get(filt_amount):
            limiters = amount_dict[filt_amount].split('-')
            return queryset.filter(amount__range=(int(limiters[0]), int(limiters[1])))
        return queryset

        return queryset.filter(amount__range=dict(self.lookups(None, None))[filt_amount])


@admin.register(SearchStats)
class SearchStatsAdmin(admin.ModelAdmin):
    list_display = ('surname', 'author_id', 'amount',)
    search_fields = ('surname', 'author_id',)
    list_filter = (RangeFilter,)