az sql server create -l northeurope -g sqlRG -n testsqlsvr01 -u azure -p test1234 -e false
az sql db create -g sqlRG -s testsqlsrv01 -n testsqldb01 -e GeneralPurpose -f Gen5 -c 2
