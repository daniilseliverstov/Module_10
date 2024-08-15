from datetime import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while line := file.readline():
            all_data.append(line)
    return all_data


filenames = [f'./file {number}.txt' for number in range(1, 5)]

start1 = datetime.now()
res1 = read_info('file 1.txt')
res2 = read_info('file 2.txt')
res3 = read_info('file 3.txt')
res4 = read_info('file 4.txt')
end1 = datetime.now()
time1 = end1 - start1
print(f'time line: {time1}')
if __name__ == '__main__':
    start2 = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end2 = datetime.now()
    time2 = end2 - start2
    print(f'time multi: {time2}')

