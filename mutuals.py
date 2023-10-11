import argparse
from mastodon import Mastodon

def print_list(l):
    for i in l:
        print(i)

def get_acct_name(account):
    acct = account["acct"]
    if "@" not in acct:
        acct += "@" + args.instance
    return acct


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--instance", type=str, help="Your mastodon instance, e.g. mastodon.social", required=True)
ap.add_argument("-t", "--token", type=str, help="Your access token, or the path to a file containing your access token", required=True)
args = ap.parse_args()

m = Mastodon(api_base_url=args.instance, access_token=args.token)

user = m.account_verify_credentials()

followers = m.account_followers(id=user["id"])
followers = m.fetch_remaining(followers)
following = m.account_following(id=user["id"])
following = m.fetch_remaining(following)

followers_acct = list(map(get_acct_name, followers))
following_acct = list(map(get_acct_name, following))
mutuals_acct = list(set(followers_acct) & set(following_acct))

with open("followers.txt", "w") as f:
    f.write("\n".join(followers_acct))

with open("following.txt", "w") as f:
    f.write("\n".join(following_acct))

with open("mutuals.txt", "w") as f:
    f.write("\n".join(mutuals_acct))
