from django.db import models


class Transaction(models.Model):
    meter_no = models.CharField(max_length=100)
    token = models.CharField(max_length =100)
    date = models.CharField(max_length=100)
    units = models.CharField(max_length=100)
    amount = models.CharField(max_length =100)
    token_amount = models.CharField(max_length =100)
    vat = models.CharField(max_length =100)
    fuel_energy_charge = models.CharField(max_length =100)
    forex_charge = models.CharField(max_length =100)
    Epra_charge = models.CharField(max_length =100)
    warma_charge = models.CharField(max_length =100)
    rep_charge = models.CharField(max_length =100)
    inflation_adjustment = models.CharField(max_length =100)

    def __str__(self):
        return self.meter_no + '  -  units: ' + self.units

class Consumption_Data(models.Model):
    meter_no = models.CharField(max_length = 100)
    current_units_balance = models.CharField(max_length = 100)
    cumulative_usage = models.CharField(max_length = 100)
    saved_date = models.CharField(max_length = 100)

    

    def __str__(self):
        return self.meter_no
