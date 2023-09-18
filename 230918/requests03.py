from urllib.request import urlopen
from html.parser import HTMLParser

class ImageParser(HTMLParser):
    def __iniit__(self):
        super().__init__()
        self.result = []
        
    def handle_starttag(self, tag, attrs): #<tag>를 처리하기 위해 오버라이딩
        if tag != 'img':
            return
        if not hasattr(self, 'result'):
            self.result = []
        for name, value in attrs:
            if name == 'src': #만약 이름이 src면 result에 추출해서 채워넣는다.
                self.result.append(value)

def parseImage(data):
    parser = ImageParser() 
    parser.feed(data)
    dataSet = set(x for x in parser.result) # 중복 불가능
    return dataSet

def main():
    url = "http://www.google.co.kr"
    
    f = urlopen(url)
    charset = f.info().get_param('charset')
    data = f.read().decode(charset)
    f.close()
    
    dataSet = parseImage(data)
    print('\n>>>>>> Fetch Image from', url)
    print(dataSet)
    print('\n'.join(sorted(dataSet)))

if __name__ == '__main__':
    main()
