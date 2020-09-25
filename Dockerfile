FROM centos

RUN yum install sudo -y
RUN yum install java-11-openjdk.x86_64 -y
RUN yum install wget -y
RUN yum install git -y
RUN yum install vim -y 
RUN wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo
RUN sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key
RUN yum install jenkins -y
RUN echo -e "jenkins ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
RUN yum install /sbin/service -y
CMD sudo service jenkins start -DEFOREGROUND && /bin/bash
EXPOSE 8080


RUN yum install python36 -y
RUN yum install  https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm -y
RUN yum update -y
RUN yum install net-tools -y
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
RUN python3 get-pip.py

RUN pip install setuptools
RUN pip install scikit-learn
RUN pip install matplotlib
RUN pip install seaborn
RUN pip install pandas
RUN pip install numpy
RUN pip install DateTime
RUN pip install Flask


