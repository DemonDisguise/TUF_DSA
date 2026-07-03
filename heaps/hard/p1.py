# Design Twitter
""" Create a simplified version of a social media platform similar to Twitter. Users should be able to post tweets, follow or unfollow other users, and view the 10 most recent tweets in their news feed. """

import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        """
        Initializes the Twitter object.
        """
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet with ID `tweetId` by the user `userId`.

        Each tweetId is guaranteed to be unique.
        """
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        """
        Retrieve the 10 most recent tweet IDs in the user's news feed.

        The news feed must:
        - Include tweets from the user themselves and users they follow
        - Be ordered from most recent to least recent
        - Return at most 10 tweet IDs
        """
        min_heap = []
        
        for t in self.tweets[userId]:
            heapq.heappush(min_heap, t)
            if len(min_heap) > 10:
                heapq.heappop(min_heap)
        
        for followee in self.following[userId]:
            for t in self.tweets[followee]:
                heapq.heappush(min_heap, t)
                if len(min_heap) > 10:
                    heapq.heappop(min_heap)
        
        result = []
        while min_heap:
            result.append(heapq.heappop(min_heap)[1])
        return result[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        User `followerId` starts following user `followeeId`.

        It is guaranteed that followerId is not already following followeeId.
        """
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        User `followerId` stops following user `followeeId`.

        It is guaranteed that followerId is currently following followeeId.
        """
        self.following[followerId].discard(followeeId)

if __name__ == "__main__":
    twitter = Twitter()

    print("Commands:")
    print("1 postTweet userId tweetId")
    print("2 getNewsFeed userId")
    print("3 follow followerId followeeId")
    print("4 unfollow followerId followeeId")
    print("Type 'exit' to stop\n")

    while True:
        inp = input("Enter command: ").strip()

        if inp.lower() == "exit":
            break

        parts = inp.split()
        if not parts:
            continue

        cmd = parts[0]

        if cmd == "postTweet":
            userId = int(parts[1])
            tweetId = int(parts[2])
            twitter.postTweet(userId, tweetId)
            print("Tweet posted")

        elif cmd == "getNewsFeed":
            userId = int(parts[1])
            feed = twitter.getNewsFeed(userId)
            print("News Feed:", feed)

        elif cmd == "follow":
            followerId = int(parts[1])
            followeeId = int(parts[2])
            twitter.follow(followerId, followeeId)
            print(f"{followerId} now follows {followeeId}")

        elif cmd == "unfollow":
            followerId = int(parts[1])
            followeeId = int(parts[2])
            twitter.unfollow(followerId, followeeId)
            print(f"{followerId} unfollowed {followeeId}")

        else:
            print("Invalid command")
        
""" 
postTweet 1 5
postTweet 1 3
postTweet 2 10
follow 1 2
getNewsFeed 1
unfollow 1 2
getNewsFeed 1
exit    
"""    