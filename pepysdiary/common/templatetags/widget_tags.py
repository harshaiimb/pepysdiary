from django import template

from pepysdiary.news.models import Post

register = template.Library()

# Things that appear in the sidebar on several pages.


@register.simple_tag
def rss_feed_link(kind):
    feeds = {
        'articles': {
            'url': 'http://feeds.feedburner.com/PepysDiary-InDepthArticles',
            'things': 'In-Depth articles',
        },
        'entries': {
            'url': 'http://feeds.feedburner.com/PepysDiary',
            'things': 'Diary entries',
        },
        'posts': {
            'url': 'http://feeds.feedburner.com/PepysDiary-SiteNews',
            'things': 'Site News posts',
        },
        'topics': {
            'url': 'http://feeds.feedburner.com/PepysDiary-Encyclopedia',
            'things': 'Encyclopedia topics',
        },
        # Not on Feedburner yet:
        # 'letters': {
        #     'url': 'http://feeds.feedburner.com/PepysDiary-SiteNews',
        #     'things': 'Site News posts',
        # }
    }
    return '<li class="feed"><a href="%s">RSS feed of %s</a></li>' % (
                                    feeds[kind]['url'], feeds[kind]['things'])


@register.simple_tag(takes_context=True)
def latest_news(context, quantity=5):
    """Displays links to the most recent Site News Posts."""
    html = ''
    post_list = Post.published_posts.all()[:quantity]
    if post_list:
        for post in post_list:
            html += """ <dt><a href="%s">%s</a></dt>
<dd>%s</dd>
""" % (post.get_absolute_url(),
        post.title,
        post.date_published.strftime(context['date_format_long_strftime']))

        html = """<h4>Latest Site News</h4>
<dl>
%s</dl>
""" % html
    return html