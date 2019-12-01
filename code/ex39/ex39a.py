things = ['a', 'b', 'c', 'd']
print(things[1])
things[1] = 'z'
print(things[1])
things

stuff = {'名前': 'Zed', '年齢': 39, '身長': 6 * 12 + 2}
print(stuff['名前'])
print(stuff['年齢'])
print(stuff['身長'])
stuff['市'] = "サンフランシスコ"
print(stuff['市'])

stuff[1] = "ワォ"
stuff[2] = "素晴らしい"
print(stuff[1])
print(stuff[2])

del stuff['市']
del stuff[1]
del stuff[2]
stuff
