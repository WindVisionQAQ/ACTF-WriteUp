import cv2 #line:2
import base64 #line:3
smile =cv2 .CascadeClassifier ('haarcascade_smile.xml')#line:4
flag68 ='UVVGQlFVRkJRVUZCUVVGQlFVRkJRVUZCUVVGQlFVRkJRVUZCUVVGQlFVRkJRVUZCUVE9PQ=='#line:5
flag24 ='UTBORFEwTkRRME5EUTBORFEwTkRRME5EUTBORFEwTkRRME5EUTBORFEwTkRRME5EUXc9PQ=='#line:6
flag17 ='VkZSVVZGUlVWRlJVVkZSVVZGUlVWRlJVVkZSVVZGUlVWRlJVVkZSVVZGUlVWRlJVVkE9PQ=='#line:7
flag3 ='UmtaR1JrWkdSa1pHUmtaR1JrWkdSa1pHUmtaR1JrWkdSa1pHUmtaR1JrWkdSa1pHUmc9PQ=='#line:8
flag56 ='ZTN0N2UzdDdlM3Q3ZTN0N2UzdDdlM3Q3ZTN0N2UzdDdlM3Q3ZTN0N2UzdDdlM3Q3ZXc9PQ=='#line:9
flag61 ='V1ZsWldWbFpXVmxaV1ZsWldWbFpXVmxaV1ZsWldWbFpXVmxaV1ZsWldWbFpXVmxaV1E9PQ=='#line:10
flag43 ='TURBd01EQXdNREF3TURBd01EQXdNREF3TURBd01EQXdNREF3TURBd01EQXdNREF3TUE9PQ=='#line:11
flag87 ='ZFhWMWRYVjFkWFYxZFhWMWRYVjFkWFYxZFhWMWRYVjFkWFYxZFhWMWRYVjFkWFYxZFE9PQ=='#line:12
flag ="UVVOVVJudFpNSFZ5WDNOdGFURmxYMjFoYXpOelgwMWxYekZ1ZEc5NGFXTmhkRE5rZlE9PQ=="#line:13
flag100 ='Y25KeWNuSnljbkp5Y25KeWNuSnljbkp5Y25KeWNuSnljbkp5Y25KeWNuSnljbkp5Y2c9PQ=='#line:14
flag27 ='WDE5ZlgxOWZYMTlmWDE5ZlgxOWZYMTlmWDE5ZlgxOWZYMTlmWDE5ZlgxOWZYMTlmWHc9PQ=='#line:15
flag22 ='YzNOemMzTnpjM056YzNOemMzTnpjM056YzNOemMzTnpjM056YzNOemMzTnpjM056Y3c9PQ=='#line:16
flag97 ='YlcxdGJXMXRiVzF0YlcxdGJXMXRiVzF0YlcxdGJXMXRiVzF0YlcxdGJXMXRiVzF0YlE9PQ=='#line:17
flag74 ='YVdscGFXbHBhV2xwYVdscGFXbHBhV2xwYVdscGFXbHBhV2xwYVdscGFXbHBhV2xwYVE9PQ=='#line:18
flag64 ='TVRFeE1URXhNVEV4TVRFeE1URXhNVEV4TVRFeE1URXhNVEV4TVRFeE1URXhNVEV4TVE9PQ=='#line:19
flag75 ='WldWbFpXVmxaV1ZsWldWbFpXVmxaV1ZsWldWbFpXVmxaV1ZsWldWbFpXVmxaV1ZsWlE9PQ=='#line:20
flag85 ='WDE5ZlgxOWZYMTlmWDE5ZlgxOWZYMTlmWDE5ZlgxOWZYMTlmWDE5ZlgxOWZYMTlmWHc9PQ=='#line:21
flag10 ='YlcxdGJXMXRiVzF0YlcxdGJXMXRiVzF0YlcxdGJXMXRiVzF0YlcxdGJXMXRiVzF0YlE9PQ=='#line:22
flag75 ='WVdGaFlXRmhZV0ZoWVdGaFlXRmhZV0ZoWVdGaFlXRmhZV0ZoWVdGaFlXRmhZV0ZoWVE9PQ=='#line:23
flag86 ='YTJ0cmEydHJhMnRyYTJ0cmEydHJhMnRyYTJ0cmEydHJhMnRyYTJ0cmEydHJhMnRyYXc9PQ=='#line:24
flag10 ='TXpNek16TXpNek16TXpNek16TXpNek16TXpNek16TXpNek16TXpNek16TXpNek16TXc9PQ=='#line:25
flag3 ='YzNOemMzTnpjM056YzNOemMzTnpjM056YzNOemMzTnpjM056YzNOemMzTnpjM056Y3c9PQ=='#line:26
flag10 ='WDE5ZlgxOWZYMTlmWDE5ZlgxOWZYMTlmWDE5ZlgxOWZYMTlmWDE5ZlgxOWZYMTlmWHc9PQ=='#line:27
flag24 ='VFUxTlRVMU5UVTFOVFUxTlRVMU5UVTFOVFUxTlRVMU5UVTFOVFUxTlRVMU5UVTFOVFE9PQ=='#line:28
flag27 ='WldWbFpXVmxaV1ZsWldWbFpXVmxaV1ZsWldWbFpXVmxaV1ZsWldWbFpXVmxaV1ZsWlE9PQ=='#line:29
flag32 ='WDE5ZlgxOWZYMTlmWDE5ZlgxOWZYMTlmWDE5ZlgxOWZYMTlmWDE5ZlgxOWZYMTlmWHc9PQ=='#line:30
flag12 ='TVRFeE1URXhNVEV4TVRFeE1URXhNVEV4TVRFeE1URXhNVEV4TVRFeE1URXhNVEV4TVE9PQ=='#line:31
flag67 ='Ym01dWJtNXVibTV1Ym01dWJtNXVibTV1Ym01dWJtNXVibTV1Ym01dWJtNXVibTV1Ymc9PQ=='#line:32
flag91 ='ZEhSMGRIUjBkSFIwZEhSMGRIUjBkSFIwZEhSMGRIUjBkSFIwZEhSMGRIUjBkSFIwZEE9PQ=='#line:33
flag51 ='YjI5dmIyOXZiMjl2YjI5dmIyOXZiMjl2YjI5dmIyOXZiMjl2YjI5dmIyOXZiMjl2Ync9PQ=='#line:34
flag86 ='ZUhoNGVIaDRlSGg0ZUhoNGVIaDRlSGg0ZUhoNGVIaDRlSGg0ZUhoNGVIaDRlSGg0ZUE9PQ=='#line:35
flag28 ='YVdscGFXbHBhV2xwYVdscGFXbHBhV2xwYVdscGFXbHBhV2xwYVdscGFXbHBhV2xwYVE9PQ=='#line:36
flag56 ='WTJOalkyTmpZMk5qWTJOalkyTmpZMk5qWTJOalkyTmpZMk5qWTJOalkyTmpZMk5qWXc9PQ=='#line:37
flag27 ='WVdGaFlXRmhZV0ZoWVdGaFlXRmhZV0ZoWVdGaFlXRmhZV0ZoWVdGaFlXRmhZV0ZoWVE9PQ=='#line:38
flag0 ='ZEhSMGRIUjBkSFIwZEhSMGRIUjBkSFIwZEhSMGRIUjBkSFIwZEhSMGRIUjBkSFIwZEE9PQ=='#line:39
flag28 ='TXpNek16TXpNek16TXpNek16TXpNek16TXpNek16TXpNek16TXpNek16TXpNek16TXc9PQ=='#line:40
flag2 ='WkdSa1pHUmtaR1JrWkdSa1pHUmtaR1JrWkdSa1pHUmtaR1JrWkdSa1pHUmtaR1JrWkE9PQ=='#line:41
flag40 ='ZlgxOWZYMTlmWDE5ZlgxOWZYMTlmWDE5ZlgxOWZYMTlmWDE5ZlgxOWZYMTlmWDE5ZlE9PQ=='#line:42
cap =cv2 .VideoCapture (0)#line:43
def func2 ():#line:45
    OOO000OOOOOO00O00 =base64 .b64decode (base64 .b64decode (flag2 ))#line:46
    return OOO000OOOOOO00O00 #line:47
def func3 ():#line:48
    OO00O00000OO0O000 =base64 .b64decode (base64 .b64decode (flag40 ))#line:49
    return OO00O00000OO0O000 #line:50
def func1 ():#line:51
    OOO0O0OO0O0OOO000 =base64 .b64decode (base64 .b64decode (flag ))#line:52
    return OOO0O0OO0O0OOO000 #line:53
def func4 ():#line:54
    O000OO00O00OO0O00 =base64 .b64decode (base64 .b64decode (flag28 ))#line:55
    return O000OO00O00OO0O00 #line:56
def O00OO00OOO00OO0O0 ():#line:57
    O000O000O0OOOO0OO =True #line:58
    while O000O000O0OOOO0OO :#line:59
        O000O000O0OOOO0OO ,O0O0O00O00OOOOOO0 =cap .read ()#line:60
        O00OO000OO0OO0O0O =cv2 .cvtColor (O0O0O00O00OOOOOO0 ,cv2 .COLOR_BGR2GRAY )#line:61
        O00OO000OO0OO0O0O =cv2 .equalizeHist (O00OO000OO0OO0O0O )#line:62
        O0OO0000O0OOOO0OO =smile .detectMultiScale (O00OO000OO0OO0O0O ,scaleFactor =1.5 ,minNeighbors =40 ,)#line:67
        for (O0OOO0OO00000O000 ,O0OO0O0O0000OOO00 ,OO0O000O0O000000O ,O0OO0O0O0OOOO0OO0 )in O0OO0000O0OOOO0OO :#line:68
            OO0O0O0OOOO00O0OO =O00OO000OO0OO0O0O [O0OO0O0O0000OOO00 :(O0OO0O0O0000OOO00 +O0OO0O0O0OOOO0OO0 ),O0OOO0OO00000O000 :(O0OOO0OO00000O000 +OO0O000O0O000000O )]#line:69
            OO00O0000OO00O00O =[]#line:70
        for (O0OOO0OO00000O000 ,O0OO0O0O0000OOO00 ,OO0O000O0O000000O ,O0OO0O0O0OOOO0OO0 )in O0OO0000O0OOOO0OO :#line:71
            cv2 .rectangle (O0O0O00O00OOOOOO0 ,(O0OOO0OO00000O000 ,O0OO0O0O0000OOO00 ),(O0OOO0OO00000O000 +OO0O000O0O000000O ,O0OO0O0O0000OOO00 +O0OO0O0O0OOOO0OO0 ),(255 ,0 ,0 ),2 )#line:72
        if (len (O0OO0000O0OOOO0OO )==1 ):#line:73
            print (func1 ())#line:74
        cv2 .imshow ('video',O0O0O00O00OOOOOO0 )#line:75
        O00000O0000OOO0O0 =cv2 .waitKey (1 )#line:76
        if O00000O0000OOO0O0 ==27 :#line:77
            break #line:78
def O00OO00OOO0OOO000 ():#line:79
    print ("Please calculate:968603471894120+2194120481028230910-23131223129=?")#line:80
    O0O0O0OOO0O0000O0 =input ()#line:81
    try :#line:82
        O0O0O0OOO0O0000O0 =int (O0O0O0OOO0O0000O0 )#line:83
        if O0O0O0OOO0O0000O0 ==int (968603471894120 +2194120481028230910 -23131223129 ):#line:84
            print ("Good, now give me your smile,I will give you flag! Enjoy your time~")#line:85
            print ("Are you ready?(Y/N)")#line:86
            OO000000O00OO00OO =input ()#line:87
            if OO000000O00OO00OO =="Y":#line:88
                O00OO00OOO00OO0O0 ()#line:89
            else :#line:90
                print ("Bye!!")#line:91
        else :#line:92
            print ("Try again")#line:93
    except :#line:94
        print ("ERROR")#line:95
O00OO00OOO0OOO000 ()#line:96
cap .release ()#line:97
cv2 .destroyAllWindows ()