def search(query, ranking=lambda r: r.stars): # query:搜索的字符串
    results = [r for r in Restaurant.all if query in r.name]
    return sorted(results, key=ranking) # sorted 返回从小到大的列表

def review_both(r, s):
    """计算两家餐厅共同的评论者数量（相似度度量）"""
    return len([x for x in r.reviews if x in s.reviews]) 
class Restaurant:
    all = []
    def __init__(self, name, stars):
        self.name = name
        self.stars = stars
        self.reviewers = reviewers
        Restaurant.all.append(self)

    def similar(self, k, similarity=review_both):
        """返回与自身最相似的k个餐馆"""
        others = list(Restaurant.all)
        others.remove(self) # 删除自身
        return sorted(others, key=lambda r: -similarity(self, r))[:k] # 取前k个
    
    def __repr__(self):
        return '<' + self.name + '>'

import json
reviewers_for_restaurant = {}
for line in open('reviewers.json'):
    r = json.load(line)
    biz = r['business_id']
    if biz not in reviewers_for_restaurant:
        reviewers_for_restaurant[biz] = [r['user_id']]
    else:
        reviewers_for_restaurant[biz].append(r['user_id'])

for line in open('restaurant.json'):
    r = json.load(line)
    reviewers = reviewers_for_restaurant(r['business_id'])
    Restaurant(r['name'], r['stars'], reviewers)

Restaurant('Thai Delight', 2)
Restaurant('Thai Basil', 3)
Restaurant('Top Dog', 5)

results = search('Thaing')
for r in results:
    print(r, 'is similar to', r.similar(3))


def fast_overlap(s, t):
    i, j ,cnt = 0, 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            cnt, i, j = cnt + 1, i + 1, j + 1
        elif s[i] < t[j]:
            i += 1
        else:
            j += 1
    return cnt