import html
import json

from datetime import datetime

from hackernews import HackerNews



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
    """ Get the ID of a post

        Descryption:
            This function will get the post id from the recent stories from hackernews page and returns
            the post which has "who wants to be hired" string in it's title

        Output:
                Type: List of single integer
        
    """

    hired_post = []
    hn = HackerNews()
    posts_list = hn.ask_stories(limit=50)
    for i in posts_list:
        if "who wants to be hired" in i.title.lower():
                hired_post.append(i.item_id)
                break

    return hired_post



def get_post_from_id():
    """ Get post object from ID
        Output:
                Type: Object
    """
    return HackerNews().get_item(get_hired_post_id()[0])

def get_post_comments():
    """Post comments
    
        Descryption:
            This function will get all the comment of the desired post
        
        Output:
            Type: List of objects 
    """

    return get_post_from_id().kids[:10]

def get_list_of_comments():
    """
    Descyption:
        This function will get ID's of all the comment objects of post
    Output:
        Type: List of int's
    
    """
    return HackerNews().get_items_by_ids(get_post_comments())


list_of_dicts = []
list_of_lists = []

def make_lists(list_of_comments):
    """
    Descryption:
        This function will take list of comment ID's and return dictionary containing list of lists and List of dicts
        In List of lists each list has values of the keys of 'req_dict' dict of all posts.
        In List of dicts each dict is 'req_dict' and values of each comment
    
    """

    # This will loop through the list of comment objects and assign the respective value to key in 'req_dict'
    # The condition i.delted is to prevent any empty values which will result due to the deleted post
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
            req_dict['user_profile_link'] = "https://news.ycombinator.com/user?id="+str(HackerNews().get_user(str(i.by)).user_id)

            # This will append the 'req_dict' with values of keys of respective comment object
            list_of_dicts.append(req_dict)

            # This will append list of only values of 'req_dict'
            list_of_lists.append(list(req_dict.values()))
    
    return {'list_of_lists':list_of_lists,'list_of_dicts':list_of_dicts}

    

# kii = list(list_of_dicts[0].keys())
def new_thread_id():
    """
        Descryption:
            This will return the comment ID of the last added post
    """
    list_of_comments = make_lists(get_list_of_comments())
    # print(list_of_comments)
    list_of_dicts_value = list_of_comments['list_of_dicts']
    thread_id_last_post = list_of_dicts_value[0]['thread_id']

    return thread_id_last_post
