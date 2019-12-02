#!/usr/bin/python2
#KRYPTONNN GANS
#whatsapp: 085872859859
#syarat dan ketentuan
# -jgn recode boejank
# -jgn decode_-
# -kalo ada bug chat mimin:V
p = '\x1b[0m'
m = '\x1b[91m'
h = '\x1b[92m'
k = '\x1b[93m'
b = '\x1b[94m'
u = '\x1b[95m'
bm = '\x1b[96m'
bgm = '\x1b[41m'
bgp = '\x1b[47m'
res = '\x1b[40m'
star='\xe2\xad\x90'
import sys,random,json,urllib,requests,os,time
def koneksi(userss):
	wrk=json.loads(requests.get('https://api.github.com/users/'+userss).text)
	menu(wrk)
def login():
	try:
		try:
			baca=open('.cookie').read()
			koneksi(baca)
		except IOError:
			logi()
			log=raw_input("\t"+m+"["+k+"*"+m+"]"+h+"GITHUB : "+u)
			if(log=='' or log==' '):
				print('[x] login gagal')
				time.sleep(1)
				login()
			else:
				gjs=open('.cookie','w')
				gjs.write(log)
				gjs.close()
				login()
	except KeyError:
		jalan("[!] user/author yg anda masukan tidak ada"+p)
		os.system('rm .cookie')
		login()

def scriptfinder(op):
	try:
		logo(op)
		cari=gs=raw_input("\t"+m+"["+k+'?'+m+"]"+u+" Cari : "+p)
		urll=urllib.quote(cari)
		if(cari=='' or cari==' '):
			jalan("\n\t"+m+"["+k+"1"+m+"]"+b+" YG ANDA MASUKAN SALAH")
		else:
			jalan("\t"+m+"["+k+"1"+m+"]"+b+". Python")
			jalan("\t"+m+"["+k+"2"+m+"]"+b+". JavaScript")
			jalan("\t"+m+"["+k+"3"+m+"]"+b+". Shell")
			jalan("\t"+m+"["+k+"4"+m+"]"+b+". HTML")
			jalan("\t"+m+"["+k+"5"+m+"]"+b+". Swift")
			jalan("\t"+m+"["+k+"6"+m+"]"+b+". Java")
			jalan("\t"+m+"["+k+"7"+m+"]"+b+". All")
			langu=raw_input("\t"+m+"["+k+'?'+m+"]"+u+" Pilih Bahasa : "+p)
			if(langu=='' or langu==' '):
 				jalan("\n\t"+m+"["+k+"1"+m+"]"+b+"YG ANDA MASUKAN SALAH")
			elif(langu=='1' or langu=='01'):
				scrap(op,urll,'Python')
			elif(langu=='2' or langu=='02'):
				scrap(op,urll,'JavaScript')
			elif(langu=='3' or langu=='03'):
				scrap(op,urll,'Shell')
			elif(langu=='4' or langu=='04'):
				scrap(op,urll,'HTML')
			elif(langu=='5' or langu=='05'):
				scrap(op,urll,'Swift')
			elif(langu=='6' or langu=='06'):
				scrap(op,urll,'Java')
			elif(langu=='7' or langu=='07'):
				scrap(op,urll,'All')
			else:
				jalan("\t"+m+"["+k+"X"+m+"]"+u+"SALAH BRO")
				time.sleep(1)
				scriptfinder(op)
	except ValueError:
		jalan("\n\t"+m+"["+k+"X"+m+"]"+u+"YG ANDA MASUKAN SALAH"+p)
		scriptfinder(op)

def scrap(op,obje,langu):
	try:
		hasi=json.loads(requests.get('https://api.github.com/search/repositories?q='+obje+'+language:'+langu+'&sort=stars&order=desc').text)
		saring(op,hasi)
	except requests.exceptions.ConnectionError:
		jalan("[!] koneksi tidak ada"+p)
def saring(op,ab):
	try:
		logo(op)
		n=0
		jalan('\t'+m+'_'*25+'HASIL PENCARIAN'+'_'*25)
		while n < len(ab['items']):
			jalan("\t"+m+"["+k+str(n)+m+"]"+u+" %s" % ab['items'][n]['full_name']+"\tbahasa : %s" % ab['items'][n]['language']+" *: %s" % ab['items'][n]['stargazers_count'])
			n=n+1
		jalan('\t\t '+b+'ketik "99999" untuk kembali ke menu')
		jalan('\t'+m+'_'*60)
		gs=raw_input("\t"+m+"["+k+'?'+m+"]"+b+" pilih : "+p)
		gint=int(gs)
		if int(gs) < len(ab['items']):
			hw=ab['items'][gint]['clone_url']
			os.system('git clone '+hw)
			print('sukses')
			time.sleep(1)
			saring(op,ab)
		elif int(gs)== 99999:
			menu(op)
		else:
			jalan("\t"+m+"["+k+"X"+m+"]"+u+"SALAH BRO")
			saring(op,ab)
			time.sleep(1)
	except KeyboardInterrupt:
		print('')
#https://api.github.com/search/repositories?q=tetris+language:assembly&sort=stars&order=desc
def logo(nama):
	os.system('clear')
	print('\t'+m+'_'*60)
	os.system('toilet -f slant -F gay "    GINFO"')
	print(h+'\tAUTHOR : KRYPTON')
	jalan('\tWhatsapp : 085872859859')
	jalan('\t Nama :'+nama['name'])
	print('\t'+m+'_'*60)
def logi():
        os.system('clear')
        print('\t'+m+'_'*60)
        os.system('toilet -f slant -F gay "    GINFO"')
        print(h+'\tAUTHOR : KRYPTON')
	jalan('\tWhatsapp : 085872859859')
        print('\t'+m+'_'*60)
def menu(wik):
	logo(wik)
	print(k+'\t\t1. '+u+'Informasi Github ')
	print(k+'\t\t2. '+u+'Repository')
	print(k+'\t\t3. '+u+'Pengikut')
	print(k+'\t\t4. '+u+'Pencari Script')
	print(k+'\t\t5. '+u+'Keluar')
	pilihan = raw_input("\n\t"+m+"["+k+"*"+m+"]"+h+"pilih : "+u)
	if(pilihan=='1' or pilihan=='01'):
		info(wik)
	elif(pilihan=='2' or pilihan=='02'):
		repo(wik)
	elif(pilihan=='3' or pilihan=='03'):
		follower(wik)
	elif(pilihan=='4' or pilihan=='04'):
		scriptfinder(wik)
	elif(pilihan=='5' or pilihan=='05'):
		os.system('rm .cookie')
		jalan("\t"+m+"["+k+"*"+m+"]"+h+"keluar sukses"+p)
	else:
		jalan("\t"+m+"["+k+"X"+m+"]"+u+"SALAH BRO")
		time.sleep(1)
		menu(wik)


def repo(teks):
	try:
		logo(teks)
		re=json.loads(requests.get(teks['repos_url']).text)
		n=0
		while n<len(re):
			jalan("\t"+m+"["+k+str(n)+m+"]"+h+" %s" % re[n]['name']+"\t"+m+"["+k+"-"+m+"] bahasa : "+h+" %s" % re[n]['language']+"\t* : %s" % re[n]['stargazers_count']+'  <*>: %s' % re[n]['watchers'])
			n=n+1
		print('\t\t '+b+'ketik "99999" untuk kembali ke menu')
		jalan(m+'_'*60)
		clo=raw_input("\t"+m+"["+k+"*"+m+"]"+u+"Clone : "+h)
		cli=int(clo)
		clu=str(clo)
		if int(clo) < len(re):
			select=re[cli]['clone_url']
			jalan("\t"+m+"["+k+"*"+m+"]"+h+"sedang mendownload........"+p)
			os.system('git clone '+select+'>>/dev/null')
			jalan("\t"+m+"["+k+"*"+m+"]"+u+"sukses")
			repo(teks)
		elif cli ==99999:
			menu(teks)
		else:
			jalan("\t"+m+"["+k+"X"+m+"]"+u+"SALAH BRO")
			time.sleep(1)
			repo(teks)
	except ValueError:
		jalan("\t"+m+"["+k+"X"+m+"]"+u+"SALAH BRO")
		time.sleep(1)
		repo(teks)
def follower(teks):
	n=0
	re=json.loads(requests.get(teks['followers_url']).text)
	while n<len(re):
		jalan("\t"+m+"["+k+"*"+m+"]"+h+"pengikut\t :"+u+" %s" % re[n]['login'])
		n=n+1
	hshausg=raw_input(b+'enter untuk kembali ke menu'+p)
	menu(teks)
def info(data):
	try:
		try:

 			jalan(m+'_'*70)
			jalan("\t"+m+"["+k+"*"+m+"]"+u+"nama \t\t:"+k+" %s" % data['name'])
			jalan("\t"+m+"["+k+"*"+m+"]"+u+"Id \t\t\t:"+k+" %s" % data['id'])
			jalan("\t"+m+"["+k+"*"+m+"]"+u+"Node id \t\t:"+k+" %s" % data['node_id'])
			jalan("\t"+m+"["+k+"*"+m+"]"+u+"email \t\t:"+k+" %s" % data['email'])
			jalan("\t"+m+"["+k+"*"+m+"]"+u+"blog \t\t:"+k+" %s" % data['blog'])
			jalan("\t"+m+"["+k+"*"+m+"]"+u+"location \t\t:"+k+" %s" % data['location'])
			jalan("\t"+m+"["+k+"*"+m+"]"+u+"Company \t\t:"+k+" %s" % data['company'])
			jalan("\t"+m+"["+k+"*"+m+"]"+u+"Bio \t\t\t:"+k+" %s" % data['bio'])
			jalan("\t"+m+"["+k+"*"+m+"]"+u+"Tipe \t\t:"+k+" %s" % data['type'])
			jalan("\t"+m+"["+k+"+"+m+"]"+u+"Jumlah repo \t\t:"+k+" %s" % data['public_repos'])
			jalan("\t"+m+"["+k+"*"+m+"]"+u+"Jumlah Gits \t\t:"+k+" %s" % data['public_gists'])
			jalan("\t"+m+"["+k+"*"+m+"]"+u+"Jumlah Pengikut \t:"+k+" %s" % data['followers'])
			jalan("\t"+m+"["+k+"*"+m+"]"+u+"Jumlah Mengikuti\t:"+k+" %s" % data['following'])
			jalan("\t"+m+"["+k+"*"+m+"]"+u+"Di Buat \t\t:"+k+" %s" % data['created_at'])
			jalan("\t"+m+"["+k+"*"+m+"]"+u+"Di Perbarui \t\t:"+k+" %s" % data['updated_at'])
			jalan("\t"+m+"["+k+"*"+m+"]"+u+"site_admin \t\t:"+k+" %s" % data['site_admin'])
			jalan("\t"+m+"["+k+"*"+m+"]"+u+"Link Github \t\t:"+k+" %s" % data['html_url'])
			jalan(m+'_'*70)
			isshshsh=raw_input(u+'enter untuk kembali ke menu: ')
			menu(data)
		except KeyError:
			jalan("[!] user/author yg anda masukan tidak ada"+p)
	except requests.exceptions.ConnectionError:
		jalan("[!] koneksi tidak ada"+p)
def jalan(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.001)

try:
	try:
		login()
	except KeyboardInterrupt:
		jalan("\n\t"+m+"["+k+"!"+m+"]"+u+"Selamat tinggal"+p)
except KeyError:
	jalan("\n\t"+m+"["+k+"!"+m+"]"+u+"Selamat tinggal"+p)

