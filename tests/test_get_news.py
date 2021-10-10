import pytest
from unittest.mock import patch,Mock

from Hackerjobs.get_news import get_hired_post_id,make_lists,new_thread_id

from collections import namedtuple


list_of_l = [['10/07/2021, 22:04:08', None, 'plow-tycoon', "\n \n  Location: Vancouver, Canada\n  Remote: Yes\n  Willing to relocate: Not at present, but open to Europe in the future\n  Technologies: Python, JavaScript (Vue, Node, React, others), Postgres, Unix, Golang, others\n  Résumé/CV: https://drive.google.com/file/d/1JKEmJGg7bn3K1PhuhASUCHAJJFOkwTKK/view?usp=sharing\n  Email: on Resume\n\n</pre>\nHi, I'm Luke, a front-end leaning developer based out of Vancouver, Canada. I've been working with JavaScript (and various component libraries such as React, Vue, Angular), HTML, CSS, Python, and others for some portion of the last decade. I find a lot of satisfaction in troubleshooting obscure issues and incrementally improving products, while working with good people or solo.\nI burnt out and lost my previous position after COVID hit, and since then I haven't found anything, instead working on side-projects and in whatever non-tech jobs I can in the meantime :) I recently received an offer that could have been life-changing, but it was rescinded upon the company's realization that hiring a remote worker in Canada was more complex than they were prepared for. I'm quite defeated by this, and by the interviewing gauntlet that I've been doing for over a year, but am still open to full-time, part-time, and contract work as an incorporated entity.\nIn my next position, I'm looking for something where I can see where my value to the customer is going. Working at too high of an abstraction level from the problems I solve isn't healthy.", 'https://news.ycombinator.com/item?id=None', 'https://news.ycombinator.com/user?id=plow-tycoon', '10/08/2021, 17:39:32', 28788638, 28719317, '22:04:08']]
list_of_d = [{'submission_date': '10/04/2021, 21:28:10', 'link': None, 'user': 'jobeid', 'text': 'Location: Toronto, Canada\nRemote: Yes\nWilling to relocate: Maybe\nTechnologies: React, JavaScript, TypeScript, HTML, CSS, UI/UX design, Python, C#, .NET, SQL\nRésumé/CV: <a href="https://docs.google.com/document/d/1lOiZV3Xx7zBOKQjNzuP-o6EqVD6DZ2al2ZSNjsALGFs/edit?usp=sharing" rel="nofollow">https://docs.google.com/document/d/1lOiZV3Xx7zBOKQjNzuP-o6Eq...</a>\nEmail: jason.obeid98@gmail.com\nGitHub: <a href="https://github.com/JasonObeid" rel="nofollow">https://github.com/JasonObeid</a>\nI\'m a Full-Stack Developer with ~1 year of experience building user-friendly web applications. I have experience leading and taking ownership of small projects, interacting with stakeholders, executing on a product\'s vision, and also mentoring junior developers. I take extra care in making my applications accessible and internationalized. I also have some research experience in NLP, where I developed an ML-based approach to automatically generate textual descriptions for visualizations that was accepted into the 2020 International Conference on Natural Language Generation (INLG).\nI\'m looking for a Front-End or Full-Stack role where I can work with driven colleagues, gain technical and interpersonal skills, and build great products. I enjoy environments with strong mentorship and learning opportunities!', 'thread_link': 'https://news.ycombinator.com/item?id=None', 'user_profile_link': 'https://news.ycombinator.com/user?id=jobeid', 'date': '10/08/2021, 17:44:38', 'comment_id': 28748468, 'thread_id': 28719317, 'comment_timestamp': '21:28:10'}]
result = {'list_of_lists':list_of_l,'list_of_dicts':list_of_d} 

def my_side_effect(x):
    return result

@patch('Hackerjobs.get_news.get_list_of_comments')
@patch('Hackerjobs.get_news.make_lists')
def test_new_thread_id(mock_comments,mock_list):

    thread_id = 28719317
    mock_list.side_effect = my_side_effect(mock_comments)
    mock_comments.return_value = result

    r = new_thread_id()

    assert r == 28719317





