import heapq
class Twitter:

    def __init__(self):
        self.following={}
        self.tweets={}
        self.timestamp=0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp-=1
        if str(userId) not in self.tweets.keys():
            self.tweets[str(userId)]=[(self.timestamp,tweetId)]
        else:
            self.tweets[str(userId)].append((self.timestamp, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        if str(userId) not in self.following.keys():
            self.following[str(userId)]={userId}
        allFollowing=self.following[str(userId)]
        allTweets=[]
        feed=[]
        for followee in allFollowing:
            if str(followee) in self.tweets.keys():
                # pop the tweets according to the timestamp (ascending) -> maxHeap
                for tweet in self.tweets[str(followee)]:
                    heapq.heappush(allTweets, tweet)
        #print(allTweets)
        # latest 10 tweets are in the feed
        count=10
        while len(allTweets)!=0 and count>0:
            feed.append(heapq.heappop(allTweets)[1])
            count-=1
        #print(f'User{userId} has feed: {feed}')
        return feed


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId==followeeId:
            return
        if str(followerId) not in self.following.keys():
            self.following[str(followerId)]={followerId, followeeId}
        else:
            self.following[str(followerId)].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId!=followeeId and str(followerId) in self.following.keys():
            #print(f'User{followerId} current following: {self.following[str(followerId)]}')
            self.following[str(followerId)].discard(followeeId)