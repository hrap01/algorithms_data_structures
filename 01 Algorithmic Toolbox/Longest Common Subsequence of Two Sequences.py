def lcs2(n, first_sequence, m, second_sequence):
    outcome_array = [[None]*(m+1) for i in range(n + 1)]

    for i in range(n+1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                outcome_array[i][j] = 0
            elif first_sequence[i-1] == second_sequence[j-1]:
                outcome_array[i][j] = outcome_array[i-1][j-1] + 1
            else:
                outcome_array[i][j] = max(outcome_array[i-1][j], outcome_array[i][j-1])

    return outcome_array[n][m]

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(n, a, m, b))
