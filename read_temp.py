import re

text = '''
  v5[0] = -120;
  v5[1] = 118;
  v5[2] = -41;
  v5[3] = 122;
  v5[4] = -76;
  v5[5] = 90;
  v5[6] = 76;
  v5[7] = -57;
  v5[8] = -36;
  v5[9] = -17;
  v5[10] = -55;
  v5[11] = -114;
  v5[12] = -38;
  v5[13] = 89;
  v5[14] = 14;
  v5[15] = -104;
  v5[16] = -113;
  v5[17] = -5;
  v5[18] = 11;
  v5[19] = -44;
  v5[20] = -30;
  v5[21] = -79;
  v5[22] = 19;
  v5[23] = 96;
  v5[24] = -26;
  v5[25] = -57;
  v5[26] = -122;
  v5[27] = 43;
  v5[28] = -36;
  v5[29] = 113;
  v5[30] = -44;
  v5[31] = 48;
  v5[32] = -19;
  v5[33] = 42;
  v5[34] = -119;
  v5[35] = 97;
  v5[36] = -125;
  v5[37] = 128;
  v5[38] = 40;
  v5[39] = -14;
  v5[40] = -110;
  v5[41] = -30;
'''
a = []
x = re.findall(re.compile('\[(\d+)] = (.*?);'), text)
for i in x:
    a.append(0)
for i in x:
    a[int(i[0])] = int(i[1])
print('a =', a)

