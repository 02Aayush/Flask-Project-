import mysql.connector as sql
class DBManager:
    def __init__(self):
        self.conn=sql.connect(database="ccitdb",user="root",password="admin")

    def getAccList(self):
        cmd="select * from accmaster"
        cur=self.conn.cursor()
        cur.execute(cmd)
        lst=cur.fetchall()
        return lst

    def addAcc(self,nm,bl):
        cmd="select max(accno) from accmaster"
        cur=self.conn.cursor()
        cur.execute(cmd)
        rec=cur.fetchone()
        an=rec[0]+1
        cmd="insert into accmaster values(%s,%s,%s)"
        cur=self.conn.cursor()
        cur.execute(cmd,[an,nm,bl])
        self.conn.commit()
        return an

    def closeAcc(self,an):
        cmd="delete from accmaster where accno=%s"
        cur=self.conn.cursor()
        cur.execute(cmd,[an])
        self.conn.commit()
        return

    def search(self,nm):
        cmd="select * from accmaster where name like '%"+nm+"%'"
        cur=self.conn.cursor()
        cur.execute(cmd)
        lst=cur.fetchall()
        return  lst

    def accInfo(self,an):
        cmd="select * from accmaster where accno=%s"
        cur=self.conn.cursor()
        cur.execute(cmd,[an])
        rec=cur.fetchone()
        return rec

    def deposit(self,an,amt):
        cmd="update accmaster set balance=balance + %s where accno=%s"
        cur=self.conn.cursor()
        cur.execute(cmd,[amt,an])
        self.conn.commit()
        return

    def withdraw(self,an,amt):
        cmd="update accmaster set balance=balance - %s where accno=%s"
        cur=self.conn.cursor()
        cur.execute(cmd,[amt,an])
        self.conn.commit()
        return