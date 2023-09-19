from pathlib import Path
from http.client import HTTPConnection
from urllib.parse import urljoin, urlunparse
from urllib.request import urlretrieve
from html.parser import HTMLParser

# 이미지 태그를 파싱하기 위한 HTMLParser 서브 클래스
class ImageParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag != "img":
            return
        if not hasattr(self, 'result'):
            self.result = []  # 이미지 URL을 저장할 빈 리스트 생성
        for name, value in attrs:
            if name == 'src':
                self.result.append(value)  # 이미지 태그의 'src' 속성 값을 리스트에 추가

# 이미지를 다운로드하는 함수
def downloadImage(url, data):
    downDir = Path('DOWNLOAD')  # 이미지를 저장할 디렉토리 경로
    downDir.mkdir(exist_ok=True)  # 디렉토리가 존재하지 않으면 생성

    parser = ImageParser()
    parser.feed(data)  # 웹 페이지 데이터를 파싱하여 이미지 URL 추출
    dataSet = set(x for x in parser.result)  # 중복되지 않는 이미지 URL 목록 생성

    for x in sorted(dataSet):
        imageUrl = urljoin(url, x)  # 상대 URL을 절대 URL로 변환
        basename = Path(imageUrl).name  # URL에서 파일 이름 추출
        targetFile = downDir / basename  # 이미지를 저장할 파일 경로 생성

        print("Downloading...", imageUrl)
        urlretrieve(imageUrl, targetFile)  # 이미지 다운로드

# 메인 함수
def main():
    host = "www.google.co.kr"  # 웹 페이지의 호스트 주소

    conn = HTTPConnection(host)
    conn.request("GET", '')  # 웹 페이지 요청
    resp = conn.getresponse()

    charset = resp.msg.get_param('charset')  # 웹 페이지의 문자 인코딩 추출
    data = resp.read().decode(charset)  # 웹 페이지 데이터를 문자열로 디코딩
    conn.close()

    print("\n >>>>>>>>>>>>>>>>> Download Image From ", host)
    url = urlunparse(("http", host, '', '', '', ''))  # 호스트 주소를 URL로 변환
    downloadImage(url, data)  # 이미지 다운로드 함수 호출

if __name__ == '__main__':
    main()  # 스크립트가 직접 실행될 때 메인 함수 호출
