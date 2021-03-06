import configparser
import design as ds


# 프로그램이 시작했을 때 처음 한번만 사용합니다.
def chckInitFst(self):
    config = configparser.ConfigParser()
    config.read('setting.ini')

    if not 'STYLE' in config:
        config['STYLE'] = {
            'theme': 'White',
            'font_family': '맑은 고딕',
            'font_size': '10',
            'width': str(self.size().width()),
            'height': str(self.size().height()),
            'pos_x': str(self.pos().x()),
            'pos_y': str(self.pos().y()),
            'tool_pos': '2',
            'tool_style': 'icon',
            'table_grid': 'true',
            'table_header_color': '#ffff00',
            'table_row_color': '#ffffff',
            'table_colored_row': 'all'
        }
        with open('setting.ini', 'w') as configfile:
            config.write(configfile)

    if not 'theme' in config['STYLE']:
        config['STYLE']['theme'] = 'White'
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
        config['STYLE']['width'] = str(self.size().width())
        with open('setting.ini', 'w') as configfile:
            config.write(configfile)

    if not 'height' in config['STYLE']:
        config['STYLE']['height'] = str(self.size().height())
        with open('setting.ini', 'w') as configfile:
            config.write(configfile)

    if not 'pos_x' in config['STYLE']:
        config['STYLE']['pos_x'] = str(self.pos().x())
        with open('setting.ini', 'w') as configfile:
            config.write(configfile)

    if not 'pos_y' in config['STYLE']:
        config['STYLE']['pos_y'] = str(self.pos().y())
        with open('setting.ini', 'w') as configfile:
            config.write(configfile)

    if not 'tool_pos' in config['STYLE']:
        config['STYLE']['tool_pos'] = '2'
        with open('setting.ini', 'w') as configfile:
            config.write(configfile)

    if not 'tool_style' in config['STYLE']:
        config['STYLE']['tool_style'] = 'icon'
        with open('setting.ini', 'w') as configfile:
            config.write(configfile)

    if not 'table_grid' in config['STYLE']:
        config['STYLE']['table_grid'] = 'true'
        with open('setting.ini', 'w') as configfile:
            config.write(configfile)

    if not 'table_header_color' in config['STYLE']:
        config['STYLE']['table_header_color'] = '#ffff00'
        with open('setting.ini', 'w') as configfile:
            config.write(configfile)

    if not 'table_row_color' in config['STYLE']:
        config['STYLE']['table_row_color'] = '#ffffff'
        with open('setting.ini', 'w') as configfile:
            config.write(configfile)

    if not 'table_colored_row' in config['STYLE']:
        config['STYLE']['table_colored_row'] = 'all'
        with open('setting.ini', 'w') as configfile:
            config.write(configfile)

    self.resize(int(config['STYLE']['width']), int(config['STYLE']['height']))
    self.move(int(config['STYLE']['pos_x']), int(config['STYLE']['pos_y']))
    ds.selectMainStyle(self, config['STYLE']['theme'],
                       config['STYLE']['font_family'], config['STYLE']['font_size'],
                       config['STYLE']['tool_pos'], config['STYLE']['tool_style'],
                       config['STYLE']['table_grid'],
                       config['STYLE']['table_header_color'],
                       config['STYLE']['table_row_color'],
                       config['STYLE']['table_colored_row'])


def writeIni(self, par, bg, size, font, tool_pos, tool_style,
             table_grid, table_header_color, table_row_color, table_colored_row):
    config = configparser.ConfigParser()
    config.read('setting.ini')
    config['STYLE'] = {
        'theme': bg,
        'font_family': font.family(),
        'font_size': size,
        'tool_pos': tool_pos,
        'tool_style': tool_style,
        'table_grid': table_grid,
        'table_header_color': table_header_color,
        'table_row_color': table_row_color,
        'table_colored_row': table_colored_row
    }
    with open('setting.ini', 'w') as configfile:
        config.write(configfile)

    ds.selectMainStyle(par, config['STYLE']['theme'],
                       config['STYLE']['font_family'], config['STYLE']['font_size'],
                       config['STYLE']['tool_pos'], config['STYLE']['tool_style'],
                       config['STYLE']['table_grid'],
                       config['STYLE']['table_header_color'],
                       config['STYLE']['table_row_color'],
                       config['STYLE']['table_colored_row'])
    ds.setSettStyle(self, config['STYLE']['theme'],
                       config['STYLE']['font_family'], config['STYLE']['font_size'])


def writeIniLast(self):
    config = configparser.ConfigParser()
    config.read('setting.ini')
    config['STYLE']['width'] = str(self.size().width())
    config['STYLE']['height'] = str(self.size().height())
    config['STYLE']['pos_x'] = str(self.pos().x())
    config['STYLE']['pos_y'] = str(self.pos().y())
    with open('setting.ini', 'w') as configfile:
        config.write(configfile)

def chgToolBarBorder(self):
    config = configparser.ConfigParser()
    config.read('setting.ini')
    config['STYLE']['tool_pos'] = str(self.toolBarArea(self.toolbar))
    with open('setting.ini', 'w') as configfile:
        config.write(configfile)

    c = ds.Color()
    if config['STYLE']['theme'] == 'White':
        c.setWhite()
    elif config['STYLE']['theme'] == 'Blue':
        c.setBlue()
    elif config['STYLE']['theme'] == 'Green':
        c.setGreen()

    if self.toolbar.isFloating():
        ds.setToolBarBorder(self, '0', c.separate_color,
                            config['STYLE']['font_family'], config['STYLE']['font_size'])
    else:
        ds.setToolBarBorder(self, config['STYLE']['tool_pos'], c.separate_color,
                            config['STYLE']['font_family'], config['STYLE']['font_size'])

# setting이 뜰 때 한번만 사용합니다.
def chckIniSett(self):
    config = configparser.ConfigParser()
    config.read('setting.ini')
    ds.setSettStyle(self, config['STYLE']['theme'],
                    config['STYLE']['font_family'], config['STYLE']['font_size'])


# file absorptoin 창이 뜰 때 한번만 사용합니다.
def chckIniFAbsor(self):
    config = configparser.ConfigParser()
    config.read('setting.ini')
    ds.setFAbsorColor(self, config['STYLE']['theme'],
                      config['STYLE']['font_family'], config['STYLE']['font_size'])


# cell absorptoin 창이 뜰 때 한번만 사용합니다.
def chckIniCAbsor(self):
    config = configparser.ConfigParser()
    config.read('setting.ini')
    ds.setCAbsorColor(self, config['STYLE']['theme'],
                         config['STYLE']['font_family'], config['STYLE']['font_size'])


# join 창이 뜰 때 한번만 사용합니다.
def chckIniJoin(self):
    config = configparser.ConfigParser()
    config.read('setting.ini')
    ds.setJoinColor(self, config['STYLE']['theme'],
                       config['STYLE']['font_family'], config['STYLE']['font_size'])
