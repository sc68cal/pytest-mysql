"""Tests main conftest file."""
from pytest_mysql.executor import MySQLExecutor
from pytest_mysql.plugin import *
from pytest_mysql import factories


# pylint:disable=invalid-name
mysql_proc2 = factories.mysql_proc(port=3308)
mysql2 = factories.mysql("mysql_proc2", dbname="test-db")
mysql_rand_proc = factories.mysql_proc(port=None)
mysql_rand = factories.mysql("mysql_rand_proc")
# pylint:enable=invalid-name
