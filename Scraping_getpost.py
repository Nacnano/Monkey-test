from facebook_scraper import get_posts
import pandas as pd
dic=dict()
l=[]
for post in get_posts('NockAcademyTH', pages=10):
    l=post.keys()
    for key in l:
        dictmp={post['time']: post[key]}
        try:
            dic[key][post['time']] = post[key]
        except:
            dic[key] = {post['time'] : post[key]}
    
    print(post['time'])

df = pd.DataFrame(dic)
df.to_excel("Facebook Scraping for Monkey.xlsx")