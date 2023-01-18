from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs


def index(request):
    return render(request, 'home.html')


def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        page = []
        url_list = []
        pageNum = 0
        while pageNum != 1:
            url = f'https://www.pornhub.com/video/search?search={search}&page={page}'

            # url = 'https://www.google.com/search?q='+search
            res = requests.get(url)
            soup = bs(res.text, 'lxml')


            result_listings = soup.find_all('li', {'class': 'pcVideoListItem js-pop videoblock videoBox'})




            #result_image = soup.find_all('img', {'class': 'js-pop js-videoThumb thumb js-videoPreview'})

            final_result = []
            final_result_more = []

            # DEBUG
            # final_result.append(result_listings)

            for url in url_list:
                more_Listing = soup.find_all('li', {'class': 'pcVideoListItem js-pop videoblock videoBox'})

                for url in more_Listing:
                    result_title = url.find(class_='thumbnail-info-wrapper clearfix').text
                    result_url = url.find('a').get('href')
                    result_img = url.find("img").get('src')
                    result_desc = url.find(class_='title').text

                    final_result_more.append((result_title, result_url, result_desc, result_img))

            for result in result_listings:

                result_views = result.find(class_='views').text
                result_url = result.find('a').get('href')
                result_img = result.find("img").get('src')
                result_desc = result.find(class_='title').text
                result_rate = result.find(class_='rating-container neutral').text
                result_uploader = result.find(class_='videoUploaderBlock clearfix').text
                result_time = result.find(class_='marker-overlays js-noFade').text




                final_result.append((result_views, result_url, result_desc, result_img, result_rate, result_uploader, result_time))




            pageNum = pageNum + 1
            page.append(pageNum)
            url_list.append(url)


        search_result = []




        search_result.append(search)


        context = {
            'final_result': final_result,
            'search_title': search_result,
            'page_number': page,
            'url_list': url_list,
            'final_result_more': final_result_more,
        }

        return render(request, 'search.html', context)
    else:
        return render(request, 'search.html')




def catSearch(request):
    if request.method == 'POST':
        catagorySearch = request.POST['catSearch']
        page = 1
        while page != 10:
            url = f'https://www.pornhub.com/video?c={catagorySearch}&page={page}'

            # url = 'https://www.google.com/search?q='+search
            res = requests.get(url)
            soup = bs(res.text, 'lxml')


            result_listings = soup.find_all('li', {'class': 'pcVideoListItem js-pop videoblock videoBox'})
            #result_image = soup.find_all('img', {'class': 'js-pop js-videoThumb thumb js-videoPreview'})

            final_result = []
            # DEBUG
            # final_result.append(result_image)

            for result in result_listings:
                result_views = result.find(class_='views').text
                result_url = result.find('a').get('href')
                result_img = result.find("img").get('src')
                result_desc = result.find(class_='title').text
                result_rate = result.find(class_='rating-container neutral').text
                result_uploader = result.find(class_='videoUploaderBlock clearfix').text
                result_time = result.find(class_='marker-overlays js-noFade').text

                final_result.append((result_views, result_url, result_desc, result_img, result_rate, result_uploader, result_time))
            page = page + 1

        search_result = []



        search_result.append(search)

        context = {
            'final_result': final_result,
            'search_title': search_result
        }

        return render(request, 'search.html', context)
    else:
        return render(request, 'search.html')

def autoSearch(request):
    if request.method == 'POST':
        autoSearch = request.POST['autoSearch']
        page = 1
        while page != 10:
            url = f'https://www.pornhub.com/video/search?search=pornhub+car&o=tr'

            # url = 'https://www.google.com/search?q='+search
            res = requests.get(url)
            soup = bs(res.text, 'lxml')

            result_listings = soup.find_all('li', {'class': 'pcVideoListItem js-pop videoblock videoBox'})
            # result_image = soup.find_all('img', {'class': 'js-pop js-videoThumb thumb js-videoPreview'})

            final_result = []
            # DEBUG
            # final_result.append(result_image)

            for result in result_listings:
                result_title = result.find(class_='thumbnail-info-wrapper clearfix').text
                result_url = result.find('a').get('href')
                result_img = result.find("img").get('src')
                result_desc = result.find(class_='title').text

                final_result.append((result_title, result_url, result_desc, result_img))
            page = page + 1

        search_result = []

        search_result.append(search)

        context = {
            'final_result': final_result,
            'search_title': search_result
        }

        return render(request, 'search.html', context)
    else:
        return render(request, 'search.html')
