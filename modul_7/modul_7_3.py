
class WordsFinder:

    def __init__(self, *file_name):
        self.file_name = file_name

    def get_all_words(self):
        all_words = dict()
        for i_file_name in self.file_name:
            with open(i_file_name, 'r', encoding='utf-8') as file:
                str_file = file.read().lower().replace('\n', ' ')
                str_ = ''.join([str_file[i] for i in range(len(str_file)) if str_file[i] not in [',', '.', '=', '!', '?', ';', ':', ' - ']])
                list_ = str_.split(' ')
                all_words[i_file_name] = list_
        return all_words

    def find(self, word:str):
        find_word = dict()
        for key, value in self.get_all_words().items():
            find_word[key] = value.index(word.lower()) + 1
        return find_word

    def count(self, word:str):
        count_word = dict()
        for key, value in self.get_all_words().items():
            count_word[key] = value.count(word.lower())
        return count_word

if __name__ == '__main__':
    finder1 = WordsFinder('test_file.txt')
    print(finder1.get_all_words())
    print(finder1.find('captain'))
    print(finder1.count('captain'))