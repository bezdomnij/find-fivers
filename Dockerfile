FROM python:3.12.4-alpine
LABEL authors="frank"

#ENTRYPOINT ["top", "-b"]

#useradd --create-home --shell /bin/bash app_user
#WORKDIR /home/app_user
#VOLUME /app/findfivers/data
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
#chown -R app_user:app_user /findfivers
#USER app_user
CMD ["sh"]
