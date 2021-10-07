import pytest

from Hackerjobs.get_news import get_hired_post_id,get_post_from_id,get_post_comments,get_list_of_comments,make_lists


def test_get_hired_post_id():

    assert type(get_hired_post_id()[0]) == int


def test_get_post_from_id():

    assert get_post_from_id()


def test_get_post_comments():

    assert type(get_post_comments()) == list

def test_get_list_of_comments():

    assert type(get_list_of_comments()) == list

def test_make_lists():

    assert type(make_lists(get_list_of_comments())) == dict and type(make_lists(get_list_of_comments())['list_of_lists']) == list