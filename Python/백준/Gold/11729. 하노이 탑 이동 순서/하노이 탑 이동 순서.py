import sys
def hanoi(n, a, b, c, moves):
    if n == 1:
        moves.append(f"{a} {c}")
    else:
        hanoi(n-1, a, c, b, moves)
        moves.append(f"{a} {c}")
        hanoi(n-1, b, a, c, moves)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    moves = []
    hanoi(n, 1, 2, 3, moves)
    output = [str(len(moves))] + moves
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()