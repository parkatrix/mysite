from django.shortcuts import render, get_object_or_404
from .models import Instance
from .tools import getinstance, loadinstance
import pymysql

# Create your views here.
#최초 실행시 인스턴스 초기화(KICDB와 인터페이스)
getinstance()
Instance.objects.all().delete()
insts = loadinstance()

for inst in insts:
    Instance.objects.create(
        instancename=inst[1],
        servername=inst[0],
        ipaddr=inst[3],
        port=inst[4],
    )

def dbcheck_main(request):

    for inst in Instance.objects.all() :
        try:
            sql = "show slave status"
            '''sql = "select round(sum(data_length + index_length)/1024/1024/1024) as Gb from information_schema.tables"'''
            conn = pymysql.connect(host=str(inst.ipaddr), port=int(inst.port), user='kic', password='dhtkak', db='mysql',charset='utf8')
            curs = conn.cursor()
            slavestatus = curs.execute(sql)

        except Exception as e:
            inst.ms = e
            inst.save()
            pass

        else:
            if(slavestatus) :
                inst.ms=curs.fetchall()
                inst.save()
            else:
                inst.ms='Master'
                inst.save()

    instancelist=Instance.objects.order_by('instancename')
    return render(request, 'dbcheck/dbcheck_main.html',{'Instancelist':instancelist})


def instdetail(request,pk) :

    inst = get_object_or_404(Instance,pk=pk)
    sql = "select * from information_schema.global_variables order by variable_name;"
    conn = pymysql.connect(host=str(inst.ipaddr), port=int(inst.port), user='kic', password='dhtkak', db='mysql',
                           charset='utf8')
    curs = conn.cursor()
    curs.execute(sql)
    globalvar=curs.fetchall()

    return render(request, 'dbcheck/instdetail.html', {'globalvar' : globalvar, 'inst' : inst})



