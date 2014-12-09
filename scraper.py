import twitter
import time
import datetime
import json
import sys
import matplotlib.pyplot as plt
from collections import deque
api = twitter.Api(consumer_key='6GhjLPbZahCKk4gpLtFCa0XSh',
                      consumer_secret='Q1rPti2CMnEH555ZSUjTymg5KP1RAzi0PpKjjp0tXYNS27IP2K',
                      access_token_key='1259788333-dmMU7hlLFvT8z1dQDKKbjUHn3x4EQMo5QkY4tEY',
                      access_token_secret='uV4qboOa6QWcZbiojRIMaSrAJ5bowVOEnUiqpO2zeZWAJ',
                      cache=None)



screen_names1 = ['naravosubum', 'pokesimecic', 'vigeguvyjan', 'mywigerowapo', 'xurytebujeme', 'sedafagazen', 'xicurojymem', 'famidikupima', 'sazexobabibi', 'nylabemulez', 'limitesuzyn', 'xiqityrykux', 'cyzetebugajo', 'pupepehesiwi', 'suxopyqepuh', 'gedelimipohu', 'dynatomypyqu', 'fijawunajoza', 'puzukepubaz', 'wugosawabol', 'jimosypuxix', 'mivulobigizy', 'kihytuzuhyw', 'cylusemoryvu', 'penejeqisuj', 'rocajebazax', 'xebohuzynyfa', 'ququparimyp', 'cilynuviduz', 'hifutuvuzyl', 'gehixolavaj', 'syjugigyfew', 'hezazyvysywa', 'woxyhadyjon', 'tymotosoxedi', 'vixidimoxaf', 'vekumikowiky', 'gytabecuderi', 'zevocybikeju', 'xusonoquset', 'jypivesirasu', 'relopubopose', 'hycawofyhuru', 'xiguqecinazo', 'lanirajepube', 'pyhoposuled', 'sytylepoxof', 'jecimiticavi', 'qibyryqimesy', 'qazityvenybi', 'jufuluwaryvy', 'bedelovuciwi', 'noworoxyxav', 'qoqelabosub', 'fymehafecek', 'qalytyjawin', 'moledonywyz', 'zewibydupuxi', 'fynarejogyf', 'mywomomifej', 'vuriwexidobi', 'hyhexylopoq', 'zahubybedapo', 'norenopodyp', 'xuqacutyhul', 'muketaxuzyr', 'fewiwodygyga', 'lucytodyhys', 'mebadakovopy', 'benamawybig', 'jerejybavuwu', 'cewohuceqor', 'hunejelecyho', 'patugosatob', 'safalagocaz', 'relylizodaf', 'fiqocabotyv', 'jiqitecewawy', 'tobulalihena', 'fewezemuqywu', 'demoqilywuha', 'mesinepesur', 'jagakiwyvumu', 'zynacisetymo', 'lyjocufecup', 'zyrytyjawobo', 'fohihefidaw', 'wasetowadyha', 'mujysinunobu', 'hetepibozur', 'domevalodal', 'sifogiqedyxa', 'nugeqysikupy', 'fadyjojyxebu', 'mupehejecah', 'wyjomoqodul', 'qatujyqejyvo', 'sipyfujagyfu', 'wumaxigasom']
screen_names2 = ['nenacebagovu','nynybadopiso','vejokywaker','godefezocylo','kacifenexuf','vukyporylil','haxidoqydoh','xyjacejuvydo','mucomacixedu','zoqanimibis','taruzoqilud','mapapilufok','nepusegosota','nimykevukuxe','tyzimeqotedo','durubacuxiv','najyrexilox','minylocexov','padanirivuw','sutypotaxik','qajapetycyqo','xemamagurah','pobamirilexi','vaquzybikate','ritawurytax','qikividohyh','fukutavibobe','parozyretyt','gobutuditudi','jupufysyhym','mybedyjopiq','gupinepocid','lacufitidufu','kuhityxuhoq','kuvyxokunaze','wykywogofuf','sijiqopyfas','fexilyseryzi','dififiqobopu','kipobohuvyt','daqikyxacama','riziqytakega','zawaqufolyhu','cegezepuvex','qodexyrikequ','cowuferyhyb','wifazyryzyr','sofodotynuty','lupyfapapib','rowenapowuci','qakaqosihiq','cisuqavopib','lunomycemuz','jowowyxolujy','wykigybelynu','siguxemimak','rahymyvafiha','xidebywavopy','kidemekibary','hacyzamupuma','jamucagyjib','jeholetifyl','wocosujupub','lyrobadituw','gujuqativig','tekyriryvuxy','myvatidipexe','pedolomafun','tafenufugobu','qigifylytex','wupalovycuwi','mykifosyvero','ryhofohagijy','nibuwibyloc','hebobutonix','rowoqehipacu','qyjycucadan','kejobyfevij','cimuzijyfego','syviwihuqobu','rexigagofuqe','fefeqedyhuza','tyfylunyhoq','buwyxuqanedo','xezyhupolely','desihafevib','wusotazyjok','sizeryfajyr','dekirugolov','kucikymeqag','zivuqotycyq','wygojolikini','redebomizop','luzimohyquze','vamulovukuw','xagavaqecyh','kivazijezuwu','bafonexobog','fisifovyvev','rapyjugurozy']
screen_names3 = ['nihaporobys','wyjaborygoga','sivycypycas','mykufuqaqur','faqyhucodys','pivabetipeka','huqasamisedi','fafoqytahahe','zivuvatysam','zarynysowaqy','gyhegyfemica','nekohevajeh','janyrokidyzu','xytudaxaxyx','lorykugidys','guvuvasuzabo','hijixanupalo','fezabotyhat','mujytapycede','hiduzisecyr','rofihaduvipu','gezyboxyviji','jojawivysydu','jynykixukiq','mykeqyhuselu','rysigytozygi','hehiciwicyp','gaqinegiquli','zemotysydunu','barulufujupe','juxuhawydep','sofamazadyvo','satobitebyp','juhizimexiv','vemihifapoh','peqiliquqice','texemigenyna','vitibyxywik','myciwuzuzid','tydesucatifa','vamycuvajyvu','tomozucucope','tybudenajyf','qizafagagid','xisuxacubof','tulyliqycir','zedysyjygubu','konelyjapev','xynehuvutil','gawygynatofi','vygocaraqym']

names = [screen_names1, screen_names2, screen_names3]

followerFiles = ['naravosubumFollowers', 'pokesimecicFollowers', 'vigeguvyjanFollowers']

def get_times():
    time_list = []

    for n in names:
        users = api.UsersLookup(screen_name=n)
        for u in users:
            d = u.__dict__
            t = datetime.datetime.strptime(d['_created_at'][11:19],"%H:%M:%S")
            print t
            time_list.append(t)

    plt.plot(time_list)
    plt.show()

# def get_bfs(startingNode=1259788333):
#     # start from me = 1259788333
#     visitedNodes = set()
#     node_count = 0
#     queue = deque([startingNode])
#     while len(queue) > 0:
#        node = queue.pop()
#        if node in visitedNodes:
#           continue
#        visitedNodes.add(node)
#        if node_count >= 100:
#           return list(visitedNodes)
#        for n in getAdjacentNodes(node):
#           if n not in visitedNodes:
#              node_count += 1
 
#         queue.appendleft(n)
#     return False

def getAdjacentNodes(node):
    friends = api.GetFriends(user_id=node)
    print "getting Friends"
    lst = []
    for f in friends:
        lst.append(f.__dict__['_id'])
    print lst
    return lst



def get_general_info(data_dir, user_id_list, file_name):
    results = api.UsersLookup(user_id_list)


    for user in results:
        d = user.__dict__
        name = d['_screen_name']
        path = data_dir + "/" + file_name
        
        sys.stdout = open(path, 'a')
        print d


def retrieve_users(l):
    return [l[i:i + 100] for i in range(0, len(l), 100)]

def get_all():
    for f in followerFiles:
        json_data=open('data/' + f)
        data = json.load(json_data)
        ids = data["ids"]
        list_list = retrieve_users(ids)
        for l in list_list:
            get_general_info('data', l, f + '_info')

get_all()