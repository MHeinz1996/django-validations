from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as text
from django.utils import timezone

def validate_stroke_type(stroke):
    valid_strokes = ['front crawl', 'butterfly', 'breast', 'back', 'freestyle']
    if stroke not in valid_strokes:
        raise ValidationError(text(f"{stroke} is not valid. Please select a valid stroke: {valid_strokes}"))

def validate_distance(distance):
    if distance < 50:
        raise ValidationError(text(f"{distance} is not valid. Please enter a distance greater than 50."))

def validate_record_date(record_date):
    if record_date > timezone.now():
        raise ValidationError(text(f"record date cannot be in the future."))

def validate_record_broken_date(record_broken_date, record_date):
    if record_broken_date < record_date:
        raise ValidationError(text(f"record can't be broken before the record is set."))

class SwimRecord(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    team_name = models.CharField(max_length=255)
    relay = models.BooleanField()
    stroke = models.CharField(max_length=255, validators=[validate_stroke_type])
    distance = models.IntegerField(validators=[validate_distance])
    record_date = models.DateTimeField(validators=[validate_record_date])
    record_broken_date = models.DateTimeField(validators=[validate_record_broken_date])


