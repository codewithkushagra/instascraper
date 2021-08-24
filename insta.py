import instaloader

L = instaloader.Instaloader()

# acc=input("Enter account name: ")

acc='ashish_gopalika'

# HASHTAG='collab'

# L.download_profile(acc,profile_pic_only=True)

L.download_post(acc)

# for post in L.get_hashtag_posts(HASHTAG):
#     L.download_post(post, target='#'+HASHTAG)
