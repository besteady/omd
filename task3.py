from typing import List


class CountVectorizer():
    def __init__(self):
        self.feature_names = []

    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        unique_words = []

        tbl = [row.lower().split() for row in corpus]

        for row in tbl:
            for x in row:
                if x not in unique_words:
                    unique_words.append(x)

        self.feature_names = list(unique_words)

        matr = []
        for row in tbl:
            matr.append(list(map(lambda x: row.count(x), self.feature_names)))

        return matr

    def get_feature_names(self):
        return self.feature_names


if __name__ == "__main__":
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]

    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)

    assert vectorizer.get_feature_names() == \
        ['crock', 'pot', 'pasta', 'never',
         'boil', 'again', 'pomodoro', 'fresh', 'ingredients', 'parmesan', 'to',
         'taste'], f'{vectorizer.get_feature_names()}'

    assert count_matrix == [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0], [
        0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]], f'{count_matrix}'
