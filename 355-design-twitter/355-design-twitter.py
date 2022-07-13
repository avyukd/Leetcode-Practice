class Twitter:

    def __init__(self):
        self.tm = 0 # time is decremented by 1 so we can use minheap
        self.followers = defaultdict(set) # key is userId, value is all the people they follow
        self.tweets = [] # each tweet is (time, userId, tweetId)
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.tweets, (self.tm, userId, tweetId))
        self.tm -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        popped = []
        while len(feed) < 10 and len(self.tweets) > 0:
            (postTime, postUserId, postTweetId) = heapq.heappop(self.tweets)
            if postUserId == userId or postUserId in self.followers[userId]:
                feed.append(postTweetId)
            popped.append((postTime, postUserId, postTweetId))
        self.tweets += popped
        heapq.heapify(self.tweets)
        return feed        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            self.followers[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)