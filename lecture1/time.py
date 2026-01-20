'''
conever seconds into hr ,min nad secDocstring for time
'''

sec = int(input("Enter number of seconds: "))

hr = sec // 3600
re_mi = sec % 3600
mi = re_mi // 60
sec = re_mi % 60

print(f"{hr}:{mi}:{sec}")