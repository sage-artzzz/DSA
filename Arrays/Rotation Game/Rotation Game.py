def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    a = list(map(int,input().split()))
    size = a[0]
    a = a[1:]
    b = int(input())
    b = b%size
    def reverse(arr,p1,p2):
        while p1<p2:
            temp = arr[p1]
            arr[p1] = arr[p2]
            arr[p2] = temp
            p1 += 1
            p2 -= 1
    reverse(a,0,size-1)
    reverse(a,0,b-1)
    reverse(a,b,size-1)
    for i in a:
        print(i,end=" ")
    return 0

if __name__ == '__main__':
    main()

