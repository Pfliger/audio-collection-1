class Track:
    def __init__(self, name='', duration=0):
        self.name = name
        self.duration = duration

    def __str__(self):
        return f'{self.name} - {self.duration} мин'

    def __gt__(self, other):
        return self.duration > other.duration


class Album:
    def __init__(self, name='', group=''):
        self.name = name
        self.group = group
        self.tracks_list = []

    def get_tracks(self):
        for track in self.tracks_list:
            print(str(track))
        return ' '

    def __str__(self):
        result = 'Название группы: "' + self.group + '"\nНазвание альбома: "' + self.name + '"\nTracks:'
        for track in self.tracks_list:
          result += f'\n{str(track)}'
        return result

    def album_duration(self):
        result = 0
        for track in self.tracks_list:
            result += track.duration
        return result

    def add_track(self, track):
        self.tracks_list.append(track)


albums_list = []
album = Album('Infest', 'Papa Roach')
album.tracks_list = [Track('Infest', 4), Track('Last Resort', 3), Track('Broken Home', 4)]
albums_list.append(album)

album = Album('Conspiracy of One', 'Offspring')
album.tracks_list = [Track('Come Out Swinging', 2), Track('Original Prankster', 4), Track('Want You Bad', 3)]
albums_list.append(album)


def show_albums(albums_list):
    for album in albums_list:
        print(f'Название альбома: "{album.name}", исполнитель "{album.group}"')
    return ' '


def show_tracks(albums_list):
    user_input = input('Введите название альбома: ')
    for album in albums_list:
      if user_input != album.name:
        continue
      else :
        print(str(album))
        return ' '
    return 'Такого альбома не найдено'


def track_add(albums_list):
    user_input = input('Введите название альбома: ')
    for album in albums_list:
        if user_input != album.name:
            continue
        else:
            new_track = input('Введите название трека: ')
            new_duration = int(input('введите длительность трека: '))
            album.add_track(Track(new_track, new_duration))
            return ' '
    return 'Такого альбома не найдено'

# реализация магического метода сравнения
track1 = Track('Bohemian rhapsody', 6)
track2 = Track('The show must go on', 4)
print('track1: ' + str(track1) + '\ntrack2: ' + str(track2))
print(f'track1 больше чем track2: {track1 > track2} \n')



def main():
    help = 'Список команд: \nalbum - показывает список всех альбомов \ntracks - выводит список всех треков в альбоме' \
           ', их длительность и длительность всего альбома \nadd - позволяет добавить трек в указаный альбом. \nhelp - ' \
           'вызов справки \nquit - выход из приложения'
    print(help)
    while True:
        user_input = input('\nВведите команду: ')
        if user_input == 'album':
            print(show_albums(albums_list))
        elif user_input == 'tracks':
            print(show_tracks(albums_list))
        elif user_input == 'add':
            print(track_add(albums_list))
        elif user_input == 'help':
            print(help)
        elif user_input == 'quit':
            print('\nДо свидания!')
            break
        else:
            print('\nтакой команды нет в списке.')

main()
