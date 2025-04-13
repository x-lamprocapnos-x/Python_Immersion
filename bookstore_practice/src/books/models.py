from django.db import models

# Genre choices

genre_choices = (
    ('classic', 'Classing'),
    ('romantic', 'Romantic'),
    ('comic', 'Comic'),
    ('fantasy', 'Fantasy'),
    ('horror', 'Horror'),
    ('educational', 'Educational')
)

book_type_choices = (
    ('hardcover', 'Hard cover'),
    ('ebook', 'E-Book'),
    ('audiobook', 'Audiobook')
)

class Book (models.Model):
    name = models.CharField(max_length=120)
    price = models.FloatField(help_text='in US dollars $')
    genre = models.CharField(max_length=12, choices=genre_choices, default='cl')
    book_type = models.CharField(max_length=12, choices=book_type_choices, default='hc')

    def __str__(self):
        return str(self.name)
