FROM python:3.12.3

WORKDIR /app/TG_BOT_CJ

COPY /TG_BOT_CJ/requirements.txt /app/TG_BOT_CJ
RUN pip install --no-cache-dir -r requirements.txt 

COPY . .

CMD ["python", "bot.py"]