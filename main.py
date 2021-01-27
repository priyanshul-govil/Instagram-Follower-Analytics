from script_class import InstagramUnfollower
import csv
from sys import argv


def main():

    # Enter details here or use Command-Line Arguments
    username = ""
    password = ""

    if len(argv) == 3:
        username = argv[1]
        password = argv[2]

    ob = InstagramUnfollower(username, password)
    ob.execute_script()

    print("  ACCOUNTS THAT DO NOT FOLLOW YOU BACK  ")
    print("========================================\n")

    with open("unfollowers.csv", "w", newline="") as csvfile:
        #with open("whitelist.txt", "w") as whitelist:
            csvwriter = csv.writer(csvfile)
            for acc in ob.unfollowers:
                #whitelist.write(f'{acc}\n')
                print(f"{acc:30s} https://www.instagram.com/{acc}")
                csvwriter.writerow([acc, f'https://www.instagram.com/{acc}'])


    with open("ghost_followers.csv", "w", newline="") as csvfile:
        #with open("blacklist.txt", "w") as blacklist:
            csvwriter = csv.writer(csvfile)
            for acc in ob.ghost_followers:
                #blacklist.write(f'{acc}\n')
                csvwriter.writerow([acc, f'https://www.instagram.com/{acc}'])

    

if __name__ == "__main__":
    main()

