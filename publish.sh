#!/usr/bin/env bash
echo 'commit message:'
read commit_message
echo 'pushing output folder (production version) to master...'
pelican content
git add ./output
git add ./content
git commit -m "$commit_message"
git push origin master || echo "push failed"
git subtree push --prefix output origin gh-pages || echo "push failed"