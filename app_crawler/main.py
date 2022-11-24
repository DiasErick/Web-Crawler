from cbc import getCbcInfo, getCbcInfoNews, getCbcInfoSports, getCbcInfoTelevision, getCbcInfoRadio, getCbcInfoMusic

print("------------------------------------------")
print("CBC News Headline:   " + getCbcInfoNews() )
print("------------------------------------------")
print("CBC Sports Headline: " + getCbcInfoSports())
print("------------------------------------------")
print("CBC Radio Headline:  " + getCbcInfoRadio())
print("------------------------------------------")
print("CBC Music Headline:  " + getCbcInfoMusic())
print("------------------------------------------")
print("CBC TV Headline:     " + getCbcInfoTelevision())
print("------------------------------------------")