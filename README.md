# Instagram Follower Analytics

Since the change of the Instagram API, many Follower Insight apps have stopped working. This is an attempt to create a web scraping script that scrapes your Instagram account for *follower* and *following* details, and generates data as a `CSV` file. Additionally, it outputs details of **users who don't follow you back** to the terminal so that you can easily unfollow them.


## DEPENDENCIES

First things first, let's get these out of the way. Open a **terminal window** (`cmd` for Windows) and execute the following command:
```
pip install Selenium
```
We require `Firefox`, so go ahead and [download](https://www.mozilla.org/en-US/firefox/new/) that too (if not already).
Also, I hope you have `Python3` installed. If not, then [here you go](https://www.python.org/).


## NOMENCLATURE

There are quite some terms I have used. Although, they are pretty intuitive, here they are (just in case):

1. `Unfollowers`: These are the users that **you follow** but **they don't follow** you back.

2. `Ghost Followers`: These are the users that **follow you** but **you don't follow** them back.

3. `Whitelist`: This list contains the `unfollowers` that you don't want to show. In simple terms, they don't follow you back but you don't want to unfollow them.

4. `Blacklist`: This list contains the `ghost followers` that you never want to follow back.

## USAGE

Clone this repository to your local machine or download the repository as a `zip` folder and unzip it. Navigate to the root directory.


#### &emsp;Dealing with `whitelist.txt` and `blacklist.txt`
<ul>
	
<li>
	
Initially both these files will be empty. In case you wish to utilise them, go ahead and add the `username` of each of the required users in a separate line. Save the files now.

<li>
	
Optionally, you can also **un-comment** lines `23, 26` and `32, 35` in `main.py` and run the script once. This will add all `unfollowers` to `whitelist.txt` and all `ghost followers` to `blacklist.txt`. Then, you can then delete the users which you don't require in these files. **Now, save the file and comment back those lines**. Use this method if you have a lot of users initially.  

</ul>

### Now, how should we run the script?

Well, there are two ways:

1. Enter your `username` and `password` at lines `9 and 10` inside `main.py`. Run the python script using `python main.py`.

2. Use command-line arguments. Run the script using `python main.py [username] [password]`.

Note, you do not need to make any changes to `script_class.py`. Leave the remotely-controlled browser window open, and let it work in peace :wink:

**In case the script isn't able to login to Instagram (generally happens for the first time), head over to your Instagram app. You might have received a security alert. Resolve that by confirming that the sign-in attempt was you. Run the script again, it should work.**

## OUTPUT

Now that you've reached till here, two files must have been created:

1. `unfollowers.csv`: Contains username and profile page link of all unfollowers.

2. `ghost_followers.csv`: Contains username and profile page link of all ghost followers.

You may open these files with any suitable `CSV` viewer (such as `Excel`). In case you need to unfollow some user, you may head over to their profile page by clicking their respective link, and doing so manually.

Additionally, I have also made it such that all `unfollowers` along with their profile links are outputed to the terminal window, in the hope that it'll save you time!

## FURTHER SCOPE

+ Making the script unfollow users.
+ Include a list of recent unfollowers.

## CONTACT

If you have any issue, create an `ISSUE` inside GitHub.

If you need any other feature, have any suggestion, or simply want to contribute, you can reach out to me at [my LinkedIn](https://www.linkedin.com/in/priyanshul/).
