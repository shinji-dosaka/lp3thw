from sys import exit
from random import randint
from textwrap import dedent


class Scene(object):

    def enter(self):
        print("この場面はまだ構成されていない。")
        print("このクラスをサブクラス化してenter()を実装すること。")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('ゲームクリア')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # 最後の場面は必ず出力すること。
        current_scene.enter()


class Death(Scene):

    quips = [
        "君は死んだ。なんて下手くそなんだ。",
        "母親は君のことを誇りに思うだろう。彼女がもっと賢ければね。",
        "君は負け犬だ。",
        "君よりも私の犬の方が賢い。",
        "父親の冗談の方がましだ。"
    ]

    def enter(self):
        print(Death.quips[randint(0, len(Death.quips) - 1)])
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
              第25惑星パーカルのゴーソンが君たちの宇宙船に侵入し、乗組
              員全員がやられてしまった。最後の生き残りが君だ。君の最後
              の任務は武器庫にある中性子爆弾をブリッジに設置し、宇宙船
              を爆破する前に脱出用ポッドで脱出することだ。

              君が武器庫に向かって中央通路を駆け下りたそのとき、一匹の
              ゴーソンが目の前に現れた。そいつは赤い鱗状の肌と汚れた黒
              い歯をもち、邪悪な道化師のようなコスチュームをその憎悪に
              満ちた身にまとっていた。そして、武器庫のドアの前に居座り、
              君に銃を向けていまにも引き金を引こうとしている。
              """))

        action = input("> ")

        if action == "撃つ":
            print(dedent("""
                  君はすばやくブラスターを抜き、ゴーソンに向けてレーザーを
                  発砲した。しかし、そいつの道化師のようなコスチュームが体
                  の周りを流れるように動き回り、コスチュームをかすっただけ
                  でゴーソンを打ちそこなってしまった。母親に買ってもらった
                  新しいコスチュームをダメにしたことで、ゴーソンを完全に怒
                  らせてしまった。そいつは君の顔めがけて何発もブラスターを
                  発砲し、それは君が死ぬまで続いた。そして、君はゴーソンに
                  食べられてしまった。
                  """))
            return 'ゲームオーバー'

        elif action == "身をかわす":
            print(dedent("""
                  世界クラスのボクサーのように君はすばやく身をかわし、ゴー
                  ソンのブラスターから放たれたレーザーを間一髪でよけた。君
                  は巧みなステップで身をかわしていたが、足を滑らせてしまい、
                  金属の壁で頭を強打し一瞬気を失ってしまった。気づいたとき
                  には、ゴーソンに頭を踏みつけられ、君は食べられてしまった。
                  """))
            return 'ゲームオーバー'

        elif action == "ジョークをいう":
            print(dedent("""
                  幸運なことに、君は訓練学校でゴーソンの下品なジョークを学
                  んでいた。そこで覚えたジョークをゴーソンに向かっていった。
                  「Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr,
                    fur fvgf nebhaq gur ubhfr」
                  ゴーソンは一瞬動きを止め、笑いをこらえていたが、ついに笑
                  い転げて身動きできなくなってしまった。その隙をついて、君
                  はゴーソンに駆け寄り、そいつの頭を打ち砕いた。そして、武
                  器庫のドアを開けた。
                  """))
            return 'レーザー武器庫'

        else:
            print("失敗だ!")
            return '中央通路'


class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
              君は武器庫に転がり込み、身をかがめて、ほかにもゴーソンが
              隠れていないか部屋の中を探った。何の気配もなく、ひっそり
              と静まり返っていた。君は立ち上がり、部屋の奥まで駆け寄っ
              て、中性子爆弾の容器を見つけた。その容器はロックがかかっ
              ており、爆弾を入手するには暗証番号が必要だ。十回間違える
              と永遠にロックされ、爆弾を手に入れることはできない。暗証
              番号は三桁の数字だ。
              """))

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[暗証番号]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("ブッブー!")
            guesses += 1
            guess = input("[暗証番号]> ")

        if guess == code:
            print(dedent("""
                  音を立てて容器が開き、封印がとかれた。君は中性子爆弾をつ
                  かみ、その爆弾を正しい場所に置くために全速力でブリッジに
                  向かった。
                  """))
            return 'ブリッジ'
        else:
            print(dedent("""
                  最後の警告音が鳴り、容器が永遠にロックされたことを告げる
                  不快な音が聞こえた。君はその場所にへたり込んでしまった。
                  そして、ゴーソンは宇宙船を爆破し、君も宇宙の藻屑と消えた。
                  """))
            return 'ゲームオーバー'


class TheBridge(Scene):

    def enter(self):
        print(dedent("""
              君は中性子爆弾を手にブリッジに姿を現した。そこには、先ほ
              どよりももっと醜い道化師のようなコスチュームを身にまとっ
              た五匹のゴーソンが宇宙船をコントロールしようとしていた。
              ゴーソンたちは驚いたが、君の手の中にある爆弾に気づき、手
              にしている武器を使えないでいた。
              """))

        action = input("> ")

        if action == "爆弾を投げる":
            print(dedent("""
                  パニックに陥った君はゴーソンに向かって爆弾を投げ、ドアに
                  向かって慌てて逃げようとした。爆弾を投げると同時に、君は
                  ゴーソンから背中を撃たれてしまった。死ぬ間際に一匹のゴー
                  ソンが必死になって爆弾の起爆装置を解除しようとしているの
                  が見えた。おそらく爆弾は爆発し、ゴーソンたちも宇宙船もろ
                  とも宇宙の藻屑と消えるだろう。
                  """))
            return 'ゲームオーバー'

        elif action == "爆弾を置く":
            print(dedent("""
                  君は手にもった爆弾にブラスターを向けた。ゴーソンは額に汗
                  をにじませて手を上げている。君はドアに向かって少しずつ後
                  ろに下がり、ドアを開けて慎重に爆弾を床の上に置いた。爆弾
                  に向かってブラスターを構えながらドアの外に向かってジャン
                  プし、スイッチを押してドアを閉じた。そして、ゴーソンが外
                  に出られないようにブラスターでそのスイッチを撃った。爆弾
                  はブリッジに設置した。この宇宙船から脱出するために君は脱
                  出用ポッドに向かって走った。
                  """))
            return '脱出用ポッド'

        else:
            print("失敗だ!")
            return "ブリッジ"


class EscapePod(Scene):

    def enter(self):
        print(dedent("""
              宇宙船が爆発する前に脱出用ポッドへ行くため、君は大急ぎで
              船の中を駆け抜けた。ほかのゴーソンは船にはいないようだ。
              誰にも邪魔されずに脱出用ポッドのある部屋に到着した。いく
              つかのポッドは破損しているかもしれないが調べる時間はない。
              脱出用ポッドは全部で五台ある。どれかを選ばなければならな
              い。
              """))

        good_pod = randint(1, 5)
        guess = input("[ポッド番号]> ")

        if int(guess) != good_pod:
            print(dedent(f"""
                  君は{guess}番ポッドに飛び乗り、脱出ボタンを押した。ポッドは宇
                  宙空間に向かって滑り出した。その後ポッドは崩壊し、君の体
                  もジャムのように押しつぶされた。
                  """))
            return 'ゲームオーバー'

        else:
            print(dedent(f"""
                  君は{guess}番ポッドに飛び乗り、脱出ボタンを押した。ポッドは眼
                  下の惑星に向かって宇宙空間に滑り出た。振り返ると、宇宙船
                  が崩壊した次の瞬間、明るい星のように爆発した。ちょうどそ
                  の時、爆発した宇宙船からゴーソンの宇宙船が逃れるのが見え
                  た。君の任務は完了した!
                  """))
            return 'ゲームクリア'


class Finished(Scene):

    def enter(self):
        print("よくやった。君の勝ちだ!")
        return 'ゲームクリア'


class Map(object):

    scenes = {
        '中央通路': CentralCorridor(),
        'レーザー武器庫': LaserWeaponArmory(),
        'ブリッジ': TheBridge(),
        '脱出用ポッド': EscapePod(),
        'ゲームオーバー': Death(),
        'ゲームクリア': Finished(),
    }

    def __init__(self, start_scene_name):
        self.start_scene_name = start_scene_name

    def next_scene(self, scene_name):
        scene = Map.scenes.get(scene_name)
        return scene

    def opening_scene(self):
        return self.next_scene(self.start_scene_name)


a_map = Map('中央通路')
a_game = Engine(a_map)
a_game.play()
