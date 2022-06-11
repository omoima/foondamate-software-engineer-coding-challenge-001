import api
import sys
import argparse
import dateparser 

parser = argparse.ArgumentParser()
parser.add_argument('-s', type= str, required=True, help=""" -s "01-01-2022" means start date is "01-01-2022" DMY""")
parser.add_argument('-e', type= str, required=True, help=""" -e "10-01-2022" means end date is "10-01-2022" DMY""")
if len(sys.argv) != 5:
    parser.print_help()
args = parser.parse_args()

if __name__ == '__main__':
    start = dateparser.parse(args.s, settings={'DATE_ORDER': 'DMY'})
    end = dateparser.parse(args.e, settings={'DATE_ORDER': 'DMY'})

    try:
        if (start.date()) and (end.date()):
            filtered_days = api.filter(start.date(), end.date())
            api.print_graph(filtered_days)
    except:
        print("Fix your arguments.")
