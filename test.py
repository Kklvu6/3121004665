import unittest
from main import *


def main_test(route1, route2, route3):
    try:
        text1 = Text(route1)
        text2 = Text(route2)
        filename = route3
        a = text1.get_word_list()
        b = text2.get_word_list()
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
    print(f'答案文件的路径为{route3}')
    print(f'文件重复率为{distance:.2f}')
    return 0


class MyTest(unittest.TestCase):

    def test_route_error1(self):
        # 第一个参数是不存在路径，第二个参数是有内容路径
        self.assertEqual(-1, main_test('kkkkkkkkk', 'D:/pycode/lunwen查重/测试文本/orig_0.8_add.txt',
                                       'D:/pycode/lunwen查重/pyinstaller -F xxx.py'))

    def test_route_error2(self):
        # 两个参数都是不存在路径
        self.assertEqual(-1, main_test('kkkkkkkkk', 'kkkkkkkkk', 'D:/pycode/lunwen查重/result.txt'))

    def test_route_error3(self):
        # 第一个参数是有内容文件路径，第二个参数是不存在路径
        self.assertEqual(-1, main_test('D:/pycode/lunwen查重/测试文本/orig_0.8_add.txt',
                                       'kkkkkkkkk',
                                       'D:/pycode/lunwen查重/result.txt'))

    def test_file_empty1(self):
        # 第一个参数是有内容文件路径，第二个参数是空文件路径
        self.assertEqual(-2, main_test('D:/pycode/lunwen查重/测试文本/orig_0.8_add.txt',
                                       'D:/pycode/lunwen查重/测试文本/empty.txt', 'D:/pycode/lunwen查重/result.txt'))

    def test_file_empty2(self):
        # 两个参数都是有内容文件路径
        self.assertEqual(-2, main_test('D:/pycode/lunwen查重/测试文本/empty.txt',
                                       'D:/pycode/lunwen查重/测试文本/empty.txt',
                                       'D:/pycode/lunwen查重/result.txt'))

    def test_file_empty3(self):
        # 第一个参数是空文件路径，第二个参数是有内容文件路径
        self.assertEqual(-2, main_test('D:/pycode/lunwen查重/测试文本/empty.txt',
                                       'D:/pycode/lunwen查重/测试文本/orig_0.8_add.txt',
                                       'D:/pycode/lunwen查重/result.txt'))

    def test_both_errors1(self):
        # 第一个参数是不存在路径，第二个参数是有内容文件路径
        self.assertEqual(-1, main_test('kkkkkkkkkkkkkkkkkkkkkkkkkkkk',
                                       'D:/pycode/lunwen查重/测试文本/orig_0.8_add.txt',
                                       'D:/pycode/lunwen查重/result.txt'))

    def test_both_errors2(self):
        # 第一个参数是有内容文件路径，第二个参数是不存在路径
        self.assertEqual(-1, main_test('D:/pycode/lunwen查重/测试文本/orig_0.8_add.txt',
                                       'kkkkkkkkkkkkkkkkkkkkkkkkkkkk', 'D:/pycode/lunwen查重/result.txt'))

    def test_correct1(self):
        # 两个参数都是有内容文件路径
        self.assertEqual(0, main_test('D:/pycode/lunwen查重/测试文本/orig.txt',
                                      'D:/pycode/lunwen查重/测试文本/orig_0.8_add.txt',
                                      'D:/pycode/lunwen查重/result.txt'))

    def test_correct2(self):
        # 两个参数都是有内容文件路径
        self.assertEqual(0, main_test('D:/pycode/lunwen查重/测试文本/orig.txt',
                                      'D:/pycode/lunwen查重/测试文本/orig_0.8_dis_10.txt',
                                      'D:/pycode/lunwen查重/result.txt'))



if __name__ == "__main__":
    unittest.main()
