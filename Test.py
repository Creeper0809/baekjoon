import sys
import random
import copy
from collections import deque


##########################
# MazeSolver (정답 솔루션)
##########################
class MazeSolver:
    def __init__(self, M, N, grid):
        """
        초기화.
          M: 미로의 너비 (열 개수)
          N: 미로의 높이 (행 개수)
          grid: N개의 문자열 리스트 (각 문자열은 미로의 한 행)
                (단, 내부에서는 리스트의 리스트 형태로 처리)
        """
        self.M = M
        self.N = N
        self.grid = grid

    def is_area_empty(self, r, c, L):
        """
        후보 장애물 영역이 모두 빈 칸('.')인지 확인.
        (r, c)에서 시작하는 L×L 영역을 검사.
        """
        for i in range(r, r + L):
            for j in range(c, c + L):
                if self.grid[i][j] != '.':
                    return False
        return True

    def bfs_path_exists(self, grid):
        """
        grid에 대해 (0,0)에서 (N-1, M-1)까지 4방향(상하좌우) 이동으로 도달 가능한 경로가 존재하는지 BFS로 검사.
        """
        N, M = self.N, self.M
        if grid[0][0] != '.' or grid[N - 1][M - 1] != '.':
            return False
        visited = [[False] * M for _ in range(N)]
        dq = deque()
        dq.append((0, 0))
        visited[0][0] = True

        while dq:
            i, j = dq.popleft()
            if i == N - 1 and j == M - 1:
                return True
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and grid[ni][nj] == '.':
                    visited[ni][nj] = True
                    dq.append((ni, nj))
        return False

    def solve(self):
        """
        모든 후보 장애물(정사각형)을 전수 탐색하여, 장애물을 하나 설치한 후
        (0,0)에서 (N-1, M-1)으로 가는 경로가 존재하지 않으면 해당 후보의
        정사각형 크기와 위치(왼쪽 상단 좌표)를 반환한다.

        입구 (0,0)과 출구 (N-1, M-1)은 후보 영역에 포함되면 안된다.
        (출력은 1-indexed: x는 열 번호, y는 행 번호)
        """
        N, M = self.N, self.M

        # L: 장애물의 변의 길이, 가장 작은 크기부터 탐색
        for L in range(1, min(N, M) + 1):
            # (r, c): 후보 정사각형의 왼쪽 상단 좌표 (0-indexed)
            for r in range(0, N - L + 1):
                for c in range(0, M - L + 1):
                    # 입구 혹은 출구를 후보 영역에 포함하면 건너뜀
                    if (r <= 0 < r + L and c <= 0 < c + L) or (r <= N - 1 < r + L and c <= M - 1 < c + L):
                        continue
                    # 후보 영역이 모두 빈 칸이어야 함
                    if not self.is_area_empty(r, c, L):
                        continue

                    # grid 복사 후 후보 영역을 '#'로 채워 장애물을 설치한 new_grid 제작
                    new_grid = copy.deepcopy(self.grid)
                    for i in range(r, r + L):
                        for j in range(c, c + L):
                            new_grid[i][j] = '#'

                    # BFS로 (0,0)에서 (N-1, M-1)까지 경로가 존재하는지 확인
                    if not self.bfs_path_exists(new_grid):
                        # 경로가 차단되었다면 이 후보가 정답.
                        return f"{L} {c + 1} {r + 1}"  # 출력은 1-indexed: (x, y) = (c+1, r+1)
        return "Impossible"


########################################
# 테스트용 코드 (아래쪽 코드: multi_source_bfs 등)
########################################

def multi_source_bfs(sources, M, N, graph,find,direction):
    vis = [[0] * M for _ in range(N)]
    dq = deque(sources)
    for i, j in sources:
        vis[i][j] = 1
    while dq:
        i, j = dq.popleft()
        for di, dj in direction:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and graph[ni][nj] == find and not vis[ni][nj]:
                vis[ni][nj] = 1
                dq.append((ni, nj))
    return vis


def build_prefix_sum(grid, N, M):
    S = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(N):
        row_sum = 0
        for j in range(M):
            row_sum += grid[i][j]
            S[i + 1][j + 1] = S[i][j + 1] + row_sum
    return S


def safe_query(S, r1, c1, r2, c2, N, M):
    r1 = max(0, min(r1, N - 1))
    c1 = max(0, min(c1, M - 1))
    r2 = max(0, min(r2, N - 1))
    c2 = max(0, min(c2, M - 1))
    if r1 > r2 or c1 > c2:
        return 0
    return S[r2 + 1][c2 + 1] - S[r1][c2 + 1] - S[r2 + 1][c1] + S[r1][c1]


def solve_test(M, N, graph):
    num_arr = multi_source_bfs([(0, 0)], M, N, graph,'.',[[0, 1], [1, 0],[0,-1],[-1,0]])
    ru_sources = []
    for j in range(M - 1):
        if num_arr[0][j] == 0:
            ru_sources.append((0, j))
    for i in range(N - 1):
        if num_arr[i][M - 1] == 0:
            ru_sources.append((i, M - 1))
    right_up = multi_source_bfs(ru_sources, M, N, num_arr,0,[[0,1],[1,0],[-1,0],[0,-1],[1,1],[-1,-1],[-1,1],[1,-1]])
    ld_sources = []
    for j in range(M-1):
        if num_arr[N - 1][j] == 0:
            ld_sources.append((N - 1, j))
    for i in range(N-1):
        if num_arr[i][0] == 0:
            ld_sources.append((i, 0))
    left_down = multi_source_bfs(ld_sources, M, N, num_arr,0,[[0,1],[1,0],[-1,0],[0,-1],[1,1],[-1,-1],[-1,1],[1,-1]])
    num_arr[N - 1][M - 1] = 0
    right_prefix = build_prefix_sum(right_up, N, M)
    down_prefix = build_prefix_sum(left_down, N, M)
    install_prefix = build_prefix_sum(num_arr, N, M)

    ans = sys.maxsize
    ans_i = ans_j = -1
    for i in range(N):
        for j in range(M):
            if (i == 0 and j == 0) or (i == N - 1 and j == M - 1):
                continue
            if graph[i][j] != '.':
                continue
            limit = min(M - j, N - i)
            lo = -1
            hi = limit
            while lo + 1 < hi:
                mid = (lo + hi) // 2
                if i + mid == N - 1 or (safe_query(down_prefix, i - 1, j - 1, i + mid + 1, j + mid + 1, N, M) > 0):
                    is_down = True
                else:
                    is_down = False

                if j + mid == M - 1 or (safe_query(right_prefix, i - 1, j - 1, i + mid + 1, j + mid + 1, N, M) > 0):
                    is_right = True
                else:
                    is_right = False
                if is_down and i == 0:
                    hi = mid
                    continue
                if is_right and j == 0:
                    hi = mid
                    continue
                if is_down and is_right:
                    hi = mid
                else:
                    lo = mid
            need_block = lo + 2
            if ans < need_block:
                continue

            lo = -1
            hi = limit
            while lo + 1 < hi:
                mid = (lo + hi) // 2
                total = safe_query(install_prefix, i, j, i + mid, j + mid, N, M)
                if total == (mid + 1) ** 2:
                    lo = mid
                else:
                    hi = mid
            max_install = lo + 1

            if max_install >= need_block:
                if ans > need_block:
                    ans = need_block
                    ans_i, ans_j = i, j

    if ans == sys.maxsize:
        return "Impossible"
    else:
        return f"{ans} {ans_j + 1} {ans_i + 1}"


###########################
# 입력 생성 함수 (랜덤 미궁)
###########################
def generate_maze(w, h, p_empty):
    """
    매개변수:
      w, h      : 미궁의 너비와 높이 (2 ≤ w, h ≤ 1500)
      p_empty   : 보장된 경로 외에 나머지 칸을 빈 칸('.')으로 만들 확률 (0과 1 사이)
    반환:
      maze      : 2차원 리스트, 각 원소가 '.' 또는 '#'
    """
    # 모든 칸을 '#'로 초기화
    maze = [['#'] * w for _ in range(h)]

    # (0,0)에서 (h-1, w-1)까지 오른쪽과 아래로만 이동하는 단조 경로 생성 (반드시 빈 칸)
    i, j = 0, 0
    maze[i][j] = '.'
    while (i, j) != (h - 1, w - 1):
        moves = []
        if i < h - 1:
            moves.append((i + 1, j))
        if j < w - 1:
            moves.append((i, j + 1))
        i, j = random.choice(moves)
        maze[i][j] = '.'

    # 나머지 칸에 대해 확률 p_empty로 빈 칸('.')으로 채움
    for i in range(h):
        for j in range(w):
            if maze[i][j] == '.':
                continue
            if random.random() < p_empty:
                maze[i][j] = '.'

    # 입구와 출구는 확실히 빈 칸
    maze[0][0] = '.'
    maze[h - 1][w - 1] = '.'
    return maze


###########################
# 메인: 랜덤 입력 생성 후 두 솔루션 결과 비교
###########################
def main():
    count = 1
    while True:

        # 테스트용: w와 h를 작게 생성 (예: 2~50); 실제 조건은 2~1500로 가능
        w = random.randint(2, 50)
        h = random.randint(2, 50)
        p_empty = 0.3  # 나머지 칸에 대해 빈 칸으로 만들 확률

        maze = generate_maze(w, h, p_empty)

        # MazeSolver는 리스트의 리스트 형태의 grid로 처리
        grid_solver = [row[:] for row in maze]
        solver = MazeSolver(w, h, grid_solver)
        ans1 = solver.solve()

        # 테스트용 솔루션은 문자열 리스트를 사용
        graph_test = [''.join(row) for row in maze]
        ans2 = solve_test(w, h, graph_test)

        # 만약 두 결과가 다르면 입력과 두 솔루션의 결과를 출력
        if ans1[0] != ans2[0]:
            sys.stdout.write("Difference found!\n")
            sys.stdout.write(f"w, h = {w}, {h}\n")
            sys.stdout.write("Maze:\n")
            for row in maze:
                sys.stdout.write("".join(row) + "\n")
            sys.stdout.write(f"MazeSolver answer: {ans1}\n")
            sys.stdout.write(f"Test solution answer: {ans2}\n")
            break
        else:
            sys.stdout.write(f"Case {count}: Same answers.\n")
        count+=1


if __name__ == '__main__':
    main()
