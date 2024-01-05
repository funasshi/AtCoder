n = int(input())
a_list = list(map(int, input().split()))

pieces = [360]
now_top = 0


def cut(pieces, rotate):
    cutted = False
    next_pieces = []
    for i, piece in enumerate(pieces):
        if piece > rotate and not cutted:
            piece1 = rotate
            piece2 = piece-rotate
            next_pieces.append(piece1)
            next_pieces.append(piece2)
            cutted = True
            cutted_space = i
        else:
            rotate -= piece
            next_pieces.append(piece)
    return next_pieces[cutted_space+1:]+next_pieces[:cutted_space+1]


for a in a_list:
    pieces = cut(pieces, a)
print(max(pieces))
