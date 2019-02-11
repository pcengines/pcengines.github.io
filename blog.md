---
layout: default
title: Blog
permalink: /blog/
---

<section>
    <div class="jumbotron">
        <div class="container">
            <h1>PC ENGINES™</h1>
            <h3 class="blog">Blog</h3>
        </div>
    </div>
</section>

<section id="page-content">
    <div class="container">
        <div class="post-list">
            {% for post in site.posts %}
            <div class="post-box">
                <div class="post-title">
                    <a class="post-title" href="{{post.url | prepend:site.baseurl }}"> {{ post.title }}</a>
                </div>
                <div class="post-excerpt">
                    {{ post.content | strip_html | truncatewords:20}}
                </div>
                <div class="posted">
                    posted on
                    <span class="posted-on">

                        {{ post.date | date: "%A, %B %-d, %Y" }}
                    </span>
                    <span class="in">
                        in
                    </span>
                    <span class="categories-on">
                        {% for category in post.categories %}
                        {{category}}&nbsp;{% if forloop.last %}{% else %},{% endif %}
                        {% endfor %}
                    </span>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>    
</section>