""" single quotes '' are used to surround characters! :D
    can perform fun operators for string manipulation"""
def main():
    
    a_string = "howdy_do"
    if 'o' in a_string:
        print("got it!")
    mut_string = a_string
    mut_string += 'h'
    print(mut_string)


if __name__ == "__main__":
    main()