from django.db import models

class submitted_tasks(models.Model):
    employee_id = models.CharField(max_length = 10)
    client_id = models.CharField(max_length = 10)
    fund_id = models.CharField(max_length = 10)
    order_quantity = models.FloatField(max_length = 1000000000)
    order_date = models.DateField(max_length = 10)
    register_date = models.DateField(max_length = 10)
    confirmation_status = models.BooleanField(default = False)
    
    def __str__(self):
        return str(self.employee_id) + '::' + str(self.client_id) + '::' + str(self.fund_id) + '::' + str(self.order_quantity) + '::' + str(self.order_date)
    
class tasks_available(models.Model):
    fund_id = models.CharField(max_length = 10)
    start_date = models.DateField(max_length = 10)
    end_date = models.DateField(max_length = 10)
    order_type = models.CharField(max_length = 10)
    fund_valid_month = models.DateField(max_length = 10)
    
    def __str__(self):
        return str(self.fund_id)
    
class task_total(models.Model):
    task_quantity = models.FloatField(max_length = 1000000000)
    task_date = models.DateField(max_length = 10)
    
    def __str__(self):
        return str(self.task_quantity) + '::' + str(self.task_date)
    
class task_factor(models.Model):
    employee_id = models.CharField(max_length = 10)
    factor = models.CharField(max_length = 10)
    task_setting_month = models.DateField(max_length = 10)
    
    def __str__(self):
        return str(self.employee_id) + '::' + str(self.factor)
    
class fund_value(models.Model):
    fund_id = models.CharField(max_length = 10)
    net_value = models.CharField(max_length = 10)
    
    def __str__(self):
        return str(self.fund_id) + '::' + str(self.net_value)
    
    
class client_employee_relation(models.Model):
    client_id = models.CharField(max_length = 10)
    employee_id = models.CharField(max_length = 10)
    
    def __str__(self):
        return str(self.client_id) + '::' + str(self.employee_id)
    
class orders(models.Model):
    client_id = models.CharField(max_length = 10)
    fund_id = models.CharField(max_length = 10)
    order_quantity = models.CharField(max_length = 1000000000)
    order_date = models.DateField(max_length = 10)
    
    def __str__(self):
        return str(self.client_id) + '::' + str(self.fund_id) + '::' + str(self.order_quantity) + '::' + str(self.order_date)

class employee_info(models.Model):
    employee_id = models.CharField(max_length = 10)
    employee_name = models.CharField(max_length = 10)
    
    def __str__(self):
        return str(self.employee_id) + '::' + str(self.employee_name)
    
class client_info(models.Model):
    client_id = models.CharField(max_length = 10)
    client_name = models.CharField(max_length = 10)
    
    def __str__(self):
        return str(self.client_id) + '::' + str(self.client_name)