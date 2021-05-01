from .models import Sale
from django.db.models.signals import m2m_changed
from django.dispatch import receiver


@receiver(m2m_changed, sender=Sale.positions.through)
def calculate_total_price(sender, instance, action, **kwargs):
    print('action', action)

    total_price = 0
    if action == 'post_add' or action == 'post_remove':
        
        for item in instance.get_positions():
            # instance = object/record of model, get_position = add'l method in model
            # gonna loop thru each Position and get price value
            total_price += item.price

    # set now the record's total_price field value
    instance.total_price = total_price
    instance.save()