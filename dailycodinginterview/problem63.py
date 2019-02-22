def build_word_right(board, r, c, word):
    candidate = ''
    for i in range(c, min(len(board[r], len(word)))):
        candidate = candidate.join(word[r][i])
    return candidate


def build_word_down(board, r, c, word):
    candidate = ''
    for i in range(r, min(len(board[c], len(word)))):
        candidate = candidate.join(word[i][c])
    return candidate


def word_search(board, m, n, word):
    for r in range(len(m)):
        for c in range(min(len(word), len(n))):
            word_right = build_word_right(board, r, c, word)
            word_down = build_word_down(board, r, c, word)
            if word in [word_right, word_down]:
                return True
    return False