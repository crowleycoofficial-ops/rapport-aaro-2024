"""
OODA Loop Configuration
Autonomous SEO & Information Warfare System
"""

# Target Information
TARGET_URL = "https://crowleycoofficial-ops.github.io/rapport-aaro-2024/"
TARGET_KEYWORDS = [
    "AARO rapport",
    "UAP AARO",
    "F. Mathieu AARO",
    "rapport historique AARO",
    "AARO transparence",
    "Sean Kirkpatrick AARO",
    "David Grusch AARO",
    "UAP gouvernement",
    "AARO noyade poisson",
    "rétro-ingénierie AARO"
]

# Search Engines & Indexers
INDEXERS = {
    "google": "https://www.google.com/ping?sitemap=",
    "bing": "https://www.bing.com/ping?sitemap=",
    "duckduckgo": "https://www.duckduckgo.com/",
    "yandex": "https://yandex.com/ping?sitemap=",
}

# Archive Services
ARCHIVES = [
    "https://web.archive.org/save/",
    "https://archive.is/",
    "https://ghostarchive.org/",
]

# Distribution Platforms (for backlinks)
PLATFORMS = [
    {
        "name": "github_gist",
        "url": "https://gist.github.com/",
        "type": "code_sharing"
    },
    {
        "name": "pastebin",
        "url": "https://pastebin.com/",
        "type": "text_sharing"
    },
    {
        "name": "medium",
        "url": "https://medium.com/",
        "type": "article"
    },
    {
        "name": "substack",
        "url": "https://substack.com/",
        "type": "newsletter"
    },
]

# OODA Loop Timing
OBSERVE_INTERVAL = 3600  # 1 hour
ORIENT_INTERVAL = 7200  # 2 hours
DECIDE_INTERVAL = 1800  # 30 minutes
ACT_INTERVAL = 5400  # 1.5 hours

# Content Generation
VARIATIONS_PER_CYCLE = 3
BACKLINKS_PER_CYCLE = 5

# Metrics to Track
METRICS = [
    "google_position",
    "search_volume",
    "backlink_count",
    "content_variations",
    "archive_count",
    "engagement_rate",
]

# Logging
LOG_LEVEL = "INFO"
LOG_FILE = "ooda_loop.log"
