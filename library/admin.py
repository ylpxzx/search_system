from django.contrib import admin
from library.models import Book, Borrowing, Reader,Movie

class BookAdmin(admin.ModelAdmin):
    list_display = ('ISBN','title','author','press','description','price','category','cover','index','location','quantity')
class MovieAdmin(admin.ModelAdmin):
    list_display = ('rate','title','movie_url','image','info')


class ReaderAdmin(admin.ModelAdmin):
    list_display =('user','name','phone','max_borrowing','balance','photo')


class BorrowingAdmin(admin.ModelAdmin):
    list_display = ('reader','ISBN','date_issued','date_due_to_returned','date_returned','amount_of_fine')


admin.site.register(Book,BookAdmin)
admin.site.register(Borrowing,BorrowingAdmin)
admin.site.register(Reader,ReaderAdmin)
admin.site.register(Movie,MovieAdmin)
admin.site.name = '图书、电影信息管理'
admin.site.site_header = '图书、电影信息管理'
