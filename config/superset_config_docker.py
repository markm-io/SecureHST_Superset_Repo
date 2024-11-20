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

# Customization Configuration
SECRET_KEY = os.getenv("SECRET_KEY")
APP_NAME = os.getenv("APP_NAME")
APP_ICON = "/static/assets/images/custom-logo.png"
FAVICONS = [{"href": "/app/superset/static/assets/images/custom-favicon.png"}]
# Setting it to '/' would take the user to '/superset/welcome/'
LOGO_TARGET_PATH = '/'
# Specify any text that should appear to the right of the logo
LOGO_RIGHT_TEXT = os.getenv("LOGO_RIGHT_TEXT")
# Email configuration
SMTP_HOST = os.getenv("SMTP_HOST") # change to your host
SMTP_PORT = os.getenv("SMTP_PORT") # your port, e.g. 587
SMTP_STARTTLS = True
SMTP_SSL_SERVER_AUTH = True # If your using an SMTP server with a valid certificate
SMTP_SSL = False
SMTP_USER = os.getenv("SMTP_USER") # use the empty string "" if using an unauthenticated SMTP server
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD") # use the empty string "" if using an unauthenticated SMTP server
SMTP_MAIL_FROM = os.getenv("SMTP_MAIL_FROM")

# Features Configuration
SCREENSHOT_LOCATE_WAIT = 10
SCREENSHOT_LOAD_WAIT = 60
FEATURE_FLAGS = {
    "ALERT_REPORTS": True,
    "THUMBNAILS": True,
    "SCHEDULED_REPORTS": True
}
ALERT_REPORTS_NOTIFICATION_DRY_RUN = False
ALERT_MINIMUM_INTERVAL = int(timedelta(minutes=10).total_seconds())
REPORT_MINIMUM_INTERVAL = int(timedelta(minutes=5).total_seconds())
WEBDRIVER_TYPE = "chrome"
WEBDRIVER_OPTION_ARGS = [
    "--force-device-scale-factor=2.0",
    "--high-dpi-support=2.0",
    "--headless",
    "--disable-gpu",
    "--disable-dev-shm-usage",
    "--no-sandbox",
    "--disable-setuid-sandbox",
    "--disable-extensions",
]
