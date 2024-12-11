import requests


# get request

#example1
# x = requests.get('https://w3schools.com/python/demopage.htm')
# print(x.status_code)
# print(x.text)

#example2
# x = requests.get('https://api.github.com/users/naveenkrnl')
# print(x.content)



# post request

# url = 'https://www.w3schools.com/python/demopage.php'
# myObj = {'somekey':'somevalue'}

# requests.post(url , json=myObj)
# print(x.text)


r = requests.post('https://httpbin.org / post', data ={'key':'value'})
print(r)
 
# print content of request
print(r.json())

