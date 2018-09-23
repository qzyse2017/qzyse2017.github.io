# Zyck's blog

_built with [github Pages with jekyll](https://help.github.com/articles/using-jekyll-as-a-static-site-generator-with-github-pages/)_

write something worth recording
visit [https://qzyse2017.github.io](https://qzyse2017.github.io) to view the blogs.

## How to reuse the site's page layouts
1. clone this repo
```
git clone https://github.com/qzyse2017/qzyse2017.github.io
```

2. remove ```*.mardown``` files in  ```_posts``` directory

3. write some post files yourself in  ```_posts``` directory, you can refer to the format like any file in ```_posts``` directory

4. configure settings in ```_config.yml```, you may refer to [this current site](https://qzyse2017.github.io) and change the corresponding parts in ```_config.yml```

5. generate files to be showed   
under WSL and Linux, enter this repo which you have cloned and configured and written some new posts  
run command ```bundle exec jekyll serve```    
preview your local Jekyll site in your web browser at ```http://localhost:4000.```
I haven't tried how to get it done under windows or osx, you may refer to [this help page in GitHub](https://help.github.com/articles/setting-up-your-github-pages-site-locally-with-jekyll).  

6. you may also need to remove some other files like ```genContent.py``` and files under ```_site/daily_posts```  

## Generate contents automatically while committing

Although jekyll default template provides some code to generate contents while building the website, I did not notice it and wrote a simple script to generate contents myself: ``genPosts.py`` and I now added a gt hook to automatically start it every time I use `git commit`, if you also want to have a try:

1. copy the following code and name it `pre-commit`
2. put it under a git inited directory, ``dir-name/.git/hooks/``, and you want to prevent it from working, use ``git commit --no-verify``
3. use `git add <you-new-added-file-name-here>` 
4. if you do not add new posts, it is recommended that you use ```git commit --no-verify```

```shell
#!/bin/sh

if [ -n eval $(python genContent.py)]
then
	git commit content.md -m 'Renew content' --no-verify
else	
	# Handle error
	echo >&2 "Found error while generate contents, will execute normal commit without generating new contents"
fi

exit 0
```

Note:

1. if any error occurred, you can use ```git reflog``` to list all you operations and use ```git reset --hard <status-sha1> ``` here to reset your status.

2. In fact the pre-commit hook will only commit changes in ```content.md```, so you do not need to care about other files' changes wil be included.