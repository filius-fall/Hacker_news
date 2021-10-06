import html
import json

from datetime import datetime

from hackernews import HackerNews



def hn():
    """HackerNews Instance
    
        This Function creates instance of HackerNews module we installed from pip library
    """

    return HackerNews()


req_dict = {
        'submission_date': '',
        'link':'',
        'user':'',
        'text':'',
        'thread_link':'',
        'user_profile_link':'',
        'date': '',
        'comment_id':'',
        'thread_id':'',
        'comment_timestamp':''
    }


def get_hired_post_id():

    hired_post = [28719317]
    # posts_list = hn().ask_stories(limit=50)
    # for i in posts_list:
    #     if "who wants to be hired" in i.title.lower():
    #             hired_post.append(i.item_id)
    #             break

    return hired_post

def get_post_from_id():
    return hn().get_item(get_hired_post_id()[0])

def get_post_comments():

    return get_post_from_id().kids[:10]

def get_list_of_comments():
    return hn().get_items_by_ids(get_post_comments())

# get_post_comments = get_post_from_id.kids[:10]
# get_list_of_comments = hn().get_items_by_ids(get_post_comments)


list_of_dicts = []
list_of_lists = []

def make_lists(list_of_comments):

    for i in list_of_comments:
        if not i.deleted:
            req_dict['comment_id'] = i.item_id
            req_dict['submission_date'] = i.submission_time.strftime("%m/%d/%Y, %H:%M:%S")
            req_dict['link'] = i.url
            req_dict['user'] = i.by
            req_dict['comment_timestamp'] = i.submission_time.strftime("%H:%M:%S")
            req_dict['thread_id'] = get_post_from_id().item_id
            req_dict['date'] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            req_dict['text'] = html.unescape(i.text.replace('<p>','\n').replace('<code>','\n').replace('<pre>',' ').replace('</code>','\n'))
            req_dict['thread_link'] = "https://news.ycombinator.com/item?id=" + str(get_post_from_id().url)
            req_dict['user_profile_link'] = "https://news.ycombinator.com/user?id="+str(hn().get_user(str(i.by)).user_id)

            list_of_dicts.append(req_dict)
            list_of_lists.append(list(req_dict.values()))
    
    return {'list_of_lists':list_of_lists,'list_of_dicts':list_of_dicts}

    

# kii = list(list_of_dicts[0].keys())
def new_thread_id():
    return make_lists(get_list_of_comments())['list_of_dicts'][0]['thread_id']
