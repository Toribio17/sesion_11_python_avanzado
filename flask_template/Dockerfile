#FROM python:3.11
FROM centos:7
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV NODE_OPTIONS="--max-old-space-size=8192"
ENV PYTHONWARNINGS="ignore:Unverified HTTPS request"
ENV TESSDATA_PREFIX="/data_code/tesseract-4.0.0/tessdata"
ENV OUTPUT_RESULTS_PATH="services/ocr/files_to_implement/output_files"
ENV FILES_INPUT_PATH="services/ocr/files_to_implement/input_files"
ENV ENVIRONMENT="deveploment"
ENV GENERAL_PATH="/data_code/app"
ENV MONGO_CONNECTION="mongodb://localhost:27017"
ENV CLOUDANT_APIKEY="I1RHAJOe4uopBnSZht_0tgM6GS5_usZ28oeGyhWuyk_H"
ENV CLOUDANT_URL="https://03bbdcd2-aa12-41b0-9268-c568156f8bef-bluemix.cloudantnosqldb.appdomain.cloud"
ENV JWT_KEY="PythonAvanzadoClass"
ENV COS_ENDPOINT="https://s3.us-south.objectstorage.softlayer.net"
ENV BUCKET_NAME="bucket-python-avanzado"
ENV PATH_OBJECT_STORAGE="services/object_storage/folder_files"
ENV AWS_ACCESS_KEY_ID="02e5bcc516eb4a52b6dbe3fd9764ba9d"
ENV AWS_SECRET_ACCESS_KEY="21cc369e2148cde56d59fdc27328ff827c37d77ca29356ac"
ENV REGION_OBJECT="us-south"
ENV NEO4J_USER_NAME="pythonAvanzado"
ENV NEO4J_PASSWORD="python12345678"
ENV NEO4J_HOST="bolt://localhost:7687"
ENV NEO4J_DATABASE="pythonavanzadodb"
ENV JWT_TOKEN_PASSWORD="PythonAvanzado1"
ENV JWT_TOKEN_PASSWORD_ENCRYPTED="1d1ab271f8adf31e820eb7ca037fc65f6dcadb677ef686c77b6d57885290ae2a"

USER root
RUN mkdir /data_code
WORKDIR /data_code
#nos permite añadir grupos al sistema
RUN groupadd -r discovery
#
RUN useradd --no-log-init -r -g discovery discoveryuser
RUN chown -R discoveryuser /data_code
#install gcc 
RUN yum install gcc -y
RUN yum groupinstall 'development tools' -y

#Leptonica 
RUN yum install make -y
RUN yum install wget -y
RUN yum install  zlib-devel -y
RUN yum install glib2-devel -y
RUN yum install libpng-devel -y
RUN yum install libjpeg-devel -y 
RUN yum install libtiff-devel -y 
RUN yum install libwebp-devel -y 
RUN wget http://www.leptonica.org/source/leptonica-1.79.0.tar.gz
RUN tar -zxvf leptonica-1.79.0.tar.gz
RUN cd leptonica-1.79.0 && ./configure --prefix=/usr/local --disable-shared --enable-static --with-zlib --with-jpeg --with-libwebp  --with-libtiff --with-libpng
RUN cd leptonica-1.79.0 && make
RUN cd leptonica-1.79.0 && make install
RUN cp /usr/local/lib/pkgconfig/lept.pc /usr/lib64/pkgconfig

#pytesseract
RUN yum install automake autoconf libtool -y
RUN wget https://github.com/tesseract-ocr/tesseract/archive/4.0.0.tar.gz -O tesseract-4.0.0.tar.gz
RUN tar zxvf tesseract-4.0.0.tar.gz
RUN chmod -R 777  /data_code/tesseract-4.0.0
RUN export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig
RUN cd tesseract-4.0.0/ && ./autogen.sh 
RUN cd tesseract-4.0.0/ && ./configure --prefix=/usr/local --disable-shared --enable-static --with-extra-libraries=/usr/local/lib/ --with-extra-includes=/usr/local/lib/
RUN cd tesseract-4.0.0/ && make
RUN cd tesseract-4.0.0/ && make install
RUN cd tesseract-4.0.0/ && ldconfig


#pdf2image libraries
RUN yum install poppler-utils -y
COPY eng.traineddata /data_code/tesseract-4.0.0/tessdata/

RUN yum install python3-pip -y
RUN pip3 install -U pip setuptools wheel
COPY . /data_code

RUN pip3 install -r /data_code/requirements.txt
RUN ldconfig

EXPOSE 27017
EXPOSE 5003

CMD ["sh","./gunicorn.sh"] 
