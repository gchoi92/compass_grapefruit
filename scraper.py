import twitter
import time
import datetime
import json
import numpy
import ast
import sys
#import matplotlib.pyplot as plt
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

followerFilesBad = ['naravosubumFollowers', 'pokesimecicFollowers', 'vigeguvyjanFollowers']
followerFilesInfoBad = ['naravosubumFollowers_info', 'pokesimecicFollowers_info', 'vigeguvyjanFollowers_info']
followerFilesGood = ['appNexusFollowers']
followerFilesInfoGood = ['appNexusFollowers_info']

def get_times():
    time_list = []

    for n in names:
        users = api.UsersLookup(screen_name=n)
        for u in users:
            d = u.__dict__
            t = datetime.datetime.strptime(d['_created_at'][11:19],"%H:%M:%S")
            time_list.append(t)

    plt.plot(time_list)
    plt.title('Users Registered vs. Time on Wed Oct 16')
    plt.show()

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
        d['_status'] = 0
        if d['_description'] is not None:
            d['_description'] = d['_description'].replace("\"", "").replace("\'", "")
        if d['_followers_count'] is not 0:
            d['_ratio'] = float(int(d['_friends_count']))/float(int(d['_followers_count']))
        else:
            d['_ratio'] = -1.0
        print json.dumps(d)

    sys.stdout = sys.__stdout__

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


def get_uniques(files):
    keys = {}
    uniques = []
    for fi in files:
        with open('data/' + fi, "r") as f:
            entries = f.readlines()
            for entry in entries:
                entry = entry[:-1]
                json_acceptable_string = entry
                loaded = json.loads(json_acceptable_string)
                if loaded['_id'] not in keys:
                    keys[loaded['_id']] = 0
                    uniques.append(loaded)

    return uniques

def post_processing(files, out_file):
    uniques = get_uniques(files)
    print "Unique accounts: " + str(len(uniques))

    num_located = 0.0
    num_time = 0.0
    default_pics = 0.0
    url_count = 0.0
    for unique in uniques:

        if len(unique['_location']) > 2:
            num_located += 1.0
        if unique['_time_zone'] is not None and len(unique['_time_zone']) > 2:
            num_time += 1.0
        if "default_profile_images" in unique['_profile_image_url']:
            default_pics += 1.0
        if unique['_url'] is not None and len (unique['_url']) > 2:
            url_count += 1.0

    print "Percent located is: " + str(num_located/float(len(uniques)))
    print "Percent time is: " + str(num_time/float(len(uniques)))
    print "Percent default pics is: " + str(default_pics/float(len(uniques)))
    print "Percent urls is: " + str(url_count/float(len(uniques)))



    with open(out_file, "w+") as f:
        json.dump(uniques, f)

def get_friends_followers_plot(files):
    uniques = get_uniques(files)
    friends = []
    followers = []
    for u in uniques:
        friends.append(u['_friends_count'])
        followers.append(u['_followers_count'])

    print "Averages = ",
    print sum(friends) / float(len(friends)), sum(followers) / float(len(followers))
    sorted_list = sorted(zip(friends, followers))

    plt.title('Friends (green) vs. followers (red)')
    plt.plot([x for y,x in sorted_list], 'r--', [y for y,x in sorted_list], 'g--')
    plt.show()

def get_status_graph(files):
    uniques = get_uniques(files)
    statuses = []
    for u in uniques:
        statuses.append(u['_statuses_count'])

    sorted_list = sorted(statuses)
    print "Average = ",
    print sum(statuses) / float(len(statuses))
    print "Median = ",
    print numpy.median(numpy.array(statuses))

    # plt.title('Statuses count')
    # plt.plot(sorted_list[:-1], 'r^')
    # plt.show()
    # so=numpy.sort( statuses )
    # yvals=numpy.arange(len(so))/float(len(so))
    # plt.plot( so, yvals )
    # plt.title("CDF of status count")
    # plt.show()

def do_learning(filesBad, filesGood):
    from sklearn import svm

    uniques = get_uniques(filesBad)
    total_arr = []
    iden = []
    bad_last = []


    split = split_data(followerFilesInfoBad, followerFilesInfoGood)
    print len(split[0]), len(split[1]), len(split[2]), len(split[3])


    for u in split[0]:
        loc = 0
        if len(u['_location']) > 2:
            loc = 1
        temp = [loc, u['_statuses_count'], u['_ratio'], u['_followers_count'], u['_friends_count'], u['_favourites_count'], int(u['_geo_enabled']), int(u['_contributors_enabled']), int(u['_verified'])]
        total_arr.append(temp)
        iden.append(0)
        bad_last = temp

    for u in split[2]:
        loc = 0
        if len(u['_location']) > 2:
            loc = 1
        temp = [loc, u['_statuses_count'], u['_ratio'], u['_followers_count'], u['_friends_count'], u['_favourites_count'], int(u['_geo_enabled']), int(u['_contributors_enabled']), int(u['_verified'])]
        total_arr.append(temp)
        iden.append(1)

    clf = svm.SVC()
    clf.fit(total_arr, iden)

    total_test = len(split[1]) + len(split[3])
    num_bad_correct = 0
    num_good_correct = 0

    for u in split[1]:
        if len(u['_location']) > 2:
            loc = 1
        temp = [loc, u['_statuses_count'], u['_ratio'], u['_followers_count'], u['_friends_count'], u['_favourites_count'], int(u['_geo_enabled']), int(u['_contributors_enabled']), int(u['_verified'])]
        result = clf.predict([temp])[0]
        if result == 0:
            num_bad_correct += 1

    for u in split[3]:
        if len(u['_location']) > 2:
            loc = 1
        temp = [loc, u['_statuses_count'], u['_ratio'], u['_followers_count'], u['_friends_count'], u['_favourites_count'], int(u['_geo_enabled']), int(u['_contributors_enabled']), int(u['_verified'])]
        result = clf.predict([temp])[0]
        if result == 1:
            num_good_correct += 1


    total_correct = num_bad_correct + num_good_correct

    print "total: " + str(total_test)
    print "num_bad_correct: " + str(num_bad_correct)
    print "num_good_correct: " + str(num_good_correct)


    print "bad accuracy: " + str(float(num_bad_correct)/float(len(split[1])))
    print "good accuracy: " + str(float(num_good_correct)/float(len(split[3])))    
    print "total accuracy: " + str(float(total_correct)/float(total_test))


'''
randomly split training/test data at 9-1 ratio.
save to good_train, good_test, bad_train, bad_test
'''
def split_data(filesBad, filesGood):
    import random
    bad_uniques = get_uniques(filesBad)
    limit = len(bad_uniques) / 10

    train = []
    test = []
    random.shuffle(bad_uniques)

    test = bad_uniques[:limit]
    train = bad_uniques[limit:]

    good_uniques = get_uniques(filesGood)
    limit = len(good_uniques) / 10

    train2 = []
    test2 = []
    random.shuffle(good_uniques)

    test2 = good_uniques[:limit]
    train2 = good_uniques[limit:]

    return [train, test, train2, test2]
#get_all()
# post_processing(followerFilesInfo, "data/unique_results")

# get_friends_followers_plot(followerFilesInfo)
# get_status_graph(followerFilesInfo)



#split_data(followerFilesInfoBad)
do_learning(followerFilesInfoBad, followerFilesInfoGood)