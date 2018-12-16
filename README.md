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
while read local_ref local_sha remote_ref remote_sha
do
        if [ "$remote_ref" = "refs/heads/source" ]
        then
                echo 'pushing output folder (production version) to master...'
                pelican content -o output -s publishconf.py
                git subtree push --prefix output origin gh-pages
                pelican content -o output
        fi
done

exit 0
```


git subtree push --prefix output origin gh-pages