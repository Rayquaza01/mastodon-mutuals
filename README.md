# mastodon-mutuals
Export your mutuals from Mastodon

# How To Use

You'll need Python3 and Mastodon.py. Install with `pip3 install Mastodon.py`.

Run the program with `python3 mutuals.py -i instance -t token` where
 * `-i` / `--instance` is your instance (e.g. mastodon.social)
 * `-t` / `--token` is your access token.

You can generate a token at `https://<your-instance>/settins/applications`. This program needs access to read:accounts and read:follows.

After running, 3 files will be written:
 * followers.txt - containing all accounts who follow you
 * following.txt - containing all accounts that you follow
 * mutuals.txt - containing all accounts that you're mutuals with (i.e. you both follow each other)
