def create_youtube_video(title,description):
	video={"title":title,"description":description,"likes":0,"dislikes":0,"comments":{} ,"hashtags":[]}
	for i in range(5):
		video["hashtags"].append(input("enter a hashtag :"))
	return video

def like(video):
	if "likes" in video:
		video["likes"]+=1
		return video

def dislike(video):
	if "dislikes" in video:
		video["dislikes"]+=1
		return video

def add_comment(video,username,comments_text):
	video['comments'][username]=comments_text


a = create_youtube_video("hello","jjwboe")
a = like(a)
a = dislike(a)
a = add_comment(a,"morrie","commentss")
for i in range(495):
	a = like(a)
c=0
def simiularaty(d1,d2):
	 for i in range(5):
	 	for j in range(5):
	 		if d1["hashtags"][i] = d2["hashtags"][j]:
	 			c=c+1
	print ("the simiularaty = " + c * 4 +"%")


