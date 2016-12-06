import os
import shutil

__author__ = 'Ivan Povalyaev'

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


def create_dir(dirname):
        try:
            os.mkdir(dirname)
            print('Директория "{}" успешно создана'.format(dirname))
        except FileExistsError:
            print('Ошибка. Невозможно создать директорию "{}"'.format(dirname))


def remove_dir(dirname):
        try:
            os.rmdir(dirname)
            print('Директория "{}" успешно удалена'.format(dirname))
        except FileNotFoundError:
            print('Ошибка. Невозможно удалить директорию "{}"'.format(dirname))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def show_dirs(directory=None):
    return sorted([x.name for x in os.scandir(directory) if x.is_dir()])

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def copy_self():
    filename = os.path.basename(__file__)
    copyname = '{}.copy'.format(filename)
    shutil.copy(filename, copyname)


if __name__ == '__main__':
    (create_dir('dir_{}'.format(x)) for x in range(1, 10))
    (remove_dir('dir_{}'.format(x)) for x in range(1, 10))
    dirs = show_dirs()
    if dirs:
        print('Список директорий в текущем каталоге:'
              ' {}'.format(', '.join(dirs)))
    copy_self()
