import os


def main():
    for count,filename in enumerate(os.listdir('dataset/train_B_mirror')):
        dst = str(count+2000) + '.jpg'
        src = 'dataset/train_B_mirror/'+filename
        dst = 'dataset/train_B/'+dst
        os.rename(src,dst)

if __name__ == '__main__':
        main()