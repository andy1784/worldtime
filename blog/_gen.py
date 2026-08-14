import os, json, re

os.makedirs('/home/kaliuser/worldtime/blog', exist_ok=True)

DATE = '2026-08-10'
DISPLAY_DATE = 'August 10, 2026'

# Shared analytics/footer HTML
ANALYTICS_HEAD = '''    <script async src="https://www.googletagmanager.com/gtag/js?id=G-LBX0CDYSSV"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-LBX0CDYSSV');
    </script>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9728257902981529" crossorigin="anonymous"></script>'''

BODY_CLOSE = '''
    <script type="module" src="/assets/index-Dd7au40z.js" async></script>
    <script>
      document.addEventListener('DOMContentLoaded', function() {
        var seo = document.querySelector('.blog-wrap');
        if (seo) seo.style.display = 'none';
      });
    </script>
    <script>
      window.addEventListener('load',function(){
        var ahrefs=document.createElement('script');
        ahrefs.async=true;
        ahrefs.src='https://analytics.ahrefs.com/analytics.js';
        ahrefs.setAttribute('data-key','hB1VYWuwb1i/f1d8re7P2A');
        document.head.appendChild(ahrefs);
      });
    </script>
  </body>
</html>'''

FOOTER = '''
        <footer class="blog-footer">
            <a href="/privacy.html">Privacy</a>
            <a href="/about.html">About</a>
            <a href="/contact.html">Contact</a>
            <a href="/terms.html">Terms</a>
            <p style="margin-top:8px;color:#444;font-size:0.75rem">&copy; 2026 World Time Sync</p>
        </footer>'''

def make_post(filename, title, meta_desc, keywords, breadcrumb, read_time, tags, h1, content, faq_list, article_section="Time Zones", word_count=None, speakable=None):
    """
    Generate a blog post with enhanced Article schema.
    
    Args:
        filename: Output filename (e.g., 'my-post.html')
        title: Page title
        meta_desc: Meta description
        keywords: Meta keywords
        breadcrumb: Breadcrumb display name
        read_time: Minutes to read (int)
        tags: Comma-separated tags string
        h1: H1 heading
        content: HTML content string
        faq_list: List of (question, answer) tuples for FAQ schema
        article_section: Article section/category (default: "Time Zones")
        word_count: Word count (int), auto-calculated if None
        speakable: List of CSS selectors for speakable content, or None
    """
    # Calculate word count if not provided
    if word_count is None:
        # Strip HTML tags and count words
        text_content = re.sub(r'<[^>]+>', ' ', content)
        word_count = len(text_content.split())
    
    # Build FAQ JSON
    faq_json = json.dumps([{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq_list], ensure_ascii=False)
    
    canonical = f'https://worldtimessync.com/blog/{filename}'
    
    # Build Article schema with all enhanced fields
    article_schema = {
        "@context": "https://schema.org",
        "@type": "Article",  # Article type (BlogPosting is subtype but Article is preferred for Google News)
        "headline": title,
        "description": meta_desc,
        "articleSection": article_section,
        "keywords": keywords,
        "wordCount": word_count,
        "timeRequired": f"PT{read_time}M",
        "inLanguage": "en",
        "author": {"@type": "Organization", "name": "World Time Sync", "url": "https://worldtimessync.com"},
        "publisher": {
            "@type": "Organization",
            "name": "World Time Sync",
            "url": "https://worldtimessync.com",
            "logo": {
                "@type": "ImageObject",
                "url": "https://worldtimessync.com/logo.png",
                "width": 512,
                "height": 512
            }
        },
        "datePublished": DATE,
        "dateModified": DATE,
        "mainEntityOfPage": {"@type": "WebPage", "@id": canonical},
        "image": "https://worldtimessync.com/og-image.png"
    }
    
    # Add speakable if provided
    if speakable:
        article_schema["speakable"] = {
            "@type": "SpeakableSpecification",
            "cssSelector": speakable
        }
    
    article_json = json.dumps(article_schema, ensure_ascii=False)
    
    # Breadcrumb schema
    breadcrumb_json = json.dumps({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://worldtimessync.com/"},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": "https://worldtimessync.com/#blog"},
            {"@type": "ListItem", "position": 3, "name": breadcrumb, "item": canonical}
        ]
    }, ensure_ascii=False)
    
    # FAQ schema
    faq_schema = f'{{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": {faq_json}}}'
    
    # Write file
    with open(f'/home/kaliuser/worldtime/blog/{filename}', 'w', encoding='utf-8') as f:
        f.write('<!doctype html>\n')
        f.write('<html lang="en">\n')
        f.write('<head>\n')
        f.write('    <meta charset="UTF-8">\n')
        f.write('    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">\n')
        f.write('    <meta name="theme-color" content="#667eea">\n')
        f.write('    <meta name="google-site-verification" content="tNRYRY4K5ZdeEBPId3_g0GiclaIlooP5GhihYhXwknk">\n')
        f.write(f'    <title>{title}</title>\n')
        f.write(f'    <meta name="title" content="{title}">\n')
        f.write(f'    <meta name="description" content="{meta_desc}">\n')
        f.write(f'    <meta name="keywords" content="{keywords}">\n')
        f.write('    <meta name="robots" content="index, follow">\n')
        f.write('    <meta name="author" content="World Time Sync">\n')
        f.write('    <meta property="og:type" content="article">\n')
        f.write(f'    <meta property="og:url" content="{canonical}">\n')
        f.write(f'    <meta property="og:title" content="{title}">\n')
        f.write(f'    <meta property="og:description" content="{meta_desc}">\n')
        f.write('    <meta property="og:image" content="https://worldtimessync.com/og-image.png">\n')
        f.write('    <meta name="twitter:card" content="summary_large_image">\n')
        f.write(f'    <meta name="twitter:title" content="{title}">\n')
        f.write(f'    <link rel="canonical" href="{canonical}">\n')
        f.write(f'    <link rel="alternate" hreflang="x-default" href="{canonical}">\n')
        f.write(f'    <link rel="alternate" hreflang="es" href="https://worldtimessync.com/es/blog/{filename}">\n')
        f.write(f'    <link rel="alternate" hreflang="zh" href="https://worldtimessync.com/zh/blog/{filename}">\n')
        f.write(f'    <link rel="alternate" hreflang="ru" href="https://worldtimessync.com/ru/blog/{filename}">\n')
        f.write(f'    <link rel="alternate" hreflang="it" href="https://worldtimessync.com/it/blog/{filename}">\n')
        f.write(f'    <link rel="alternate" hreflang="de" href="https://worldtimessync.com/de/blog/{filename}">\n')
        f.write(f'    <link rel="alternate" hreflang="ja" href="https://worldtimessync.com/ja/blog/{filename}">\n')
        f.write('    <link rel="preload" href="/assets/blog.css" as="style">\n')
        f.write('<noscript><link rel="stylesheet" href="/assets/blog.css"></noscript>\n')
        f.write('    <link rel="icon" type="image/svg+xml" href="/favicon.svg">\n')
        f.write('    <link rel="stylesheet" href="/assets/index-ufePLcBr.css">\n')
        f.write(ANALYTICS_HEAD + '\n')
        f.write(f'    <script type="application/ld+json">\n')
        f.write(f'    {article_json}\n')
        f.write(f'    </script>\n')
        f.write(f'    <script type="application/ld+json">\n')
        f.write(f'    {breadcrumb_json}\n')
        f.write(f'    </script>\n')
        f.write(f'    <script type="application/ld+json">\n')
        f.write(f'    {faq_schema}\n')
        f.write(f'    </script>\n')
        f.write('\n</head>\n')
        f.write('<body>\n')
        f.write('    <a href="#main-content" class="skip-link">Skip to main content</a>\n')
        f.write('    <div id="root" role="application" aria-label="World Time Online Application">\n')
        f.write('        <div class="app-loading" aria-busy="true" aria-live="polite">\n')
        f.write('            <div class="app-loading-spinner" role="status" aria-label="Loading application"></div>\n')
        f.write('            <p class="app-loading-text">Loading World Time...</p>\n')
        f.write('        </div>\n')
        f.write('    </div>\n')
        f.write('    <main id="main-content">\n')
        f.write('        <article class="blog-wrap">\n')
        f.write('            <nav class="blog-breadcrumb" aria-label="Breadcrumb">\n')
        f.write(f'                <a href="/">Home</a> › <a href="/#blog">Blog</a> › <span aria-current="page">{breadcrumb}</span>\n')
        f.write('            </nav>\n')
        f.write(f'            <h1>{h1}</h1>\n')
        f.write(f'            <div class="blog-meta">���� {DISPLAY_DATE} &nbsp;·&nbsp; ��� {read_time} min read &nbsp;·&nbsp; ��� {tags}</div>\n')
        f.write('\n')
        f.write(content)
        f.write('\n')
        f.write(FOOTER + '\n')
        f.write('    </main>\n')
        f.write(BODY_CLOSE + '\n')
    
    size = os.path.getsize(f'/home/kaliuser/worldtime/blog/{filename}')
    print(f'Written: {filename} ({size} bytes)')
