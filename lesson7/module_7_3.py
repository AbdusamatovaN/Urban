class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, 'r', encoding='utf-8') as file:
                word_list = []
                for line in file:
                    line = line.lower()
                    for s in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        line = line.replace(s, '')
                    word_list += line.split()
                all_words[i] = word_list
        return all_words

    def find(self, word):
        for name, words in self.get_all_words().items():
            for i, w in enumerate(words):
                if word.lower() == w:
                    return {name: i + 1}

    def count(self, word):
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                return {name: words.count(word.lower())}


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего


