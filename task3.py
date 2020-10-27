from typing import List, Counter, OrderedDict
from collections import Counter, OrderedDict
from itertools import chain


class OrderedCounter(Counter, OrderedDict):
    pass


class CountVectorizer():
    def __init__(self):
        self.feature_names = None

    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        tbl = [row.lower().split() for row in corpus]

        self.feature_names = OrderedCounter(chain(*tbl)).keys()

        matr = []
        for row in tbl:
            d = OrderedDict().fromkeys(self.feature_names, 0)
            d.update(Counter(row))
            matr.append(list(d.values()))

        return matr

    def get_feature_names(self):
        return list(self.feature_names)


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
