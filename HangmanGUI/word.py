import random

class Word:

    # 초기화(생성자), 파일을 읽어들여서 단어 데이터 베이스 초기화
    def __init__(self, filename):

        self.words = []
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()
        # >> 파일을 열어서 행별로 구분한 리스트를 만들고 파일을 닫음

        self.count = 0

        for line in lines:
            word = line.rstrip()
            self.words.append(word)
            self.count += 1
        # 각 행의 오른쪽 공백문자를 제거하고 self.words 리스트에 덧붙임.
        # 이 수효를 self.count에 기록.
        print('%d words in DB' % self.count)


    def test(self):
        return 'default'

    # 랜덤으로 비밀 단어를 선택해주는 기능
    def randFromDB(self):
        r = random.randrange(self.count)
        return self.words[r]
        # 단어 데이터베이스 내에서 인덱스 범위 내에서 난수발생시켜서
        # 해당위치의 단어를 리턴

