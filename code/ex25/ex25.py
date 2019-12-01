def break_words(stuff):
    """この関数は、文章を単語に分割する。"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """単語を並べ替える。"""
    return sorted(words)

def print_first_word(words):
    """最初の単語を取り除いて、出力する。"""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """最後の単語を取り除いて、出力する。"""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """文章を受け取り、単語を並べ替えて返す。"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """文章の最初と最後の単語を出力する。"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """文章の単語を並べ替えて、最初と最後の単語を出力する。"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
