FROM python:3.7-slim

ENV PYPI_MIRROR=https://pypi.tuna.tsinghua.edu.cn/simple
ENV TZ=Asia/Shanghai

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

#RUN pip install pandas==0.24.2 requests==2.21.0 schedule==0.6.0 -i $PYPI_MIRROR

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN pip install -r requirements.txt -i $PYPI_MIRROR

CMD ["python", "./Runner/run_all.py"]
