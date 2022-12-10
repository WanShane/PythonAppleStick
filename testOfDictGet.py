dictOfThumbs = {}
ThirtyTwoThumbs = dictOfThumbs.fromkeys(range(32), '赞')
print(ThirtyTwoThumbs)
for eachKey in ThirtyTwoThumbs.keys():
    print(eachKey)
for eachValue in ThirtyTwoThumbs.values():
    print(eachValue)
for eachItem in ThirtyTwoThumbs.items():
    print(eachItem)
