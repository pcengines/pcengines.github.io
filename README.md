# This repository contains pcengines.github.io page files.

#### To create a new post

- Create a .markdown file inside _posts folder.

- Name the file according to the standard jekyll format.

```
   2016-03-30-i-love-design.markdown
```

- Write the Front Matter and content in the file.

    ```
          ---
          layout: post | default | page
          title:  String Post Title
          date:   Time Stamp
          categories: String | Array of Strings Category / Categories 
          ---
    ```

    ```
        ---
        layout: post
        title:  "The One with the Blackout"
        date:   2016-03-30 19:45:31 +0530
        categories: ["life", "friends"]
        ---
    ```  


#### Create new pages, such a breeze!

- Create a .md file in the root directory.
- 
- Name the file with the desired page link name.

```
   about.md
```

```
   design.md
```

- Write the Front Matter and content in the file.

```
          ---
          layout: page
          title: String Title of the webpage
          permalink: / String / Permalink for the webpage
          tagline: String Optional DevJournal Feature : Tagline for the page
          ---
```      
```
        ---
        layout: page
        title:  "Science"
        permalink:   /science/
        tagline : "Humanity is overrated."
        ---
```

#### Local preview

Instructions for Ubuntu:

1. Installation (do it only once):

```shell
sudo apt-get install ruby-full build-essential zlib1g-dev
echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
gem install jekyll bundler
```

2. Rebuilding and launching preview server:

```shell
bundle install
bundle exec jekyll serve
```

#### Issues

If you want to create an issue, [here](https://github.com/pcengines/apu2-documentation/issues)
is the right place for that.