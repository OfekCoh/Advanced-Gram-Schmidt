# from django.db import models

# Create your datebase objects here.



# class ToDoList(models.Model):
#     name=models.CharField(max_length=200)

#     def __str__(self):
#         return self.name 
    

# class Item(models.Model):
#     todolist= models.ForeignKey(ToDoList, on_delete=models.CASCADE) #if we delete todolist we delete the items- thats the casacde thing
#     text=models.CharField(max_length=300)
#     complete= models.BooleanField()

#     def __str__(self):
#         return self.text
    


# because we made Item be "in relation" with ToDoList then ToDoList now has a set of items

#create a todolist:
#  o= ToDoList(name="Ofek")
# o.save()

#add item to the list
# o.item_set.create(text="finish first web-app", complete=False)

#o.item_set.all()    .get(id=#)   