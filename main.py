#Класс Задачи
class Task():
    def __init__(self, description ="", deadline ="", status = False):
        self.description = description
        self.deadline = deadline
        self.status = status

    #Функция изменения статуса задачи
    def ready(self):
        self.status = True
        print("Задача выполнена.")

    #Функция отображения задачи
    def show(self):
        print(f"Задача: {self.description}, дедлайн: {self.deadline}")

my_task = []    #Список задач

#Функция добавления новой задачи
def add_task(description,deadline,status = False):
    task = Task(description, deadline, status)
    my_task.append(task)
    print("Задача добавлена")

#Функция отображения задач с желаемым статусом status
def view_tasks(status):
    s = "'Выполнено'" if status == True else "'Не выполнено'"
    print(f"Список задач со статусом {s}:")
    for t in my_task:
        if t.status == status:
            t.show()

add_task("Сходить в магазин","12.09.24 14:00")
add_task("Сделать задание в Зерокодер","13.09.24 12:00")
add_task("Помочь сделать уроки сыну","12.09.24 20:00")

view_tasks(False)
my_task[1].ready()
view_tasks(False)
view_tasks(True)