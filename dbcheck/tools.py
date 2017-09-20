import cx_Oracle
import pymysql
import csv

def loadinstance() :
    instancelist = []
    f = open('./dbcheck/instance1.csv','r')
    csvReader= csv.reader(f)

    for row in csvReader :
        instancelist.append(row)
    f.close()

    return instancelist


def getinstance() :

    print("Getting instance list from KICDB..")

    con = cx_Oracle.connect('kic','dhtkak','KICDB')
    cursor = con.cursor()
    sql = "SELECT SERVER, SID, OPERATION, DB_IP_ADDRESS,LSNR_PORT,SYSTEM_NAME " \
          "FROM KICDB.TB_DB_LIST " \
          "WHERE OPERATION IN ('PROD','TEST') " \
          "AND DB_PRODUCT = 'MariaDB' " \
          "order by server"
    rows = cursor.execute(sql)

    f = open('./dbcheck/instance1.csv','w')

    for row in rows :
        for col in row :
           f.write(str(col))
           f.write(",")
        f.write("\n")

    print("Complete!!")


def slavecheck(instancelist) :

    f = open('slavelist.csv','w')

    for inst in instancelist :
        # print(inst)
        sql = "show slave status"
        try :
            conn = pymysql.connect(host=str(inst[3]),port=int(inst[4]), user='kic', password='dhtkak', db='mysql', charset='utf8')
            curs = conn.cursor()
            slavestatus = curs.execute(sql)
            if(slavestatus) :
                print('servername : %12s     instancename : %7s is Slave ' %(inst[0], inst[1]) )
                res=curs.fetchall()
                print(res)
                f.write(inst[0] + '\t' + inst[1] + '\t' + 'S' + res +  '\n')
            # print(curs.fetchone())
            conn.close()
        except :
            f.write(inst[0] + '\t' + inst[1] + '\t' + 'M' + '\n')
            pass

def queryexecute(instancelist) :

    servername = input("수행할 서버명을 입력하세요 : ")
    query = input("쿼리를 입력하세요 : ")

    target={'servername' :'', 'ipaddr' : '', 'port' : ''}
    target['servername']=servername

    for instance in instancelist :
        if(instance[0]==servername) :
            target['ipaddr']=instance[3]
            target['port']=instance[4]
            break

    if(target['ipaddr'] == '') :
        print("servername error!")
        return

    print(query)
    print(target)

    con = pymysql.connect(host=str(target['ipaddr']),port=int(target['port']), user='kic', password='dhtkak', db='mysql', charset='utf8')
    cursor = con.cursor()
    sql = query

    cursor.execute(sql)
    rows = cursor.fetchall()

    con.close()

    return rows

def printresult(res) :
    for row in res:
        for val in row :
            print('{0:20s}'.format(str(val)), end='   ')
        print()

    return
