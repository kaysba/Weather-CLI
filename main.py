import argparse
import display
import api

def get_args():

    parser = argparse.ArgumentParser(description="Usage : \n--city for selecting the city.\n--lang for specifing the language.")
    parser.add_argument('--city', type=str, help='Name of the city')
    parser.add_argument('--lang', type=str, help='Language selection (en : English, fr : French, ar : Arabic...')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = get_args()
    if args.city is None:
        print("You need to specify a city.")
        exit(1)
    display.display(api.get_data(args.city, args.lang))
