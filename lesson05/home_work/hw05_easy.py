import os
import shutil

__author__ = 'Ivan Povalyaev'

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


def create_dirs():
    for x in ('dir_{}'.format(x) for x in range(1, 10)):
        try:
            os.mkdir(x)
        except FileExistsError:
            print('Error. Directory "{}" already exists.'.format(x))


def remove_dirs():
    for x in ('dir_{}'.format(x) for x in range(1, 10)):
        try:
            os.rmdir(x)
        except FileNotFoundError:
            print('Error. Directory "{}" not found'.format(x))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def show_dirs():
    return sorted([x.name for x in os.scandir() if x.is_dir()])

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def copy_self():
    filename = os.path.basename(__file__)
    copyname = '{}.copy'.format(filename)
    shutil.copy(filename, copyname)


if __name__ == '__main__':
    create_dirs()
    remove_dirs()
    dirs = show_dirs()
    if dirs:
        print('Список директорий в текущем каталоге:'
              ' {}'.format(', '.join(dirs)))
    copy_self()
