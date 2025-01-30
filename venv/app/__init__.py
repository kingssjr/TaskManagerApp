# Inicializa o pacote app
from .database import Database
from .models import User, Task
from .views import TaskManagerView
from .controllers import TaskManagerController
from .utils import hash_password, verify_password