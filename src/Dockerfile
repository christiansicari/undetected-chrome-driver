FROM ultrafunk/undetected-chromedriver
WORKDIR /app
COPY app/ .
RUN pip3 install -r requirements.txt
EXPOSE 3389
CMD ["python3", "/app/main.py"]