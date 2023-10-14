# Scrapy settings for spider_studos project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "spider_studos"

SPIDER_MODULES = ["spider_studos.spiders"]
NEWSPIDER_MODULE = "spider_studos.spiders"


#ADDONS, Valor: <scrapy.settings.BaseSettings object at 0x0000027407760690>
AJAXCRAWL_ENABLED, Valor: False
ASYNCIO_EVENT_LOOP, Valor: None
AUTOTHROTTLE_DEBUG, Valor: False
AUTOTHROTTLE_ENABLED, Valor: False
AUTOTHROTTLE_MAX_DELAY, Valor: 60.0
AUTOTHROTTLE_START_DELAY, Valor: 5.0
AUTOTHROTTLE_TARGET_CONCURRENCY, Valor: 1.0
CLOSESPIDER_ERRORCOUNT, Valor: 0
CLOSESPIDER_ITEMCOUNT, Valor: 0
CLOSESPIDER_PAGECOUNT, Valor: 0
CLOSESPIDER_TIMEOUT, Valor: 0
#COMMANDS_MODULE, Valor: 
COMPRESSION_ENABLED, Valor: True
CONCURRENT_ITEMS, Valor: 100
CONCURRENT_REQUESTS, Valor: 16
CONCURRENT_REQUESTS_PER_DOMAIN, Valor: 8
CONCURRENT_REQUESTS_PER_IP, Valor: 0
COOKIES_DEBUG, Valor: False
COOKIES_ENABLED, Valor: True
#DEFAULT_ITEM_CLASS, Valor: scrapy.item.Item
#DEFAULT_REQUEST_HEADERS, Valor: <scrapy.settings.BaseSettings object at 0x0000027407760410>
DEPTH_LIMIT, Valor: 0
DEPTH_PRIORITY, Valor: 0
DEPTH_STATS_VERBOSE, Valor: False
DNSCACHE_ENABLED, Valor: True
DNSCACHE_SIZE, Valor: 10000
#DNS_RESOLVER, Valor: scrapy.resolver.CachingThreadedResolver
DNS_TIMEOUT, Valor: 60
#DOWNLOADER, Valor: scrapy.core.downloader.Downloader
#DOWNLOADER_CLIENTCONTEXTFACTORY, Valor: scrapy.core.downloader.contextfactory.ScrapyClientContextFactory
#DOWNLOADER_CLIENT_TLS_CIPHERS, Valor: DEFAULT
#DOWNLOADER_CLIENT_TLS_METHOD, Valor: TLS
DOWNLOADER_CLIENT_TLS_VERBOSE_LOGGING, Valor: False
#DOWNLOADER_HTTPCLIENTFACTORY, Valor: scrapy.core.downloader.webclient.ScrapyHTTPClientFactory
#DOWNLOADER_MIDDLEWARES, Valor: <scrapy.settings.BaseSettings object at 0x0000027407760790>
#DOWNLOADER_MIDDLEWARES_BASE, Valor: <scrapy.settings.BaseSettings object at 0x0000027407760A90>
DOWNLOADER_STATS, Valor: True
DOWNLOAD_DELAY, Valor: 0
DOWNLOAD_FAIL_ON_DATALOSS, Valor: True
#DOWNLOAD_HANDLERS, Valor: <scrapy.settings.BaseSettings object at 0x0000027407761210>
#DOWNLOAD_HANDLERS_BASE, Valor: <scrapy.settings.BaseSettings object at 0x0000027407761290>
DOWNLOAD_MAXSIZE, Valor: 1073741824
DOWNLOAD_TIMEOUT, Valor: 180
DOWNLOAD_WARNSIZE, Valor: 33554432
#DUPEFILTER_CLASS, Valor: scrapy.dupefilters.RFPDupeFilter
#EDITOR, Valor: %s -m idlelib.idle
#EXTENSIONS, Valor: <scrapy.settings.BaseSettings object at 0x0000027407761690>
#EXTENSIONS_BASE, Valor: <scrapy.settings.BaseSettings object at 0x00000274077617D0>
#FEEDS, Valor: <scrapy.settings.BaseSettings object at 0x0000027407762010>
#FEED_EXPORTERS, Valor: <scrapy.settings.BaseSettings object at 0x0000027407762150>
#FEED_EXPORTERS_BASE, Valor: <scrapy.settings.BaseSettings object at 0x0000027407761CD0>
FEED_EXPORT_BATCH_ITEM_COUNT, Valor: 0
FEED_EXPORT_ENCODING, Valor: None
FEED_EXPORT_FIELDS, Valor: None
FEED_EXPORT_INDENT, Valor: 0
#FEED_STORAGES, Valor: <scrapy.settings.BaseSettings object at 0x00000274077616D0>
#FEED_STORAGES_BASE, Valor: <scrapy.settings.BaseSettings object at 0x0000027407762750>
FEED_STORAGE_FTP_ACTIVE, Valor: False
#FEED_STORAGE_GCS_ACL, Valor: 
#FEED_STORAGE_S3_ACL, Valor: 
FEED_STORE_EMPTY, Valor: True
FEED_TEMPDIR, Valor: None
FEED_URI_PARAMS, Valor: None
#FILES_STORE_GCS_ACL, Valor: 
#FILES_STORE_S3_ACL, Valor: private
FTP_PASSIVE_MODE, Valor: True
#FTP_PASSWORD, Valor: guest
#FTP_USER, Valor: anonymous
GCS_PROJECT_ID, Valor: None
HTTPCACHE_ALWAYS_STORE, Valor: False
#HTTPCACHE_DBM_MODULE, Valor: dbm
#HTTPCACHE_DIR, Valor: httpcache
HTTPCACHE_ENABLED, Valor: False
HTTPCACHE_EXPIRATION_SECS, Valor: 0
HTTPCACHE_GZIP, Valor: False
HTTPCACHE_IGNORE_HTTP_CODES, Valor: []
HTTPCACHE_IGNORE_MISSING, Valor: False
HTTPCACHE_IGNORE_RESPONSE_CACHE_CONTROLS, Valor: []
HTTPCACHE_IGNORE_SCHEMES, Valor: ['file']
#HTTPCACHE_POLICY, Valor: scrapy.extensions.httpcache.DummyPolicy
#HTTPCACHE_STORAGE, Valor: scrapy.extensions.httpcache.FilesystemCacheStorage
#HTTPPROXY_AUTH_ENCODING, Valor: latin-1
HTTPPROXY_ENABLED, Valor: True
#IMAGES_STORE_GCS_ACL, Valor: 
#IMAGES_STORE_S3_ACL, Valor: private
#ITEM_PIPELINES, Valor: <scrapy.settings.BaseSettings object at 0x0000027407763950>
#ITEM_PIPELINES_BASE, Valor: <scrapy.settings.BaseSettings object at 0x0000027407763690>
#ITEM_PROCESSOR, Valor: scrapy.pipelines.ItemPipelineManager
LOGSTATS_INTERVAL, Valor: 60.0
#LOG_DATEFORMAT, Valor: %Y-%m-%d %H:%M:%S
LOG_ENABLED, Valor: True
#LOG_ENCODING, Valor: utf-8
LOG_FILE, Valor: None
LOG_FILE_APPEND, Valor: True
#LOG_FORMAT, Valor: %(asctime)s [%(name)s] %(levelname)s: %(message)s
#LOG_FORMATTER, Valor: scrapy.logformatter.LogFormatter
#LOG_LEVEL, Valor: DEBUG
LOG_SHORT_NAMES, Valor: False
LOG_STDOUT, Valor: False
#MAIL_FROM, Valor: scrapy@localhost
#MAIL_HOST, Valor: localhost
MAIL_PASS, Valor: None
MAIL_PORT, Valor: 25
MAIL_USER, Valor: None
MEMDEBUG_ENABLED, Valor: False
MEMDEBUG_NOTIFY, Valor: []
MEMUSAGE_CHECK_INTERVAL_SECONDS, Valor: 60.0
MEMUSAGE_ENABLED, Valor: True
MEMUSAGE_LIMIT_MB, Valor: 0
MEMUSAGE_NOTIFY_MAIL, Valor: []
MEMUSAGE_WARNING_MB, Valor: 0
METAREFRESH_ENABLED, Valor: True
METAREFRESH_IGNORE_TAGS, Valor: []
METAREFRESH_MAXDELAY, Valor: 100
RANDOMIZE_DOWNLOAD_DELAY, Valor: True
REACTOR_THREADPOOL_MAXSIZE, Valor: 10
REDIRECT_ENABLED, Valor: True
REDIRECT_MAX_TIMES, Valor: 20
REDIRECT_PRIORITY_ADJUST, Valor: 2
REFERER_ENABLED, Valor: True
#REFERRER_POLICY, Valor: scrapy.spidermiddlewares.referer.DefaultReferrerPolicy
#REQUEST_FINGERPRINTER_CLASS, Valor: scrapy.utils.request.RequestFingerprinter
REQUEST_FINGERPRINTER_IMPLEMENTATION, Valor: 2.6
RETRY_ENABLED, Valor: True
#RETRY_EXCEPTIONS, Valor: ['twisted.internet.defer.TimeoutError', 'twisted.internet.error.TimeoutError', 'twisted.internet.error.DNSLookupError', 'twisted.internet.error.ConnectionRefusedError', 'twisted.internet.error.ConnectionDone', 'twisted.internet.error.ConnectError', 'twisted.internet.error.ConnectionLost', 'twisted.internet.error.TCPTimedOutError', 'twisted.web.client.ResponseFailed', <class 'OSError'>, 'scrapy.core.downloader.handlers.http11.TunnelError']
RETRY_HTTP_CODES, Valor: [500, 502, 503, 504, 522, 524, 408, 429]
RETRY_PRIORITY_ADJUST, Valor: -1
RETRY_TIMES, Valor: 2
ROBOTSTXT_OBEY, Valor: False
#ROBOTSTXT_PARSER, Valor: scrapy.robotstxt.ProtegoRobotParser
ROBOTSTXT_USER_AGENT, Valor: None
#SCHEDULER, Valor: scrapy.core.scheduler.Scheduler
SCHEDULER_DEBUG, Valor: False
#SCHEDULER_DISK_QUEUE, Valor: scrapy.squeues.PickleLifoDiskQueue
#SCHEDULER_MEMORY_QUEUE, Valor: scrapy.squeues.LifoMemoryQueue
#SCHEDULER_PRIORITY_QUEUE, Valor: scrapy.pqueues.ScrapyPriorityQueue
SCRAPER_SLOT_MAX_ACTIVE_SIZE, Valor: 5000000
#SPIDER_CONTRACTS, Valor: <scrapy.settings.BaseSettings object at 0x0000027407763450>
#SPIDER_CONTRACTS_BASE, Valor: <scrapy.settings.BaseSettings object at 0x0000027407761710>
#SPIDER_LOADER_CLASS, Valor: scrapy.spiderloader.SpiderLoader
SPIDER_LOADER_WARN_ONLY, Valor: False
#SPIDER_MIDDLEWARES, Valor: <scrapy.settings.BaseSettings object at 0x000002740775E4D0>
#SPIDER_MIDDLEWARES_BASE, Valor: <scrapy.settings.BaseSettings object at 0x000002740775E510>
STATSMAILER_RCPTS, Valor: []
#STATS_CLASS, Valor: scrapy.statscollectors.MemoryStatsCollector
STATS_DUMP, Valor: True
TELNETCONSOLE_ENABLED, Valor: 1
#TELNETCONSOLE_HOST, Valor: 127.0.0.1
TELNETCONSOLE_PASSWORD, Valor: None
TELNETCONSOLE_PORT, Valor: [6023, 6073]
#ELNETCONSOLE_USERNAME, Valor: scrapy
#TEMPLATES_DIR, Valor: C:\Users\Player\AppData\Local\Programs\Python\Python311\Lib\site-packages\scrapy\templates
TWISTED_REACTOR, Valor: None
URLLENGTH_LIMIT, Valor: 2083
#USER_AGENT, Valor: Scrapy/2.10.0 (+https://scrapy.org)
