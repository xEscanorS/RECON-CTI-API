FROM python:3

WORKDIR /projeto/cti

COPY . .

COPY requirements.txt /projeto/cti

RUN pip3 install --no-cache-dir -r requirements.txt

RUN chmod +x ./projeto/cti/cti_script.sh

CMD ["./projeto/cti/cti_script.sh"]
