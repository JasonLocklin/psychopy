#!/bin/sh
#Update Repo, merging from upstream, pushing to github
git pull upstream master && git push && echo "Update successful"

