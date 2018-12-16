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
echo 'pushing output folder (production version) to master...'
pelican content -o output -s publishconf.py
git push origin master || echo "Commit failed"
git subtree push --prefix output origin gh-pages || echo "Commit failed"
pelican content -o output
```


git subtree push --prefix output origin gh-pages