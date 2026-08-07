# Dataify SDK — API 参数手册

本手册由 `dataify_sdk._codegen.generate` 从 Go 参考项目自动生成。每个函数**直接调用 Dataify 上游 REST 接口**(不走 MCP),下列参数均为该函数暴露的上游请求参数及其描述。

- 工具模块数: 70
- 生成函数数: 113

## 目录

- [airbnb_product_by_searchurl](#airbnb-product-by-searchurl)
- [amazon_comment_by_url](#amazon-comment-by-url)
- [amazon_global_product_by_url](#amazon-global-product-by-url)
- [amazon_global_product_by_category_url](#amazon-global-product-by-category-url)
- [amazon_global_product_by_keywords](#amazon-global-product-by-keywords)
- [amazon_global_product_by_keywords_brand](#amazon-global-product-by-keywords-brand)
- [amazon_product_by_asin](#amazon-product-by-asin)
- [amazon_product_by_url](#amazon-product-by-url)
- [amazon_product_by_keywords](#amazon-product-by-keywords)
- [amazon_product_by_category_url](#amazon-product-by-category-url)
- [amazon_product_by_best_sellers](#amazon-product-by-best-sellers)
- [amazon_product_list_by_keywords_domain](#amazon-product-list-by-keywords-domain)
- [amazon_seller_by_url](#amazon-seller-by-url)
- [bing_images](#bing-images)
- [bing_maps](#bing-maps)
- [bing_news](#bing-news)
- [bing_search](#bing-search)
- [bing_shopping](#bing-shopping)
- [bing_videos](#bing-videos)
- [booking_hotellist_by_url](#booking-hotellist-by-url)
- [crunchbase_company_by_url](#crunchbase-company-by-url)
- [crunchbase_company_by_keywords](#crunchbase-company-by-keywords)
- [duckduckgo_search](#duckduckgo-search)
- [ebay_ebay_by_url](#ebay-ebay-by-url)
- [ebay_ebay_by_category_url](#ebay-ebay-by-category-url)
- [ebay_ebay_by_keywords](#ebay-ebay-by-keywords)
- [ebay_ebay_by_listurl](#ebay-ebay-by-listurl)
- [facebook_comment_by_comments_url](#facebook-comment-by-comments-url)
- [facebook_event_by_eventlist_url](#facebook-event-by-eventlist-url)
- [facebook_event_by_search_url](#facebook-event-by-search-url)
- [facebook_post_by_posts_url](#facebook-post-by-posts-url)
- [facebook_profile_by_profiles_url](#facebook-profile-by-profiles-url)
- [github_repository_by_repo_url](#github-repository-by-repo-url)
- [github_repository_by_search_url](#github-repository-by-search-url)
- [github_repository_by_url](#github-repository-by-url)
- [glassdoor_company_by_url](#glassdoor-company-by-url)
- [glassdoor_company_by_inputfilter](#glassdoor-company-by-inputfilter)
- [glassdoor_company_by_keywords](#glassdoor-company-by-keywords)
- [glassdoor_company_by_listurl](#glassdoor-company-by-listurl)
- [glassdoor_joblistings_by_url](#glassdoor-joblistings-by-url)
- [glassdoor_joblistings_by_keywords](#glassdoor-joblistings-by-keywords)
- [glassdoor_joblistings_by_listurl](#glassdoor-joblistings-by-listurl)
- [google_ai_mode](#google-ai-mode)
- [google_finance](#google-finance)
- [google_flights](#google-flights)
- [google_hotels](#google-hotels)
- [google_images](#google-images)
- [google_jobs](#google-jobs)
- [google_lens](#google-lens)
- [google_local](#google-local)
- [google_comment_by_url](#google-comment-by-url)
- [google_map_details_by_url](#google-map-details-by-url)
- [google_map_details_by_cid](#google-map-details-by-cid)
- [google_map_details_by_location](#google-map-details-by-location)
- [google_map_details_by_placeid](#google-map-details-by-placeid)
- [google_maps](#google-maps)
- [google_news](#google-news)
- [google_patents](#google-patents)
- [google_play](#google-play)
- [google_play_store_information_by_url](#google-play-store-information-by-url)
- [google_play_store_reviews_by_url](#google-play-store-reviews-by-url)
- [google_scholar](#google-scholar)
- [google_search](#google-search)
- [google_shopping](#google-shopping)
- [google_shopping_by_keywords](#google-shopping-by-keywords)
- [google_trends](#google-trends)
- [google_videos](#google-videos)
- [indeed_companies_info_by_company_list_url](#indeed-companies-info-by-company-list-url)
- [indeed_companies_info_by_keyword](#indeed-companies-info-by-keyword)
- [indeed_companies_info_by_industry_and_state](#indeed-companies-info-by-industry-and-state)
- [indeed_companies_info_by_company_url](#indeed-companies-info-by-company-url)
- [indeed_job_listings_by_job_url](#indeed-job-listings-by-job-url)
- [ins_comment_by_posturl](#ins-comment-by-posturl)
- [ins_profiles_by_username](#ins-profiles-by-username)
- [ins_profiles_by_profileurl](#ins-profiles-by-profileurl)
- [ins_reel_by_url](#ins-reel-by-url)
- [ins_allreel_by_url](#ins-allreel-by-url)
- [ins_reel_by_listurl](#ins-reel-by-listurl)
- [linkedin_company_information_by_url](#linkedin-company-information-by-url)
- [linkedin_job_listings_information_by_job_listing_url](#linkedin-job-listings-information-by-job-listing-url)
- [linkedin_job_listings_information_by_job_url](#linkedin-job-listings-information-by-job-url)
- [linkedin_job_listings_information_by_keyword](#linkedin-job-listings-information-by-keyword)
- [reddit_comment_by_url](#reddit-comment-by-url)
- [reddit_posts_by_url](#reddit-posts-by-url)
- [reddit_posts_by_keywords](#reddit-posts-by-keywords)
- [reddit_posts_by_subredditurl](#reddit-posts-by-subredditurl)
- [tiktok_comment_by_url](#tiktok-comment-by-url)
- [tiktok_posts_by_listurl](#tiktok-posts-by-listurl)
- [tiktok_profiles_by_url](#tiktok-profiles-by-url)
- [tiktok_profiles_by_listurl](#tiktok-profiles-by-listurl)
- [tiktok_shop_by_url](#tiktok-shop-by-url)
- [twitter_post_by_profileurl](#twitter-post-by-profileurl)
- [twitter_profile_by_profileurl](#twitter-profile-by-profileurl)
- [twitter_profile_by_username](#twitter-profile-by-username)
- [walmart_product_by_url](#walmart-product-by-url)
- [walmart_product_by_category_url](#walmart-product-by-category-url)
- [walmart_product_by_sku](#walmart-product-by-sku)
- [walmart_product_by_keywords](#walmart-product-by-keywords)
- [yandex_search](#yandex-search)
- [youtube_audio_by_url](#youtube-audio-by-url)
- [youtube_comment_by_id](#youtube-comment-by-id)
- [youtube_product_by_id](#youtube-product-by-id)
- [youtube_profiles_by_keyword](#youtube-profiles-by-keyword)
- [youtube_profiles_by_url](#youtube-profiles-by-url)
- [youtube_transcript_by_id](#youtube-transcript-by-id)
- [youtube_video_by_url](#youtube-video-by-url)
- [youtube_video_post_by_url](#youtube-video-post-by-url)
- [youtube_video_post_by_search_filters](#youtube-video-post-by-search-filters)
- [youtube_video_post_by_hashtag](#youtube-video-post-by-hashtag)
- [youtube_video_post_by_podcast_url](#youtube-video-post-by-podcast-url)
- [youtube_video_post_by_keyword](#youtube-video-post-by-keyword)
- [youtube_video_post_by_explore](#youtube-video-post-by-explore)
- [zillow_product_by_filter](#zillow-product-by-filter)

## airbnb_product_by_searchurl

当用户需要 Airbnb房产信息、Airbnb房源信息、Airbnb房源搜索、Airbnb product、Airbnb homes，与采集、抓取、爬取、获取、提取等动词组合时触发。提交 Airbnb房产信息采集 Builder 任务，采集器标识固定为 airbnb_product_by-searchurl。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `airbnb.com`
- spider_id: `airbnb_product_by-searchurl`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `searchurl` | `searchurl` | 否 | —(空) | 网址，该参数用于指定采集 Airbnb 中的房源搜索网址。用于 airbnb_product_by-searchurl，默认值为 https://www.airbnb.com/s/Greece/homes?query=Greece&refinement_paths%5B%5D=%2Fhomes&place_id=ChIJY2xxEcdKWxMRHS2a3HUXOjY&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2025-03-01&monthly_length=3&monthly_end_date=2025-06-01&search_mode=regular_search&price_filter_input_type=0&channel=EXPLORE&date_picker_type=calendar&source=structured_search_input_header&search_type=filter_change&price_filter_num_nights=5&flexible_date_search_filter_type=1。 |
| `country` | `country` | 否 | —(空) | 国家，该参数用于指定采集 Airbnb 中的房源所属国家。非必填，默认值为 HK，参数值取国家列表中的 typeValue 列。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## amazon_comment_by_url

当用户需要 Amazon 产品评论、Amazon 商品评论、Amazon 评论信息、Amazon review、产品评价信息，与采集、抓取、爬取、获取、提取等动词组合时触发。提交 Amazon 产品评论采集 Builder 任务，采集器标识固定为 amazon_comment_by-url。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `amazon.com`
- spider_id: `amazon_comment_by-url`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `url` | `url` | 否 | —(空) | URLs，该参数用于指定待采集的访问 URL 地址。用于 amazon_comment_by-url。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## amazon_global_product_by_url

当用户需要 Amazon 全球产品详情、Amazon 全球商品详情、Amazon 全球产品信息、全球商品信息、Amazon 全球产品 URL、类别 URL、关键词搜索、关键词品牌搜索，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Amazon 全球产品详情采集 Builder 任务，支持 amazon_global-product_by-url、amazon_global-product_by-category-url、amazon_global-product_by-keywords、amazon_global-product_by-keywords-brand。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `amazon.com`
- spider_id: `amazon_global-product_by-url`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `url` | `url` | 否 | —(空) | URLs，该参数用于指定待采集的访问 URL 地址。用于 amazon_global-product_by-url、amazon_global-product_by-category-url；未传时按采集器使用文档默认 URL。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## amazon_global_product_by_category_url

当用户需要 Amazon 全球产品详情、Amazon 全球商品详情、Amazon 全球产品信息、全球商品信息、Amazon 全球产品 URL、类别 URL、关键词搜索、关键词品牌搜索，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Amazon 全球产品详情采集 Builder 任务，支持 amazon_global-product_by-url、amazon_global-product_by-category-url、amazon_global-product_by-keywords、amazon_global-product_by-keywords-brand。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `amazon.com`
- spider_id: `amazon_global-product_by-category-url`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `url` | `url` | 否 | —(空) | URLs，该参数用于指定待采集的访问 URL 地址。用于 amazon_global-product_by-url、amazon_global-product_by-category-url；未传时按采集器使用文档默认 URL。 |
| `maximum` | `maximum` | 否 | `5` | 最大数量，该参数用于指定采集的最大数量。用于 amazon_global-product_by-category-url，默认值为 5。 |
| `sort_by` | `sort_by` | 否 | `畅销排行` | 排序方式。用于 amazon_global-product_by-category-url，仅传 cn 列：畅销排行、最新上架、平均评价、价格：从高到低、价格：从低到高、精选推荐。默认畅销排行。 |
| `get_sponsored` | `get_sponsored` | 否 | —(空) | 获取赞助商品。用于 amazon_global-product_by-category-url，参数值为 true 或 false，默认值为 true。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## amazon_global_product_by_keywords

当用户需要 Amazon 全球产品详情、Amazon 全球商品详情、Amazon 全球产品信息、全球商品信息、Amazon 全球产品 URL、类别 URL、关键词搜索、关键词品牌搜索，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Amazon 全球产品详情采集 Builder 任务，支持 amazon_global-product_by-url、amazon_global-product_by-category-url、amazon_global-product_by-keywords、amazon_global-product_by-keywords-brand。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `amazon.com`
- spider_id: `amazon_global-product_by-keywords`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `keyword` | `keyword` | 否 | —(空) | 关键词，搜索产品的关键词。amazon_global-product_by-keywords 默认 coffee；amazon_global-product_by-keywords-brand 默认 shirts。 |
| `domain` | `domain` | 否 | `https://www.amazon.com` | 域名，请输入需要搜索关键词的主域名，例如：https://www.amazon.com。用于 amazon_global-product_by-keywords，默认值为 https://www.amazon.com。 |
| `lowest_price` | `lowest_price` | 否 | `20` | 最低价格，该参数用于指定要筛选的最低商品价格。用于 amazon_global-product_by-keywords，默认值为 20。 |
| `highest_price` | `highest_price` | 否 | `50` | 最高价格，该参数用于指定要筛选的最高商品价格。用于 amazon_global-product_by-keywords，默认值为 50。 |
| `page_turning` | `page_turning` | 否 | `2` | 采集页数，请输入要采集多少页的产品。用于 amazon_global-product_by-keywords、amazon_global-product_by-keywords-brand，默认值为 2。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## amazon_global_product_by_keywords_brand

当用户需要 Amazon 全球产品详情、Amazon 全球商品详情、Amazon 全球产品信息、全球商品信息、Amazon 全球产品 URL、类别 URL、关键词搜索、关键词品牌搜索，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Amazon 全球产品详情采集 Builder 任务，支持 amazon_global-product_by-url、amazon_global-product_by-category-url、amazon_global-product_by-keywords、amazon_global-product_by-keywords-brand。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `amazon.com`
- spider_id: `amazon_global-product_by-keywords-brand`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `keyword` | `keyword` | 否 | —(空) | 关键词，搜索产品的关键词。amazon_global-product_by-keywords 默认 coffee；amazon_global-product_by-keywords-brand 默认 shirts。 |
| `brands` | `brands` | 否 | `Adidas` | 品牌，该参数用于指定采集的品牌信息，请输入 Amazon 平台有的品牌名称，如果找不到该品牌选项，则采集字段将为空。用于 amazon_global-product_by-keywords-brand，默认值为 Adidas。 |
| `page_turning` | `page_turning` | 否 | `2` | 采集页数，请输入要采集多少页的产品。用于 amazon_global-product_by-keywords、amazon_global-product_by-keywords-brand，默认值为 2。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## amazon_product_by_asin

当用户需要 Amazon 产品详情、商品详情、商品信息、产品信息、ASIN、产品 URL、关键词搜索、类别 URL 或畅销商品 URL 加采集、抓取、爬取、获取、提取时触发。复用一个工具提交 Amazon 产品详情采集 Builder 任务，支持 amazon_product_by-asin、amazon_product_by-url、amazon_product_by-keywords、amazon_product_by-category-url、amazon_product_by-best-sellers。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `amazon.com`
- spider_id: `amazon_product_by-asin`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `asin` | `asin` | 否 | `B0BZYCJK89` | ASIN，该参数用于指定采集 Amazon 产品的唯一标识符。ASIN 通常是一个 10 位字母和数字的组合，比如 B0BZYCJK89。用于 amazon_product_by-asin。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## amazon_product_by_url

当用户需要 Amazon 产品详情、商品详情、商品信息、产品信息、ASIN、产品 URL、关键词搜索、类别 URL 或畅销商品 URL 加采集、抓取、爬取、获取、提取时触发。复用一个工具提交 Amazon 产品详情采集 Builder 任务，支持 amazon_product_by-asin、amazon_product_by-url、amazon_product_by-keywords、amazon_product_by-category-url、amazon_product_by-best-sellers。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `amazon.com`
- spider_id: `amazon_product_by-url`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `url` | `url` | 否 | —(空) | URLs，该参数用于指定待采集的访问 URL 地址。用于 amazon_product_by-url、amazon_product_by-category-url；也可用于 amazon_product_by-best-sellers。 |
| `zip_code` | `zip_code` | 否 | `94107` | 邮政编码，该参数用于指定采集页面中配送区域的邮政编码。用于 amazon_product_by-url，默认 94107。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## amazon_product_by_keywords

当用户需要 Amazon 产品详情、商品详情、商品信息、产品信息、ASIN、产品 URL、关键词搜索、类别 URL 或畅销商品 URL 加采集、抓取、爬取、获取、提取时触发。复用一个工具提交 Amazon 产品详情采集 Builder 任务，支持 amazon_product_by-asin、amazon_product_by-url、amazon_product_by-keywords、amazon_product_by-category-url、amazon_product_by-best-sellers。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `amazon.com`
- spider_id: `amazon_product_by-keywords`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `keyword` | `keyword` | 否 | `coffee` | 关键词，搜索产品的关键词。用于 amazon_product_by-keywords。 |
| `page_turning` | `page_turning` | 否 | —(空) | 采集页数，请输入要采集多少页的产品。用于 amazon_product_by-keywords、amazon_product_by-category-url、amazon_product_by-best-sellers。关键词采集默认 2，其它列表采集默认 1。 |
| `lowest_price` | `lowest_price` | 否 | `20` | 最低价格，该参数用于指定要筛选的最低商品价格。用于 amazon_product_by-keywords。 |
| `highest_price` | `highest_price` | 否 | `50` | 最高价格，该参数用于指定要筛选的最高商品价格。用于 amazon_product_by-keywords。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## amazon_product_by_category_url

当用户需要 Amazon 产品详情、商品详情、商品信息、产品信息、ASIN、产品 URL、关键词搜索、类别 URL 或畅销商品 URL 加采集、抓取、爬取、获取、提取时触发。复用一个工具提交 Amazon 产品详情采集 Builder 任务，支持 amazon_product_by-asin、amazon_product_by-url、amazon_product_by-keywords、amazon_product_by-category-url、amazon_product_by-best-sellers。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `amazon.com`
- spider_id: `amazon_product_by-category-url`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `url` | `url` | 否 | —(空) | URLs，该参数用于指定待采集的访问 URL 地址。用于 amazon_product_by-url、amazon_product_by-category-url；也可用于 amazon_product_by-best-sellers。 |
| `page_turning` | `page_turning` | 否 | —(空) | 采集页数，请输入要采集多少页的产品。用于 amazon_product_by-keywords、amazon_product_by-category-url、amazon_product_by-best-sellers。关键词采集默认 2，其它列表采集默认 1。 |
| `sort_by` | `sort_by` | 否 | `畅销排行` | 排序方式。用于 amazon_product_by-category-url，仅传 cn 列：畅销排行、最新上架、平均评价、价格：从高到低、价格：从低到高、精选推荐。默认畅销排行。 |
| `collect_subcategories` | `collect_subcategories` | 否 | —(空) | 收集子类别，该参数用于指定在主类别下要采集的子类别商品范围。仅在传入非空值时提交。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## amazon_product_by_best_sellers

当用户需要 Amazon 产品详情、商品详情、商品信息、产品信息、ASIN、产品 URL、关键词搜索、类别 URL 或畅销商品 URL 加采集、抓取、爬取、获取、提取时触发。复用一个工具提交 Amazon 产品详情采集 Builder 任务，支持 amazon_product_by-asin、amazon_product_by-url、amazon_product_by-keywords、amazon_product_by-category-url、amazon_product_by-best-sellers。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `amazon.com`
- spider_id: `amazon_product_by-best-sellers`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `url` | `url` | 否 | —(空) | URLs，该参数用于指定待采集的访问 URL 地址。用于 amazon_product_by-url、amazon_product_by-category-url；也可用于 amazon_product_by-best-sellers。 |
| `page_turning` | `page_turning` | 否 | —(空) | 采集页数，请输入要采集多少页的产品。用于 amazon_product_by-keywords、amazon_product_by-category-url、amazon_product_by-best-sellers。关键词采集默认 2，其它列表采集默认 1。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## amazon_product_list_by_keywords_domain

当用户需要 Amazon 产品列表、Amazon 商品列表、Amazon 搜索结果列表、Amazon 关键词商品列表，与采集、抓取、爬取、获取、提取等动词组合时触发。提交 Amazon 产品列表采集 Builder 任务，采集器标识固定为 amazon_product-list_by-keywords-domain。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `amazon.com`
- spider_id: `amazon_product-list_by-keywords-domain`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `keyword` | `keyword` | 否 | `X-box` | 关键词，搜索产品的关键词。用于 amazon_product-list_by-keywords-domain，默认值为 X-box。 |
| `domain` | `domain` | 否 | `https://www.amazon.com/` | 域名，请输入需要搜索关键词的主域名，例如：https://www.amazon.com。用于 amazon_product-list_by-keywords-domain，默认值为 https://www.amazon.com/。 |
| `page_turning` | `page_turning` | 否 | `1` | 采集页数，请输入要采集多少页的产品。即如果输入 2，就是需要把搜索结果页的第一页、第二页的所有产品都采集过来。默认值为 1。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## amazon_seller_by_url

当用户需要 Amazon 卖家信息、Amazon 店铺信息、Amazon 商家信息、卖家资料、seller 信息，与采集、抓取、爬取、获取、提取等动词组合时触发。提交 Amazon 卖家信息采集 Builder 任务，采集器标识固定为 amazon_seller_by-url。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `amazon.com`
- spider_id: `amazon_seller_by-url`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `url` | `url` | 否 | —(空) | URLs，该参数用于指定待采集的访问 URL 地址。用于 amazon_seller_by-url。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## bing_images

当用户需要通过 Bing Images 搜索图片结果，或按图片尺寸、颜色、类型、比例、人脸、年龄、版权等条件筛选图片时触发。

- 上游接口: Search Engine (`POST /request`)
- engine: `bing_images`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `q` | Query | 否 | `Pizza` | 该参数定义爬取时的搜索结果，默认值为 Pizza。您可以输入任意想要查询的关键词，也可以是任意语言。 |
| `json_` | JSON | 否 | `1` | 该参数定义采集结果的输出格式；可选择 JSON、HTML（支持下载）格式，默认为 JSON；1 返回 JSON，2 返回 JSON+HTML，3 返回 HTML，4 返回 Light JSON。 |
| `mkt` | MKT | 否 | —(空) | 参数定义了爬取时搜索结果的界面显示语言。该参数采用 <语言代码>-<国家/地区代码> 的形式。例如：en-US。 |
| `cc` | CC | 否 | —(空) | 该参数定义了爬取时可以指定搜索结果按照国家/地区用户的习惯展示。它是一个由两个字母组成的国家/地区代码，例如：us、ru、uk。 |
| `first` | First | 否 | `0` | 该参数控制自然结果的偏移量。此参数默认为 0。例如 first=10 会将第 10 个自然结果移动到第一个位置。 |
| `count` | Count | 否 | —(空) | 该参数控制每页的结果数量。此参数仅为建议值，可能无法反映返回的结果数。 |
| `imagesize` | ImageSize | 否 | —(空) | 该参数用于按尺寸过滤图片。可用值：small - 小，medium - 中，large - 大，wallpaper - 超大。 |
| `color2` | Color2 | 否 | —(空) | 该参数用于按颜色过滤图片。可用值：color - 仅彩色，bw - 黑白，FGcls_RED - 红色，FGcls_ORGANGE - 橙色，FGcls_YELLOW - 黄色，FGcls_GREEN - 绿色，FGcls_TEAL - 青色，FGcls_BLUE - 蓝色，FGcls_PURPLE - 紫色，FGcls_PINK - 粉色，FGcls_BROWN - 棕色，FGcls_BLACK - 黑色，FGcls_GRAY - 灰色，FGcls_WHITE - 白色。 |
| `photo` | Photo | 否 | —(空) | 该参数用于按图片类型过滤图片。可用值：photo - 照片，clipart - 剪贴画，linedrawing - 线条画，animatedgif - 动图，animatedgifhttps - HTTPS 动图，transparent - 透明，shopping - 购物。 |
| `aspect` | Aspect | 否 | —(空) | 该参数用于按布局过滤图片。可用值：square - 方形，wide - 宽，tall - 高。 |
| `face` | Face | 否 | —(空) | 该参数用于按人物类型过滤图片。可用值：face - 仅限面部，portrait - 头肩。 |
| `age` | Age | 否 | —(空) | 该参数用于按日期过滤图片。可用值：lt1440 - 过去 24 小时，lt10080 - 过去一周，lt43200 - 过去一个月，lt525600 - 过去一年。 |
| `license` | License | 否 | —(空) | 该参数用于按使用许可过滤图片。可用值：Type-Any - 所有 Creative Commons，L1 - Public Domain，L2_L3_L4_L5_L6_L7 - 免费共享和使用，L2_L3_L4 - 免费共享和商业使用，L2_L3_L5_L6 - 免费修改、共享和使用，L2_L3 - 免费修改、共享和商业使用。 |
| `no_cache` | NoCache | 否 | `false` | 默认情况下，5 分钟内缓存相同参数的搜索结果；将 no_cache 设为 true 可跳过缓存，设为 false（默认）则使用缓存结果；缓存搜索免费，且不计入搜索统计。 |

## bing_maps

当用户需要查询 Bing Maps 地图结果、地点搜索、地图位置、place_id 或分页地图数据时触发。

- 上游接口: Search Engine (`POST /request`)
- engine: `bing_maps`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `q` | Query | 否 | —(空) | 该参数定义搜索查询。您可以使用常规必应地图搜索中使用的任何内容。 |
| `json_` | JSON | 否 | `1` | 该参数定义采集结果的输出格式；可选择 JSON、HTML（支持下载）格式，默认为 JSON；1 返回 JSON，2 返回 JSON+HTML，3 返回 HTML，4 返回 Light JSON。 |
| `cp` | CP | 否 | —(空) | 该参数定义您希望 q（查询）应用到的位置的 GPS 坐标。它必须按纬度 + ~ + 经度的顺序构建。例如：40.7455096~-74.0083012。 |
| `setlang` | SetLang | 否 | —(空) | 该参数定义搜索使用的语言。它遵循 ISO_3166-1 格式，例如 us 代表美国，de 代表德国，gb 代表英国等。 |
| `place_id` | PlaceID | 否 | —(空) | 该参数定义必应地图上地点的唯一引用。 |
| `first` | First | 否 | `0` | 该参数控制本地结果的偏移量。此参数默认为 0。例如，当 count=10 时，第二页结果从 first=10 开始。 |
| `count` | Count | 否 | —(空) | 该参数控制每页的结果数量。此参数仅为建议值，可能无法反映返回的结果数。每页最大结果为 10。 |
| `no_cache` | NoCache | 否 | `false` | 默认情况下，5 分钟内缓存相同参数的搜索结果；将 no_cache 设为 true 可跳过缓存，设为 false（默认）则使用缓存结果；缓存搜索免费，且不计入搜索统计。 |

## bing_news

当用户需要通过 Bing News 查询新闻搜索结果，或按关键词、地区、语言、日期排序、安全过滤等条件获取新闻内容时触发。

- 上游接口: Search Engine (`POST /request`)
- engine: `bing_news`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `q` | Query | 否 | `Pizza` | 该参数定义爬取时的搜索结果，默认值为 Pizza。您可以输入任意想要查询的关键词，也可以是任意语言。 |
| `json_` | JSON | 否 | `1` | 该参数定义采集结果的输出格式；可选择 JSON、HTML（支持下载）格式，默认为 JSON；1 返回 JSON，2 返回 JSON+HTML，3 返回 HTML，4 返回 Light JSON。 |
| `mkt` | MKT | 否 | —(空) | 参数定义了爬取时搜索结果的界面显示语言。该参数采用 <语言代码>-<国家/地区代码> 的形式。例如：en-US。 |
| `cc` | CC | 否 | —(空) | 该参数定义了爬取时可以指定搜索结果按照国家/地区用户的习惯展示。它是一个由两个字母组成的国家/地区代码，例如：us、ru、uk。 |
| `first` | First | 否 | `0` | 该参数控制自然结果的偏移量。此参数默认为 0。例如 first=10 会将第 10 个自然结果移动到第一个位置。 |
| `count` | Count | 否 | —(空) | 该参数控制每页的结果数量。此参数仅为建议值，可能无法反映返回的结果数。 |
| `qft` | QFT | 否 | —(空) | 该参数定义按日期排序的结果。 |
| `safeSearch` | SafeSearch | 否 | —(空) | 该参数定义成人内容的过滤级别。可用值：Off、Moderate、Strict。 |
| `no_cache` | NoCache | 否 | `false` | 默认情况下，5 分钟内缓存相同参数的搜索结果；将 no_cache 设为 true 可跳过缓存，设为 false（默认）则使用缓存结果；缓存搜索免费，且不计入搜索统计。 |

## bing_search

当用户需要通过 Bing 搜索公开网页信息，或按位置、经纬度、国家/地区、语言、安全过滤、分页和高级过滤条件获取网页搜索结果时触发。

- 上游接口: Search Engine (`POST /request`)
- engine: `bing`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `q` | Query | 否 | `pizza` | 该参数定义爬取时的搜索结果，默认值为 pizza。您可以输入任意想要查询的关键词，也可以是任意语言。 |
| `json_` | JSON | 否 | `1` | 该参数定义采集结果的输出格式；可选择 JSON、HTML（支持下载）格式，默认为 JSON；1 返回 JSON，2 返回 JSON+HTML，3 返回 HTML，4 返回 Light JSON。 |
| `location` | Location | 否 | —(空) | 该参数定义搜索发起的地理位置。如果有多个位置与请求的位置匹配，将选择最受欢迎的一个。 |
| `lat` | Lat | 否 | —(空) | 定义搜索起点的 GPS 纬度。 |
| `lon` | Lon | 否 | —(空) | 定义搜索起点的 GPS 经度。 |
| `mkt` | MKT | 否 | —(空) | 该参数定义爬取时搜索结果的界面显示语言。该参数采用 <语言代码>-<国家/地区代码> 的形式。例如：en-US。该字符串不区分大小写。 |
| `cc` | CC | 否 | —(空) | 该参数定义爬取时可以指定搜索结果按照国家/地区用户的习惯展示。它是一个由两个字母组成的国家/地区代码，例如：us、ru、uk。 |
| `first` | First | 否 | `0` | 该参数控制自然结果的偏移量。此参数默认为 0。例如 first=10 会将第 10 个自然结果移动到第一个位置。 |
| `safeSearch` | SafeSearch | 否 | —(空) | 该参数定义成人内容的过滤级别。可设置为：Off - 返回包含成人文本、图片或视频的网页；Moderate - 返回包含成人文本但不包含成人图片或视频的网页；Strict - 不返回包含成人文本、图片或视频的网页。 |
| `filters` | Filters | 否 | —(空) | 该参数允许使用更复杂的过滤选项，例如按日期范围过滤（例如：ez5_18169_18230）或使用特定的显示过滤器（例如：ufn:\"Wunderman+Thompson\"+sid:\"5bede9a2-1bda-9887-e6eb-30b1b8b6b513\"+catguid:\"5bede9a2-1bda-9887-e6eb-30b1b8b6b513_cfb02057\"+segment:\"generic.carousel\"+entitysegment:\"Organization\"）。 |
| `no_cache` | NoCache | 否 | `false` | 默认情况下，5 分钟内缓存相同参数的搜索结果；将 no_cache 设为 true 可跳过缓存，设为 false（默认）则使用缓存结果；缓存搜索免费，且不计入搜索统计。 |

## bing_shopping

当用户需要通过 Bing Shopping 查询商品、购物搜索结果、商品列表，或按购物偏移量和过滤条件获取购物数据时触发。

- 上游接口: Search Engine (`POST /request`)
- engine: `bing_shopping`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `q` | Query | 否 | `Pizza` | 该参数定义爬取时的搜索结果，默认值为 Pizza。您可以输入任意想要查询的关键词，也可以是任意语言。 |
| `json_` | JSON | 否 | `1` | 该参数定义采集结果的输出格式；可选择 JSON、HTML（支持下载）格式，默认为 JSON；1 返回 JSON，2 返回 JSON+HTML，3 返回 HTML，4 返回 Light JSON。 |
| `mkt` | MKT | 否 | —(空) | 参数定义了爬取时搜索结果的界面显示语言。该参数采用 <语言代码>-<国家/地区代码> 的形式。例如：en-US。 |
| `cc` | CC | 否 | —(空) | 该参数定义了爬取时可以指定搜索结果按照国家/地区用户的习惯展示。它是一个由两个字母组成的国家/地区代码，例如：us、ru、uk。 |
| `efirst` | EFirst | 否 | —(空) | 该参数控制购物结果的偏移量。例如 efirst=10 会将第 10 个购物结果移动到第一个位置。 |
| `filters` | Filters | 否 | —(空) | 该参数允许使用更复杂的过滤选项，例如按日期范围过滤（例如：ez5_18169_18230）或使用特定的显示过滤器（例如：ufn:\"Wunderman+Thompson\"+sid:\"5bede9a2-1bda-9887-e6eb-30b1b8b6b513\"+catguid:\"5bede9a2-1bda-9887-e6eb-30b1b8b6b513_cfb02057\"+segment:\"generic.carousel\"+entitysegment:\"Organization\"）。可以通过使用必应搜索并复制 filters 查询参数来构造精确的值。 |
| `no_cache` | NoCache | 否 | `false` | 默认情况下，5 分钟内缓存相同参数的搜索结果；将 no_cache 设为 true 可跳过缓存，设为 false（默认）则使用缓存结果；缓存搜索免费，且不计入搜索统计。 |

## bing_videos

当用户需要通过 Bing Videos 搜索视频结果，或按时长、日期、分辨率、来源网站、价格、国家/地区和语言筛选视频时触发。

- 上游接口: Search Engine (`POST /request`)
- engine: `bing_videos`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `q` | Query | 否 | `Pizza` | 该参数定义爬取时的搜索结果，默认值为 Pizza。您可以输入任意想要查询的关键词，也可以是任意语言。 |
| `json_` | JSON | 否 | `1` | 该参数定义采集结果的输出格式；可选择 JSON、HTML（支持下载）格式，默认为 JSON；1 返回 JSON，2 返回 JSON+HTML，3 返回 HTML。 |
| `mkt` | MKT | 否 | —(空) | 参数定义了爬取时搜索结果的界面显示语言。该参数采用 <语言代码>-<国家/地区代码> 的形式。例如：en-US。 |
| `cc` | CC | 否 | —(空) | 该参数定义了爬取时可以指定搜索结果按照国家/地区用户的习惯展示。它是一个由两个字母组成的国家/地区代码，例如：us、ru、uk。 |
| `setlang` | SetLang | 否 | —(空) | 该参数定义搜索使用的语言。它遵循 2 字符的 ISO_3166-1 格式，例如：us 代表美国，de 代表德国，gb 代表英国。 |
| `first` | First | 否 | `0` | 该参数控制自然结果的偏移量。此参数默认 0。例如 first=10 会将第 10 个自然结果移动到第一个位置。 |
| `length` | Length | 否 | —(空) | 该参数用于按时长过滤视频。可用值：short（少于 5 分钟）、medium（5-20 分钟）、long（超过 20 分钟）。 |
| `date` | Date | 否 | —(空) | 该参数用于按日期过滤视频。可用值：lt1440（过去 24 小时）、lt10080（过去一周）、lt43200（过去一个月）、lt525600（过去一年）。 |
| `resolution` | Resolution | 否 | —(空) | 该参数用于按分辨率类型过滤视频。可用值：lowerthan_360p、360p、480p、720p、1080p。 |
| `source_site` | SourceSite | 否 | —(空) | 该参数用于按来源过滤视频。可用值包括：dailymotion.com、vimeo.com、metacafe.com、hulu.com、vevo.com、myspace.com、mtv.com、cbsnews.com、foxnews.com、cnn.com、msn.com。 |
| `price` | Price | 否 | —(空) | 该参数用于按价格过滤视频。可用值：free（免费）、paid（付费）。 |
| `no_cache` | NoCache | 否 | `false` | 默认情况下，5 分钟内缓存相同参数的搜索结果；将 no_cache 设为 true 可跳过缓存，设为 false（默认）则使用缓存结果；缓存搜索免费，且不计入搜索统计。 |

## booking_hotellist_by_url

当用户需要 Booking 酒店信息、Booking 酒店详情、Booking hotel information、Booking hotel list，与采集、抓取、爬取、获取、提取等动词组合时触发。提交 Booking 酒店信息采集 Builder 任务，采集器标识固定为 booking_hotellist_by-url。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `booking.com`
- spider_id: `booking_hotellist_by-url`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `url` | `url` | 否 | —(空) | Booking URL，该参数用于指定采集 Booking 酒店信息链接。用于 booking_hotellist_by-url，默认值为 https://www.booking.com/hotel/gb/westlands-of-pitlochry.en-gb.html#tab-main。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## crunchbase_company_by_url

当用户需要 Crunchbase 信息、Crunchbase 公司信息、Crunchbase 企业信息、Crunchbase company，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Crunchbase 公司信息采集 Builder 任务，支持 crunchbase_company_by-url 和 crunchbase_company_by-keywords。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `crunchbase.com`
- spider_id: `crunchbase_company_by-url`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `url` | `url` | 否 | —(空) | Crunchbase URL，该参数用于指定采集 Crunchbase 中的公司 URL。用于 crunchbase_company_by-url，默认值为 https://www.crunchbase.com/organization/aisci。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## crunchbase_company_by_keywords

当用户需要 Crunchbase 信息、Crunchbase 公司信息、Crunchbase 企业信息、Crunchbase company，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Crunchbase 公司信息采集 Builder 任务，支持 crunchbase_company_by-url 和 crunchbase_company_by-keywords。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `crunchbase.com`
- spider_id: `crunchbase_company_by-keywords`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `keyword` | `keyword` | 否 | —(空) | 关键词，该参数用于指定采集 Crunchbase 中搜索公司的关键词。用于 crunchbase_company_by-keywords，默认值为 NetBooster。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## duckduckgo_search

当用户需要通过 DuckDuckGo 搜索公开网页信息，或希望获取 DuckDuckGo 的隐私搜索结果、网页结果或搜索摘要时触发。

- 上游接口: Search Engine (`POST /request`)
- engine: `duckduckgo`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `q` | Query | 否 | `pizza` | 该参数定义爬取时的搜索结果，默认值为 pizza。您可以输入任意想要查询的关键词，也可以是任意语言。 |
| `json_` | JSON | 否 | `1` | 该参数定义采集结果的输出格式；可选择 JSON、HTML（支持下载）格式，默认为 JSON；1 返回 JSON，2 返回 JSON+HTML，3 返回 HTML，4 返回 Light JSON。 |
| `kl` | KL | 否 | —(空) | 该参数定义 DuckDuckGo 搜索要使用的地区。地区代码示例：us-en 代表美国，uk-en 代表英国，fr-fr 代表法国。请访问 DuckDuckGo 地区页面查看支持的地区完整列表。 |
| `search_assist` | SearchAssist | 否 | `false` | 该参数决定是否在响应中返回 DuckDuckGo 的 AI 搜索辅助。可设置为 true 或 false（默认）。search_assist 和 m 不能一起使用。 |
| `safe` | Safe | 否 | `-1` | 该参数定义成人内容的过滤级别。可设置为：1 - 严格，-1 - 中等（默认），-2 - 关闭。 |
| `df` | DateFilter | 否 | —(空) | 该参数定义按日期过滤的结果。可设置为：d - 过去一天，w - 过去一周，m - 过去一月，y - 过去一年；也可以按 start_date..end_date 格式传递自定义日期，例如：2021-06-15..2024-06-16。 |
| `start` | Start | 否 | `0` | 该参数定义结果偏移量，它跳过指定数量的结果。当 start 设置为 0 或留空时，最多可返回 25 个自然结果；当 start 大于 0 时，最多可返回 10 个自然结果。DuckDuckGo 可能返回重复结果或数量可变的结果，这在使用较大的 start 和 m 参数时更可能发生。 |
| `m` | MaxResults | 否 | `10` | 该参数定义要返回的最大结果数量。默认值：10，最小值：1，最大值：50。当 start 设置为 0 或留空时，最多可返回 25 个自然结果。DuckDuckGo 可能返回重复结果或数量可变的结果，这在使用较大的 start 和 m 参数时更可能发生。m 和 search_assist 不能一起使用。 |
| `no_cache` | NoCache | 否 | `false` | 默认情况下，5 分钟内缓存相同参数的搜索结果；将 no_cache 设为 true 可跳过缓存，设为 false（默认）则使用缓存结果；缓存搜索免费，且不计入搜索统计。 |

## ebay_ebay_by_url

当用户需要 ebay 信息、eBay 商品信息、eBay 产品信息、eBay 类别商品、eBay 店铺商品，与采集、抓取、爬取、获取、提取等动词组合时触发。从 ebay.com 提取商品列表、售价区间、卖家详情、拍卖记录、库存状态、用户评价、物流配送信息等数据。复用一个工具提交 eBay 信息采集 Builder 任务，支持 ebay_ebay_by-url、ebay_ebay_by-category-url、ebay_ebay_by-keywords 和 ebay_ebay_by-listurl。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `ebay.com`
- spider_id: `ebay_ebay_by-url`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `url` | `url` | 否 | —(空) | eBay URL 或 Category URL。用于 ebay_ebay_by-url 时默认值为 https://www.ebay.com/itm/296197468977?itmmeta=01HRWJ04NFHYT9AX0XZB8F18G1&hash=item44f6beb331%3Ag%3ADEQAAOSw3CxlhTJ%7E&_trkparms=%2526rpp_cid%253D6523c97b0b7882040b9472b6；用于 ebay_ebay_by-category-url 时默认值为 https://www.ebay.com/b/Collectible-Japanese-Bells-1900-Now/165467/bn_3104829；用于 ebay_ebay_by-listurl 时默认值为 https://www.ebay.com/str/kptradingdeals?_trksid=p4429486.m145687.l149086。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## ebay_ebay_by_category_url

当用户需要 ebay 信息、eBay 商品信息、eBay 产品信息、eBay 类别商品、eBay 店铺商品，与采集、抓取、爬取、获取、提取等动词组合时触发。从 ebay.com 提取商品列表、售价区间、卖家详情、拍卖记录、库存状态、用户评价、物流配送信息等数据。复用一个工具提交 eBay 信息采集 Builder 任务，支持 ebay_ebay_by-url、ebay_ebay_by-category-url、ebay_ebay_by-keywords 和 ebay_ebay_by-listurl。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `ebay.com`
- spider_id: `ebay_ebay_by-category-url`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `url` | `url` | 否 | —(空) | eBay URL 或 Category URL。用于 ebay_ebay_by-url 时默认值为 https://www.ebay.com/itm/296197468977?itmmeta=01HRWJ04NFHYT9AX0XZB8F18G1&hash=item44f6beb331%3Ag%3ADEQAAOSw3CxlhTJ%7E&_trkparms=%2526rpp_cid%253D6523c97b0b7882040b9472b6；用于 ebay_ebay_by-category-url 时默认值为 https://www.ebay.com/b/Collectible-Japanese-Bells-1900-Now/165467/bn_3104829；用于 ebay_ebay_by-listurl 时默认值为 https://www.ebay.com/str/kptradingdeals?_trksid=p4429486.m145687.l149086。 |
| `count` | `count` | 否 | —(空) | 数量，该参数用于指定采集结果的最大数量。用于 ebay_ebay_by-category-url、ebay_ebay_by-keywords 和 ebay_ebay_by-listurl，默认值为 60。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## ebay_ebay_by_keywords

当用户需要 ebay 信息、eBay 商品信息、eBay 产品信息、eBay 类别商品、eBay 店铺商品，与采集、抓取、爬取、获取、提取等动词组合时触发。从 ebay.com 提取商品列表、售价区间、卖家详情、拍卖记录、库存状态、用户评价、物流配送信息等数据。复用一个工具提交 eBay 信息采集 Builder 任务，支持 ebay_ebay_by-url、ebay_ebay_by-category-url、ebay_ebay_by-keywords 和 ebay_ebay_by-listurl。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `ebay.com`
- spider_id: `ebay_ebay_by-keywords`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `keywords` | `keywords` | 否 | —(空) | 关键词，该参数用于指定采集 eBay 产品的搜索关键词。用于 ebay_ebay_by-keywords，默认值为 baby toys。 |
| `count` | `count` | 否 | —(空) | 数量，该参数用于指定采集结果的最大数量。用于 ebay_ebay_by-category-url、ebay_ebay_by-keywords 和 ebay_ebay_by-listurl，默认值为 60。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## ebay_ebay_by_listurl

当用户需要 ebay 信息、eBay 商品信息、eBay 产品信息、eBay 类别商品、eBay 店铺商品，与采集、抓取、爬取、获取、提取等动词组合时触发。从 ebay.com 提取商品列表、售价区间、卖家详情、拍卖记录、库存状态、用户评价、物流配送信息等数据。复用一个工具提交 eBay 信息采集 Builder 任务，支持 ebay_ebay_by-url、ebay_ebay_by-category-url、ebay_ebay_by-keywords 和 ebay_ebay_by-listurl。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `ebay.com`
- spider_id: `ebay_ebay_by-listurl`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `url` | `url` | 否 | —(空) | eBay URL 或 Category URL。用于 ebay_ebay_by-url 时默认值为 https://www.ebay.com/itm/296197468977?itmmeta=01HRWJ04NFHYT9AX0XZB8F18G1&hash=item44f6beb331%3Ag%3ADEQAAOSw3CxlhTJ%7E&_trkparms=%2526rpp_cid%253D6523c97b0b7882040b9472b6；用于 ebay_ebay_by-category-url 时默认值为 https://www.ebay.com/b/Collectible-Japanese-Bells-1900-Now/165467/bn_3104829；用于 ebay_ebay_by-listurl 时默认值为 https://www.ebay.com/str/kptradingdeals?_trksid=p4429486.m145687.l149086。 |
| `count` | `count` | 否 | —(空) | 数量，该参数用于指定采集结果的最大数量。用于 ebay_ebay_by-category-url、ebay_ebay_by-keywords 和 ebay_ebay_by-listurl，默认值为 60。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## facebook_comment_by_comments_url

当用户需要 Facebook 帖子评论、Facebook 评论、Facebook post comments、帖子回复信息，与采集、抓取、爬取、获取、提取等动词组合时触发。提交 Facebook 帖子评论采集 Builder 任务，采集器标识固定为 facebook_comment_by-comments-url。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `facebook.com`
- spider_id: `facebook_comment_by-comments-url`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `url` | `url` | 否 | —(空) | 帖子 URL，该参数用于指定要采集的 Facebook 帖子 URL。用于 facebook_comment_by-comments-url，默认值为 https://www.facebook.com/share/p/1K6xfHFkrK/。 |
| `get_all_replies` | `get_all_replies` | 否 | —(空) | 全部回复，该参数用于指定是否要采集全部回复。选择 True 则采集全部回复，优先级高于 limit_records。可选值：True、False，默认值为 True。 |
| `limit_records` | `limit_records` | 否 | —(空) | 回复数量上限，该参数用于指定采集的最多回复数量。当值为空时，采集数量默认 1 页（最多 10 条）。默认值为 10。 |
| `comments_sort` | `comments_sort` | 否 | —(空) | 评论排序方式。可选值：All comments、Most Relevent、Newest；默认值为 All comments。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## facebook_event_by_eventlist_url

当用户需要 Facebook 活动、Facebook 活动信息、Facebook event、活动列表、活动搜索结果，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Facebook 活动采集 Builder 任务，支持 facebook_event_by-eventlist-url 和 facebook_event_by-search-url。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `facebook.com`
- spider_id: `facebook_event_by-eventlist-url`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `url` | `url` | 否 | —(空) | 活动列表 URL 或活动搜索 URL。用于 facebook_event_by-eventlist-url 时默认值为 https://www.facebook.com/nohoclub/events；用于 facebook_event_by-search-url 时默认值为 https://www.facebook.com/events/explore/us-atlanta/107991659233606。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## facebook_event_by_search_url

当用户需要 Facebook 活动、Facebook 活动信息、Facebook event、活动列表、活动搜索结果，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Facebook 活动采集 Builder 任务，支持 facebook_event_by-eventlist-url 和 facebook_event_by-search-url。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `facebook.com`
- spider_id: `facebook_event_by-search-url`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `url` | `url` | 否 | —(空) | 活动列表 URL 或活动搜索 URL。用于 facebook_event_by-eventlist-url 时默认值为 https://www.facebook.com/nohoclub/events；用于 facebook_event_by-search-url 时默认值为 https://www.facebook.com/events/explore/us-atlanta/107991659233606。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## facebook_post_by_posts_url

当用户需要 Facebook 帖子、Facebook 帖子信息、Facebook post、帖子内容，与采集、抓取、爬取、获取、提取等动词组合时触发。提交 Facebook 帖子采集 Builder 任务，采集器标识固定为 facebook_post_by-posts-url。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `facebook.com`
- spider_id: `facebook_post_by-posts-url`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `url` | `url` | 否 | —(空) | 帖子 URL，该参数用于指定要采集的 Facebook 帖子 URL。用于 facebook_post_by-posts-url，默认值为 https://www.facebook.com/permalink.php?story_fbid=pfbid0gNjZBhqCxSqj9xJS5aygNwqFqNEM2fYbTFKKbsvvGdEfTgFyAYWSckvkEHPqAE7gl&id=61574926580533&rdid=86oaujwNGCCdPLfj#。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## facebook_profile_by_profiles_url

当用户需要 Facebook 个人主页、Facebook 个人资料、Facebook profile、个人主页信息，与采集、抓取、爬取、获取、提取等动词组合时触发。提交 Facebook 个人主页采集 Builder 任务，采集器标识固定为 facebook_profile_by-profiles-url。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `facebook.com`
- spider_id: `facebook_profile_by-profiles-url`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `url` | `url` | 否 | —(空) | 个人主页 URL，该参数用于指定要采集的个人主页 URL。用于 facebook_profile_by-profiles-url，默认值为 https://www.facebook.com/MayeMusk。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## github_repository_by_repo_url

当用户需要 Github仓库信息、GitHub 仓库信息、Github repository、GitHub 代码 URL、GitHub 搜索仓库，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Github仓库信息采集 Builder 任务，支持 github_repository_by-repo-url、github_repository_by-search-url 和 github_repository_by-url。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `github.com`
- spider_id: `github_repository_by-repo-url`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `repo_url` | `repo_url` | 否 | —(空) | 仓库URL，该参数用于指定要采集的仓库 URL。用于 github_repository_by-repo-url，默认值为 https://github.com/TheAlgorithms/Python。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## github_repository_by_search_url

当用户需要 Github仓库信息、GitHub 仓库信息、Github repository、GitHub 代码 URL、GitHub 搜索仓库，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Github仓库信息采集 Builder 任务，支持 github_repository_by-repo-url、github_repository_by-search-url 和 github_repository_by-url。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `github.com`
- spider_id: `github_repository_by-search-url`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `search_url` | `search_url` | 否 | —(空) | 搜索URL，该参数用于指定要采集的 Search URL。用于 github_repository_by-search-url，默认值为 https://github.com/search?q=ML&type=repositories。 |
| `page_turning` | `page_turning` | 否 | —(空) | 页数限制，该参数用于指定采集结果数量的限制。用于 github_repository_by-search-url，默认值为 1。 |
| `max_num` | `max_num` | 否 | —(空) | 最大仓库数量，该参数用于指定采集的最大仓库数量。用于 github_repository_by-search-url，默认值为 15。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## github_repository_by_url

当用户需要 Github仓库信息、GitHub 仓库信息、Github repository、GitHub 代码 URL、GitHub 搜索仓库，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Github仓库信息采集 Builder 任务，支持 github_repository_by-repo-url、github_repository_by-search-url 和 github_repository_by-url。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `github.com`
- spider_id: `github_repository_by-url`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `url` | `url` | 否 | —(空) | URL，该参数用于指定要采集的代码URL。用于 github_repository_by-url，默认值为 https://github.com/TheAlgorithms/Python/blob/master/divide_and_conquer/power.py。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## glassdoor_company_by_url

当用户需要 Glassdoor 公司概况信息、Glassdoor 公司信息、Glassdoor company overview、Glassdoor 公司 URL、Glassdoor 公司搜索，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Glassdoor 公司概况信息采集 Builder 任务，支持 glassdoor_company_by-url、glassdoor_company_by-inputfilter、glassdoor_company_by-keywords 和 glassdoor_company_by-listurl。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `glassdoor.com`
- spider_id: `glassdoor_company_by-url`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `url` | `url` | 否 | —(空) | Glassdoor URL，该参数用于指定采集 Glassdoor 公司网址。用于 glassdoor_company_by-url 和 glassdoor_company_by-listurl；by-url 默认值为 https://www.glassdoor.co.uk/Overview/Working-at-Apple-EI_IE1138.11,16.htm，by-listurl 默认值为 https://www.glassdoor.com/Explore/browse-companies.htm?filterType=RATING_OVERALL&locId=1347&locType=S&locName=Texas%252C%2520US&occ=Manager&page=1&overall_rating_low=1。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## glassdoor_company_by_inputfilter

当用户需要 Glassdoor 公司概况信息、Glassdoor 公司信息、Glassdoor company overview、Glassdoor 公司 URL、Glassdoor 公司搜索，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Glassdoor 公司概况信息采集 Builder 任务，支持 glassdoor_company_by-url、glassdoor_company_by-inputfilter、glassdoor_company_by-keywords 和 glassdoor_company_by-listurl。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `glassdoor.com`
- spider_id: `glassdoor_company_by-inputfilter`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `location` | `location` | 否 | `United States` | 地点，该参数用于指定采集公司的办公室位置搜索关键词。用于 glassdoor_company_by-inputfilter，默认值为 United States。 |
| `company_name` | `company_name` | 否 | `Tesla` | 公司名称，此参数用于指定要采集的公司名称关键词。用于 glassdoor_company_by-inputfilter，默认值为 Tesla。 |
| `industries` | `industries` | 否 | `Information Technology` | 行业，该参数用于指定采集公司的行业搜索关键词。用于 glassdoor_company_by-inputfilter，默认值为 Information Technology。 |
| `Job_title` | Job title | 否 | —(空) | 职位，该参数用于指定采集公司的含有的职位关键词。用于 glassdoor_company_by-inputfilter，严格按文档字段名 Job title 提交，默认值为 Data。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## glassdoor_company_by_keywords

当用户需要 Glassdoor 公司概况信息、Glassdoor 公司信息、Glassdoor company overview、Glassdoor 公司 URL、Glassdoor 公司搜索，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Glassdoor 公司概况信息采集 Builder 任务，支持 glassdoor_company_by-url、glassdoor_company_by-inputfilter、glassdoor_company_by-keywords 和 glassdoor_company_by-listurl。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `glassdoor.com`
- spider_id: `glassdoor_company_by-keywords`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `search_url` | `search_url` | 否 | —(空) | 搜索网址，该参数是您需要输入基于公司搜索词 URL。用于 glassdoor_company_by-keywords，默认值为 https://www.glassdoor.com/Search/results.htm?keyword=Apple。 |
| `max_search_results` | `max_search_results` | 否 | —(空) | 最大搜索结果数，该参数用于指定采集公司信息的最大数量。用于 glassdoor_company_by-keywords，默认值为 5。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## glassdoor_company_by_listurl

当用户需要 Glassdoor 公司概况信息、Glassdoor 公司信息、Glassdoor company overview、Glassdoor 公司 URL、Glassdoor 公司搜索，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Glassdoor 公司概况信息采集 Builder 任务，支持 glassdoor_company_by-url、glassdoor_company_by-inputfilter、glassdoor_company_by-keywords 和 glassdoor_company_by-listurl。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `glassdoor.com`
- spider_id: `glassdoor_company_by-listurl`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `url` | `url` | 否 | —(空) | Glassdoor URL，该参数用于指定采集 Glassdoor 公司网址。用于 glassdoor_company_by-url 和 glassdoor_company_by-listurl；by-url 默认值为 https://www.glassdoor.co.uk/Overview/Working-at-Apple-EI_IE1138.11,16.htm，by-listurl 默认值为 https://www.glassdoor.com/Explore/browse-companies.htm?filterType=RATING_OVERALL&locId=1347&locType=S&locName=Texas%252C%2520US&occ=Manager&page=1&overall_rating_low=1。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## glassdoor_joblistings_by_url

当用户需要 Glassdoor 招聘信息、Glassdoor 职位信息、Glassdoor job listings、Glassdoor 招聘搜索链接，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Glassdoor 招聘信息采集 Builder 任务，支持 glassdoor_joblistings_by-url、glassdoor_joblistings_by-keywords 和 glassdoor_joblistings_by-listurl。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `glassdoor.com`
- spider_id: `glassdoor_joblistings_by-url`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `url` | `url` | 否 | —(空) | 列表网址或招聘搜索链接，该参数用于指定采集 Glassdoor 职位列表网址或 Glassdoor 招聘信息的搜索链接。用于 glassdoor_joblistings_by-url 和 glassdoor_joblistings_by-listurl，默认值按文档为同一个 Glassdoor 职位 URL。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## glassdoor_joblistings_by_keywords

当用户需要 Glassdoor 招聘信息、Glassdoor 职位信息、Glassdoor job listings、Glassdoor 招聘搜索链接，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Glassdoor 招聘信息采集 Builder 任务，支持 glassdoor_joblistings_by-url、glassdoor_joblistings_by-keywords 和 glassdoor_joblistings_by-listurl。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `glassdoor.com`
- spider_id: `glassdoor_joblistings_by-keywords`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `keyword` | `keyword` | 否 | `data analyst` | 关键词，该参数是通过职位名称等关键字搜索进行采集招聘信息。用于 glassdoor_joblistings_by-keywords，默认值为 data analyst。 |
| `location` | `location` | 否 | `New York` | 地点，该参数用于指定采集特定位置的招聘信息。用于 glassdoor_joblistings_by-keywords，默认值为 New York。 |
| `country` | `country` | 否 | `US` | 国家，该参数用于指定采集招聘信息的国家。接口取 country 选项的 typeValue，默认按确认使用 US。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## glassdoor_joblistings_by_listurl

当用户需要 Glassdoor 招聘信息、Glassdoor 职位信息、Glassdoor job listings、Glassdoor 招聘搜索链接，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Glassdoor 招聘信息采集 Builder 任务，支持 glassdoor_joblistings_by-url、glassdoor_joblistings_by-keywords 和 glassdoor_joblistings_by-listurl。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `glassdoor.com`
- spider_id: `glassdoor_joblistings_by-listurl`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `url` | `url` | 否 | —(空) | 列表网址或招聘搜索链接，该参数用于指定采集 Glassdoor 职位列表网址或 Glassdoor 招聘信息的搜索链接。用于 glassdoor_joblistings_by-url 和 glassdoor_joblistings_by-listurl，默认值按文档为同一个 Glassdoor 职位 URL。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## google_ai_mode

当用户需要通过 Google AI Mode 获取 AI 搜索结果，或需要按位置、国家/地区、语言控制 Google AI Mode 查询结果时触发。

- 上游接口: Search Engine (`POST /request`)
- engine: `google_ai_mode`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `q` | Query | 否 | `pizza` | 定义搜索的查询内容，默认值为 pizza。 |
| `json_` | JSON | 否 | `1` | 定义采集结果的输出格式。1 返回 JSON 格式数据，2 返回 JSON+HTML 格式数据，3 返回 HTML 格式数据，4 返回 Light JSON。默认值为 1。 |
| `location` | Location | 否 | —(空) | 定义搜索发起的地理位置。如果有多个位置与请求的位置匹配，将选择最受欢迎的一个。此参数不能与 uule、lat 和 lon 参数一起使用。 |
| `uule` | UULE | 否 | —(空) | 希望用于搜索的 Google 编码位置。此参数不能与 location、lat、lon 和 radius 参数一起使用。 |
| `no_cache` | NoCache | 否 | `false` | 默认情况下，5 分钟内缓存相同参数的搜索结果。设为 true 可跳过缓存，设为 false（默认）则使用缓存结果。缓存搜索免费，且不计入搜索统计。 |
| `gl` | GL | 否 | —(空) | 定义 Google 搜索要使用的国家/地区。它是一个两位数的国家/地区代码。例如 us 代表美国，uk 代表英国，fr 代表法国。 |
| `hl` | HL | 否 | —(空) | 定义 Google 搜索要使用的语言。它是一个两位数的语言代码。例如 en 代表英语，es 代表西班牙语，fr 代表法语。 |

## google_finance

当用户需要查询 Google Finance 股票、指数、基金、市场行情、金融资产或证券相关搜索结果时触发。

- 上游接口: Search Engine (`POST /request`)
- engine: `google_finance`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `q` | Query | 否 | —(空) | 该参数定义您想要搜索的查询内容。可以是股票、指数、共同基金、货币或期货。 |
| `json_` | JSON | 否 | `1` | 该参数定义采集结果的输出格式。可选择 JSON、HTML（支持下载）格式，默认为 JSON；1 返回 JSON，2 返回 JSON+HTML，3 返回 HTML，4 返回 Light JSON。 |
| `hl` | HL | 否 | —(空) | 该参数定义 Google 职位搜索要使用的语言。它是一个两位数的语言代码，例如 en 代表英语，es 代表西班牙语，fr 代表法语。 |
| `window` | Window | 否 | `1D` | 该参数用于设置图表的时间范围。可设置为 1D - 1 天（默认），5D - 5 天，1M - 1 个月，6M - 6 个月，YTD - 年初至今，1Y - 1 年，5Y - 5 年，MAX - 最大值。 |
| `no_cache` | NoCache | 否 | `false` | 默认情况下，5 分钟内缓存相同参数的搜索结果。将 no_cache 设为 true 可跳过缓存，设为 false（默认）则使用缓存结果。缓存搜索免费，且不计入搜索统计。 |

## google_flights

当用户需要查询 Google Flights 航班信息、机票价格、往返/单程/多城市航班、舱位、航空公司、经停、行李或排放过滤结果时触发。

- 上游接口: Search Engine (`POST /request`)
- engine: `google_flights`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `departure_id` | DepartureID | 否 | —(空) | 定义出发机场代码或地点 kgmid。可以通过逗号分隔指定多个出发机场。例如 CDG,ORY,/m/04jpl。 |
| `arrival_id` | ArrivalID | 否 | —(空) | 定义到达机场代码或地点 kgmid。例如 /m/0vzm 是德克萨斯州奥斯汀的地点 kgmid。可以通过逗号分隔指定多个到达机场。例如 CDG,ORY,/m/04jpl。 |
| `json_` | JSON | 否 | `1` | 定义采集结果的输出格式。1 返回 JSON 格式数据，2 返回 JSON+HTML 格式数据，3 返回 HTML 格式数据，4 返回 Light JSON。默认值为 1。 |
| `gl` | GL | 否 | —(空) | 定义 Google Flights 搜索要使用的国家/地区。它是一个两位数的国家/地区代码。例如 us 代表美国，uk 代表英国，fr 代表法国。 |
| `hl` | HL | 否 | —(空) | 定义 Google Flights 搜索要使用的语言。它是一个两位数的语言代码。例如 en 代表英语，es 代表西班牙语，fr 代表法语。 |
| `currency` | Currency | 否 | `USD` | 定义返回价格的货币。默认为 USD。 |
| `type_` | FlightType | 否 | `1` | 定义航班类型。1 为往返（默认），2 为单程，3 为多城市。当此参数设置为 3 时，使用 multi_city_json 设置航班信息。 |
| `outbound_date` | OutboundDate | 否 | —(空) | 定义出发日期，格式为 YYYY-MM-DD。例如 2026-03-13。 |
| `return_date` | ReturnDate | 否 | —(空) | 定义返程日期，格式为 YYYY-MM-DD。例如 2026-03-19。如果 type 参数设置为 1（往返），则此参数为必填。 |
| `travel_class` | TravelClass | 否 | `1` | 定义旅行舱位。1 为经济舱（默认），2 为高级经济舱，3 为商务舱，4 为头等舱。 |
| `multi_city_json` | MultiCityJSON | 否 | —(空) | 定义多城市航班的航班信息。它是一个包含多个航班信息对象的 JSON 字符串。 |
| `show_hidden` | ShowHidden | 否 | `false` | 设置为 true 以包含隐藏的航班结果。默认为 false。 |
| `exclude_basic` | ExcludeBasic | 否 | `false` | 设置为 true 以排除基础经济舱结果。得到的票价将包含免费选座和随身行李。默认为 false。目前，此过滤器仅适用于美国国内航班，且只能在 gl 为 us 且 travel_class 为 1 时使用。 |
| `deep_search` | DeepSearch | 否 | `false` | 设置为 true 以启用深度搜索，这可能会产生更好的结果，但响应时间更长。深度搜索结果与浏览器中 Google Flights 页面上找到的结果相同。出于性能考虑，默认情况下此选项设置为 false。 |
| `adults` | Adults | 否 | `1` | 定义成人数量。默认为 1。 |
| `children` | Children | 否 | `0` | 定义儿童数量。默认为 0。 |
| `infants_in_seat` | InfantsInSeat | 否 | `0` | 定义占座婴儿数量。默认为 0。 |
| `infants_on_lap` | InfantsOnLap | 否 | `0` | 定义不占座婴儿数量。默认为 0。 |
| `sort_by` | SortBy | 否 | `1` | 定义结果的排序顺序。1 为优选航班（默认），2 为价格，3 为起飞时间，4 为到达时间，5 为飞行时长，6 为排放量。 |
| `stops` | Stops | 否 | `0` | 定义航班经停次数。0 为任何经停次数（默认），1 为仅直飞，2 为 1 次或更少经停，3 为 2 次或更少经停。 |
| `exclude_airlines` | ExcludeAirlines | 否 | —(空) | 定义要排除的航空公司代码。多个航空公司用逗号分隔。不能与 include_airlines 一起使用。 |
| `include_airlines` | IncludeAirlines | 否 | —(空) | 定义要包含的航空公司代码。多个航空公司用逗号分隔。不能与 exclude_airlines 一起使用。 |
| `bags` | Bags | 否 | `0` | 定义随身行李数量。默认为 0。此参数不应超过允许携带随身行李的乘客总数（成人、儿童和占座婴儿）。 |
| `max_price` | MaxPrice | 否 | —(空) | 定义最高机票价格。默认为无限制。 |
| `outbound_times` | OutboundTimes | 否 | —(空) | 定义出发时间范围。它是一个包含两个（仅起飞）或四个（起飞和到达）逗号分隔数字的字符串。 |
| `return_times` | ReturnTimes | 否 | —(空) | 定义返程时间范围。它是一个包含两个（仅起飞）或四个（起飞和到达）逗号分隔数字的字符串。每个数字代表一个小时的开始。 |
| `emissions` | Emissions | 否 | —(空) | 定义航班的排放水平。1 表示仅选择低碳排放航班。 |
| `layover_duration` | LayoverDuration | 否 | —(空) | 定义中转时长（以分钟为单位）。它是一个包含两个逗号分隔数字的字符串。例如 90,330 表示 1 小时 30 分钟到 5 小时 30 分钟。 |
| `exclude_conns` | ExcludeConns | 否 | —(空) | 定义要排除的中转机场代码。机场 ID 为大写 3 字母代码，可以在 Google Flights 或 IATA 上搜索。 |
| `max_duration` | MaxDuration | 否 | —(空) | 定义最长飞行时长（以分钟为单位）。例如 1500 表示 25 小时。 |
| `departure_token` | DepartureToken | 否 | —(空) | 用于选择航班并获取返程航班（对于往返航班）或行程下一段的航班（对于多城市航班）。在出发航班结果中找到此令牌。它不能与 booking_token 一起使用。 |
| `no_cache` | NoCache | 否 | `false` | 默认情况下，5 分钟内缓存相同参数的搜索结果。设为 true 可跳过缓存，设为 false（默认）则使用缓存结果。缓存搜索免费，且不计入搜索统计。 |

## google_hotels

当用户需要查询 Google Hotels 酒店搜索结果、住宿价格、入住退房日期、评分、设施、酒店类型或住宿筛选条件时触发。

- 上游接口: Search Engine (`POST /request`)
- engine: `google_hotels`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `q` | Query | 否 | `pizza` | 定义搜索的查询内容，默认值为 pizza。 |
| `json_` | JSON | 否 | `1` | 该参数定义采集结果的输出格式。可选择 JSON、HTML（支持下载）格式，默认为 JSON；1 返回 JSON，2 返回 JSON+HTML，3 返回 HTML，4 返回 Light JSON。 |
| `hl` | HL | 否 | —(空) | 该参数定义 Google 职位搜索要使用的语言。它是一个两位数的语言代码，例如 en 代表英语，es 代表西班牙语，fr 代表法语。 |
| `gl` | GL | 否 | —(空) | 该参数定义 Google 酒店搜索要使用的国家/地区。它是一个两位数的国家/地区代码，例如 us 代表美国，uk 代表英国，fr 代表法国。 |
| `currency` | Currency | 否 | `USD` | 该参数定义返回价格的货币。默认为 USD。 |
| `check_in_date` | CheckInDate | 否 | —(空) | 该参数定义入住日期。格式为 YYYY-MM-DD。例如：2026-03-13。 |
| `check_out_date` | CheckOutDate | 否 | —(空) | 该参数定义退房日期。格式为 YYYY-MM-DD。例如：2026-03-14。 |
| `adults` | Adults | 否 | `2` | 该参数定义成人数量。默认为 2。 |
| `children` | Children | 否 | `0` | 该参数定义儿童数量。默认为 0。 |
| `children_ages` | ChildrenAges | 否 | —(空) | 该参数定义儿童的年龄。年龄范围为 1 到 17，未满 1 岁的儿童视为 1 岁。单个儿童示例：5。多个儿童示例（用逗号 , 分隔）：5,8,10。指定的儿童年龄数量必须与 children 参数匹配。 |
| `sort_by` | SortBy | 否 | —(空) | 该参数用于对结果进行排序。默认按相关性排序。可用选项：3 - 最低价格，8 - 最高评分，13 - 评论最多。 |
| `min_price` | MinPrice | 否 | —(空) | 该参数定义价格范围的下限。 |
| `max_price` | MaxPrice | 否 | —(空) | 该参数定义价格范围的上限。 |
| `property_types` | PropertyTypes | 否 | —(空) | 该参数定义仅在结果中包含特定类型的住宿。单个类型示例：17。多个类型示例（用逗号 , 分隔）：17,12,18。 |
| `amenities` | Amenities | 否 | —(空) | 该参数定义仅包含提供指定设施的结果。对于度假租赁，请访问 Google 度假租赁设施页面查看支持的度假租赁设施完整列表。单个设施示例：35。多个设施示例（用逗号 , 分隔）：35,9,19。 |
| `rating` | Rating | 否 | —(空) | 该参数用于将结果过滤到特定评分。可用选项：7 - 3.5+，8 - 4.0+，9 - 4.5+。 |
| `brands` | Brands | 否 | —(空) | 该参数定义您希望搜索结果集中的品牌，多个品牌示例用逗号 , 分隔。 |
| `hotel_class` | HotelClass | 否 | —(空) | 该参数定义仅在结果中包含特定酒店星级。多个星级示例用逗号 , 分隔。 |
| `free_cancellation` | FreeCancellation | 否 | —(空) | 该参数定义显示提供免费取消的结果。此参数不适用于度假租赁。可用值为 true 或 false。 |
| `special_offers` | SpecialOffers | 否 | —(空) | 该参数定义显示有特惠的结果。此参数不适用于度假租赁。可用值为 true 或 false。 |
| `eco_certified` | EcoCertified | 否 | —(空) | 该参数定义显示获得生态认证的结果。此参数不适用于度假租赁。可用值为 true 或 false。 |
| `vacation_rentals` | VacationRentals | 否 | —(空) | 该参数定义搜索度假租赁结果。默认搜索的是酒店。可用值为 true 或 false。 |
| `bedrooms` | Bedrooms | 否 | `0` | 该参数定义最小卧室数量。默认为 0。此参数仅适用于度假租赁。 |
| `bathrooms` | Bathrooms | 否 | `0` | 该参数定义最小浴室数量。默认为 0。此参数仅适用于度假租赁。 |
| `next_page_token` | NextPageToken | 否 | —(空) | 该参数定义下一页令牌。它用于检索下一页结果。 |
| `no_cache` | NoCache | 否 | `false` | 默认情况下，5 分钟内缓存相同参数的搜索结果。将 no_cache 设为 true 可跳过缓存，设为 false（默认）则使用缓存结果。缓存搜索免费，且不计入搜索统计。 |
| `property_token` | PropertyToken | 否 | —(空) | 该参数用于获取住宿详细信息，包括名称、地址、电话、价格、附近地点等。 |

## google_images

当用户需要通过 Google Images 搜索图片结果，或按图片尺寸、颜色、类型、版权、位置、语言等条件筛选图片时触发。

- 上游接口: Search Engine (`POST /request`)
- engine: `google_images`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `q` | Query | 否 | `pizza` | 定义搜索的查询内容，默认值为 pizza。 |
| `json_` | JSON | 否 | `1` | 定义采集结果的输出格式。1 返回 JSON 格式数据，2 返回 JSON+HTML 格式数据，3 返回 HTML 格式数据，4 返回 Light JSON。默认值为 1。 |
| `google_domain` | GoogleDomain | 否 | `google.com` | 定义要使用的 Google 域名。默认为 google.com。 |
| `gl` | GL | 否 | —(空) | 定义 Google 搜索要使用的国家/地区。它是一个两位数的国家/地区代码。例如 us 代表美国，uk 代表英国，fr 代表法国。 |
| `hl` | HL | 否 | —(空) | 定义 Google 搜索要使用的语言。它是一个两位数的语言代码。例如 en 代表英语，es 代表西班牙语，fr 代表法语。 |
| `cr` | CR | 否 | —(空) | 定义一个或多个将搜索限制在的国家/地区。它使用 country{两位大写国家/地区代码} 指定国家/地区，并使用 I 作为分隔符。例如 countryFRIcountryDE 将仅搜索法国和德国的页面。 |
| `lr` | LR | 否 | —(空) | 定义一个或多个将搜索限制在的语言。它使用 lang_{两位语言代码} 指定语言，并使用 I 作为分隔符。例如 lang_frIlang_de 将仅搜索法语和德语的页面。 |
| `location` | Location | 否 | —(空) | 定义搜索发起的地理位置。如果有多个位置与请求的位置匹配，将选择最受欢迎的一个。此参数不能与 uule、lat 和 lon 参数一起使用。 |
| `uule` | UULE | 否 | —(空) | 希望用于搜索的 Google 编码位置。此参数不能与 location、lat、lon 和 radius 参数一起使用。 |
| `lat` | Lat | 否 | —(空) | 定义搜索起点的 GPS 纬度。使用 lon 参数时必须同时提供此参数。 |
| `lon` | Lon | 否 | —(空) | 定义搜索起点的 GPS 经度。使用 lat 参数时必须同时提供此参数。 |
| `radius` | Radius | 否 | —(空) | 定义搜索结果偏向的范围（以米为单位）。取值范围：桌面端 1-199，平板/移动端 1-1000。 |
| `start` | Start | 否 | `0` | 定义结果偏移量。它跳过指定数量的结果，用于分页。例如 0 默认是第一页结果，10 是第二页结果，20 是第三页结果，以此类推。 |
| `tbm` | TBM | 否 | `isch` | 定义要执行的搜索类型。isch 为 Google 图片，lcl 为 Google 本地，vid 为 Google 视频，nws 为 Google 新闻，shop 为 Google 购物，pts 为 Google 专利。 |
| `ludocid` | Ludocid | 否 | —(空) | 定义地点的 Google CID（客户标识符），可以使用 Google 的 CID 转换器获取它。 |
| `lsig` | Lsig | 否 | —(空) | 用于强制显示知识图谱地图视图。可以通过本地包 API 或 Google 本地 API 查找 lsig ID。 |
| `kgmid` | KGMID | 否 | —(空) | 定义要抓取的 Google 知识图谱列表的 ID（KGMID）。 |
| `si` | SI | 否 | —(空) | 定义要抓取的 Google 搜索的缓存搜索参数。 |
| `ibp` | IBP | 否 | —(空) | 负责渲染某些元素的布局和扩展。例如 gwp;0,7 用于扩展使用 ludocid 的搜索，以显示扩展的知识图谱。 |
| `uds` | UDS | 否 | —(空) | 启用搜索过滤。它是 Google 提供的一个字符串作为过滤器。 |
| `tbs` | TBS | 否 | —(空) | 定义常规查询字段中无法实现的高级搜索参数。例如专利、日期、新闻、视频、图片、应用或文本内容的高级搜索。 |
| `safe` | Safe | 否 | —(空) | 定义成人内容的过滤级别。可以设置为 active 或 off，默认情况下 Google 会模糊处理露骨内容。 |
| `nfpr` | NFPR | 否 | —(空) | 当原始查询拼写错误时，定义是否排除来自自动更正查询的结果。设置为 1 排除这些结果，设置为 0 包含它们（默认）。 |
| `filter` | Filter | 否 | `1` | 定义“类似结果”和“省略结果”的过滤器是开启还是关闭。设置为 1（默认）启用这些过滤器，设置为 0 禁用这些过滤器。 |
| `device` | Device | 否 | `desktop` | 定义用于获取结果的设备。可设置为 desktop（默认值）使用常规浏览器，tablet 使用平板浏览器（目前使用 iPad），或 mobile 使用移动浏览器。 |
| `render_js` | RenderJS | 否 | —(空) | 如果为 true，系统将使用浏览器执行页面脚本并返回完整渲染后的 HTML。开启后会显著增加采集耗时，请按需使用。 |
| `no_cache` | NoCache | 否 | `false` | 默认情况下，5 分钟内缓存相同参数的搜索结果。设为 true 可跳过缓存，设为 false（默认）则使用缓存结果。缓存搜索免费，且不计入搜索统计。 |
| `ai_overview` | AIOverview | 否 | —(空) | 控制是否获取 Google 搜索结果中的 AI 概览（AI Overview）内容。成功获取 AI 概览通常计为 1 次响应；当首次请求仅返回 page_token 时，系统自动进行的第二次请求将额外计费，总共消耗 2 次响应。 |

## google_jobs

当用户需要通过 Google Jobs 查询招聘职位、岗位列表、下一页职位结果，或按地点、半径、远程办公、过滤条件检索工作信息时触发。

- 上游接口: Search Engine (`POST /request`)
- engine: `google_jobs`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `q` | Query | 是 | — | 定义想要搜索的查询内容。 |
| `json_` | JSON | 否 | `1` | 定义采集结果的输出格式。1 返回 JSON 格式数据，2 返回 JSON+HTML 格式数据，3 返回 HTML 格式数据，4 返回 Light JSON。默认值为 1。 |
| `google_domain` | GoogleDomain | 否 | `google.com` | 定义要使用的 Google 域名。默认为 google.com。 |
| `gl` | GL | 否 | —(空) | 定义 Google 搜索要使用的国家/地区。它是一个两位数的国家/地区代码。例如 us 代表美国，uk 代表英国，fr 代表法国。 |
| `hl` | HL | 否 | —(空) | 定义 Google 职位搜索要使用的语言。它是一个两位数的语言代码。例如 en 代表英语，es 代表西班牙语，fr 代表法语。 |
| `location` | Location | 否 | —(空) | 定义搜索发起的地理位置。如果有多个位置与请求的位置匹配，将选择最受欢迎的一个。 |
| `uule` | UULE | 否 | —(空) | 希望用于搜索的 Google 编码位置。uule 和 location 参数不能同时使用。 |
| `next_page_token` | NextPageToken | 否 | —(空) | 定义下一页令牌，用于检索下一页结果。每页最多返回 10 条结果。 |
| `chips` | Chips | 否 | —(空) | 定义额外的查询条件。职位搜索页面顶部包含称为 chips 的元素，提取其值以传递给 chips 参数。 |
| `lrad` | LRAD | 否 | —(空) | 定义以公里为单位的搜索半径。不严格限制半径范围。 |
| `ltype` | LType | 否 | —(空) | 按居家办公过滤结果。此参数已被 Google 弃用，可设置为 true 或 1。 |
| `uds` | UDS | 否 | —(空) | 启用搜索过滤。它是 Google 提供的一个字符串作为过滤器。 |
| `no_cache` | NoCache | 否 | `false` | 默认情况下，5 分钟内缓存相同参数的搜索结果。设为 true 可跳过缓存，设为 false（默认）则使用缓存结果。缓存搜索免费，且不计入搜索统计。 |

## google_lens

当用户需要通过 Google Lens 基于图片 URL 识别图片内容、查找视觉匹配、商品匹配、完全匹配或关于此图片的信息时触发。

- 上游接口: Search Engine (`POST /request`)
- engine: `google_lens`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `url` | URL | 否 | —(空) | 该参数定义要执行 Google Lens 搜索的图片 URL。 |
| `json_` | JSON | 否 | `1` | 该参数定义采集结果的输出格式；可选择 JSON、HTML（支持下载）格式，默认为 JSON。1 返回 JSON，2 返回 JSON+HTML，3 返回 HTML，4 返回 Light JSON。 |
| `hl` | HL | 否 | —(空) | 该参数定义 Google Lens 搜索要使用的语言。它是一个两位数的语言代码。例如：en 代表英语，es 代表西班牙语，fr 代表法语。 |
| `country` | Country | 否 | —(空) | 该参数定义 Google Lens 搜索要使用的特定国家/地区位置。它是一个两位数的国家/地区代码。例如：us 代表美国，fr 代表法国，de 代表德国。 |
| `type_` | SearchType | 否 | `all` | 该参数定义要执行的搜索类型，默认值为 all。可用值：all、products、about_this_image、exact_matches、visual_matches。 |
| `q` | Query | 否 | —(空) | 该参数定义在 Google Lens 搜索中一并使用的搜索查询。仅当 type 为 all、visual_matches 或 products 时适用。 |
| `safe` | Safe | 否 | —(空) | 该参数定义成人内容的过滤级别。可设置为 active 或 off。 |
| `no_cache` | NoCache | 否 | `false` | 默认情况下，5 分钟内缓存相同参数的搜索结果；将 no_cache 设置为 true 可跳过缓存，设置为 false（默认）则使用缓存结果；缓存搜索免费，且不计入搜索统计。 |

## google_local

当用户需要查询 Google 本地搜索结果、附近商家、地点列表、本地服务或基于位置的本地结果时触发。

- 上游接口: Search Engine (`POST /request`)
- engine: `google_local`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `q` | Query | 是 | — | 定义想要搜索的查询内容。 |
| `json_` | JSON | 否 | `1` | 定义采集结果的输出格式。1 返回 JSON 格式数据，2 返回 JSON+HTML 格式数据，3 返回 HTML 格式数据，4 返回 Light JSON。默认值为 1。 |
| `google_domain` | GoogleDomain | 否 | `google.com` | 定义要使用的 Google 域名。默认为 google.com。 |
| `gl` | GL | 否 | —(空) | 定义 Google 搜索要使用的国家/地区。它是一个两位数的国家/地区代码。例如 us 代表美国，uk 代表英国，fr 代表法国。 |
| `hl` | HL | 否 | —(空) | 定义 Google 职位搜索要使用的语言。它是一个两位数的语言代码。例如 en 代表英语，es 代表西班牙语，fr 代表法语。 |
| `location` | Location | 否 | —(空) | 定义搜索发起的地理位置。如果有多个位置与请求的位置匹配，将选择最受欢迎的一个。 |
| `uule` | UULE | 否 | —(空) | 希望用于搜索的 Google 编码位置。uule 和 location 参数不能同时使用。 |
| `start` | Start | 否 | —(空) | 定义结果偏移量。它跳过指定数量的结果，用于分页。该值取决于返回的结果数量，可以是 10 或 20。例如，移动端返回 10 条结果时，start 应为 10、20、30。 |
| `ludocid` | Ludocid | 否 | —(空) | 定义地点的 Google CID（客户标识符）。 |
| `tbs` | TBS | 否 | —(空) | 定义常规查询字段中无法实现的高级搜索参数。 |
| `no_cache` | NoCache | 否 | `false` | 默认情况下，5 分钟内缓存相同参数的搜索结果。设为 true 可跳过缓存，设为 false（默认）则使用缓存结果。缓存搜索免费，且不计入搜索统计。 |

## google_comment_by_url

当用户需要 Google 地图评论信息、Google 地图评论、Google Maps reviews、Google 商家评论，与采集、抓取、爬取、获取、提取等动词组合时触发。提交 Google 地图评论信息采集 Builder 任务，采集器标识固定为 google_comment_by-url。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `google.com`
- spider_id: `google_comment_by-url`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `url` | `url` | 否 | —(空) | Google 地图 URL，该参数用于指定待采集的 Google 地图访问链接信息。用于 google_comment_by-url，默认值为 https://www.google.com/maps/place/Waterfront+Botanical+Gardens/@38.2630366,-85.7288454,15z/data=!4m8!3m7!1s0x8869731e16a7bdbd:0x2f5d238fefed7ca1!8m2!3d38.2632837!4d-85.7239738!9m1!1b1!16s%2Fg%2F11c709xzzx?hl=en&entry=ttu。 |
| `days_limit` | `days_limit` | 否 | —(空) | 天数限制，该参数用于指定待采集的 Google 地图评论发布天数限制，即从当前日期开始向前检索评论的天数。默认值为 20。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## google_map_details_by_url

当用户需要 Google 地图信息、Google 地图详细信息、Google Maps details、Google 商家信息，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Google 地图详细信息采集 Builder 任务，支持 google_map-details_by-url、google_map-details_by-cid、google_map-details_by-location 和 google_map-details_by-placeid。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `google.com`
- spider_id: `google_map-details_by-url`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `url` | `url` | 否 | —(空) | Google 地图 URL，该参数用于指定待采集的 Google 地图访问链接信息。用于 google_map-details_by-url，默认值为 https://www.google.com/maps/place/Pizza+Inn+Magdeburg/data=!4m7!3m6!1s0x47a5f50c083530a3:0xfdba8746b538141!8m2!3d52.1263086!4d11.6094743!16s%2Fg%2F11kqmtk3dt!19sChIJozA1CAz1pUcRQYFTa3So2w8?authuser=0&hl=en&rclk=1。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## google_map_details_by_cid

当用户需要 Google 地图信息、Google 地图详细信息、Google Maps details、Google 商家信息，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Google 地图详细信息采集 Builder 任务，支持 google_map-details_by-url、google_map-details_by-cid、google_map-details_by-location 和 google_map-details_by-placeid。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `google.com`
- spider_id: `google_map-details_by-cid`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `CID` | `CID` | 否 | —(空) | CID，该参数用于指定待采集的 CID 信息。用于 google_map-details_by-cid，默认值为 2476046430038551731。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## google_map_details_by_location

当用户需要 Google 地图信息、Google 地图详细信息、Google Maps details、Google 商家信息，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Google 地图详细信息采集 Builder 任务，支持 google_map-details_by-url、google_map-details_by-cid、google_map-details_by-location 和 google_map-details_by-placeid。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `google.com`
- spider_id: `google_map-details_by-location`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `keyword` | `keyword` | 否 | —(空) | Google 关键词，该参数用于指定通过特定关键词搜索地图信息，可以是位置、邮政编码或类别。用于 google_map-details_by-location，默认值为 pizza。 |
| `country` | `country` | 否 | —(空) | Google 国家，该参数用于指定要搜索的国家。用于 google_map-details_by-location，默认值为 United States。 |
| `lat` | `lat` | 否 | —(空) | 纬度，该参数用于指定要搜索的位置的纬度。用于 google_map-details_by-location，默认值为 38。 |
| `long` | `long` | 否 | —(空) | 经度，该参数用于指定要搜索的位置的经度。用于 google_map-details_by-location，默认值为 77。 |
| `zoom_level` | `zoom_level` | 否 | —(空) | 缩放级别，该参数用于指示要搜索的缩放级别。用于 google_map-details_by-location，默认值为 20。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## google_map_details_by_placeid

当用户需要 Google 地图信息、Google 地图详细信息、Google Maps details、Google 商家信息，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Google 地图详细信息采集 Builder 任务，支持 google_map-details_by-url、google_map-details_by-cid、google_map-details_by-location 和 google_map-details_by-placeid。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `google.com`
- spider_id: `google_map-details_by-placeid`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `place_id` | `place_id` | 否 | —(空) | 商家ID，该参数用于指定 Google 地图的商家 ID。用于 google_map-details_by-placeid，默认值为 ChIJ3S-JXmauEmsRUcIaWtf4MzE。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## google_maps

当用户需要查询 Google Maps 地点、商家、本地位置、地图搜索结果，或基于经纬度、地点 ID、CID、地图缩放范围获取地图数据时触发。

- 上游接口: Search Engine (`POST /request`)
- engine: `google_maps`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `q` | Query | 是 | — | 定义想要搜索的查询内容。 |
| `json_` | JSON | 否 | `1` | 定义采集结果的输出格式。1 返回 JSON 格式数据，2 返回 JSON+HTML 格式数据，3 返回 HTML 格式数据，4 返回 Light JSON。默认值为 1。 |
| `ll` | LL | 否 | —(空) | 定义搜索起点的 GPS 坐标。其值必须符合 @ + 纬度 + , + 经度 + , + 缩放级别/地图高度格式，例如 @40.7455096,-74.0083012,14z 或 @43.8521864,11.2168835,10410m。此参数不能与 location、lat、lon、z 或 m 参数一起使用。 |
| `location` | Location | 否 | —(空) | 定义地点，其 GPS 坐标用作搜索起点，最终会被编码为 ll 参数的一部分。此参数应与 z 或 m 参数一起使用，不能与 ll、lat 或 lon 参数一起使用。 |
| `lat` | Lat | 否 | —(空) | 定义搜索起点的 GPS 纬度，最终会被编码为 ll 参数的一部分。使用 lon 参数时必须同时提供此参数。此参数应与 z 或 m 参数一起使用，不能与 ll 或 location 参数一起使用。 |
| `lon` | Lon | 否 | —(空) | 定义搜索起点的 GPS 经度，最终会被编码为 ll 参数的一部分。使用 lat 参数时必须同时提供此参数。此参数应与 z 或 m 参数一起使用，不能与 ll 或 location 参数一起使用。 |
| `z` | Zoom | 否 | —(空) | 定义地图缩放级别。最小值为 3（地图完全缩小），最大有效值取决于位置，范围从 18 到 23。使用 location 或 lat/lon 参数时，必须指定 z 或 m。 |
| `m` | MapHeight | 否 | —(空) | 定义以米为单位的地图高度。最小值为 1，最大值为 15028132，大致相当于赤道上的 3z。最终会被编码为 ll 参数的一部分。使用 location 或 lat/lon 参数时，必须指定 m 或 z。 |
| `nearby` | Nearby | 否 | —(空) | 强制返回更接近指定位置的搜索结果。当 q 参数包含 near me 关键词时，强烈建议使用此参数；当 q 参数包含地点时，不建议使用。此参数应与 ll、location 或 lat/lon 参数一起使用。可设置为 true 或 false。 |
| `google_domain` | GoogleDomain | 否 | `google.com` | 定义要使用的 Google 域名。默认为 google.com。 |
| `hl` | HL | 否 | —(空) | 定义 Google 地图搜索要使用的语言。它是一个两位数的语言代码。例如 en 代表英语，es 代表西班牙语，fr 代表法语。 |
| `gl` | GL | 否 | —(空) | 定义 Google 地图搜索要使用的国家/地区。它是一个两位数的国家/地区代码。例如 us 代表美国，uk 代表英国，fr 代表法国。 |
| `start` | Start | 否 | `0` | 定义结果偏移量。它跳过指定数量的结果，用于分页。例如 0 默认是第一页结果，20 是第二页结果，40 是第三页结果，依此类推。 |
| `type_` | SearchType | 否 | —(空) | 定义要执行的搜索类型。search 返回 q 参数列出的结果列表；place 在设置 data 参数时返回特定地点结果。使用 place_id 或 data_cid 时不需要此参数。 |
| `data` | Data | 否 | —(空) | 此参数已弃用，请改用 place_id 或 data_cid。该参数可用于过滤搜索结果。 |
| `place_id` | PlaceID | 否 | —(空) | 定义 Google 地图中地点的唯一引用。地点 ID 可用于大多数地点，包括企业、地标、公园和交叉路口。 |
| `data_cid` | DataCID | 否 | —(空) | 定义地点的 Google CID（客户标识符）。data_cid 和 place_id 不能同时使用。 |
| `no_cache` | NoCache | 否 | `false` | 默认情况下，5 分钟内缓存相同参数的搜索结果。设为 true 可跳过缓存，设为 false（默认）则使用缓存结果。缓存搜索免费，且不计入搜索统计。 |

## google_news

当用户需要查询 Google News 新闻结果、获取某个关键词、主题、出版物、版块或报道的新闻内容时触发。

- 上游接口: Search Engine (`POST /request`)
- engine: `google_news`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `q` | Query | 否 | `pizza` | 定义搜索的查询内容，默认值为 pizza。 |
| `json_` | JSON | 否 | `1` | 定义采集结果的输出格式。1 返回 JSON 格式数据，2 返回 JSON+HTML 格式数据，3 返回 HTML 格式数据，4 返回 Light JSON。默认值为 1。 |
| `no_cache` | NoCache | 否 | `false` | 默认情况下，5 分钟内缓存相同参数的搜索结果。设为 true 可跳过缓存，设为 false（默认）则使用缓存结果。缓存搜索免费，且不计入搜索统计。 |
| `gl` | GL | 否 | `us` | 定义 Google 搜索要使用的国家/地区。它是一个两位数的国家/地区代码。例如 us 代表美国，uk 代表英国，fr 代表法国。默认值 us |
| `hl` | HL | 否 | —(空) | 定义 Google 搜索要使用的语言。它是一个两位数的语言代码。例如 en 代表英语，es 代表西班牙语，fr 代表法语。 |
| `topic_token` | TopicToken | 否 | —(空) | 定义 Google 新闻主题令牌。用于访问特定主题，例如世界、商业、科技。 |
| `kgmid` | KGMID | 否 | —(空) | 定义 Google 新闻结果中主题或地点的知识图谱 ID（KGMID）。它是一个以 /m/ 或 /g/ 开头的字符串。例如 /m/0vzm 是德克萨斯州奥斯汀的 kgmid。 |
| `publication_token` | PublicationToken | 否 | —(空) | 定义 Google 新闻出版物令牌。用于访问来自特定发布者，例如 CNN、BBC、卫报的新闻结果。 |
| `section_token` | SectionToken | 否 | —(空) | 定义 Google 新闻版块令牌。用于访问特定主题的子版块，例如“商业 -> 经济”。 |
| `story_token` | StoryToken | 否 | —(空) | 定义 Google 新闻报道令牌。用于访问特定报道的完整报道新闻结果。 |
| `so` | SortBy | 否 | `0` | 定义排序方法。结果可以按相关性或日期排序，默认按相关性排序。0 表示相关性，1 表示日期。 |

## google_patents

当用户需要查询 Google Patents 专利搜索结果、专利标题、发明人、申请人、专利号或专利文献数据时触发。

- 上游接口: Search Engine (`POST /request`)
- engine: `google_patents`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `q` | Query | 否 | —(空) | 该参数定义您想要搜索的查询内容。您可以使用分号 ; 分隔多个搜索词。例如：(Coffee) OR (Tea);(A47J)。 |
| `json_` | JSON | 否 | `1` | 该参数定义采集结果的输出格式；可选择 JSON、HTML（支持下载）格式，默认为 JSON；1 返回 JSON，2 返回 JSON+HTML，3 返回 HTML，4 返回 Light JSON。 |
| `page` | Page | 否 | `1` | 该参数定义页码，用于分页。1（默认）是第一页结果，2 是第二页结果，依此类推。 |
| `num` | Num | 否 | —(空) | 该参数控制每页的结果数量。最小值：10，最大值：100。 |
| `sort` | Sort | 否 | —(空) | 该参数定义排序方法。默认按相关性排序。可用值：new - Newest，old - Oldest。 |
| `clustered` | Clustered | 否 | —(空) | 该参数定义结果的分组方式。支持的值：true - 按分类分组。 |
| `dups` | Dups | 否 | `family` | 该参数定义去重方法。可选 family（Family，默认）或 language（Publication）。 |
| `patents` | Patents | 否 | `true` | 该参数控制是否包含 Google 专利结果，默认为 true。参数值：true。 |
| `scholar` | Scholar | 否 | `false` | 该参数控制是否包含 Google 学术结果，默认为 false。参数值：true。 |
| `before` | Before | 否 | —(空) | 该参数定义结果的最大日期。格式为 type:YYYYMMDD，type 可以是 priority、filing、publication 之一。例如：priority:20221231、publication:20230101。 |
| `after` | After | 否 | —(空) | 该参数定义结果的最小日期。格式为 type:YYYYMMDD，type 可以是 priority、filing、publication 之一。例如：priority:20221231、publication:20230101。 |
| `inventor` | Inventor | 否 | —(空) | 该参数定义专利的发明人。使用逗号 , 分隔多个发明人。将包含逗号的名称括在括号中，例如：(Doe, John)。 |
| `assignee` | Assignee | 否 | —(空) | 该参数定义专利的受让人。使用逗号 , 分隔多个受让人。将包含逗号的名称括在括号中，例如：(Tesla, Inc)。 |
| `country` | Country | 否 | —(空) | 该参数按国家/地区过滤专利结果。使用逗号 , 分隔多个国家/地区代码。例如：WO,US。 |
| `language` | Language | 否 | —(空) | 该参数按语言过滤专利结果。使用逗号 , 分隔多个语言。 |
| `status` | Status | 否 | —(空) | 该参数按状态过滤专利结果。支持的值：GRANT - 授权专利，APPLICATION - 专利申请。 |
| `type_` | PatentType | 否 | —(空) | 该参数按类型过滤专利结果。支持的值：PATENT - 专利，DESIGN - 外观设计。 |
| `litigation` | Litigation | 否 | —(空) | 该参数按诉讼状态过滤专利结果。支持的值：YES - 有相关诉讼，NO - 无已知诉讼。 |
| `no_cache` | NoCache | 否 | `false` | 默认情况下，5 分钟内缓存相同参数的搜索结果；将 no_cache 设为 true 可跳过缓存，设为 false（默认）则使用缓存结果；缓存搜索免费，且不计入搜索统计。 |

## google_play

当用户需要查询 Google Play 应用、游戏或商店搜索结果，获取应用列表、详情或与 Google Play 内容相关的数据时触发。

- 上游接口: Search Engine (`POST /request`)
- engine: `google_play`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `q` | Query | 否 | —(空) | 该参数定义您要在 Google Play 应用商店中搜索的查询内容。 |
| `json_` | JSON | 否 | `1` | 该参数定义采集结果的输出格式。可选择 JSON、HTML（支持下载）格式，默认为 JSON；1 返回 JSON，2 返回 JSON+HTML，3 返回 HTML，4 返回 Light JSON。 |
| `hl` | HL | 否 | —(空) | 该参数定义 Google 职位搜索要使用的语言。它是一个两位数的语言代码，例如 en 代表英语，es 代表西班牙语，fr 代表法语。 |
| `gl` | GL | 否 | `us` | 该参数定义 Google Play 搜索要使用的国家/地区。它是一个两位数的国家/地区代码，例如 us（默认）代表美国，uk 代表英国，fr 代表法国。 |
| `apps_category` | AppsCategory | 否 | —(空) | 该参数定义应用商店类别。 |
| `next_page_token` | NextPageToken | 否 | —(空) | 该参数定义下一页令牌。它用于检索下一页结果。它不应与 section_page_token、see_more_token 和 chart 参数一起使用。 |
| `section_page_token` | SectionPageToken | 否 | —(空) | 该参数定义用于从各个版块检索分页结果的版块页面令牌。它不应与 next_page_token、see_more_token 和 chart 参数一起使用。 |
| `chart` | Chart | 否 | —(空) | 该参数用于显示热门排行榜。最多可返回 50 条结果。它不应与 section_page_token、see_more_token 和 next_page_token 参数一起使用。 |
| `see_more_token` | SeeMoreToken | 否 | —(空) | 该参数定义用于从各个版块检索分页结果的“查看更多”令牌。它通常在下一页结果中找到。它不应与 section_page_token、next_page_token 和 chart 参数一起使用。 |
| `store_device` | StoreDevice | 否 | —(空) | 该参数定义用于排序结果的设备。此参数不能与 apps_category 或 q 参数一起使用。可用值包括 phone、tablet、tv、chromebook、watch、car。 |
| `age` | Age | 否 | —(空) | 该参数定义年龄段子类别。age 仅在 apps_category=FAMILY（儿童应用）时使用。可用值包括 AGE_RANGE1、AGE_RANGE2、AGE_RANGE3。 |
| `no_cache` | NoCache | 否 | `false` | 默认情况下，5 分钟内缓存相同参数的搜索结果。将 no_cache 设为 true 可跳过缓存，设为 false（默认）则使用缓存结果。缓存搜索免费，且不计入搜索统计。 |

## google_play_store_information_by_url

当用户需要 Google Play 商店信息、Google Play App 信息、Google Play 应用信息、Play Store information、Google Play store information，与采集、抓取、爬取、获取、提取等动词组合时触发。提交 Google Play商店信息采集 Builder 任务，采集器标识固定为 google-play-store_information_by-url。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `play.google.com`
- spider_id: `google-play-store_information_by-url`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `app_url` | `app_url` | 否 | —(空) | App URL，Google Play 网站上的 App URL。用于 google-play-store_information_by-url，默认值为 https://play.google.com/store/apps/details?id=com.linkedin.android。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## google_play_store_reviews_by_url

当用户需要 Google Play 商店评论、Google Play 评论、Google Play App 评论、Play Store reviews、Google Play store reviews，与采集、抓取、爬取、获取、提取等动词组合时触发。提交 Google Play 商店评论采集 Builder 任务，采集器标识固定为 google-play-store_reviews_by-url。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `play.google.com`
- spider_id: `google-play-store_reviews_by-url`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `app_url` | `app_url` | 否 | —(空) | App URL，Google Play 网站上的 App URL。用于 google-play-store_reviews_by-url，默认值为 https://play.google.com/store/apps/details?id=com.linkedin.android。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## google_scholar

当用户需要查询 Google Scholar 学术论文、作者、引用、出版物或学术搜索结果时触发。

- 上游接口: Search Engine (`POST /request`)
- engine: `google_scholar`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `q` | Query | 否 | —(空) | 该参数定义您想要搜索的查询内容。 |
| `json_` | JSON | 否 | `1` | 该参数定义采集结果的输出格式。可选择 JSON、HTML（支持下载）格式，默认为 JSON；1 返回 JSON，2 返回 JSON+HTML，3 返回 HTML，4 返回 Light JSON。 |
| `hl` | HL | 否 | —(空) | 该参数定义 Google 职位搜索要使用的语言。它是一个两位数的语言代码，例如 en 代表英语，es 代表西班牙语，fr 代表法语。 |
| `lr` | LR | 否 | —(空) | 该参数定义一个或多个将搜索限制在的语言。它使用 lang_{两位语言代码} 指定语言，并使用 \| 作为分隔符，例如 lang_fr\|lang_de 将仅搜索法语和德语的页面。 |
| `start` | Start | 否 | `0` | 该参数定义结果偏移量。它跳过指定数量的结果，用于分页。例如 0（默认）是第一页结果，10 是第二页结果，20 是第三页结果，依此类推。 |
| `num` | Num | 否 | `10` | 该参数定义返回的最大结果数量，范围为 1 到 20，默认为 10。 |
| `cites` | Cites | 否 | —(空) | 该参数定义用于触发“被引”搜索的文章唯一 ID。使用 cites 将显示 Google 学术中引用该文献的列表。示例值：cites=1275980731835430123。cites 和 q 参数同时使用会触发在引用文献中的搜索。 |
| `as_ylo` | AsYlo | 否 | —(空) | 该参数定义您希望包含结果的起始年份。例如将 as_ylo 设置为 2018 年，则该年份之前的结果将被省略。此参数可与 as_yhi 参数结合使用。 |
| `as_yhi` | AsYhi | 否 | —(空) | 该参数定义您希望包含结果的结束年份。例如将 as_yhi 设置为 2018 年，则该年份之后的结果将被省略。此参数可与 as_ylo 参数结合使用。 |
| `scisbd` | Scisbd | 否 | `0` | 该参数定义过去一年添加的文献，按日期排序。可设置为 1 以仅包含摘要，或设置为 2 以包含全部内容。默认值为 0，表示文献按相关性排序。 |
| `cluster` | Cluster | 否 | —(空) | 该参数定义用于触发“所有版本”搜索的文章唯一 ID。示例值：cluster=1275980731835430123。禁止将 cluster 与 q 和 cites 参数一起使用。请仅使用 cluster 参数。 |
| `as_sdt` | AsSdt | 否 | `0` | 该参数既可用作搜索类型，也可用作过滤器。作为过滤器（仅在搜索文章时有效）：0 排除专利（默认），7 包含专利。作为搜索类型：4 选择判例法（仅限美国法院）。 |
| `safe` | Safe | 否 | —(空) | 该参数定义成人内容的过滤级别。可以设置为 active 或 off，默认情况下 Google 会模糊处理露骨内容。 |
| `filter` | Filter | 否 | `1` | 该参数定义“类似结果”和“省略结果”的过滤器是开启还是关闭。可以设置为 1（默认）以启用这些过滤器，或设置为 0 以禁用这些过滤器。 |
| `as_vis` | AsVis | 否 | `0` | 该参数定义是否希望包含引用。可以设置为 1 以排除这些结果，或设置为 0（默认）以包含它们。 |
| `as_rr` | AsRR | 否 | `0` | 该参数定义是否仅显示综述文章（这些文章包括主题综述，或讨论您搜索的作品或作者）。可以设置为 1 以启用此过滤器，或设置为 0（默认）以显示所有结果。 |
| `no_cache` | NoCache | 否 | `false` | 默认情况下，5 分钟内缓存相同参数的搜索结果。将 no_cache 设为 true 可跳过缓存，设为 false（默认）则使用缓存结果。缓存搜索免费，且不计入搜索统计。 |

## google_search

当用户需要通过 Google 搜索公开网页信息、获取通用网页搜索结果，或按国家、语言、位置、设备、时间条件等控制 Google 搜索结果时触发。

- 上游接口: Search Engine (`POST /request`)
- engine: `google`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `q` | Query | 否 | `pizza` | 定义搜索的查询内容，默认值为 pizza。 |
| `json_` | JSON | 否 | `1` | 定义采集结果的输出格式。1 返回 JSON 格式数据，2 返回 JSON+HTML 格式数据，3 返回 HTML 格式数据，4 返回 Light JSON。默认值为 1。 |
| `google_domain` | GoogleDomain | 否 | `google.com` | 定义要使用的 Google 域名。默认为 google.com。 |
| `gl` | GL | 否 | —(空) | 定义 Google 搜索要使用的国家/地区。它是一个两位数的国家/地区代码。例如 us 代表美国，uk 代表英国，fr 代表法国。 |
| `hl` | HL | 否 | —(空) | 定义 Google 搜索要使用的语言。它是一个两位数的语言代码。例如 en 代表英语，es 代表西班牙语，fr 代表法语。 |
| `cr` | CR | 否 | —(空) | 定义一个或多个将搜索限制在的国家/地区。它使用 country{两位大写国家/地区代码} 指定国家/地区，并使用 I 作为分隔符。例如 countryFRIcountryDE 将仅搜索法国和德国的页面。 |
| `lr` | LR | 否 | —(空) | 定义一个或多个将搜索限制在的语言。它使用 lang_{两位语言代码} 指定语言，并使用 I 作为分隔符。例如 lang_frIlang_de 将仅搜索法语和德语的页面。 |
| `location` | Location | 否 | —(空) | 定义搜索发起的地理位置。如果有多个位置与请求的位置匹配，将选择最受欢迎的一个。此参数不能与 uule、lat 和 lon 参数一起使用。 |
| `uule` | UULE | 否 | —(空) | 希望用于搜索的 Google 编码位置。此参数不能与 location、lat、lon 和 radius 参数一起使用。 |
| `start` | Start | 否 | `0` | 定义结果偏移量。它跳过指定数量的结果，用于分页。例如 0 默认是第一页结果，10 是第二页结果，20 是第三页结果，以此类推。 |
| `tbs` | TBS | 否 | —(空) | 定义常规查询字段中无法实现的高级搜索参数。例如专利、日期、新闻、视频、图片、应用或文本内容的高级搜索。 |
| `safe` | Safe | 否 | —(空) | 定义成人内容的过滤级别。可以设置为 active 或 off，默认情况下 Google 会模糊处理露骨内容。 |
| `nfpr` | NFPR | 否 | —(空) | 当原始查询拼写错误时，定义是否排除来自自动更正查询的结果。设置为 1 排除这些结果，设置为 0 包含它们（默认）。 |
| `filter` | Filter | 否 | `1` | 定义“类似结果”和“省略结果”的过滤器是开启还是关闭。设置为 1（默认）启用这些过滤器，设置为 0 禁用这些过滤器。 |
| `device` | Device | 否 | `desktop` | 定义用于获取结果的设备。可设置为 desktop（默认值）使用常规浏览器，tablet 使用平板浏览器（目前使用 iPad），或 mobile 使用移动浏览器。 |
| `render_js` | RenderJS | 否 | —(空) | 如果为 true，系统将使用浏览器执行页面脚本并返回完整渲染后的 HTML。开启后会显著增加采集耗时，请按需使用。 |
| `no_cache` | NoCache | 否 | `false` | 默认情况下，5 分钟内缓存相同参数的搜索结果。设为 true 可跳过缓存，设为 false（默认）则使用缓存结果。缓存搜索免费，且不计入搜索统计。 |
| `ai_overview` | AIOverview | 否 | —(空) | 控制是否获取 Google 搜索结果中的 AI 概览（AI Overview）内容。成功获取 AI 概览通常计为 1 次响应；当首次请求仅返回 page_token 时，系统自动进行的第二次请求将额外计费，总共消耗 2 次响应。 |

## google_shopping

当用户需要查询 Google Shopping 商品搜索结果、商品价格、促销、包邮、小企业商品，或按价格区间、排序和购物过滤条件检索商品时触发。

- 上游接口: Search Engine (`POST /request`)
- engine: `google_shopping`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `q` | Query | 否 | —(空) | 定义想要搜索的查询内容。提供 shoprs 参数时不需要同时提供 q 参数。 |
| `json_` | JSON | 否 | `1` | 定义采集结果的输出格式。1 返回 JSON 格式数据，2 返回 JSON+HTML 格式数据，3 返回 HTML 格式数据，4 返回 Light JSON。默认值为 1。 |
| `google_domain` | GoogleDomain | 否 | `google.com` | 定义要使用的 Google 域名。默认为 google.com。 |
| `gl` | GL | 否 | —(空) | 定义 Google 搜索要使用的国家/地区。它是一个两位数的国家/地区代码。例如 us 代表美国，uk 代表英国，fr 代表法国。 |
| `hl` | HL | 否 | —(空) | 定义 Google 职位搜索要使用的语言。它是一个两位数的语言代码。例如 en 代表英语，es 代表西班牙语，fr 代表法语。 |
| `location` | Location | 否 | —(空) | 定义搜索发起的地理位置。如果有多个位置与请求的位置匹配，将选择最受欢迎的一个。 |
| `uule` | UULE | 否 | —(空) | 希望用于搜索的 Google 编码位置。uule 和 location 参数不能同时使用。 |
| `start` | Start | 否 | —(空) | 定义结果偏移量。它跳过指定数量的结果，用于分页。该值取决于返回的结果数量，可以是 10 或 20。例如，移动端返回 10 条结果时，start 应为 10、20、30。 |
| `shoprs` | Shoprs | 否 | —(空) | 定义包含关于查询和搜索过滤器元数据的令牌。提供 shoprs 参数时不需要同时提供 q 参数。要应用多个过滤器，请使用 \|\| 分隔符连接它们，例如 shoprs_1\|\|shoprs_2\|\|shoprs_3。 |
| `min_price` | MinPrice | 否 | —(空) | 价格范围查询的下限。该参数会覆盖嵌入到 shoprs 参数中的相应过滤器。 |
| `max_price` | MaxPrice | 否 | —(空) | 价格范围查询的上限。该参数会覆盖嵌入到 shoprs 参数中的相应过滤器。 |
| `sort_by` | SortBy | 否 | —(空) | 定义结果的排序顺序。1 为价格从低到高，2 为价格从高到低。该参数会覆盖嵌入到 shoprs 参数中的相应过滤器。 |
| `free_shipping` | FreeShipping | 否 | —(空) | 仅显示包邮产品。该参数会覆盖嵌入到 shoprs 参数中的相应过滤器。 |
| `on_sale` | OnSale | 否 | —(空) | 仅显示促销产品。该参数会覆盖嵌入到 shoprs 参数中的相应过滤器。 |
| `small_business` | SmallBusiness | 否 | —(空) | 仅显示来自小企业的产品。该参数会覆盖嵌入到 shoprs 参数中的相应过滤器。 |
| `no_cache` | NoCache | 否 | `false` | 默认情况下，5 分钟内缓存相同参数的搜索结果。设为 true 可跳过缓存，设为 false（默认）则使用缓存结果。缓存搜索免费，且不计入搜索统计。 |

## google_shopping_by_keywords

当用户需要 Google 购物信息、Google Shopping 商品信息、Google 购物商品、Google 商品数据，与采集、抓取、爬取、获取、提取等动词组合时触发。提交 Google 购物信息采集 Builder 任务，采集器标识固定为 google_shopping_by-keywords。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `google.com`
- spider_id: `google_shopping_by-keywords`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `keyword` | `keyword` | 否 | —(空) | 产品关键词，该参数用于指定关键字来收集产品数据。用于 google_shopping_by-keywords，默认值为 iphone。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## google_trends

当用户需要查询 Google Trends 趋势数据、关键词热度、地区趋势、相关主题或相关查询时触发。

- 上游接口: Search Engine (`POST /request`)
- engine: `google_trends`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `q` | Query | 否 | `pizza` | 定义搜索的查询内容，默认值为 pizza。 |
| `json_` | JSON | 否 | `1` | 定义采集结果的输出格式。1 返回 JSON 格式数据，2 返回 JSON+HTML 格式数据，3 返回 HTML 格式数据，4 返回 Light JSON。默认值为 1。 |
| `hl` | HL | 否 | —(空) | 定义 Google 职位搜索要使用的语言。它是一个两位数的语言代码。例如 en 代表英语，es 代表西班牙语，fr 代表法语。 |
| `geo` | Geo | 否 | —(空) | 定义搜索发起的地理位置。默认为全球，当 geo 参数值未设置或为空时激活。 |
| `region` | Region | 否 | —(空) | 用于在使用“按细分区域的比较”和“按区域的兴趣”数据类型图表时获取更具体的结果。其他数据类型图表不接受 region 参数。默认值取决于设置的 geo 位置。可用值包括 COUNTRY、REGION、DMA、CITY。 |
| `data_type` | DataType | 否 | —(空) | 定义想要执行的搜索类型。可用值包括 TIMESERIES（时间趋势分析）、GEO_MAP（区域对比分析）、GEO_MAP_0（区域兴趣分布）、RELATED_TOPICS（相关主题推荐）、RELATED_QUERIES（相关查询推荐）。 |
| `tz` | TZ | 否 | `420` | 定义时区偏移量。默认值为 420（太平洋夏令时间 PDT: -07:00）。值以分钟为单位，范围从 -1439 到 1439。 |
| `cat` | Category | 否 | `0` | 定义搜索类别。默认值为 0（所有类别）。可以在 Google 趋势类别列表中找到或下载所有支持的值。示例值包括 0、3、5、7、8、11、12、13、14、16。 |
| `gprop` | GProp | 否 | —(空) | 按属性对结果进行排序。默认属性为网页搜索，当 gprop 参数值未设置或为空时激活。可用值包括 images（图像搜索）、news（新闻搜索）、froogle（Google 购物）、youtube（YouTube 搜索）。 |
| `date` | Date | 否 | —(空) | 定义日期。 |
| `csv` | CSV | 否 | —(空) | 用于检索 CSV 结果。设置为 true 可将 CSV 结果作为数组检索。可用值为 true 或 false。 |
| `include_low_search_volume` | IncludeLowSearchVolume | 否 | —(空) | 用于在结果中包含低搜索量区域。设置为 true 以在结果中包含低搜索量区域。可用值为 true 或 false。 |
| `no_cache` | NoCache | 否 | `false` | 默认情况下，5 分钟内缓存相同参数的搜索结果。设为 true 可跳过缓存，设为 false（默认）则使用缓存结果。缓存搜索免费，且不计入搜索统计。 |

## google_videos

当用户需要通过 Google Videos 搜索视频结果，或按地区、语言、位置、安全过滤、时间条件等获取视频搜索数据时触发。

- 上游接口: Search Engine (`POST /request`)
- engine: `google_videos`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `q` | Query | 是 | — | 定义想要搜索的查询内容。 |
| `json_` | JSON | 否 | `1` | 定义采集结果的输出格式。1 返回 JSON 格式数据，2 返回 JSON+HTML 格式数据，3 返回 HTML 格式数据，4 返回 Light JSON。默认值为 1。 |
| `google_domain` | GoogleDomain | 否 | `google.com` | 定义要使用的 Google 域名。默认为 google.com。 |
| `gl` | GL | 否 | —(空) | 定义 Google 搜索要使用的国家/地区。它是一个两位数的国家/地区代码。例如 us 代表美国，uk 代表英国，fr 代表法国。 |
| `hl` | HL | 否 | —(空) | 定义 Google 职位搜索要使用的语言。它是一个两位数的语言代码。例如 en 代表英语，es 代表西班牙语，fr 代表法语。 |
| `location` | Location | 否 | —(空) | 定义搜索发起的地理位置。如果有多个位置与请求的位置匹配，将选择最受欢迎的一个。 |
| `uule` | UULE | 否 | —(空) | 希望用于搜索的 Google 编码位置。uule 和 location 参数不能同时使用。 |
| `start` | Start | 否 | —(空) | 定义结果偏移量。它跳过指定数量的结果，用于分页。该值取决于返回的结果数量，可以是 10 或 20。例如，移动端返回 10 条结果时，start 应为 10、20、30。 |
| `tbs` | TBS | 否 | —(空) | 定义常规查询字段中无法实现的高级搜索参数。 |
| `no_cache` | NoCache | 否 | `false` | 默认情况下，5 分钟内缓存相同参数的搜索结果。设为 true 可跳过缓存，设为 false（默认）则使用缓存结果。缓存搜索免费，且不计入搜索统计。 |
| `lr` | LR | 否 | —(空) | 定义一个或多个将搜索限制在的语言。它使用 lang_{两位语言代码} 指定语言，并使用 \| 作为分隔符。例如 lang_fr\|lang_de 将仅搜索法语和德语的页面。 |
| `safe` | Safe | 否 | —(空) | 定义成人内容的过滤级别。可以设置为 active 或 off，默认情况下 Google 会模糊处理露骨内容。 |
| `nfpr` | NFPR | 否 | —(空) | 当原始查询拼写错误时，定义是否排除来自自动更正查询的结果。可以设置为 1 以排除这些结果，或设置为 0 以包含它们（默认）。 |
| `filter` | Filter | 否 | `1` | 定义“类似结果”和“省略结果”的过滤器是开启还是关闭。可以设置为 1（默认）以启用这些过滤器，或设置为 0 以禁用这些过滤器。 |

## indeed_companies_info_by_company_list_url

当用户需要 Indeed 公司信息、Indeed companies info、Indeed 公司列表、Indeed 公司关键词、Indeed 行业地区公司，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Indeed 公司信息采集 Builder 任务，支持 indeed_companies-info_by-company-list-url、indeed_companies-info_by-keyword、indeed_companies-info_by-industry-and-state 和 indeed_companies-info_by-company-url。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `indeed.com`
- spider_id: `indeed_companies-info_by-company-list-url`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `company_list_url` | `company_list_url` | 否 | —(空) | Indeed公司列表URL，该参数用于指定采集公司列表的URL。用于 indeed_companies-info_by-company-list-url，默认值为 https://www.indeed.com/companies/browse-companies。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## indeed_companies_info_by_keyword

当用户需要 Indeed 公司信息、Indeed companies info、Indeed 公司列表、Indeed 公司关键词、Indeed 行业地区公司，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Indeed 公司信息采集 Builder 任务，支持 indeed_companies-info_by-company-list-url、indeed_companies-info_by-keyword、indeed_companies-info_by-industry-and-state 和 indeed_companies-info_by-company-url。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `indeed.com`
- spider_id: `indeed_companies-info_by-keyword`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `keyword` | `keyword` | 否 | —(空) | 公司关键词，该参数用于指定采集公司的关键词。用于 indeed_companies-info_by-keyword，默认值为 openai。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## indeed_companies_info_by_industry_and_state

当用户需要 Indeed 公司信息、Indeed companies info、Indeed 公司列表、Indeed 公司关键词、Indeed 行业地区公司，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Indeed 公司信息采集 Builder 任务，支持 indeed_companies-info_by-company-list-url、indeed_companies-info_by-keyword、indeed_companies-info_by-industry-and-state 和 indeed_companies-info_by-company-url。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `indeed.com`
- spider_id: `indeed_companies-info_by-industry-and-state`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `industry` | `industry` | 否 | —(空) | Indeed行业，该参数用于指定采集公司所属行业。用于 indeed_companies-info_by-industry-and-state，默认值为 Accounting & Tax。 |
| `state` | `state` | 否 | —(空) | Indeed 地区，该参数用于指定采集公司所在地区。用于 indeed_companies-info_by-industry-and-state，默认值为 Alabama - 60 companies。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## indeed_companies_info_by_company_url

当用户需要 Indeed 公司信息、Indeed companies info、Indeed 公司列表、Indeed 公司关键词、Indeed 行业地区公司，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Indeed 公司信息采集 Builder 任务，支持 indeed_companies-info_by-company-list-url、indeed_companies-info_by-keyword、indeed_companies-info_by-industry-and-state 和 indeed_companies-info_by-company-url。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `indeed.com`
- spider_id: `indeed_companies-info_by-company-url`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `company_url` | `company_url` | 否 | —(空) | Indeed公司URL，该参数用于指定要采集的公司URL。用于 indeed_companies-info_by-company-url，默认值为 https://www.indeed.com/cmp/Allstate-Insurance。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## indeed_job_listings_by_job_url

当用户需要 Indeed 职位列表、Indeed 职位信息、Indeed job listings、Indeed job URL，与采集、抓取、爬取、获取、提取等动词组合时触发。提交 Indeed 职位列表采集 Builder 任务，采集器标识固定为 indeed_job-listings_by-job-url。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `indeed.com`
- spider_id: `indeed_job-listings_by-job-url`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `job_url` | `job_url` | 否 | —(空) | Indeed职位URL，该参数用于指定采集的 Indeed 职位 URL。用于 indeed_job-listings_by-job-url，默认值为 https://fr.indeed.com/viewjob?jk=55b3e5dfa0c2ff66。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## ins_comment_by_posturl

当用户需要 Instagram 帖子评论、Instagram 评论、Instagram post comments、IG 帖子评论信息，与采集、抓取、爬取、获取、提取等动词组合时触发。提交 Instagram 帖子评论采集 Builder 任务，采集器标识固定为 ins_comment_by-posturl。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `instagram.com`
- spider_id: `ins_comment_by-posturl`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `posturl` | `posturl` | 否 | —(空) | 帖子 URL，该参数用于指定待采集的 Instagram 的帖子 URL。用于 ins_comment_by-posturl，默认值为 https://www.instagram.com/cats_of_instagram/reel/C4GLo_eLO2e/。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## ins_profiles_by_username

当用户需要 Instagram 个人资料、Instagram 用户资料、Instagram profile、Instagram 用户信息、IG 个人资料，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Instagram 个人资料采集 Builder 任务，支持 ins_profiles_by-username 和 ins_profiles_by-profileurl。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `instagram.com`
- spider_id: `ins_profiles_by-username`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `username` | `username` | 否 | —(空) | Instagram 用户名，该参数用于指定待采集的 Instagram 的用户名信息。用于 ins_profiles_by-username，默认值为 zoobarcelona。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## ins_profiles_by_profileurl

当用户需要 Instagram 个人资料、Instagram 用户资料、Instagram profile、Instagram 用户信息、IG 个人资料，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Instagram 个人资料采集 Builder 任务，支持 ins_profiles_by-username 和 ins_profiles_by-profileurl。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `instagram.com`
- spider_id: `ins_profiles_by-profileurl`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `profileurl` | `profileurl` | 否 | —(空) | 个人资料 URL，该参数用于指定待采集产品的个人资料访问 URL。用于 ins_profiles_by-profileurl，默认值为 https://www.instagram.com/cats_of_world_/。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## ins_reel_by_url

当用户需要 Instagram Reel 信息、Instagram Reels、Instagram 短视频、IG Reel，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Instagram Reel 信息采集 Builder 任务，支持 ins_reel_by-url、ins_allreel_by-url 和 ins_reel_by-listurl。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `instagram.com`
- spider_id: `ins_reel_by-url`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `url` | `url` | 否 | —(空) | URL，该参数用于指定待采集的 Instagram 的访问 URL 地址。ins_reel_by-url 默认值为 https://www.instagram.com/reel/C5Rdyj_q7YN/，ins_allreel_by-url 默认值为 https://www.instagram.com/billieeilish，ins_reel_by-listurl 默认值为 https://www.instagram.com/espn。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## ins_allreel_by_url

当用户需要 Instagram Reel 信息、Instagram Reels、Instagram 短视频、IG Reel，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Instagram Reel 信息采集 Builder 任务，支持 ins_reel_by-url、ins_allreel_by-url 和 ins_reel_by-listurl。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `instagram.com`
- spider_id: `ins_allreel_by-url`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## ins_reel_by_listurl

当用户需要 Instagram Reel 信息、Instagram Reels、Instagram 短视频、IG Reel，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Instagram Reel 信息采集 Builder 任务，支持 ins_reel_by-url、ins_allreel_by-url 和 ins_reel_by-listurl。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `instagram.com`
- spider_id: `ins_reel_by-listurl`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## linkedin_company_information_by_url

当用户需要 LinkedIn 公司信息、领英公司信息、LinkedIn company information、LinkedIn 公司 URL，与采集、抓取、爬取、获取、提取等动词组合时触发。提交 LinkedIn 公司信息采集 Builder 任务，采集器标识固定为 linkedin_company_information_by-url。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `linkedin.com`
- spider_id: `linkedin_company_information_by-url`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `url` | `url` | 否 | —(空) | 公司URL，该参数用于指定要采集的公司URL。用于 linkedin_company_information_by-url，默认值为 https://www.linkedin.com/company/dynamo-software。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## linkedin_job_listings_information_by_job_listing_url

当用户需要 LinkedIn 职位列表、领英职位列表、LinkedIn 招聘信息、领英招聘信息、LinkedIn job listings，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 LinkedIn 职位列表采集 Builder 任务，支持 linkedin_job_listings_information_by-job-listing-url、linkedin_job_listings_information_by-job-url 和 linkedin_job_listings_information_by-keyword。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `linkedin.com`
- spider_id: `linkedin_job_listings_information_by-job-listing-url`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `job_listing_url` | `job_listing_url` | 否 | —(空) | 职位列表URL，该参数用于指定要采集的职位列表URL。用于 linkedin_job_listings_information_by-job-listing-url，默认值为 https://www.linkedin.com/jobs/reddit-inc.-jobs-worldwide?f_C=150573。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## linkedin_job_listings_information_by_job_url

当用户需要 LinkedIn 职位列表、领英职位列表、LinkedIn 招聘信息、领英招聘信息、LinkedIn job listings，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 LinkedIn 职位列表采集 Builder 任务，支持 linkedin_job_listings_information_by-job-listing-url、linkedin_job_listings_information_by-job-url 和 linkedin_job_listings_information_by-keyword。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `linkedin.com`
- spider_id: `linkedin_job_listings_information_by-job-url`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `job_url` | `job_url` | 否 | —(空) | 职位URL，该参数用于指定要采集的职位URL。用于 linkedin_job_listings_information_by-job-url，默认值为文档提供的 LinkedIn 职位 URL。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## linkedin_job_listings_information_by_keyword

当用户需要 LinkedIn 职位列表、领英职位列表、LinkedIn 招聘信息、领英招聘信息、LinkedIn job listings，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 LinkedIn 职位列表采集 Builder 任务，支持 linkedin_job_listings_information_by-job-listing-url、linkedin_job_listings_information_by-job-url 和 linkedin_job_listings_information_by-keyword。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `linkedin.com`
- spider_id: `linkedin_job_listings_information_by-keyword`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `location` | `location` | 否 | `New York` | 职位位置，该参数用于指定通过特定位置搜索职位。用于 linkedin_job_listings_information_by-keyword，默认值为 New York。 |
| `keyword` | `keyword` | 否 | `product manager` | 关键词，该参数用于指定通过特定关键词搜索职位。用于 linkedin_job_listings_information_by-keyword，非必填，默认值为 product manager。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## reddit_comment_by_url

当用户需要 Reddit 帖子评论、Reddit 评论、Reddit post comments、Reddit 回复信息，与采集、抓取、爬取、获取、提取等动词组合时触发。提交 Reddit 帖子评论采集 Builder 任务，采集器标识固定为 reddit_comment_by-url。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `reddit.com`
- spider_id: `reddit_comment_by-url`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `url` | `url` | 否 | —(空) | Reddit URL，该参数用于指定采集 Reddit 帖子的 URL。用于 reddit_comment_by-url，默认值为 https://www.reddit.com/r/datascience/comments/1cmnf0m/comment/l32204i/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button。 |
| `days_back` | `days_back` | 否 | —(空) | 发布天数限制，该参数用于指定采集您输入的天数内发布的所有评论。默认值为 10。 |
| `comment_limit` | `comment_limit` | 否 | —(空) | 回复数量限制，该参数用于指定采集评论时返回的回复评论数量。默认值为 5。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## reddit_posts_by_url

当用户需要 Reddit 帖子信息、Reddit 帖子、Reddit posts、subreddit 帖子，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Reddit 帖子信息采集 Builder 任务，支持 reddit_posts_by-url、reddit_posts_by-keywords 和 reddit_posts_by-subredditurl。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `reddit.com`
- spider_id: `reddit_posts_by-url`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `url` | `url` | 否 | —(空) | Reddit URL 或 subreddit URL。reddit_posts_by-url 默认值为 https://www.reddit.com/r/battlefield2042/comments/1cmqs1d/official_update_on_the_next_battlefield_game/；reddit_posts_by-subredditurl 默认值为 https://www.reddit.com/r/battlefield2042。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## reddit_posts_by_keywords

当用户需要 Reddit 帖子信息、Reddit 帖子、Reddit posts、subreddit 帖子，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Reddit 帖子信息采集 Builder 任务，支持 reddit_posts_by-url、reddit_posts_by-keywords 和 reddit_posts_by-subredditurl。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `reddit.com`
- spider_id: `reddit_posts_by-keywords`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `keyword` | `keyword` | 否 | —(空) | Reddit 关键词，该参数用于指定采集 Reddit 帖子的搜索关键词。用于 reddit_posts_by-keywords，默认值为 datascience。 |
| `num_of_posts` | `num_of_posts` | 否 | —(空) | 最大帖子数，该参数用于指定采集帖子的最大数量。用于 reddit_posts_by-keywords 和 reddit_posts_by-subredditurl，默认值为 10。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## reddit_posts_by_subredditurl

当用户需要 Reddit 帖子信息、Reddit 帖子、Reddit posts、subreddit 帖子，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Reddit 帖子信息采集 Builder 任务，支持 reddit_posts_by-url、reddit_posts_by-keywords 和 reddit_posts_by-subredditurl。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `reddit.com`
- spider_id: `reddit_posts_by-subredditurl`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `url` | `url` | 否 | —(空) | Reddit URL 或 subreddit URL。reddit_posts_by-url 默认值为 https://www.reddit.com/r/battlefield2042/comments/1cmqs1d/official_update_on_the_next_battlefield_game/；reddit_posts_by-subredditurl 默认值为 https://www.reddit.com/r/battlefield2042。 |
| `sort_by` | `sort_by` | 否 | —(空) | 排序方式，该参数用于指定采集帖子的排序方式。用于 reddit_posts_by-subredditurl，可选值：Hot、Top、New、Rising，默认值为 Rising。 |
| `num_of_posts` | `num_of_posts` | 否 | —(空) | 最大帖子数，该参数用于指定采集帖子的最大数量。用于 reddit_posts_by-keywords 和 reddit_posts_by-subredditurl，默认值为 10。 |
| `sort_by_time` | `sort_by_time` | 否 | —(空) | 时间排序，该参数用于指定采集帖子的时间排序方式。用于 reddit_posts_by-subredditurl，可选值：Now、Today、This Week、This Month、This Year、All Time，默认值为 Now。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## tiktok_comment_by_url

当用户需要 TikTok 评论信息、Tiktok 评论信息、TikTok 帖子评论、Tiktok 视频评论、TikTok comment，与采集、抓取、爬取、获取、提取等动词组合时触发。提交 TikTok 评论信息采集 Builder 任务，采集器标识固定为 tiktok_comment_by-url。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `tiktok.com`
- spider_id: `tiktok_comment_by-url`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `url` | `url` | 否 | —(空) | TikTok 帖子 URL，该参数用于指定待采集的 TikTok 具体帖子网址。用于 tiktok_comment_by-url，默认值为 https://www.tiktok.com/@heymrcat/video/7216019547806092550。 |
| `page_turning` | `page_turning` | 否 | —(空) | 页数限制，该参数用于指定采集结果数量的限制（请输入页数）。用于 tiktok_comment_by-url，可选参数，默认值为 1。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## tiktok_posts_by_listurl

当用户需要 TikTok 帖子信息、Tiktok 帖子信息、TikTok 视频帖子、Tiktok 列表帖子、TikTok posts，与采集、抓取、爬取、获取、提取等动词组合时触发。提交 TikTok 帖子信息采集 Builder 任务，采集器标识固定为 tiktok_posts_by-listurl。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `tiktok.com`
- spider_id: `tiktok_posts_by-listurl`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `url` | `url` | 否 | —(空) | URL，此参数用于指定要获取的列表 URL。用于 tiktok_posts_by-listurl，默认值为 https://www.tiktok.com/discover/dog。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## tiktok_profiles_by_url

当用户需要 TikTok 个人资料信息、Tiktok 个人资料信息、TikTok 用户资料、Tiktok 创作者资料、TikTok profiles，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 TikTok 个人资料信息采集 Builder 任务，支持 tiktok_profiles_by-url 和 tiktok_profiles_by-listurl。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `tiktok.com`
- spider_id: `tiktok_profiles_by-url`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `url` | `url` | 否 | —(空) | TikTok 个人资料URL，该参数用于指定待采集的 TikTok 个人资料网址。用于 tiktok_profiles_by-url，默认值为 https://www.tiktok.com/@fofimdmell。 |
| `country` | `country` | 否 | —(空) | 国家，该参数用于指定要搜索的国家。接口按文档示例取值，默认值为 us。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## tiktok_profiles_by_listurl

当用户需要 TikTok 个人资料信息、Tiktok 个人资料信息、TikTok 用户资料、Tiktok 创作者资料、TikTok profiles，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 TikTok 个人资料信息采集 Builder 任务，支持 tiktok_profiles_by-url 和 tiktok_profiles_by-listurl。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `tiktok.com`
- spider_id: `tiktok_profiles_by-listurl`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `search_url` | `search_url` | 否 | —(空) | TikTok搜索URL，该参数用于指定待采集的 TikTok 搜索结果网址。用于 tiktok_profiles_by-listurl，默认值为 https://www.tiktok.com/explore?lang=en。 |
| `country` | `country` | 否 | —(空) | 国家，该参数用于指定要搜索的国家。接口按文档示例取值，默认值为 us。 |
| `page_turning` | `page_turning` | 否 | —(空) | 页数限制，该参数用于指定采集结果数量的限制（请输入页数）。用于 tiktok_profiles_by-listurl，默认值为 1。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## tiktok_shop_by_url

当用户需要 TikTok 商店信息、Tiktok 商店信息、TikTok Shop 信息、TikTok 店铺信息，与采集、抓取、爬取、获取、提取等动词组合时触发。提交 TikTok 商店信息采集 Builder 任务，采集器标识固定为 tiktok_shop_by-url。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `tiktok.com`
- spider_id: `tiktok_shop_by-url`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `url` | `url` | 否 | —(空) | TikTok商店URL，该参数用于指定待采集的 TikTok 商店网址。用于 tiktok_shop_by-url，默认值为 https://www.tiktok.com/shop/pdp/long-sleeve-crew-neck-tee-3-pack-by-galaxy-by-harvic-cotton-blend/1729461570693075200。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## twitter_post_by_profileurl

当用户需要 Twitter 帖子、Twitter(X) 帖子信息、X 帖子、X 平台帖子，与采集、抓取、爬取、获取、提取等动词组合时触发。Twitter 已更名为 X。提交 Twitter(X) 帖子信息采集 Builder 任务，采集器标识固定为 twitter_post_by-profileurl。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `x.com`
- spider_id: `twitter_post_by-profileurl`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `url` | `url` | 否 | —(空) | Twitter 个人资料 URL，该参数用于指定采集 Twitter 个人资料的 URL。用于 twitter_post_by-profileurl，默认值为 https://x.com/elonmusk。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## twitter_profile_by_profileurl

当用户需要 Twitter 个人资料、Twitter(X) 个人资料、X 个人资料、X 用户资料，与采集、抓取、爬取、获取、提取等动词组合时触发。Twitter 已更名为 X。复用一个工具提交 Twitter(X) 个人资料采集 Builder 任务，支持 twitter_profile_by-profileurl 和 twitter_profile_by-username。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `x.com`
- spider_id: `twitter_profile_by-profileurl`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `url` | `url` | 否 | —(空) | Twitter 个人资料 URL，该参数用于指定采集 Twitter 个人资料的 URL。用于 twitter_profile_by-profileurl，默认值为 https://x.com/elonmusk。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## twitter_profile_by_username

当用户需要 Twitter 个人资料、Twitter(X) 个人资料、X 个人资料、X 用户资料，与采集、抓取、爬取、获取、提取等动词组合时触发。Twitter 已更名为 X。复用一个工具提交 Twitter(X) 个人资料采集 Builder 任务，支持 twitter_profile_by-profileurl 和 twitter_profile_by-username。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `x.com`
- spider_id: `twitter_profile_by-username`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `user_name` | `user_name` | 否 | —(空) | Twitter 用户名，该参数用于指定待采集的 Twitter 的个人资料用户名。用于 twitter_profile_by-username，默认值为 elonmusk。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## walmart_product_by_url

当用户需要 Walmart 产品信息、Walmart 商品信息、Walmart 产品详情、Walmart 商品列表、Walmart product，与采集、抓取、爬取、获取、提取等动词组合时触发。从 walmart.com 提取商品列表、售价区间、品类分类、库存状态、配送方式、用户评价等数据。复用一个工具提交 Walmart 产品信息采集 Builder 任务，支持 walmart_product_by-url、walmart_product_by-category-url、walmart_product_by-sku 和 walmart_product_by-keywords。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `walmart.com`
- spider_id: `walmart_product_by-url`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `url` | `url` | 否 | —(空) | Walmart URL，该参数用于指定待采集的 Walmart 产品 URL。用于 walmart_product_by-url，默认值为 https://www.walmart.com/ip/HI-CHEW-Stand-Up-Pouch-Getaway-Mix-11-65oz/12284762931?athAsset=eyJhdGhjcGlkIjoiMTIyODQ3NjI5MzEiLCJhdGhzdGlkIjoiQ1MwNTV+Q1MwMDR+Q1MwOTgiLCJhdGhlZSI6eyJhIjoyNy44NCwiYiI6Mjk1MS40MSwidyI6MC4wMDk0MjcxMjc3OTA0NzcxMjMsImwiOjAuNX0sImF0aHBvc2IiOiI4IiwiYXRoYW5jaWQiOiIxMDE2NDUwNzU1IiwiYXRocmsiOjAuMH0%3D&athena=true&adsRedirect=true。 |
| `all_variations` | `all_variations` | 否 | — | 所有变体，该参数用于指定是否收集所有产品变量，设置为 true 为收集。参数值为 true 或 false；walmart_product_by-url 默认 true，其余采集器默认 false。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## walmart_product_by_category_url

当用户需要 Walmart 产品信息、Walmart 商品信息、Walmart 产品详情、Walmart 商品列表、Walmart product，与采集、抓取、爬取、获取、提取等动词组合时触发。从 walmart.com 提取商品列表、售价区间、品类分类、库存状态、配送方式、用户评价等数据。复用一个工具提交 Walmart 产品信息采集 Builder 任务，支持 walmart_product_by-url、walmart_product_by-category-url、walmart_product_by-sku 和 walmart_product_by-keywords。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `walmart.com`
- spider_id: `walmart_product_by-category-url`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `category_url` | `category_url` | 否 | —(空) | 类别URL，该参数用于指定 Walmart 的特定类别网址来查找新产品。用于 walmart_product_by-category-url，默认值为 https://www.walmart.com/shop/deals/food/。 |
| `all_variations` | `all_variations` | 否 | — | 所有变体，该参数用于指定是否收集所有产品变量，设置为 true 为收集。参数值为 true 或 false；walmart_product_by-url 默认 true，其余采集器默认 false。 |
| `page_turning` | `page_turning` | 否 | — | 页数限制，该参数用于指定采集结果数量的限制（请输入页数）。walmart_product_by-category-url 默认 1；walmart_product_by-keywords 默认 2。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## walmart_product_by_sku

当用户需要 Walmart 产品信息、Walmart 商品信息、Walmart 产品详情、Walmart 商品列表、Walmart product，与采集、抓取、爬取、获取、提取等动词组合时触发。从 walmart.com 提取商品列表、售价区间、品类分类、库存状态、配送方式、用户评价等数据。复用一个工具提交 Walmart 产品信息采集 Builder 任务，支持 walmart_product_by-url、walmart_product_by-category-url、walmart_product_by-sku 和 walmart_product_by-keywords。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `walmart.com`
- spider_id: `walmart_product_by-sku`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `sku` | `sku` | 否 | —(空) | SKU，该参数用于指定待采集的 SKU 产品唯一代码。用于 walmart_product_by-sku，默认值为 439179861。 |
| `all_variations` | `all_variations` | 否 | — | 所有变体，该参数用于指定是否收集所有产品变量，设置为 true 为收集。参数值为 true 或 false；walmart_product_by-url 默认 true，其余采集器默认 false。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## walmart_product_by_keywords

当用户需要 Walmart 产品信息、Walmart 商品信息、Walmart 产品详情、Walmart 商品列表、Walmart product，与采集、抓取、爬取、获取、提取等动词组合时触发。从 walmart.com 提取商品列表、售价区间、品类分类、库存状态、配送方式、用户评价等数据。复用一个工具提交 Walmart 产品信息采集 Builder 任务，支持 walmart_product_by-url、walmart_product_by-category-url、walmart_product_by-sku 和 walmart_product_by-keywords。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `walmart.com`
- spider_id: `walmart_product_by-keywords`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `keyword` | `keyword` | 否 | —(空) | 关键词，该参数用于指定采集的搜索关键词。用于 walmart_product_by-keywords，默认值为 leggins。 |
| `domain` | `domain` | 否 | —(空) | 主域名，该参数用于指定采集 Walmart 产品信息的主域名。用于 walmart_product_by-keywords，默认值为 https://www.walmart.com/。 |
| `all_variations` | `all_variations` | 否 | — | 所有变体，该参数用于指定是否收集所有产品变量，设置为 true 为收集。参数值为 true 或 false；walmart_product_by-url 默认 true，其余采集器默认 false。 |
| `page_turning` | `page_turning` | 否 | — | 页数限制，该参数用于指定采集结果数量的限制（请输入页数）。walmart_product_by-category-url 默认 1；walmart_product_by-keywords 默认 2。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## yandex_search

当用户需要通过 Yandex 搜索公开网页信息，或面向 Yandex 搜索场景按关键词、地区、语言等条件获取搜索结果时触发。

- 上游接口: Search Engine (`POST /request`)
- engine: `yandex`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `text` | Text | 否 | `pizza` | 该参数定义搜索查询，默认值为 pizza。您可以使用常规 Yandex 搜索中使用的任何内容。 |
| `json_` | JSON | 否 | `1` | 该参数定义采集结果的输出格式；可选择 JSON、HTML（支持下载）格式，默认为 JSON；1 返回 JSON，2 返回 JSON+HTML，3 返回 HTML，4 返回 Light JSON。 |
| `yandex_domain` | YandexDomain | 否 | `yandex.com` | 该参数定义要使用的 Yandex 域名。默认为 yandex.com。可用值：yandex.com、yandex.ru、ya.ru、yandex.by、yandex.kz、yandex.uz、yandex.com.tr、yandex.az、yandex.com.ge、yandex.com.am、yandex.co.il、yandex.md、yandex.tm、yandex.tj、yandex.eu。 |
| `lang` | Lang | 否 | `en` | 该参数定义 Yandex 搜索要使用的语言。当 yandex_domain 为 yandex.com 时，默认为 en。 |
| `lr` | LR | 否 | —(空) | 该参数定义将搜索结果限制在的国家或地区 ID。 |
| `p` | Page | 否 | `0` | 该参数定义页码。分页从 0 开始。 |
| `family_mode` | FamilyMode | 否 | `1` | 该参数启用或禁用家庭模式（安全搜索）。可设置为：0 - 关闭，1 - 中等，2 - 严格。默认为 1（中等）。 |
| `fix_typo` | FixTypo | 否 | `true` | 该参数启用或禁用自动拼写纠正。可设置为 true 或 false。默认为 true。 |
| `groups_on_page` | GroupsOnPage | 否 | `10` | 该参数定义单页结果上显示的最大群组数。默认为 10。 |
| `no_cache` | NoCache | 否 | `false` | 默认情况下，5 分钟内缓存相同参数的搜索结果；将 no_cache 设为 true 可跳过缓存，设为 false（默认）则使用缓存结果；缓存搜索免费，且不计入搜索统计。 |

## youtube_audio_by_url

当用户需要 YouTube 音频文件、YouTube 音频下载、YouTube audio file、音频文件，与采集、抓取、爬取、获取、提取、下载等动词组合时触发。提交 YouTube 音频文件采集 Builder 任务，采集器标识固定为 youtube_audio_by-url。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `youtube.com`
- spider_id: `youtube_audio_by-url`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `url` | `url` | 否 | —(空) | URLs，该参数用于指定待采集的访问 URL 地址。用于 youtube_audio_by-url，默认值为 https://www.youtube.com/watch?v=_SdpvpvVrLY。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## youtube_comment_by_id

当用户需要 YouTube 评论信息、YouTube 视频评论、YouTube 评论列表、YouTube comment、视频评论信息，与采集、抓取、爬取、获取、提取等动词组合时触发。提交 YouTube 评论信息采集 Builder 任务，采集器标识固定为 youtube_comment_by-id。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `youtube.com`
- spider_id: `youtube_comment_by-id`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `video_id` | `video_id` | 否 | `8RePenzQH80` | 视频唯一 ID，该参数用于指定待采集的 YouTube 视频的唯一 ID。用于 youtube_comment_by-id，默认值为 8RePenzQH80。 |
| `load_replies` | `load_replies` | 否 | `10` | 加载回复，该参数用于指定页面加载回复时用到的时间。用于 youtube_comment_by-id，默认值为 10。 |
| `num_of_comments` | `num_of_comments` | 否 | `10` | 评论数量，该参数用于指定需要采集的评论数量。用于 youtube_comment_by-id，默认值为 10。 |
| `sort_by` | `sort_by` | 否 | `Top comments` | 评论排序方式，该参数用于指定 YouTube 评论排序。用于 youtube_comment_by-id，可选值：Top comments、Newest first，默认值为 Top comments。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## youtube_product_by_id

当用户需要 YouTube 视频基本信息、YouTube 视频信息、YouTube 视频详情、YouTube product、视频基础资料，与采集、抓取、爬取、获取、提取等动词组合时触发。提交 YouTube 视频基本信息采集 Builder 任务，采集器标识固定为 youtube_product_by-id。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `youtube.com`
- spider_id: `youtube_product_by-id`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `video_id` | `video_id` | 否 | —(空) | 视频唯一 ID，该参数用于指定待采集的 YouTube 视频的唯一 ID。用于 youtube_product_by-id，默认值为 8RePenzQH80。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## youtube_profiles_by_keyword

当用户需要 YouTube 个人资料、YouTube 频道资料、YouTube 频道信息、YouTube profile、YouTube 用户信息，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 YouTube 个人资料采集 Builder 任务，支持 youtube_profiles_by-keyword 和 youtube_profiles_by-url。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `youtube.com`
- spider_id: `youtube_profiles_by-keyword`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `keyword` | `keyword` | 否 | `MrBeast` | YouTube 关键词，该参数用于指定 YouTube 频道进行搜索的关键字。用于 youtube_profiles_by-keyword，默认值为 MrBeast。 |
| `page_turning` | `page_turning` | 否 | `1` | 采集页数，请输入要采集多少页的产品。用于 youtube_profiles_by-keyword，默认值为 1。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## youtube_profiles_by_url

当用户需要 YouTube 个人资料、YouTube 频道资料、YouTube 频道信息、YouTube profile、YouTube 用户信息，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 YouTube 个人资料采集 Builder 任务，支持 youtube_profiles_by-keyword 和 youtube_profiles_by-url。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `youtube.com`
- spider_id: `youtube_profiles_by-url`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `url` | `url` | 否 | —(空) | 频道 URL，该参数用于指定待采集的 YouTube 频道的访问 URL 地址。用于 youtube_profiles_by-url，默认值为 https://www.youtube.com/@mrbeast。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## youtube_transcript_by_id

当用户需要 YouTube 字幕文件、YouTube 字幕、YouTube transcript、视频字幕、字幕下载，与采集、抓取、爬取、获取、提取、下载等动词组合时触发。提交 YouTube 字幕文件采集 Builder 任务，采集器标识固定为 youtube_transcript_by-id。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `youtube.com`
- spider_id: `youtube_transcript_by-id`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `video_id` | `video_id` | 否 | —(空) | 视频唯一 ID，该参数用于指定待采集的 YouTube 视频的唯一 ID。用于 youtube_transcript_by-id，默认值为 8RePenzQH80。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## youtube_video_by_url

当用户需要 YouTube 视频文件、YouTube 视频下载、YouTube video file、视频文件，与采集、抓取、爬取、获取、提取、下载等动词组合时触发。提交 YouTube 视频文件采集 Builder 任务，采集器标识固定为 youtube_video_by-url。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `youtube.com`
- spider_id: `youtube_video_by-url`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `url` | `url` | 否 | —(空) | URLs，该参数用于指定待采集的访问 URL 地址。用于 youtube_video_by-url，默认值为 https://www.youtube.com/watch?v=_SdpvpvVrLY。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## youtube_video_post_by_url

当用户需要 YouTube 视频帖子、YouTube 视频列表、YouTube 频道视频、YouTube 搜索视频、YouTube 话题标签视频、YouTube 播客视频、YouTube 探索视频，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 YouTube 视频帖子采集 Builder 任务，支持 youtube_video-post_by-url、youtube_video-post_by-search-filters、youtube_video-post_by-hashtag、youtube_video-post_by-podcast-url、youtube_video-post_by-keyword、youtube_video-post_by-explore。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `youtube.com`
- spider_id: `youtube_video-post_by-url`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `url` | `url` | 否 | —(空) | URL。用于频道 Video URL、播客 URL 或探索 URL；不同采集器未传时按文档默认 URL 提交。 |
| `order_by` | `order_by` | 否 | `Latest` | 排序方式。用于 youtube_video-post_by-url，可传 最新、热门、最旧，提交值为 Latest、Popular、Oldest；默认 Latest。 |
| `start_index` | `start_index` | 否 | `1` | 起始条数，该参数用于指定从第几条视频开始采集信息。用于 youtube_video-post_by-url，默认值为 1。 |
| `num_of_posts` | `num_of_posts` | 否 | —(空) | 帖子数量，此参数用于指定要采集的帖子数量。不同采集器按文档默认值提交。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## youtube_video_post_by_search_filters

当用户需要 YouTube 视频帖子、YouTube 视频列表、YouTube 频道视频、YouTube 搜索视频、YouTube 话题标签视频、YouTube 播客视频、YouTube 探索视频，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 YouTube 视频帖子采集 Builder 任务，支持 youtube_video-post_by-url、youtube_video-post_by-search-filters、youtube_video-post_by-hashtag、youtube_video-post_by-podcast-url、youtube_video-post_by-keyword、youtube_video-post_by-explore。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `youtube.com`
- spider_id: `youtube_video-post_by-search-filters`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `keyword_search` | `keyword_search` | 否 | `popular music` | 搜索关键词。用于 youtube_video-post_by-search-filters，默认值为 popular music。 |
| `features` | `features` | 否 | `All` | 特征。用于 youtube_video-post_by-search-filters，可传 All、全部、Live、4K、HD、Subtitles/CC、Creative Commons、360°、VR180、3D、HDR；默认 All。 |
| `type_` | type | 否 | `Video` | 类型。用于 youtube_video-post_by-search-filters，可选 Video、Movie，默认值为 Video。 |
| `duration` | `duration` | 否 | `Under 3 minutes` | 持续时间。用于 youtube_video-post_by-search-filters，可传 Under 3 minutes、4 分钟以内、4-20 分钟、20 分钟以上、全部；默认 Under 3 minutes。 |
| `upload_date` | `upload_date` | 否 | `上一小时` | 上传日期。用于 youtube_video-post_by-search-filters，可传 上一小时、今天、本周、本月、今年、全部；默认 上一小时。 |
| `num_of_posts` | `num_of_posts` | 否 | —(空) | 帖子数量，此参数用于指定要采集的帖子数量。不同采集器按文档默认值提交。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## youtube_video_post_by_hashtag

当用户需要 YouTube 视频帖子、YouTube 视频列表、YouTube 频道视频、YouTube 搜索视频、YouTube 话题标签视频、YouTube 播客视频、YouTube 探索视频，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 YouTube 视频帖子采集 Builder 任务，支持 youtube_video-post_by-url、youtube_video-post_by-search-filters、youtube_video-post_by-hashtag、youtube_video-post_by-podcast-url、youtube_video-post_by-keyword、youtube_video-post_by-explore。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `youtube.com`
- spider_id: `youtube_video-post_by-hashtag`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `hashtag` | `hashtag` | 否 | `shopping` | 话题标签，按标签筛选视频，请参考 https://www.youtube.com/hashtag。用于 youtube_video-post_by-hashtag，默认值为 shopping。 |
| `num_of_posts` | `num_of_posts` | 否 | —(空) | 帖子数量，此参数用于指定要采集的帖子数量。不同采集器按文档默认值提交。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## youtube_video_post_by_podcast_url

当用户需要 YouTube 视频帖子、YouTube 视频列表、YouTube 频道视频、YouTube 搜索视频、YouTube 话题标签视频、YouTube 播客视频、YouTube 探索视频，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 YouTube 视频帖子采集 Builder 任务，支持 youtube_video-post_by-url、youtube_video-post_by-search-filters、youtube_video-post_by-hashtag、youtube_video-post_by-podcast-url、youtube_video-post_by-keyword、youtube_video-post_by-explore。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `youtube.com`
- spider_id: `youtube_video-post_by-podcast-url`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `url` | `url` | 否 | —(空) | URL。用于频道 Video URL、播客 URL 或探索 URL；不同采集器未传时按文档默认 URL 提交。 |
| `num_of_posts` | `num_of_posts` | 否 | —(空) | 帖子数量，此参数用于指定要采集的帖子数量。不同采集器按文档默认值提交。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## youtube_video_post_by_keyword

当用户需要 YouTube 视频帖子、YouTube 视频列表、YouTube 频道视频、YouTube 搜索视频、YouTube 话题标签视频、YouTube 播客视频、YouTube 探索视频，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 YouTube 视频帖子采集 Builder 任务，支持 youtube_video-post_by-url、youtube_video-post_by-search-filters、youtube_video-post_by-hashtag、youtube_video-post_by-podcast-url、youtube_video-post_by-keyword、youtube_video-post_by-explore。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `youtube.com`
- spider_id: `youtube_video-post_by-keyword`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `keyword` | `keyword` | 否 | `top videos` | 关键词。用于 youtube_video-post_by-keyword，默认值为 top videos。 |
| `num_of_posts` | `num_of_posts` | 否 | —(空) | 帖子数量，此参数用于指定要采集的帖子数量。不同采集器按文档默认值提交。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## youtube_video_post_by_explore

当用户需要 YouTube 视频帖子、YouTube 视频列表、YouTube 频道视频、YouTube 搜索视频、YouTube 话题标签视频、YouTube 播客视频、YouTube 探索视频，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 YouTube 视频帖子采集 Builder 任务，支持 youtube_video-post_by-url、youtube_video-post_by-search-filters、youtube_video-post_by-hashtag、youtube_video-post_by-podcast-url、youtube_video-post_by-keyword、youtube_video-post_by-explore。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `youtube.com`
- spider_id: `youtube_video-post_by-explore`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `url` | `url` | 否 | —(空) | URL。用于频道 Video URL、播客 URL 或探索 URL；不同采集器未传时按文档默认 URL 提交。 |
| `all_tabs` | `all_tabs` | 否 | —(空) | 所有标签页。用于 youtube_video-post_by-explore，参数值为 true 或 false，默认 true。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

## zillow_product_by_filter

当用户需要 Zillow 房产信息、Zillow 房产详细信息、Zillow 房源信息、Zillow property details，与采集、抓取、爬取、获取、提取等动词组合时触发。提交 Zillow 房产详细信息采集 Builder 任务，采集器标识固定为 zillow_product_by-filter。

- 上游接口: Scraper Builder (`POST /builder?platform=1`)
- spider_name: `zillow.com`
- spider_id: `zillow_product_by-filter`

| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `keywords_location` | keywords-location | 否 | —(空) | 地点关键词，该参数用于指定 Zillow 搜索页面的搜索地址信息，可以是邮政编码、具体城市或地址。用于 zillow_product_by-filter，默认值为 South Bend。 |
| `listingCategory` | `listingCategory` | 否 | —(空) | 列表类别，该参数用于指定 Zillow 搜索房产类别的参数。可选值：Sold、For Rent、For Sale。默认值为 For Rent。 |
| `HomeType` | `HomeType` | 否 | —(空) | 主页类型，该参数用于指定 Zillow 搜索房产主页类型的参数。可选值：Houses、Townhomes、Multi-family、Condos/Co-ops、Lots/Land、Apartments、Manufactured。默认值为 Houses。 |
| `days_on_zillow` | `days_on_zillow` | 否 | —(空) | 在zillow上的日子，该参数用于指定采集发布在 Zillow 网站多久时长的房屋。可选值：Any、1 day、7 days、14 days、30 days、90 days、6 months、12 months、24 months、36 months。默认值为 Any。 |
| `maximum` | `maximum` | 否 | —(空) | 最大数量，该参数用于指定采集的最大数量。默认值为 10。 |
| `file_name` | `file_name` | 否 | `{{TasksID}}` | Builder file_name 字段。不传默认为 {{TasksID}}。 |

