2. Edit the ``/etc/yangtest/yangtest.conf`` file and complete the following
   actions:

   * In the ``[database]`` section, configure database access:

     .. code-block:: ini

        [database]
        ...
        connection = mysql+pymysql://yangtest:YANGTEST_DBPASS@controller/yangtest
