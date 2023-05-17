from functools import cmp_to_key

#그리디로는 안풀림 백트래킹인가 ㅏㅏㅏㅏㅏ아ㅏㅏㅏㅏㅏㅏ 입력값 30만인거보면 dp인데음ㅁㅁ

N = int(input())
arr = list(map(int,input().split()))

answer = []
def dfs()