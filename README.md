# Hacker News Job Scrapper

This application will fetch all the comments from "Who wants to be hired?" post of every month and store it in google sheets

## Description

Every month, [Hacker News](https://site.ycombinator.com/) has 3 threads that are of importance to companies looking to hire people, and to people looking for jobs:

1. Who's Hiring?
2. [Who Wants to Be Hired?](https://news.ycombinator.com/item?id=28719317)
3. Freelancer/Looking for Freelancer?

So this application uses Hacker News API to get "Who wants to be Hired?" post from every month and get details of comments of that post like submission time, user name, user id, comment text etc. 

The data we get from this API is stored into Google sheets using Sheets API

## Getting Started

### Dependencies

* Python 3.2 or above
* Should have [Google API](https://developers.google.com/workspace/guides/create-project)
* Create JSON [token](https://help.talend.com/r/E3i03eb7IpvsigwC58fxQg/EjqPCVhQjCFPP6pU5Bzvdw)

### Installing

Go to the directory of the code

```
$ cd <directory of code you downloaded or pulled from this git repo>
```

Install all the required libraries using below command 

```python
$ pip install -e .
```

Create a folder called 'hackerjobs' in .config folder in your home directory

for example in linux we use

```bash
$ mkdir home/$USER/.config/hackerjobs
```



### Executing program

* Move to the repo directory
* Add config variables to .env in .config folder
```bash
$ hackerjobs config --api-name 'sheets'
$ hackerjobs config --client-secret-file-name '<name-of-the-token_json-file>'
$ hackerjobs config --secret-file '<dir-to-the-token_json_file>'
$ hackerjobs config --spread-sheet-id <google-sheet-id-of-your-sheet>
$ hackerjobs config --api-version 'v4' or '<required-version-you-want-to-use>'
```

after giving configuration variables we can execute the command using

```
$ hackerjobs who-wants-to-be-hired
```



## Help

Any advise for common problems or issues.
```
$ hackerjobs --help
```

## Authors

Contributors names and contact info

Sreeram Ambalam

asreeram1729@gmail.com

[Twitter](https://twitter.com/filius_fall)

[Blog](https://filius-fall.github.io/)

