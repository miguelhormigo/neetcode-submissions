class Twitter:

    def __init__(self):
        self.next_id = 0
        self.users = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.next_id, tweetId])
        self.next_id += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        i = len(feed) - 1
        for i in range(len(self.tweets[userId]) - 1, -1, -1):
            tweet = self.tweets[userId][i]
            heapq.heappush(feed, tweet)
            if len(feed) == 10:
                break
        
        for user in self.users[userId]:
            for i in range(len(self.tweets[user]) - 1, -1, -1):
                tweet = self.tweets[user][i]
                if len(feed) > 10 and tweet[0] < feed[0][0]:
                    break
                heapq.heappush(feed, tweet)
                if len(feed) > 10:
                    heapq.heappop(feed)
        
        feed.sort(reverse=True)
        return [tweet_id for _, tweet_id in feed]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)
