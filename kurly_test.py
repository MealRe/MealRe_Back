import requests

firstpage = 1
lastpage = 10
for num in range(firstpage, lastpage):
    req = requests.get(
        f'https://api.kurly.com/v1/categories/912?page_limit=99&page_no={num}&delivery_type=0&sort_type=0&ver=1581568745455')
    data = req.json()
    products = data['data']['products']
    result = []
    for product in products:
        result.append({
            'no': product['no'],
            'name': product['name'],
            'price': product['price'],
            'desc': product['shortdesc'],
            'img': product['thumbnail_image_url'],
        })
    result = [{
        'no': product['no'],
        'name': product['name'],
        'price': product['price'],
        'desc': product['shortdesc'],
        'img': product['thumbnail_image_url']
    } for product in products]
    for value in result:
        print(value)