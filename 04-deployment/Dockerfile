FROM agrigorev/zoomcamp-model:mlops-2024-3.10.13-slim

RUN pip install pandas scikit-learn==1.5.0 numpy==2.0.0 pyarrow

WORKDIR /app

ADD starter.py .

ENTRYPOINT ["python","./starter.py"]

CMD [ "2023", "4" ]