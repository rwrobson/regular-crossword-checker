import re


xpatt = [ '.*H.*H.*',
          '(DI|NS|TH|OM)*',
          'F.*[AO].*[AO].*',
          '(O|RHH|MM)*',
          '.*',
          'C*MC(CCC|MM)*',
          '[^C]*[^R]*III.*',
          '(...?)\\1*', 
          '([^X]|XCC)*', 
          '(RR|HHH)*.?', 
          'N.*X.X.X.*E', 
          'R*D*M*', 
          '.(C|HH)*' ]

ypatt = [ '.*SE.*UE.*',
          '.*LR.*RL.*',
          '.*OXR.*',
          '([^EMC]|EM)*',
          '(HHX|[^HX])*',
          '.*PRR.*DDC.*',
          '.*',
          '[AM]*CM(RC)*R?',
          '([^MC]|MM|CC)*',
          '(E|CR|MN)*',
          'P+(..)\\1.*',
          '[CHMNOR]*I[CHMNOR]*',
          '(ND|ET|IN)[^X]*' ]
          
zpatt = [ '.*G.*V.*H.*',
          '[CR]*',
          '.*XEXM*',
          '.*DD.*CCM.*',
          '.*XHCR.*X.*',
          '.*(.)(.)(.)(.)\\4\\3\\2\\1.*',
          '.*(IN|SE|HI)',
          '[^C]*MMM[^C]*',
          '.*(.)C\\1X\\1.*',
          '[CEIMU]*OH[AEMOR]*',
          '(RX|[^R])*',
          '[^M]*M[^M]*',
          '(S|MM|HHH)*',]

def lstr(row):
    if row < 7:
        return row + 7
    else:
        return 19 - row

xstr = [ 
       'NHPEHAM', 
       'DIOMOMOM', 
       'FOXNXAXPH', 
       'MMOMMMMRHH',
       'MCXNMMCRXEM',
       'CMCCCCMMMMMM',
       'HRXRCMIIIHXLS',
       'OREOREOREORE',
       'VCXCCHHMXCC',
       'RRRRHHHRRU',
       'NCXDXEXLE',
       'RRDDMMMM',
       'GCCHHCC' ]


#xstr = [ 
#       'NHPEHAM', 
#       'DIOMOMOM', 
#       'FOXNXAXPH', 
#       'MMOMMMMRHH',
#       'MCXNMMCRXEM',
#       'CMCCCCMMMMMM',
#       'RRXRCMIIIOXLS',
#       'HREHREHREHRE',
#       'VCXCCHHMOO ',
#       'RRRRHHHRRU',
#       'NCXDXEXLE',
#       'RRDDMMMM',
#       'GCCHHCC' ]
# Y 2: "MMXHORXMH" does not match ".*OXR.*"

ystr=[]
zstr=[]
       
for row in range(0, 13):
    if len(xstr[row]) != lstr(row):
        print("xw[%d] length == %d, not %d" % (row, len(xstr[row]), lstr(row)))

for row in range(0, 13):
    ys = ''
    zs = ''
    rowoff = 0 if row < 7 else row - 6
    for pos in range(0, lstr(row)):
        posoff = 0 if pos < 7 - rowoff else pos + rowoff - 6
        ys = ys + xstr[pos + rowoff][row - posoff]
        zs = zs + xstr[12 - (pos + rowoff)][row - posoff]
    ystr.append(ys)
    zstr.append(zs)

ystr = list(reversed(ystr))

def test(dim, row, regex, test_str):
    result = re.match("^%s$" % regex, test_str)
    if not result:
      print('%s %d: "%s" does not match "%s"' % (dim, row, test_str, regex))	

for row in range(0, 12):
    test("X", row, xpatt[row], xstr[row])      
    test("Y", row, ypatt[row], ystr[row])      
    test("Z", row, zpatt[row], zstr[row])      