FROM joyzoursky/python-chromedriver:3.8
WORKDIR /app
COPY requirements.txt .
RUN python -m pip --no-cache-dir install --requirement requirements.txt && rm requirements.txt
COPY . .
