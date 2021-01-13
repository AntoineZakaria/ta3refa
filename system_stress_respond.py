import requests
from lxml import html
from bs4 import BeautifulSoup
from time import time
from math import sqrt
from joblib import Parallel, delayed



domain_name='https://a331eae7648b.ngrok.io'
def single_request_home (domain_name):
    requests.get(domain_name)
    #print('one request sent')



#testing server response time get home for one person
start_time = time()
for i in range(1):
    requests.get(domain_name)
end_time= time()
time_diff=end_time-start_time
print("=========================================")
print(f'testing server response time get home for one person : {time_diff}')


#test 10 requestes home bage at one time
start_time = time()
Parallel(n_jobs=10)(delayed(single_request_home)(domain_name) for i in range(10))
end_time= time()
time_diff=end_time-start_time
print("=========================================")
print(f'test 10 requestes home bage at one time : {time_diff}')

#test 20 requestes home bage at one time
start_time = time()
Parallel(n_jobs=10)(delayed(single_request_home)(domain_name) for i in range(20))
end_time= time()
time_diff=end_time-start_time
print("=========================================")
print(f'test 20 requestes home bage at one time : {time_diff}')


#test 1 requestes single_product bage at one time
start_time = time()
Parallel(n_jobs=10)(delayed(single_request_home)(f'{domain_name}/single_product/show_product/10') for i in range(1))
end_time= time()
time_diff=end_time-start_time
print("=========================================")
print(f'test 1 requestes single_product bage at one time : {time_diff}')

#test 10 requestes single_product bage at one time
start_time = time()
Parallel(n_jobs=10)(delayed(single_request_home)(f'{domain_name}/single_product/show_product/10') for i in range(10))
end_time= time()
time_diff=end_time-start_time
print("=========================================")
print(f'test 10 requestes single_product bage at one time : {time_diff}')

#test 20 requestes single_product bage at one time
start_time = time()
Parallel(n_jobs=10)(delayed(single_request_home)(f'{domain_name}/single_product/show_product/10') for i in range(20))
end_time= time()
time_diff=end_time-start_time
print("=========================================")
print(f'test 20 requestes single_product bage at one time : {time_diff}')



# stress testing 50 user at once request home bage
start_time = time()
Parallel(n_jobs=10)(delayed(single_request_home)(f'{domain_name}') for i in range(50))
end_time= time()
time_diff=end_time-start_time
print("=========================================")
print(f'stress testing 50 user at once request home bage : {time_diff}')

# stress testing 50 user at once request home bage
start_time = time()
Parallel(n_jobs=10)(delayed(single_request_home)(f'{domain_name}/single_product/show_product/10') for i in range(50))
end_time= time()
time_diff=end_time-start_time
print("=========================================")
print(f'stress testing 50 user at once request single_product bage : {time_diff}')
