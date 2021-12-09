import sys
def test(para):
    print(para)
    return para
def main():
    print(f"number of arguments {len(sys.argv)}")
    print(f"try function call {test(5)}")
    print(f"Arguments are {str(sys.argv)}")
if __name__ == "__main__":
    main()
