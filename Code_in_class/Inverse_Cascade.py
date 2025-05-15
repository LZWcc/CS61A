def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)
grow = lambda n : f_then_g(grow, print, n // 10)
shrink = lambda n : f_then_g(print, shrink, n // 10)


def count_partitions(n, m):
    """计算将正整数 n 划分成不超过 m 的正整数之和的方案数"""
    if n == 0:  # 需要划分的数为0, 只有一种方案
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        """dp[n][m] = dp[n - m][m] + dp[n][m - 1]"""
        with_m = count_partitions(n - m, m)
        """使用了一个m, 剩余的n-m仍可以使用不超过m的数"""
        without_m = count_partitions(n, m - 1)
        """不使用m, 只使用不超过m-1的数"""
        return with_m + without_m
