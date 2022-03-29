from django.db import models
from pytz import timezone
from datetime import datetime,timezone


# Create your models here.

class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=True)
    

class SoftDeleteModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, default=None)
    objects = SoftDeleteManager()
    all_objects = models.Manager()
    
    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = datetime.now(timezone.utc)
        self.save()
        
    def restore (self):
        self.is_deleted = False
        self.deleted_at = None
        self.save()
        
    class Meta:
        abstract = True
        
        

class CartItem(SoftDeleteModel):
    product_name = models.CharField(max_length=200)
    product_price = models.FloatField()
    product_quantity = models.PositiveIntegerField()
