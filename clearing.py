from os import path, walk, remove
from time import ctime, time as now

def bak (days=60, direction='bak'):
    if int(days) < 10:
        confirm = input ('Срок давности меньше 10 дней, подтверждаете? ')
        if not any (confirm.lower() in var for var in
                    ('yes', 'yeah', 'да', 'верно')):
            return False
    
    date = now() - days * 24 * 60 * 60
    log = open (direction+'/deleted.log', 'a')
    log.write(ctime(now())+',\t'+str(days)+'\n'+
                  '------------------------\n')
    count = 0
    for name, dirs, files in walk(direction):
        for file in files:
            last = path.getatime(direction+'/'+file)
            if (last < date and file[-4:]=='.bak'):
                try:
                    remove(direction+'/'+file)
                except Exception:
                    log.write('\t'+"wasn't removed:\n"+
                                  '\t'+file+'\t'+ctime(last)+'\n')
                else:
                    log.write('\t'+file+'\t'+ctime(last)+'\n')
                    count += 1
    log.write('\n')
    log.close()
    return count

if __name__ == '__main__':
    days = input ('Введите максимальную давность файлов: ')
    bak(days)
