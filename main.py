from text import Text
import numpy as np


def get_word_vector(word_list1, word_list2):
    key_word = list(set(word_list1 + word_list2))
    # 给定形状和类型的用0填充的矩阵存储向量
    word_vector1 = np.zeros(len(key_word))
    word_vector2 = np.zeros(len(key_word))
    # 计算词频
    # 依次确定向量的每个位置的值
    for i in range(len(key_word)):
        # 遍历key_word中每个词在句子中的出现次数
        for j in range(len(word_list1)):
            if key_word[i] == word_list1[j]:
                word_vector1[i] += 1
        for k in range(len(word_list2)):
            if key_word[i] == word_list2[k]:
                word_vector2[i] += 1
    return word_vector1, word_vector2


def cos_dist(vector1, vector2):
    # 返回向量余弦相似度
    dist = float(np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2)))
    return dist


def main():
    # D:\pycode\lunwen查重\测试文本\orig.txt
    # D:\pycode\lunwen查重\测试文本\orig_0.8_add.txt
    # pyinstaller -F xxx.py
    # D:/pycode/lunwen查重/result.txt
    try:
        text1 = Text(input('请输入第一个文本的绝对路径:\n'))
        text2 = Text(input('请输入第二个文本的绝对路径:\n'))
        filename = input('请输入输出文件路径：\n')
        a = text1.get_word_list(1)
        b = text2.get_word_list(1)
    except FileNotFoundError:
        print('未找到文件路径！')
        return -1
    if text1.get_size() == 0 or text2.get_size() == 0:
        print('文件为空！')
        return -2
    vec1, vec2 = get_word_vector(a, b)
    distance = cos_dist(vec1, vec2)
    with open(filename, 'w') as f:
        f.write(f'文件重复率为{distance:.2f}')
    print(f'答案文件的路径为：{filename}')
    print(f'文件重复率为{distance:.2f}')
    input('press to quit')


if __name__ == '__main__':
    main()
