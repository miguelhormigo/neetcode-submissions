class Twitter:

    def __init__(self):
        self.next_id = 0
        self.users = defaultdict(list)
        self.follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.users[userId].append([self.next_id, tweetId])
        self.next_id += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        in_feed = self.follows[userId]
        in_feed.add(userId)

        feed = []

        for user in in_feed:
            for tweet in self.users[user][-10:]:
                if not feed or len(feed) < 10 or tweet > feed[0]:
                    heapq.heappush(feed, tweet)
                    if len(feed) > 10:
                        heapq.heappop(feed)

        return [tweet[1] for tweet in sorted(feed, reverse=True)]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
