# Zyck's blog

_built with [github Pages with jekyll](https://help.github.com/articles/using-jekyll-as-a-static-site-generator-with-github-pages/)_

write something interesting to myself
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

