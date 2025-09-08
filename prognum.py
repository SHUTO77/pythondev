# prognum.py

def fib(n):
    """1番目と2番目が1のフィボナッチ数列で、n番目の値を返す（nは1以上）"""
    if n == 1 or n == 2:          # ベースケース
        return 1
    return fib(n - 1) + fib(n - 2) # 再帰ケース
