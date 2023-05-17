if __name__ == '__main__':
    try:
        with open('readme.txt', 'w') as f:
            f.write('Create a new text file!')
    except FileNotFoundError:
        print("Can't create the txt file.")

