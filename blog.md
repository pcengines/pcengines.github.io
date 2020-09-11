---
layout: default
title: Blog
permalink: /blog/
---

<section>
    <div class="jumbotron">
        <div class="container">
            <span class="header-decor"></span>
            <h1>Blog</h1>
        </div>
    </div>
    <img class="jumbotron-img" src="/assets/bground.jpg" alt="PC ENGINES" />
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
                <a class="read-more" href="{{post.url | prepend:site.baseurl }}">read more</a>
            </div>
            {% endfor %}
        </div>
    </div>

</section>
