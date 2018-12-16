## Blog made in Pelican

to use local .gitconfig file
```bash
git config --local include.path ../.gitconfig
```

to publish blog (push output subtree to gh-pages)
```bash
git pb
```


.git/hooks/pre-push
```shell
#!/bin/sh
echo 'commit message:'
read commit_message
echo 'pushing output folder (production version) to master...'
pelican content -o output -s publishconf.py
git add ./output
git add ./content
git commit -m $commit_message
git push origin master || echo "push failed"
git subtree push --prefix output origin gh-pages || echo "push failed"
pelican content -o output
```


git subtree push --prefix output origin gh-pages