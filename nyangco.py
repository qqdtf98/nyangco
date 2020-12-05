from bangtal import *
import time

import threading

mainScene = Scene("메인", "res/wallpaper/main.png")
mapScene = Scene("지도", "res/wallpaper/ingame2.png")
startScene = Scene("공격개시","res/wallpaper/ingame.png")
stage1 = Scene("한국","res/wallpaper/stage1.png")
stage2 = Scene("일본","res/wallpaper/stage2.png")
stage3 = Scene("중국","res/wallpaper/stage3.png")

stageNum = 1
prevScene = mainScene
nowScene = mainScene
stageObject = None

FRIEND = 0
ENEMY = 1

STAGE1 = 1
STAGE2 = 2
STAGE3 = 3

class Stage():
  def __init__(self,stage):
    if(stage == STAGE1):
      self.friend = Friend(100,1000,stage)
    elif(stage == STAGE2):
      self.friend = Friend(500,2000,stage)
    elif(stage == STAGE3):
      self.friend = Friend(1000,3000,stage)
    # 타이머 생성
    # 아군객체 생성, 적군 객체 생성

class Friend():
  def startTimer(self):
    self.timer = threading.Timer(1, self.startTimer)

    if self.moneyNow + 5 <= self.moneyMax:
      self.moneyNow = self.moneyNow + 5
    
    rest = self.moneyNow

    if int(self.moneyNow / 1000) > 0:
      self.moneyThou.setImage(f"res/etc/{int(self.moneyNow / 1000)}.png")
      rest = self.moneyNow - int(self.moneyNow / 1000)*1000
      self.moneyThou.show()
    else:
      self.moneyThou.hide()

    if int(rest/100) > 0:
      self.moneyHun.setImage(f"res/etc/{int(rest / 100)}.png")
      rest = self.moneyNow - int(self.moneyNow / 100)*100
      self.moneyHun.show()
    else:
      self.moneyHun.hide()

    if int(rest/10) > 0:
      self.moneyTens.setImage(f"res/etc/{int(rest/10)}.png")
      rest = self.moneyNow - int(self.moneyNow / 10)*10
      self.moneyTens.show()
    else:
      self.moneyTens.hide()

    self.moneyUnits.setImage(f"res/etc/{rest}.png")
    self.moneyUnits.show()

    self.timer.start()

  def endTimer(self):
    self.timer.cancel()

  def onMoneyTimeout(self):
    if self.moneyNow + 5 <= self.moneyMax:
      self.moneyNow = self.moneyNow + 5
      print(self.moneyNow)

  def __init__(self,moneyMax,castleStat,stage):
    self.moneyMax = moneyMax
    self.moneyNow = 0
    self.castle = Castle(FRIEND,castleStat)
    self.friends = [None for i in range(5)]
    self.moneyTotImg = Object(f"res/etc/{stage}_money.png")
    self.moneyTotImg.locate(nowScene,1000,650)
    self.moneyTotImg.setScale(0.5)
    self.moneyTotImg.show()
    self.sliceImg = Object(f"res/etc/slice.png")
    self.sliceImg.locate(nowScene,960,650)
    self.sliceImg.setScale(0.5)
    self.sliceImg.show()
    self.moneyThou = Object(f"res/etc/0.png")
    self.moneyThou.locate(nowScene,840,650)
    self.moneyThou.setScale(0.5)
    self.moneyHun = Object(f"res/etc/0.png")
    self.moneyHun.locate(nowScene,870,650)
    self.moneyHun.setScale(0.5)
    self.moneyTens = Object(f"res/etc/0.png")
    self.moneyTens.locate(nowScene,900,650)
    self.moneyTens.setScale(0.5)
    self.moneyUnits = Object(f"res/etc/0.png")
    self.moneyUnits.locate(nowScene,930,650)
    self.moneyUnits.setScale(0.5)

    self.startTimer()

class Castle():
  def __init__(self,type,status):
    self.status = status
    self.type = type

class Point(Object):
  def __init__(self,file,type):
    super().__init__(file)
    self.type = type
    self.onMouseAction = self.point_onClick

  def point_onClick(self,x,y,action):
    global stageNum
    if self.type == STAGE1:
      koreaImg.show()
      japanImg.hide()
      chinaImg.hide()
      stageNum = STAGE1
    elif self.type == STAGE2:
      koreaImg.hide()
      japanImg.show()
      chinaImg.hide()
      stageNum = STAGE2
    elif self.type == STAGE3:
      koreaImg.hide()
      japanImg.hide()
      chinaImg.show()
      stageNum = STAGE3

gameBtn = Object("res/etc/game.png")
gameBtn.locate(mainScene, 200,200)
gameBtn.show()

startBtn = Object("res/etc/start.png")
startBtn.locate(mapScene, 1000,200)
startBtn.setScale(0.5)
startBtn.show()

startImg = Object("res/wallpaper/start.png")
startImg.locate(mapScene,100,100)
startImg.setScale(0.2)

backBtn = Object("res/etc/back.png")

pauseBtn = Object("res/etc/pause.png")
pauseBtn.locate(stage1, 0,600)
pauseBtn.setScale(0.6)
pauseBtn.show()

pauseImg = Object("res/etc/pauseimg.png")
pauseImg.locate(stage1, 400,200)
continueBtn = Object("res/etc/continue.png")
continueBtn.locate(stage1, 530,330)
exitBtn = Object("res/etc/exit.png")
exitBtn.locate(stage1, 530,230)


catCastle = Object("res/castle/cat_castle.png")
enCastle = Object("res/castle/en_castle.png")

point1 = Point("res/etc/point.png",STAGE1)  #한국
point1.locate(mapScene, 580,335)
point1.show()
koreaImg = Object("res/etc/korea.png")
koreaImg.locate(mapScene, 660,585)
koreaImg.show()

point2 = Point("res/etc/point.png",STAGE2)  #일본
point2.locate(mapScene, 750,300)
point2.show()
japanImg = Object("res/etc/japan.png")
japanImg.locate(mapScene, 660,585)

point3 = Point("res/etc/point.png",STAGE3)  #중국
point3.locate(mapScene, 360,200)
point3.show()
chinaImg = Object("res/etc/china.png")
chinaImg.locate(mapScene, 660,585)

def gameBtn_onClick(x,y,action):
  global prevScene
  prevScene = mainScene
  backBtn.locate(mapScene,3,40)
  backBtn.show()
  mapScene.enter()
gameBtn.onMouseAction = gameBtn_onClick

def startBtn_onClick(x,y,action):
  global prevScene
  startImg.show()
  timer = Timer(1)
  timer.start()

  def onTimeout():
    global stageObject
    global nowScene
    startImg.hide()
    prevScene = mapScene
    if stageNum == STAGE1:
      nowScene = stage1
      stageObject = Stage(STAGE1)
    elif stageNum == STAGE2:
      nowScene = stage2
      stageObject = Stage(STAGE2)
    elif stageNum == STAGE3:
      nowScene = stage3
      stageObject = Stage(STAGE3)

    catCastle.locate(nowScene,1000,200)
    catCastle.show()
    enCastle.locate(nowScene,0,150)
    enCastle.setScale(0.8)
    enCastle.show()

    nowScene.enter()
    pauseBtn.locate(nowScene, 0,600)
    locatePauseBox(nowScene)
  timer.onTimeout = onTimeout

startBtn.onMouseAction = startBtn_onClick

def locatePauseBox(stage):
    pauseBtn.locate(stage, 0,600)
    pauseImg.locate(stage, 400,200)
    continueBtn.locate(stage, 530,330)
    exitBtn.locate(stage, 530,230)

def backBtn_onClick(x,y,action):
  prevScene.enter()
backBtn.onMouseAction = backBtn_onClick

def pauseBtn_onClick(x,y,action):
  pauseImg.show()
  continueBtn.show()
  exitBtn.show()
pauseBtn.onMouseAction = pauseBtn_onClick

def exitBtn_onClick(x,y,action):
  stageObject.friend.endTimer()
  prevScene.enter()
  hidePauseBox()
exitBtn.onMouseAction = exitBtn_onClick

def continueBtn_onClick(x,y,action):
  hidePauseBox()
continueBtn.onMouseAction = continueBtn_onClick

def hidePauseBox():
  pauseImg.hide()
  continueBtn.hide()
  exitBtn.hide()

startGame(mainScene)