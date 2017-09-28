Prerequisites
-------------

Before you install and configure the chehn service,
you must create a database, service credentials, and API endpoints.

#. To create the database, complete these steps:

   * Use the database access client to connect to the database
     server as the ``root`` user:

     .. code-block:: console

        $ mysql -u root -p

   * Create the ``yangtest`` database:

     .. code-block:: none

        CREATE DATABASE yangtest;

   * Grant proper access to the ``yangtest`` database:

     .. code-block:: none

        GRANT ALL PRIVILEGES ON yangtest.* TO 'yangtest'@'localhost' \
          IDENTIFIED BY 'YANGTEST_DBPASS';
        GRANT ALL PRIVILEGES ON yangtest.* TO 'yangtest'@'%' \
          IDENTIFIED BY 'YANGTEST_DBPASS';

     Replace ``YANGTEST_DBPASS`` with a suitable password.

   * Exit the database access client.

     .. code-block:: none

        exit;

#. Source the ``admin`` credentials to gain access to
   admin-only CLI commands:

   .. code-block:: console

      $ . admin-openrc

#. To create the service credentials, complete these steps:

   * Create the ``yangtest`` user:

     .. code-block:: console

        $ openstack user create --domain default --password-prompt yangtest

   * Add the ``admin`` role to the ``yangtest`` user:

     .. code-block:: console

        $ openstack role add --project service --user yangtest admin

   * Create the yangtest service entities:

     .. code-block:: console

        $ openstack service create --name yangtest --description "chehn" chehn

#. Create the chehn service API endpoints:

   .. code-block:: console

      $ openstack endpoint create --region RegionOne \
        chehn public http://controller:XXXX/vY/%\(tenant_id\)s
      $ openstack endpoint create --region RegionOne \
        chehn internal http://controller:XXXX/vY/%\(tenant_id\)s
      $ openstack endpoint create --region RegionOne \
        chehn admin http://controller:XXXX/vY/%\(tenant_id\)s
