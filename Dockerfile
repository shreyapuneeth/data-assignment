# set base image (host OS)
FROM python
COPY /src/test_subscriber.py . 
CMD ["python", "test_subscriber.py"]  