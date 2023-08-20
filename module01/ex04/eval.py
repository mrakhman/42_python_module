def is_valid(coefs, words):
        if len(coefs) != len(words):
            return False

        if not isinstance(coefs, list) \
        or not isinstance(words, list) \
        or not all(isinstance(el, float) for el in coefs) \
        or not all(isinstance(el, str) for el in words):
            return False
        return True

class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        if not is_valid(coefs, words):
            print(-1)
            return -1

        zipped = zip(coefs, words)
        res = 0
        for el in zipped:
            res += el[0] * len(el[1])
        print(res)
        return res

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if not is_valid(coefs, words):
            print(-1)
            return -1

        res = 0
        for i, coef in enumerate(coefs):
            res += coef * len(words[i])
        print(res)
        return res


if __name__ == '__main__':
    ## zip_evaluate
    print("zip_evaluate:")
    # Correct
    coefs1 = [1., 2., 1., 4., 0.5]
    words1 = ['Le', 'Lorem', 'Ipsum', 'est', 'simple']
    Evaluator.zip_evaluate(coefs1, words1)

    # -1: lists should be of the same size
    coefs2 = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
    words2 = ["Le", "Lorem", "Ipsum", "n`", "est", "pas", "simple"]
    Evaluator.zip_evaluate(coefs2, words2)

    # -1: type of all coefs should be float
    coefs3 = [0.0, -1.0, 1, -12.0, 0.0, 42]
    words3 = ["Le", "Lorem", "Ipsum", "est", "pas", "simple"]
    Evaluator.zip_evaluate(coefs2, words2)

    # -1: type of all words should be str
    coefs4 = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
    words4 = ["Le", "Lorem", "Ipsum", "est", "pas", 1.0]
    Evaluator.zip_evaluate(coefs2, words2)

    print()

    ## enumerate_evaluate
    print("enumerate_evaluate:")
    # Correct
    coefs1 = [1., 2., 1., 4., 0.5]
    words1 = ['Le', 'Lorem', 'Ipsum', 'est', 'simple']
    Evaluator.enumerate_evaluate(coefs1, words1)

    # -1: lists should be of the same size
    coefs2 = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
    words2 = ["Le", "Lorem", "Ipsum", "n`", "est", "pas", "simple"]
    Evaluator.enumerate_evaluate(coefs2, words2)

    # -1: type of all coefs should be float
    coefs3 = [0.0, -1.0, 1, -12.0, 0.0, 42]
    words3 = ["Le", "Lorem", "Ipsum", "est", "pas", "simple"]
    Evaluator.enumerate_evaluate(coefs2, words2)

    # -1: type of all words should be str
    coefs4 = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
    words4 = ["Le", "Lorem", "Ipsum", "est", "pas", 1.0]
    Evaluator.enumerate_evaluate(coefs2, words2)

