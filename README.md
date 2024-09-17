# ACCUKNOX Django Project

## Project Overview

This repository contains the Django project for the "ACCUKNOX" assignment. The project demonstrates various aspects of Django signals and transactions, as well as implementing custom class behavior in Django views.

## Project Structure

- **Folder Name:** `Accunox_f`
- **Django Project Name:** `my_project`
- **Apps Defined:**
  - `question_1`
  - `question_2`
  - `question_3`
  - `Question_4`

## Questions and Answers

### Question 1: Default Execution of Django Signals

**Q:** By default, are Django signals executed synchronously or asynchronously?

**A:** By default, Django signals are executed synchronously. This means that when a signal is sent, the signal handlers are executed in the same thread and process as the code that triggered the signal.

**Flow Diagram:**
Sender ----> Signal Dispatcher ----> Receiver | | | | Model, View, etc.

**Supporting Code Snippet:**
```python
# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel

@receiver(post_save, sender=MyModel)
def my_handler(sender, instance, **kwargs):
    print("Signal handler executed")

# views.py
from django.http import HttpResponse
from .models import MyModel
import datetime

def create_model_instance(request):
    print(f"View started at {datetime.datetime.now()}")
    obj = MyModel.objects.create(name="Test Instance")
    print(f"View finished at {datetime.datetime.now()}")
    return HttpResponse("Check the console for timestamp logs")
```

###

### Question 2: Thread Execution of Django Signals
**Q:**: Do Django signals run in the same thread as the caller?

**A:**: Yes, Django signals run in the same thread as the caller. This means that the signal handlers are executed in the same thread as the request that triggered the signal.
**Supporting Code Snippet:**

```python
Copy code
# views.py
from django.http import HttpResponse
from django.contrib.auth.models import User

def trigger_signal_view(request):
    import threading
    print(f"Main Thread: {threading.current_thread().name}")
    user = User.objects.create(username="signal_test_user")
    return HttpResponse("Signal triggered, check your console output.")
```

### 

### Question 3: Django Transactions and Signal Behavior
**URLs**:
<ul>
  <li>
    Create User: http://127.0.0.1:8000/create-user/
  </li>
  <li>
    Update User: http://127.0.0.1:8000/update-user/
  </li>
  <li>
  Create User with Rollback: http://127.0.0.1:8000/create-user-with-rollback/
  </li>
</ul>
**Expected Behavior:**

Create User Profile: Creates a new UserProfile instance and returns a confirmation message.
Update User Profile: Updates an existing UserProfile instance or returns an error if the user doesn't exist.
Create User with Rollback: Attempts to create a new UserProfile but rolls back the transaction due to an error.
**Supporting Code Snippet:**

```
python
# views.py
from django.db import transaction
from .models import UserProfile

def create_user_with_rollback(request):
    try:
        with transaction.atomic():
            user = UserProfile.objects.create(name="Ashu Bhai", email="ashuu@example.com")
            raise Exception("Simulated rollback error")
    except Exception as e:
        return HttpResponse(f"Error: {e}")

```
###

### Question 4: Custom Rectangle Class
### Q: Create a Rectangle class with specified requirements.

A: Implement a Rectangle class that allows iteration and provides dimensions in a specified format.

**Supporting Code Snippet:**

```
python
Copy code
# models.py
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}
View URL: http://127.0.0.1:8000/rectangle/

```
###

### Setup Instructions
**Clone the Repository:**

```
git clone https://github.com/yourusername/Accunox_f.git
cd Accunox_f
Install Dependencies:

pip install -r requirements.txt
Apply Migrations:

python manage.py migrate

**Run the Development Server:**


python manage.py runserver
Visit the URLs Provided:

http://127.0.0.1:8000/create/
http://127.0.0.1:8000/trigger-signal/
http://127.0.0.1:8000/create-user/
http://127.0.0.1:8000/update-user/
http://127.0.0.1:8000/create-user-with-rollback/
http://127.0.0.1:8000/rectangle/

```
<ul>
  <li>
    Contact::
  </li>
  <li>
    Name: Ashu Tiwari
  </li>  
  <li>
    Email: cs21b007@iittp.ac.in
  </li>
</ul>


