# MySQL Dependencies Installation Guide

## Install MySQLdb Module

### Install MySQL connector and client via pip:
```bash
pip install mysql-connector-python-rf mysqlclient
```

If the above command fails, install the required dependencies:

**On Debian/Ubuntu:**
```bash
apt-get install default-libmysqlclient-dev
```

**On CentOS/RedHat:**
```bash
yum install mysql-devel gcc gcc-devel python-devel
```
