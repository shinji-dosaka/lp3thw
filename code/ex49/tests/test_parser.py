import pytest
from ex48 import parser

def test_sentence():
    s = parser.Sentence(('noun', 'bear'),
                         ('verb', 'eat'),
                         ('noun', 'honey'))
    assert s.subject == 'bear'
    assert s.verb == 'eat'
    assert s.object == 'honey'

def test_peeks():
    assert parser.peek([]) is None
    word_list = [('noun', 'bear'),
                 ('verb', 'eat'),
                 ('noun', 'honey')]
    assert parser.peek(word_list) == 'noun'

def test_matches():
    assert parser.match([], 'noun') is None
    word_list = [('noun', 'bear'),
                 ('verb', 'eat'),
                 ('noun', 'honey')]
    assert parser.match(word_list, 'noun') == ('noun', 'bear')

def test_skip():
    word_list = [('stop', 'in'),
                 ('stop', 'the'),
                 ('noun', 'cabinet')]
    parser.skip(word_list, 'stop')
    assert word_list == [('noun', 'cabinet')]

def test_perse_verb():
    word_list = [('verb', 'eat'),
                 ('noun', 'honey')]
    assert parser.parse_verb(word_list) == ('verb', 'eat')

def test_perse_verb_errors():
    word_list = [('noun', 'bear'),
                 ('verb', 'eat'),
                 ('noun', 'honey')]
    pytest.raises(parser.ParserError, parser.parse_verb, word_list)

    word_list = [('noun', 'bear'),
                 ('verb', 'eat'),
                 ('noun', 'honey')]
    with pytest.raises(parser.ParserError):
        parser.parse_verb(word_list)

def test_parse_objects():
    word_list = [('stop', 'the'),
                 ('noun', 'bear')]
    assert parser.parse_object(word_list) == ('noun', 'bear')

    word_list = [('stop', 'from'),
                 ('direction', 'north')]
    assert parser.parse_object(word_list) == ('direction', 'north')

def test_parse_subjects():
    word_list = [('noun', 'bear'),
                 ('verb', 'eat'),
                 ('noun', 'honey')]
    assert parser.parse_subject(word_list) == ('noun', 'bear')

    word_list = [('verb', 'run'),
                 ('direction', 'north')]
    assert parser.parse_subject(word_list) == ('noun', 'player')

def test_parse_sentences():
    word_list = [('noun', 'bear'),
                 ('verb', 'eat'),
                 ('stop', 'the'),
                 ('noun', 'honey')]
    s = parser.parse_sentence(word_list)
    assert s.subject == 'bear'
    assert s.verb == 'eat'
    assert s.object == 'honey'

    word_list = [('verb', 'run'),
                 ('direction', 'north')]
    s = parser.parse_sentence(word_list)
    assert s.subject == 'player'
    assert s.verb == 'run'
    assert s.object == 'north'
