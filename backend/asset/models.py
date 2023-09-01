from django.db.models import Model, CharField, IntegerField, FloatField, BooleanField, DateField, ManyToManyField, ForeignKey, PROTECT
   
class Property(Model):
    name = CharField(max_length=200)

    def __str__(self):
        return self.name   

class Category(Model):
    name = CharField(max_length=200)

    def __str__(self):
        return self.name       
    
class Asset(Model):
    purchase_value = FloatField(null=True)
    code = IntegerField(null=True)
    propertys = ManyToManyField(Property)
    state = BooleanField(null=True)
    category = ForeignKey(Category, on_delete=PROTECT, null=True)
    purchase_date = DateField(null=True)
    useful_life = IntegerField(null=True)
    responsible = CharField(max_length=100, null=True)
    ubication = CharField(max_length=100, null=True)
    name = CharField(max_length=200, null=True)

    def __str__(self):
        return self.name