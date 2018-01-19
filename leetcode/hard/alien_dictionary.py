
import collections

class Solution:

    def alien_order(self, words):
        parent, child = collections.defaultdict(set), collections.defaultdict(set)
        for pair in zip(words, words[1:]):
            print("pair", pair)
            for a, b in zip(*pair):
                if a != b:
                    print("a:", a)
                    print("b:", b)
                    child[a].add(b)
                    parent[b].add(a)
                    break


        print("Parent", parent)
        print("Child", child)


        chars = set(''.join(words))
        free = chars - set(parent)
        order = ''


        while free:
            a = free.pop()
            order += a
            for b in child[a]:
                parent[b].discard(a)
                if not parent[b]:
                    free.add(b)

        print("order:", order)

        return order * (set(order) == chars)
