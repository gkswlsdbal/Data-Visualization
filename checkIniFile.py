import configparser
import design as ds
from PyQt5.QtGui import *


# 프로그램이 시작했을 때 처음 한번만 사용합니다.
def chckInitFst(self):
    config = configparser.ConfigParser()
    config.read('setting.ini')

    if not 'STYLE' in config:
        config['STYLE'] = {
            'theme': 'white',
            'font_family': '맑은 고딕',
            'font_size': '10',
            'width': str(self.frameGeometry().width()),
            'height': str(self.frameGeometry().height()),
            'pos_x': str(self.x()),
            'pos_y': str(self.y())
        }
        with open('setting.ini', 'w') as configfile:
            config.write(configfile)

    if not 'theme' in config['STYLE']:
        config['STYLE']['theme'] = 'white'
        with open('setting.ini', 'w') as configfile:
            config.write(configfile)

    if not 'font_family' in config['STYLE']:
        config['STYLE']['font_family'] = '맑은 고딕'
        with open('setting.ini', 'w') as configfile:
            config.write(configfile)

    if not 'font_size' in config['STYLE']:
        config['STYLE']['font_size'] = '10'
        with open('setting.ini', 'w') as configfile:
            config.write(configfile)

    if not 'width' in config['STYLE']:
        config['STYLE']['width'] = str(self.frameGeometry().width())
        with open('setting.ini', 'w') as configfile:
            config.write(configfile)

    if not 'height' in config['STYLE']:
        config['STYLE']['height'] = str(self.frameGeometry().height())
        with open('setting.ini', 'w') as configfile:
            config.write(configfile)

    if not 'pos_x' in config['STYLE']:
        config['STYLE']['pos_x'] = str(self.x())
        with open('setting.ini', 'w') as configfile:
            config.write(configfile)

    if not 'pos_y' in config['STYLE']:
        config['STYLE']['pos_y'] = str(self.y())
        with open('setting.ini', 'w') as configfile:
            config.write(configfile)

    self.resize(int(config['STYLE']['width']), int(config['STYLE']['height']))
    self.move(int(config['STYLE']['pos_x']), int(config['STYLE']['pos_y']))
    ds.selectMainColor(self, config['STYLE']['theme'],
                       config['STYLE']['font_family'], config['STYLE']['font_size'])

def writeIni(self, par, bg, size, font):
    config = configparser.ConfigParser()
    config.read('setting.ini')
    config['STYLE'] = {
        'theme': bg,
        'font_family': font.family(),
        'font_size': size
    }
    with open('setting.ini', 'w') as configfile:
        config.write(configfile)

    ds.selectMainColor(par, config['STYLE']['theme'],
                       config['STYLE']['font_family'], config['STYLE']['font_size'])
    ds.selectSettColor(self, config['STYLE']['theme'],
                       config['STYLE']['font_family'], config['STYLE']['font_size'])

def writeIniLast(self):
    config = configparser.ConfigParser()
    config.read('setting.ini')
    config['STYLE']['width'] = str(self.frameGeometry().width())
    config['STYLE']['height'] = str(self.frameGeometry().height())
    config['STYLE']['pos_x'] = str(self.x())
    config['STYLE']['pos_y'] = str(self.y())
    with open('setting.ini', 'w') as configfile:
        config.write(configfile)


# setting이 뜰 때 한번만 사용합니다.
def chckIniDialog(self):
    config = configparser.ConfigParser()
    config.read('setting.ini')
    ds.selectSettColor(self, config['STYLE']['theme'],
                       config['STYLE']['font_family'], config['STYLE']['font_size'])


# file absorptoin 창이 뜰 때 한번만 사용합니다.
def chckIniFAbsor(self):
    config = configparser.ConfigParser()
    config.read('setting.ini')
    ds.selectFAbsorColor(self, config['STYLE']['theme'],
                         config['STYLE']['font_family'], config['STYLE']['font_size'])

# cell absorptoin 창이 뜰 때 한번만 사용합니다.
def chckIniCAbsor(self):
    config = configparser.ConfigParser()
    config.read('setting.ini')
    ds.selectCAbsorColor(self, config['STYLE']['theme'],
                         config['STYLE']['font_family'], config['STYLE']['font_size'])

# join 창이 뜰 때 한번만 사용합니다.
def chckIniJoin(self):
    config = configparser.ConfigParser()
    config.read('setting.ini')
    ds.selectJoinColor(self, config['STYLE']['theme'],
                         config['STYLE']['font_family'], config['STYLE']['font_size'])
