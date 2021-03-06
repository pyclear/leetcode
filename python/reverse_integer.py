#!/usr/bin/env python
# encoding: utf-8
# author: cappyclearl


class Solution(object):
    x_min = -2147483648
    x_max = 2147483647

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_str = str(x)
        # 直接判断是否存在负号，
        # 其实应该加判断是否存在正号的
        if x_str.isdigit():
            tmp = int(x_str[::-1])
            if tmp > self.x_max:
                return 0
            return tmp
        else:
            x_int = x_str[1:]
            x_result = -int(x_int[::-1])
            if x_result < self.x_min:
                return 0
            return x_result


if __name__ == '__main__':
    s = Solution()
    assert s.reverse('123') == 321
    assert s.reverse('-123') == -321
