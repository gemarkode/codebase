---
layout: default
title: About
permalink: /about/
---

<pre class="language-php" id="highlight"></pre>
<script>
  (function() {
    // Select node, and escape special characters
    var el = document.querySelector('.xml'),
        esc = _.escape(el.innerHTML);
    el.innerHTML = esc;
    hljs.highlightBlock(el);
})();

var url = 'https://raw.githubusercontent.com/gemarkode/hacktoberfest/main/renovate.json';
fetch(url)
.then(res => res.text())
.then((out) => {
  document.getElementById("highlight").innerText = out
})
.catch(err => { throw err });
</script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.6.0/styles/monokai-sublime.min.css">
  <script src="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.2.0/build/highlight.min.js"></script>
  <script>window.onload = function() {
    var aCodes = document.getElementsByTagName('pre');
    for (var i=0; i < aCodes.length; i++) {
        hljs.highlightBlock(aCodes[i]);
    }
};</script>
  
You’ll find this post in your `_posts` directory. Go ahead and edit it and re-build the site to see your changes. You can rebuild the site in many different ways, but the most common way is to run `jekyll serve`, which launches a web server and auto-regenerates your site when a file is updated.

Jekyll requires blog post files to be named according to the following format:

`YEAR-MONTH-DAY-title.MARKUP`

Where `YEAR` is a four-digit number, `MONTH` and `DAY` are both two-digit numbers, and `MARKUP` is the file extension representing the format used in the file. After that, include the necessary front matter. Take a look at the source for this post to get an idea about how it works.

Jekyll also offers powerful support for code snippets:

```php
def print_hi(name)
  puts "Hi, #{name}"
end
print_hi('Tom')
#=> prints 'Hi, Tom' to STDOUT.
```

Check out the [Jekyll docs][jekyll-docs] for more info on how to get the most out of Jekyll. File all bugs/feature requests at [Jekyll’s GitHub repo][jekyll-gh]. If you have questions, you can ask them on [Jekyll Talk][jekyll-talk].

[jekyll-docs]: https://jekyllrb.com/docs/home
[jekyll-gh]:   https://github.com/jekyll/jekyll
[jekyll-talk]: https://talk.jekyllrb.com/
