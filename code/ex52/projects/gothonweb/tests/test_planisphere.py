from gothonweb.planisphere import *


def test_room():
    gold = Room("黄金の部屋",
                "この部屋は黄金がいっぱいだ。北側に扉がある。")
    assert gold.name == "黄金の部屋"
    assert gold.paths == {}

def test_room_paths():
    center = Room("中央の部屋", "中央の部屋(テスト用)")
    north = Room("北側の部屋", "北側の部屋(テスト用)")
    south = Room("南側の部屋", "南側の部屋(テスト用)")

    center.add_paths({'北': north, '南': south})
    assert center.go('北') == north
    assert center.go('南') == south

def test_map():
    start = Room("スタート地点",
                 "西に行くことも、穴の中を下ることもできる。")
    west = Room("森",
                "ここには木がたくさんある。君は東に行くことができる。")
    down = Room("迷宮",
                "ここは真っ暗だ。君は上に行くことができる。")

    start.add_paths({'西': west, '下': down})
    west.add_paths({'東': start})
    down.add_paths({'上': start})

    assert start.go('西') == west
    assert start.go('西').go('東') == start
    assert start.go('下').go('上') == start

def test_gothon_game_map():
    start_room = load_room(START)
    assert start_room.go('撃つ') == generic_death
    assert start_room.go('身をかわす') == generic_death

    room = start_room.go('ジョークをいう')
    assert room == laser_weapon_armory
