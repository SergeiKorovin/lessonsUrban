import time as t

class UrTube:
    def __init__(self):
        self.users = {}
        self.videos = []
        self.current_user = None

    def log_in (self, nickname, password):
        if nickname in self.users:
            if hash(str(self.users[nickname][0])) == hash(password):
                self.current_user = nickname
            else:
                print('Такой пользователь не найден')

    def register (self, nickname, password, age):
        if nickname not in self.users:
            self.users[nickname] = (password, age)
            self.log_in(nickname, password)
        else:
            print(f'Пользователь {nickname} уже существует')

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        list_video = []
        for i_args in args:
            if i_args.title not in list_video:
                self.videos.append(i_args)
                list_video.append(i_args.title)

    def get_videos (self, word):
        get_video = []
        for i_videos in self.videos:
            if word.lower() in i_videos.title.lower():
                get_video.append(i_videos.title)
        return get_video

    def watch_video(self, film):
        if self.current_user != None:
            if self.users[self.current_user][1] >= 18:
                for i_video in self.videos:
                    if film == i_video.title:
                        for i in range(0, i_video.duration + 1):
                            print(i, end=' ')
                            t.sleep(0.5)
                        print('Конец видео')
            else:
                print('Вам нет 18 лет, пожалуйста покиньте страницу')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')


class Video:
    def __init__(self, title: str, duration: int, adult_mode=True):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = False


class User:
    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __eq__(self, other):
        return self.nickname == other.nickname and self.password == other.password

    def __hash__(self):
        return hash(str(self.password))

if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')

    # Попытка воспроизведения несуществующего видео
    # # ur.watch_video('Лучший язык программирования 2024 года!')


