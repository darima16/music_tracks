from decor_play import *

albums = []
with open('records.txt', encoding='utf-8') as f:
    for album in f.readlines():
        num = album.split(':')[0][0]
        title = album.split(':')[0].split('  ')[1]
        songs = album.split(':')[1].split('  ')
        singer = songs[0]
        year = songs[1]
        name = songs[2]
        time = songs[3][:-1]

        song = Album(num, title, singer, year, name, time)

        albums.append(song)

def commands():
    while True:
        command = input('Введите номер команды: ')
        try:
            command = int(command)
        except:
            pass

        if command in [1, 2, 3, 4, 5, 6]:
            return command
        else:
            print('Неверный ввод!')


def turn_on(num):

    for track in albums:
        if track.get_num() == num:
            track.turn_on()
            print('Музыка включена')


def turn_off():

    for track in albums:
        if track.work == True:
            track.turn_off()
        else:
            print('Музыка не играет')

def main():
    while True:
        print('1. Просомтр каталог аудизаписей \n'
              '2. Включить трек \n'
              '3. Поставить на паузу \n'
              '4. Повысить громкость \n'
              '5. Понизить громкость \n'
              '6. Выход')
        command = commands()

        if command == 1:
            print('|{:^5}|{:^20}|{:^15}|{:^15}|{:^15}|{:^15}|'.format('#','Название альбома', 'Исполнитель',
                                                            'Год выпуска', 'Название трека',
                                                             'В1ремя'))
            for album in albums:
                print(album)

        elif command == 2:
            num = int(input('Введите позицию аудизаписи '))
            print(turn_on(num))

        elif command == 3:
            turn_off()

        elif command == 4:
            for track in albums:
                if track.work:
                    if track.volume < 100:
                        track.value = 'up'
                        print('Громкомть увеличена')
                    else:
                        print('Это максимум')
                else:
                    print('Включите музыку!')

        elif command == 5:
            for track in albums:
                if track.work:
                    if track.volume > 25:
                        track.value = 'up'
                        print('Громкомть уменьшена')
                    else:
                        print('Это минимум')
                else:
                    print('Включите музыку!')
        else:
            break


if __name__ == '__main__':
    main()
