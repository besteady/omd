from typing import List
from collections import Counter
from itertools import chain
from math import log


class CountVectorizer:
    def __init__(self):
        self.feature_names = None

    def fit_transform(self, corpus: List[str]) -> List[List[float]]:
        tbl = [row.lower().split() for row in corpus]

        self.feature_names = Counter(chain(*tbl)).keys()

        matr: List[List[float]] = []
        for row in tbl:
            d = dict.fromkeys(self.feature_names, 0)
            d.update(Counter(row))
            matr.append(list(d.values()))

        return matr

    def get_feature_names(self):
        return list(self.feature_names)


class TfidfTransformer:
    def __init__(self) -> None:
        self.count_matrix: List[List[float]] = []

    def tf_transform(self) -> List[List[float]]:
        tf_transformed = []

        for row in self.count_matrix:
            div_val = sum([1 if x > 0 else 0 for x in row])
            tf_row = [x / div_val for x in row]
            tf_transformed.append(tf_row)

        return tf_transformed

    def idf_transform(self) -> List[float]:
        idf_transformed = []

        all_docs = len(self.count_matrix)

        for col_ind in range(len(self.count_matrix[0])):
            count = 0
            for row_ind in range(len(self.count_matrix)):
                if self.count_matrix[row_ind][col_ind] > 0:
                    count += 1
            idf_transformed.append(log((all_docs + 1) / (count + 1)) + 1)

        return idf_transformed

    def fit_transform(self, count_matrix: List[List[float]]):
        self.count_matrix = count_matrix

        res = []
        tf_transformed = self.tf_transform()
        idf_transformed = self.idf_transform()

        for tf_row in tf_transformed:
            res.append([tf * idf for idf, tf in zip(idf_transformed, tf_row)])

        return res


class TfidfVectorizer(CountVectorizer):
    def __init__(self) -> None:
        self.transformer = TfidfTransformer()
        super().__init__()

    def fit_transform(self, corpus: List[str]) -> List[List[float]]:
        count_matrix = super().fit_transform(corpus)
        return self.transformer.fit_transform(count_matrix)


if __name__ == "__main__":
    corpus = [
        "Crock Pot Pasta Never boil pasta again",
        "Pasta Pomodoro Fresh ingredients Parmesan to taste",
    ]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)

    assert vectorizer.get_feature_names() == [
        "crock",
        "pot",
        "pasta",
        "never",
        "boil",
        "again",
        "pomodoro",
        "fresh",
        "ingredients",
        "parmesan",
        "to",
        "taste",
    ], f"{vectorizer.get_feature_names()}"

    # pprint(tfidf_matrix)

    assert tfidf_matrix == [
        [
            0.23424418468469405,
            0.23424418468469405,
            0.3333333333333333,
            0.23424418468469405,
            0.23424418468469405,
            0.23424418468469405,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
        ],
        [
            0.0,
            0.0,
            0.14285714285714285,
            0.0,
            0.0,
            0.0,
            0.20078072972973776,
            0.20078072972973776,
            0.20078072972973776,
            0.20078072972973776,
            0.20078072972973776,
            0.20078072972973776,
        ],
    ], f"{tfidf_matrix}"
