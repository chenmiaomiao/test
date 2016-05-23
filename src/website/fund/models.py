from django.db import models

class submitted_tasks(models.Model):
    employee_id = models.CharField(max_length = 10)
    client_id = models.CharField(max_length = 10)
    quantity = models.FloatField(max_length = 1000000000)
    order_date = models.CharField(max_length = 10)
    register_date = models.CharField(max_length = 10)
    confirmation_status = models.BooleanField(default = False)
    
class task_list(models.Model):
    fund_id = models.CharField(max_length = 10)
    start_date = models.DateField(max_length = 10)
    end_date = models.DateField(max_length = 10)
    order_type = models.CharField(max_length = 10)
    fund_valid_date = models.DateField(max_length = 10)
    
class task_per_month(models.Model):
    task_quantity = models.FloatField(max_length = 1000000000)
    task_date = models.DateField(max_length = 10)
    
class task_factor(models.Model):
    employee_id = models.CharField(max_length = 10)
    factor = models.CharField(max_length = 10)
    task_valid_date = models.DateField(max_length = 10)

class fund_value(models.Model):
    fund_id = models.CharField(max_length = 10)
    net_value = models.CharField(max_length = 10)

class client_employee_relation(models.Model):
    client_id = models.CharField(max_length = 10)
    employee_id = models.CharField(max_length = 10)

class order_list(models.Model):
    client_id = models.CharField(max_length = 10)
    fund_id = models.CharField(max_length = 10)
    quantity = models.CharField(max_length = 1000000000)
    order_date = models.DateField(max_length = 10)

class employee_info(models.Model):
    employee_id = models.CharField(max_length = 10)
    employee_name = models.CharField(max_length = 10)

class client_info(models.Model):
    client_id = models.CharField(max_length = 10)
    client_name = models.CharField(max_length = 10)