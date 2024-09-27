def hanoi(n, source, destination, auxiliary):
    # Base case: only one disk to move
    print(n)
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    # Move n-1 disks from source to auxiliary, using destination as a temporary peg
    hanoi(n - 1, source, auxiliary, destination)

    # Move the nth disk from source to destination
    print(f"Move disk {n} from {source} to {destination}")

    # Move the n-1 disks from auxiliary to destination, using source as a temporary peg
    hanoi(n - 1, auxiliary, destination, source)


# Driver code
n = 3  # Number of disks
hanoi(n, 'A', 'C', 'B')  # A = Source, C = Destination, B = Auxiliary

