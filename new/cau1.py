url = 'https://vov.gov.vn/Rss/RssChuyende?pageSize=&chuyendeId=14'
hyperlink = [url]
for i in range (2,135):
    link = 'https://vov.gov.vn/Rss/RssChuyende?page='+str(i)+'&chuyendeId=14'
    hyperlink = hyperlink + [link]
print(hyperlink)
