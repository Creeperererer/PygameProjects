import rpa as r
import tagui as t

r.init()
r.url('https://www.google.com')
r.type('//*[@name="q"]', '治疗脑瘫的方法[enter]')
print(r.read('result-stats'))
r.snap('page', 'results.png')
r.close()