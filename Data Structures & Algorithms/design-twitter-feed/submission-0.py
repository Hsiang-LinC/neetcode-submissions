class Twitter:

    def __init__(self):
        '''
            maintain a table of follower/followee
            a table to posted Tweet, with its tweetId, userId and time (order)
        '''
        self.followTable = defaultdict(set)   # {followerId: [followeeIds]}
        self.posts = defaultdict(list)     # {userId: [(time, tweetId)]}
        self.t = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.t += 1
        self.posts[userId].append([-self.t, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        followees = self.followTable[userId] | {userId}
        

        posts = []
        for f in followees:
            posts.extend(self.posts[f])
        heapq.heapify(posts)

        res = []
        while posts and len(res) < 10:
            res.append(heapq.heappop(posts)[1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followTable[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followTable[followerId].discard(followeeId)
