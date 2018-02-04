# -*- coding: utf-8 -*-
#!/usr/bin/python

import urllib
import urllib2
import re
import thread
import time
from subprocess import call

number = 0
update_page11_ck = ''
update_page_1_ck = ''
update_page22_ck = ''
update_page_2_ck = ''
update_page33_ck = ''
update_page_3_ck = ''
update_page44_ck = ''
update_page_4_ck = ''
update_page55_ck = ''
update_page_5_ck = ''
update_page66_ck = ''
update_page_6_ck = ''

def gpflash( str_url,zh_name,n):
	url = str_url
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	headers = { 'User-Agent' : user_agent }
	req = urllib2.Request(url, headers = headers)
	response = urllib2.urlopen(req)
	mypage = response.read()

	unicodePage = mypage.decode("utf-8")

	myItems = re.findall(r'.*?<span class="segment-name">(.*?)</span>.*?<span class="segment-weight weight">(.*?)</span></div>', unicodePage)

	stItems = re.findall(r'.*?<span class="stock-name"><div class="name">(.*?)</div><div class="price">(.*?)</div></span><span class="stock-weight weight">(.*?)</span>', unicodePage)
	update_page1 = re.findall(r'.*?"updated_at_format":"(.*?)"},',unicodePage)
	update_page_1 = update_page1[0]

	print zh_name,' = ',n
	print '   --------------'
	print '    分类','   ','仓位'
	for item in myItems:
		print '   ',item[0].encode('utf-8'),'   ',item[1].encode('utf-8')
	print '   --------------'	
	print '    股票','   ','仓位'
	for st in stItems:
		print '   ', st[0].encode('utf-8'),'   ',st[2].encode('utf-8'), '  ', get_price(st[1]), ')'
	print'|'
	return update_page_1


def jkzh( str_url, zh_name, n, update_page11_jk = '', update_page_1_jk = '' ):
	if n !=0:
		update_page11_jk = update_page_1_jk
	update_page_1_jk = gpflash( str_url,zh_name,n )
	return (update_page11_jk , update_page_1_jk)

def checkzh(update_page11_ck, update_page_1_ck, zh_name):
	zh_name_all = zh_name + "已调仓"
	if (update_page11_ck != update_page_1_ck) & bool(update_page11_ck):
		cmd = 'display notification \"' + \
   	 zh_name_all + '\" with title \"title\"'
		call(["osascript", "-e", cmd])

def get_price(code):
	url = 'https://xueqiu.com/S/' + code
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	headers = { 'User-Agent' : user_agent }
	req = urllib2.Request(url, headers = headers)
	response = urllib2.urlopen(req)
	mypage = response.read()
	unicodePage = mypage.decode("utf-8")

	myprice = re.findall(r'.*?<meta name="description" content="(.*?)\).*?', unicodePage)
	return myprice[0]


while True:
	
	( update_page11_ck,update_page_1_ck ) = jkzh('https://xueqiu.com/P/ZH1230914', "Jack_he的组合2号乌龟—价值", number , update_page11_ck ,update_page_1_ck)
	checkzh( update_page11_ck, update_page_1_ck,  "Jack_he的组合2号乌龟—价值" )

	( update_page22_ck,update_page_2_ck ) = jkzh('https://xueqiu.com/P/ZH989316', "纳履而去的组合滟滟随波千万里-价值", number , update_page22_ck ,update_page_2_ck)
	checkzh( update_page22_ck, update_page_2_ck,  "纳履而去的组合滟滟随波千万里-价值" )

	( update_page33_ck,update_page_3_ck ) = jkzh('https://xueqiu.com/P/ZH002754', "十三飞的组合一飞冲天-价值成长", number , update_page33_ck ,update_page_3_ck)
	checkzh( update_page33_ck, update_page_3_ck,  "十三飞的组合一飞冲天-价值成长" )

	( update_page44_ck,update_page_4_ck ) = jkzh('https://xueqiu.com/P/ZH003851', "丹书铁卷的组合铁券1号-价值", number , update_page44_ck ,update_page_4_ck)
	checkzh( update_page44_ck, update_page_4_ck,  "丹书铁卷的组合铁券1号-价值" )

	( update_page55_ck,update_page_5_ck ) = jkzh('https://xueqiu.com/P/ZH1124083', "dunhun的组合我们的征途-成长", number , update_page55_ck ,update_page_5_ck)
	checkzh( update_page55_ck, update_page_5_ck,  "dunhun的组合我们的征途-成长" )

	( update_page66_ck,update_page_6_ck ) = jkzh('https://xueqiu.com/P/ZH1124083', "小盘股王子的组合千金难买龙回头-成长", number , update_page66_ck ,update_page_6_ck)
	checkzh( update_page66_ck, update_page_6_ck,  "小盘股王子的组合千金难买龙回头-成长" )

	number = number + 1
	print '================================================================'
	print '================================================================'
	print ''
	print ''
	time.sleep(50)




