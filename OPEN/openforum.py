#! /usr/bin/python3

# Disclaimer: This script is for educational purposes only. None of the authors, contributors, administrators, vandals, or anyone else connected with sources, in any way whatsoever, can be responsible for your use of the information contained in or linked from these web pages. 


import webbrowser
import time
x = ' '

cstop = [ 'https:-//exploit.in/', 'https:-//www.nulled.to/', 'https:-//cracked.io/' , 'https:-//sinister.ly/' 'https://duckduckgo.com/']

onions = '''

Sours - 
https://tor.taxi/  
https://oniontree.org/  
https://onion.live/

CryptBB - 

http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/

ENDCHAN IMAGE BOARD -
 
http://enxx3byspwsdo446jujc52ucy2pf5urdbhqw3kbsfhlfjwmbpj5smdad.onion/
 
DREAD FORUM -
 
http://dreadytofatroptsdj6io7l3xptbet6onoyno2yv7jicoxknyazubrad.onion 
 
RAMBLE -
 
http://rambleeeqrhty6s5jgefdfdtc6tfgg4jj6svr4jpgk4wjtg3qshwbaad.onion/

'''

ran = '''


Sours -  
https://www.ransom-db.com/ransomware-groups
http://ransomwr3tsydeii4q43vazm7wofla5ujdajquitomtd47cxjtfgwyyd.onion/
https://github.com/fastfire/deepdarkCTI/
https://github.com/fastfire/deepdarkCTI/blob/main/ransomware_gang.md


List - 

AKO Group - http://37rckgo66iydpvgpwve7b2el5q2zhjw4tv4lmyewufnpx4lhkekxkoqd.onion
AlphaVM (BlackCat) - http://alphvmmm27o3abo3r2mlmjrpdmzle3rykajqc5xsj7j7ejksbpsa36ad.onion
Arvin - http://3kp6j22pz3zkv76yutctosa6djpj4yib2icvdqxucdaxxedumhqicpad.onion
Astro Team - http://anewset3pcya3xvk73hj7yunuamutxxsm5sohkdi32blhmql55tvgqad.onion 
Atomsilo - http://mhdehvkomeabau7gsetnsrhkfign4jgnx3wajth5yb5h6kvzbd72wlqd.onion
Avaddon - http://avaddongun7rngel.onion
AvosLocker - http://avosqxh72b5ia23dl5fgwcpndkctuzqvh2iefk5imp3pi5gfhel5klad.onion
Babuk - http://nq4zyac4ukl4tykmidbzgdlvaboqeqsemkp4t35bzvjeve6zm2lqcjid.onion
Bl@ckt0r - http://bl4cktorpms2gybrcyt52aakcxt6yn37byb65uama5cimhifcscnqkid.onion
BlackByte - http://f5uzduboq4fa2xkjloprmctk7ve3dm46ff7aniis66cbekakvksxgeqd.onion
BlackMatter (DarkSide/FIN7) - http://blackmax7su6mbwtcyo3xwtpfxpm356jjqrs34y4crcytpw7mifuedyd.onion
Black Shadow - http://544corkfh5hwhtn4.onion
Bonaci - http://bonacifryrxr4siz6ptvokuihdzmjzpveruklxumflz5thmkgauty2qd.onion
Cl0p - http://santat7kpllt6iyvqbr7q4amdv6dzrh6paatvyrzl7ry3zm72zigf4ad.onion
Conti - http://continewsnv5otx5kaoje7krkto2qbu3gtqef22mnr7eaxw3y6ncz3ad.onion
Cuba - http://cuba4ikm4jakjgmkezytyawtdgr2xymvy6nvzgw5cglswg3si76icnqd.onion
CRYP70N1C0D3 - http://7k4yyskpz3rxq5nyokf6ztbpywzbjtdfanweup3skctcxopmt7tq7eid.onion
DarkRypt - https://darkrypt.io
DarkSide - http://darksidc3iux462n6yunevoag52ntvwp6wulaz3zirkmh4cnz6hhj7id.onion
DopplePaymer - http://hpoo4dosa3x4ognfxpqcrjwnsigvslm7kv6hvmhh2yqczaxy3j6qnwad.onion
El Comenta (SynACK) - http://xqkz2rmrqkeqf6sjbrb47jfwnqxcd4o2zvaxxzrpbh2piknms37rw2ad.onion
Entropy - http://leaksv7sroztl377bbohzl42i3ddlfsxopcb6355zc7olzigedm5agad.onion
Everest - http://ransomocmou6mnbquqz44ewosbkjk3o5qjsl3orawojexfook2j7esad.onion
Grief - http://griefcameifmv4hfr3auozmovz5yi6m3h3dwbuqw7baomfxoxz4qteid.onion
Groove - http://ws3dh6av66sjbxxkjpw5ao3wqzmtejnkzheswm4dz5rrwvular7xvkqd.onion
Haron - http://ft4zr2jzlqoyob7yg4fcpwyt37hox3ajajqnfkdvbfrkjioyunmqnpad.onion
Hive - http://hiveleakdbtnp76ulyhi52eag6c6tyc3xw7ez7iqy6wc34gd2nekazyd.onion
HolyGhost - http://matmq3z3hiovia3voe2tix2x54sghc3tszj74xgdy4tqtypoycszqzqd.onion
Hotarus - r6d636w47ncnaukrpvlhmtdbvbeltc6enfcuuow3jclpmyga7cz374qd.onion
Lockbit1.0 - http://lockbitkodidilol.onion
LockBit2.0 - http://lockbitapt6vx57t3eeqjofwgcglmutr3a35nygvokja5uuccip4ykyd.onion
LockData Auction (Crylock) - http://wm6mbuzipviusuc42kcggzkdpbhuv45sn7olyamy6mcqqked3waslbqd.onion
Lorenz - http://lorenzmlwpzgxq736jzseuterytjueszsvznuibanxomlpkyxk6ksoyd.onion
LV - http://4qbxi3i2oqmyzxsjg4fwe4aly3xkped52gq5orp6efpkeskvchqe27id.onion
LV2 - http://rbvuetuneohce3ouxjlbxtimyyxokb4btncxjbo44fbgxqy7tskinwad.onion
Marketo - http://jvdamsif53dqjycuozlaye2s47p7xij4x6hzwzwhzrqmv36gkyzohhqd.onion
Medusa - http://qd7pcafncosqfqu3ha6fcx4h6sr7tzwagzpcdcnytiw3b6varaeqv5yd.onion
Midas - http://midasbkic5eyfox4dhnijkzc7v7e4hpmsb2qgux7diqbpna4up4rtdad.onion/blog.php
Mobikwik Indian Data Leak - http://mobikwikoonux37wauz6oqymshuvebj5u763rutlogc2fb2o3ugcazid.onion
Moses Staff - http://moses-staff.se
Mount Locker - http://mountnewsokhwilx.onion
N3tw0rm - n3twormruynhn3oetmxvasum2miix2jgg56xskdoyihra4wthvlgyeyd.onion
Nefilim Group - http://hxt254aygrsziejn.onion
Nightsky - http://gg5ryfgogainisskdvh4y373ap3b2mxafcibeh2lvq5x7fx76ygcosad.onion
Pandora - http://vbfqeh5nugm6r2u2qvghsdxm3fotf5wbxb5ltv6vw77vus5frdpuaiid.onion
Pay2Key - http://pay2key2zkg7arp3kv3cuugdaqwuesifnbofun4j6yjdw5ry7zw2asid.onion
Payload.bin - vbmisqjshn4yblehk2vbnil53tlqklxsdaztgphcilto3vdj4geao5qd.onion
Prometheus - http://promethw27cbrcot.onion/blog
Pysa - http://pysa2bitc5ldeyfak4seeruqymqs4sj5wt5qkcq7aoyg4h2acqieywad.onion
Quantum - http://quantum445bh3gzuyilxdzs5xdepf3b7lkcupswvkryf3n7hgzpxebid.onion
Ragnarok Leaks - http://wobpitin77vdsdiswr43duntv6eqw4rvphedutpaxycjdie6gg3binad.onion
Ragnarok Leak Site - http://sushlnty2j7qdzy64qnvyb6ajkwg7resd3p6agc2widnawodtcedgjid.onion
Ragnar Locker - http://rgleaktxuey67yrgspmhvtnrqtgogur35lwdrup4d3igtbm3pupc4lyd.onion
RAMP (Babuk/Payload.bin) - http://wavbeudogz6byhnardd2lkp2jafims3j7tj6k6qnywchn2csngvtffqd.onion
RansomEXX - http://rnsm777cdsjrsdlbs4v5qoeppu3px6sb2igmh53jzrx7ipcrbjz5b2ad.onion
Ranzy - http://37rckgo66iydpvgpwve7b2el5q2zhjw4tv4lmyewufnpx4lhkekxkoqd.onion
REvil - http://blogxxu75w63ujqarv476otld7cyjkq4yoswzt4ijadkjwvg3vrvd5yd.onion/Blog
Rook - http://gamol6n6p2p4c3ad7gxmx3ur7wwdwlywebo2azv3vv5qlmjmole2zbyd.onion
Sabbath - http://54bb47h.blog
Snatch - http://hl66646wtlp2naoqnhattngigjp5palgqmbwixepcjyq5i534acgqyad.onion
Spook - http://spookuhvfyxzph54ikjfwf2mwmxt572krpom7reyayrmxbkizbvkpaid.onion/blog
Suncrypt - http://x2miyuiwpib2imjr5ykyjngdu7v6vprkkhjltrk4qafymtawey4qzwid.onion
Vice Society - http://vsociethok6sbprvevl4dlwbqrzyhxcxaqpvcqt5belwvsuxaxsutyad.onion
Xing - http://xingnewj6m4qytljhfwemngm7r7rogrindbq7wrfeepejgxc3bwci7qd.onion

******************************************************************************************

UPDATE:

BlackMatter: http://blackmax7su6mbwtcyo3xwtpfxpm356jj...dyd.onion/
Prometheus: http://promethw27cbrcot.onion/blog/
Arvin Club: http://3kp6j22pz3zkv76yutctosa6djpj4yib2...pad.onion/
Babuk: http://nq4zyac4ukl4tykmidbzgdlvaboqeqsem...#section-3
AvosLocker: http://avosqxh72b5ia23dl5fgwcpndkctuzqvh...lad.onion/
Bl@kt0r: http://bl4cktorpms2gybrcyt52aakcxt6yn37b...reach.html
Everest: http://ransomocmou6mnbquqz44ewosbkjk3o5q...sad.onion/
Clop Leaks: http://santat7kpllt6iyvqbr7q4amdv6dzrh6p...4ad.onion/
Conti: http://continewsnv5otx5kaoje7krkto2qbu3g...3ad.onion/
Dopple Leaks: http://hpoo4dosa3x4ognfxpqcrjwnsigvslm7k...wad.onion/
Grief Leaks: http://griefcameifmv4hfr3auozmovz5yi6m3h...eid.onion/
Hive: http://hiveleakdbtnp76ulyhi52eag6c6tyc3x...zyd.onion/
LockData: http://wm6mbuzipviusuc42kcggzkdpbhuv45sn...bqd.onion/
Lorenz: http://lorenzmlwpzgxq736jzseuterytjueszs...oyd.onion/
Corporate leaks: http://hxt254aygrsziejn.onion/
Pay2Key: http://pay2key2zkg7arp3kv3cuugdaqwuesifn...sid.onion/
Payload.bin: http://vbmisqjshn4yblehk2vbnil53tlqklxsd...5qd.onion/
Pysa's Partners: http://pysa2bitc5ldeyfak4seeruqymqs4sj5w...tners.html
RagnarLocker: http://rgleaktxuey67yrgspmhvtnrqtgogur35...lyd.onion/
Ransomexx: http://rnsm777cdsjrsdlbs4v5qoeppu3px6sb2...2ad.onion/
Happy Blog: http://dnpscnbaix6nkwvystl3yxglz7nteicqr...qyd.onion/
SunCrypt: http://x2miyuiwpib2imjr5ykyjngdu7v6vprkk...zwid.onion
Vice Society: http://4hzyuotli6maqa4u.onion/
Xing Team: http://xingnewj6m4qytljhfwemngm7r7rogrin...7qd.onion/

The following sites are offline:

Avaddon: http://avaddongun7rngel.onion/ (v2, I couldn't find the v3 link)
Darkside: http://darksidc3iux462n6yunevoag52ntvwp6...7id.onion/ (offline)
Ranzy: http://37rckgo66iydpvgpwve7b2el5q2zhjw4t...oqd.onion/ (offline)
Astro: http://anewset3pcya3xvk73hj7yunuamutxxsm...qad.onion/ (offline)
Mount: http://mountnewsokhwilx.onion/ (v2, I couldn't find the v3 link)

'''

KITCHEN = onions + ran 
def view_forum():
    choice = input(f'What Section would you like to access? \n [Enter the Letter or type "all" for everything ...]: ')
    if choice == 'c':
        for url in cstop:
            time.sleep(2)
            webbrowser.open_new_tab(url)
    elif choice == 'o':
        print(f'{onions}')
    elif choice == 'r':
        print(f'{ran}')
    elif choice == 'all':
        print(f'{KITCHEN}')

def print_forum():
    choice = input(f'What Section would you like to access? \n [Enter the Letter]: ')
    if choice == 'c':
        for url in cstop:
            time.sleep(2)
            webbrowser.open_new_tab(url)
    elif choice == 'o':
        file = open(f"ONI.txt", "w")
        file.write(f'{onions}')
        file.close()
        print('[+] Onion Links Printed in Script Directory -')
    elif choice == 'r':
        file = open(f"RAN.txt", "w")
        file.write(f'{ran}')
        file.close()
        print('[+] Rans Sources Printed in Script Directory -')

which = input(f'Would you like to \"save\" or \"view\" Sections? :    ')

print(x*2)
print('TABLE OF CONTENTS:')
print(x)
print('cstop(c): Open Clearnets  ')
print('tech(o): All Onion Links ')
print('Xtras(r): Ran Links')
print(x*2)

if which == 'save':
    print_forum()
elif which == 'view':
    view_forum()
else:
    print(' [!] It seems you made a typo - that option does not exist')
