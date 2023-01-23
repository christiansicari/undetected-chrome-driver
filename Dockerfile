FROM ultrafunk/undetected-chromedriver
WORKDIR /app
COPY src/ .
COPY requirements.txt /app
RUN pip3 install -r requirements.txt
EXPOSE 3389
CMD ["python3", "/app/main.py"]