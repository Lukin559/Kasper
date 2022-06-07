with open('function.txt') as a:
    function = a.read()
    a.seek(0, 0)
    lines = a.readlines()
R = 1
a = 1
print(lines)
for i in range(len(lines)):
    if i == 0:
        line = lines[0].split('(')[1].split(',')
        for s in range(len(line)):
            if s == len(line) - 1:
                n_l = line[s].split()[0]
                function = function.replace(n_l.strip(), ' ' + 'a'+str(s+1))
            else:
                if s != 0:
                    function = function.replace(line[s], ' ' + 'a'+str(s+1))
                else:
                    function = function.replace(line[s], 'a'+str(s+1))
        a = len(line)
    else:
        if lines[i].find('=[') != -1:
            n_l = lines[i].split('=')[0]
            function = function.replace(n_l.strip(), 'R'+str(R))
            R += 1
        if lines[i].find(' =') != -1:
            n_l = lines[i].split('=')[0]
            function = function.replace(n_l.strip(), 'a' + str(a))
            a += 1

function = function.replace(' )', ')')
function = function.replace(' (', '(')
function = function.replace(' ]', ']')
function = function.replace(' [', '[')
function = function.replace(' ,', ', ')
function = function.replace(' .', '.')
function = function.replace('=', '= ')

print(function)

