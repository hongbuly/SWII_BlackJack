# 파일 입출력
def load():
    try:
        f = open("money.dat", 'r')
        return int(f.readline())
    except:
        f = open("money.dat", 'w')
        f.write('100000')
        return 100000
    f.close()


def write(money):
    f = open("money.dat", 'w')
    f.write(money)
    f.close()
