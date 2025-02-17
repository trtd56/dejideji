import pyxel

class Game:
    def __init__(self):
        pyxel.init(160, 120, title="Click to Move")
        pyxel.load("deji.pyxres")  # 画像リソースをロード
        self.x = 80  # キャラクターの初期位置
        self.y = 60
        self.speed = 2  # 移動速度
        self.target_x = self.x  # 目標地点
        self.direction = -1  # -1: 右向き, 1: 左向き
        self.frame = 0  # アニメーションフレーム
        self.frame_count = 0  # アニメーション更新用カウンタ
        pyxel.run(self.update, self.draw)

    def update(self):
        moving = self.x != self.target_x  # 移動中か判定

        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.target_x = pyxel.mouse_x  # クリックした位置を目標にする
            self.direction = -1 if self.target_x > self.x else 1  # 方向を更新
        
        # キャラクターを目標地点に向けて移動させる
        if self.x < self.target_x:
            self.x = min(self.x + self.speed, self.target_x)
        elif self.x > self.target_x:
            self.x = max(self.x - self.speed, self.target_x)
        
        # 移動中のみアニメーションをゆっくり更新
        if moving:
            self.frame_count += 1
            if self.frame_count % 10 == 0:  # 10フレームごとに更新
                self.frame = 1 if self.frame == 2 else 2  # 1 ↔ 2 のループ
        else:
            self.frame = 0  # 停止中は最初のフレーム
    
    def draw(self):
        pyxel.cls(0)
        
        # フレームごとの座標を設定
        if self.frame == 0:
            u, v = 0, 0
        elif self.frame == 1:
            u, v = 26, 0
        else:
            u, v = 0, 38
        
        pyxel.blt(self.x - 12, self.y - 18, 0, u, v, 24 * self.direction, 36, 0)  # 画像サイズを修正して描画

Game()
