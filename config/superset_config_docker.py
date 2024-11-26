#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

#
# This is an example "local" configuration file. In order to set/override config
# options that ONLY apply to your local environment, simply copy/rename this file
# to docker/pythonpath_dev/superset_config_docker.py
# It ends up being imported by docker/superset_config.py which is loaded by
# superset/config.py
#
import os
from datetime import timedelta
from superset.tasks.types import ExecutorType
from superset.superset_typing import CacheConfig

# Customization Configuration
SECRET_KEY = os.getenv("SECRET_KEY")
APP_NAME = os.getenv("APP_NAME")
APP_ICON = "/static/assets/images/custom-logo.png"
FAVICONS = [{"href": "/app/superset/static/assets/images/custom-favicon.png"}]
LOGO_TARGET_PATH = '/' # Setting it to '/' would take the user to '/superset/welcome/'
LOGO_RIGHT_TEXT = os.getenv("LOGO_RIGHT_TEXT") # Specify any text that should appear to the right of the logo

# Email configuration
SMTP_HOST = os.getenv("SMTP_HOST") # change to your host
SMTP_PORT = os.getenv("SMTP_PORT") # your port, e.g. 587
SMTP_STARTTLS = True
SMTP_SSL_SERVER_AUTH = True # If your using an SMTP server with a valid certificate
SMTP_SSL = False
SMTP_USER = os.getenv("SMTP_USER") # use the empty string "" if using an unauthenticated SMTP server
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD") # use the empty string "" if using an unauthenticated SMTP server
SMTP_MAIL_FROM = os.getenv("SMTP_MAIL_FROM")
ENABLE_PROXY_FIX = True

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = os.getenv("REDIS_PORT", "6379")
REDIS_CELERY_DB = os.getenv("REDIS_CELERY_DB", "0")
REDIS_RESULTS_DB = os.getenv("REDIS_RESULTS_DB", "1")

# Features Configuration
SCREENSHOT_LOCATE_WAIT = 10
SCREENSHOT_LOAD_WAIT = 60
FEATURE_FLAGS = {
    "ALERT_REPORTS": True,
    "THUMBNAILS": True,
    "SCHEDULED_REPORTS": True,
    "THUMBNAILS_SQLA_LISTENERS": True,
    "DASHBOARD_VIRTUALIZATION": True,
}


# Thumbnail Configuration
THUMBNAIL_SELENIUM_USER = "admin"
THUMBNAIL_EXECUTE_AS = [ExecutorType.SELENIUM]

THUMBNAIL_CACHE_CONFIG: CacheConfig = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_DEFAULT_TIMEOUT': 7 * 86400,  # 7 days
    'CACHE_KEY_PREFIX': 'thumbnail_',
    'CACHE_REDIS_HOST': REDIS_HOST,
    'CACHE_REDIS_PORT': REDIS_PORT,
    'CACHE_REDIS_DB': REDIS_CELERY_DB
}

ALERT_REPORTS_NOTIFICATION_DRY_RUN = False
ALERT_MINIMUM_INTERVAL = int(timedelta(minutes=10).total_seconds())
REPORT_MINIMUM_INTERVAL = int(timedelta(minutes=5).total_seconds())
WEBDRIVER_BASEURL = "http://superset_app:8088/"  # When using docker compose baseurl should be http://superset_app:8088/
WEBDRIVER_BASEURL_USER_FRIENDLY = os.getenv("WEBDRIVER_BASEURL_USER_FRIENDLY") # The base URL for the email report hyperlinks.
WEBDRIVER_TYPE = "firefox"
FILTER_STATE_CACHE_CONFIG = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_DEFAULT_TIMEOUT': 86400,
    'CACHE_KEY_PREFIX': 'superset_filter_cache',
    'CACHE_REDIS_URL': 'redis://localhost:6379/0'
}
