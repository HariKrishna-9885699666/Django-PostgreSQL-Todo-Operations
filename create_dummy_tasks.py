import os
import django
from faker import Faker

# Setup Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo.settings')
django.setup()

from todoplayground.models import TodoItem

fake = Faker()

def create_random_ToDoItem(n):
    for _ in range(n):
        task = fake.sentence(nb_words=10)

        todo = TodoItem(
            task=task,
        )
        todo.save()

if __name__ == "__main__":
    create_random_ToDoItem(100)
    print("100 random tasks created successfully!")