import tweepy
import yaml
import random
import re
import json
import logging

class Bot:
    MAX_TWEET_SIZE = 280

    def __init__(self, name):
        self.data_filename = name + ".json"
        self.logging_filename = name + ".log"
        logging.basicConfig(filename=self.logging_filename, level=logging.INFO, format='%(asctime)s %(message)s')
        logging.info("Bot started")
        self.load_data()
        self.connect()
        logging.info("Init complete")
    
    def connect(self):
        auth_data = self.data['auth']
        auth = tweepy.OAuthHandler(auth_data['CONSUMER_KEY'], auth_data['CONSUMER_SECRET'])
        auth.set_access_token(auth_data['ACCESS_TOKEN'], auth_data['ACCESS_TOKEN_SECRET'])
        self.api = tweepy.API(auth)

    def load_data(self):
        with open(self.data_filename, encoding='utf8') as file:
            self.data = json.load(file)

    def save_data(self):
        with open(self.data_filename, 'w', encoding='utf8') as file:
            json.dump(self.data, file)

    def update_data(self):
        for s in self.api.mentions_timeline(count=100):
            status_data = {
                'text': s.text,
                'reply_to': s.in_reply_to_status_id,
                'user_id': s.user.id,
                'user_name': s.user.name,
                'user_screen_name': s.user.screen_name
            }
            self.data['mentions'][s.id] = status_data
        self.save_data()

    def tweet(self, text):
        print("About to tweet '" + text + "'")
        if len(text) > self.MAX_TWEET_SIZE:
            print("Tweet too long: ", len(text))
            return
        self.api.update_status(text)
    
    def tweet_new_post(self, post_file):
        with open("../_posts/" + post_file, encoding='utf8') as file:
            desc = re.search('twitter_description: "(.*)"', file.read()).group(1)
        text = "פוסט חדש בבלוג:" + '\n' + desc + '\n' + self.name_to_link(post_file)
        self.tweet(text)


    def reply(self, text, id):
        self.api.update_status(status = text, in_reply_to_status_id = id , auto_populate_reply_metadata=True)

    def tweet_introductory_post(self, index = None):
        with open('_data\introductory_posts.yml', encoding='utf8') as file:
            posts = yaml.load(file, Loader=yaml.FullLoader)
        if index is not None:
            post = posts[index]
        else:
            post = random.choice(posts)
        url = SITE + post['url']
        description = post['text']
        text = "והיום בפינת פוסט המבוא:" + '\n' + description + '.' + '\n' + url
        self.tweet(text)

    def post_long_text(self, long_text):
        MAX_LENGTH = 270
        paragraphs = re.split('(?<=\. |! |\? |\.\n|!\n|\?\n|; |;\n|\n\n|: |:\n)', long_text)
        current_tweet = ''
        tweets = []
        for p in paragraphs:
            if len(p) > MAX_LENGTH:
                raise RuntimeError("Paragraph too long: ", p, " (", len(p),")")
            if len(current_tweet) + len(p) > MAX_LENGTH:
                tweets.append(current_tweet)
                current_tweet = ''
            current_tweet += p
        tweets.append(current_tweet)
        n = len(tweets)
        tweets = [t.strip() + ' ({}/{})'.format(i+1,n) for i,t in enumerate(tweets)]
        id = None
        for t in tweets:
            if id is None:
                id = self.api.update_status(t).id
            else:
                self.api.update_status(status = t, in_reply_to_status_id = id , auto_populate_reply_metadata=True)
    
    def reply_to_questions(self, start_id):
        with open('questions.yml', encoding='utf8') as file:
            questions = yaml.load(file, Loader=yaml.FullLoader)
        tweets_to_check = list(reversed(self.api.mentions_timeline(start_id, count=100)))
        for t in tweets_to_check:
            print(t.text[::-1])
        for q in questions:
            for t in tweets_to_check:
                if re.search(q['regex'],t.text) is not None:
                    response = 'האם שאלת על "{}"?\n{}\n{}'.format(q['question'], q['reply'], SITE + q['link'])
                    self.reply(response, t.id)
                    print("Replied to ", t.id)

    def name_to_link(self, filename):
        (year, month, day, name) = re.search(r'(\d\d\d\d)-(\d\d)-(\d\d)-(.*)\.md', filename).groups()
        return self.data['site'] + "/" + year + "/" + month + "/" + day + "/" + name + "/"
        



bot = Bot('not_precise')
bot.tweet_new_post('2020-01-24-what_is_mipstar_equals_re_part_2.md')

# bot = Bot('gadial')
# bot.tweet_post('http://gadial.net/2020/01/20/what_are_percents/', '2020-01-20-what_are_percents.md')

# tweets = tweepy.Cursor(bot.api.user_timeline, tweet_mode='extended').items(20)
# for tweet in tweets:
#     content = tweet.full_text
#     print(content)

# bot.update_data()
# print(bot.data)
# bot.reply_to_questions(1217488783907676161)
