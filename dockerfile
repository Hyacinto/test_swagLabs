FROM python:3.10-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    firefox-esr \
    wget \
    xvfb \
    libx11-6 \
    libx11-xcb1 \
    libxcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libxi6 \
    libxrandr2 \
    libxrender1 \
    libxtst6 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives

RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.35.0/geckodriver-v0.35.0-linux64.tar.gz \
    && tar -xvzf geckodriver-v0.35.0-linux64.tar.gz \
    && mv geckodriver /usr/local/bin/ \
    && rm geckodriver-v0.35.0-linux64.tar.gz

RUN apt-get update && apt-get install -y --no-install-recommends \
    openjdk-17-jre-headless \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/allure-framework/allure2/releases/download/2.22.0/allure-2.22.0.tgz \
    && tar -xvzf allure-2.22.0.tgz -C /opt/ \
    && ln -s /opt/allure-2.22.0/bin/allure /usr/local/bin/allure \
    && rm allure-2.22.0.tgz


WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x ./run_tests.sh

CMD ["./run_tests.sh"]
