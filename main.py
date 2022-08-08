import httpx, re, string, random, threading, time, ctypes
from bs4 import BeautifulSoup

print(r'''

         __        __                       _          _ __
 _    __/ /  ___ _/ /____ ___ ____  ___    (_)__ _  __(_) /____   ___ ____ ___
| |/|/ / _ \/ _ `/ __(_-</ _ `/ _ \/ _ \  / / _ \ |/ / / __/ -_) / _ `/ -_) _ \
|__,__/_//_/\_,_/\__/___/\_,_/ .__/ .__/ /_/_//_/___/_/\__/\__/  \_, /\__/_//_/
                            /_/  /_/                            /___/
                                iliya#1111
''')

y = int(input('Threads > '))

ctypes.windll.kernel32.SetConsoleTitleW('Found: 0')

def gen():
    found = 0
    while True:
        characters = string.ascii_letters + string.digits
        result_str = ''.join(random.choice(characters) for i in range(22))
        url = f'https://chat.whatsapp.com/invite/{result_str}'
        headers = {'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36'}
        #_json={"model": "text-davinci-002", "prompt": f"{prompt}", "temperature": 0, "max_tokens": 250}
        r = httpx.get(url, headers=headers)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')
            pattern = 'WhatsApp Group Invite'
            try:
                image = soup.find('img', {'src': 'https://static.whatsapp.net/rsrc.php/v3/yB/r/_0dVljceIA5.png'})
                if image['src'] == 'https://static.whatsapp.net/rsrc.php/v3/yB/r/_0dVljceIA5.png':
                    print(url)
            except:
                found = found + 1
                ctypes.windll.kernel32.SetConsoleTitleW(f"Found: {str(found)}")
                print(url)
                with open('invites.txt', 'a') as f:
                    f.write('\n')
                    f.write(url)
                    f.close()


        else:
            pass

def main():
    for i in range(y):
        t = threading.Thread(target=gen)
        t.start()
        time.sleep(.1)

if __name__ == "__main__":
    main()
