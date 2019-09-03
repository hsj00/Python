'''
- input: total posts (m), number of posts in a page (n)
- output: total pages
- function name: getTotalPage
'''

def getTotalPage(m, n):
    page = round(m/n)
    return page

print(getTotalPage(30, 10))
