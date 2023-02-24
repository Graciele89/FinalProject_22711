from django import forms
#https://en.wikipedia.org/wiki/List_of_cities,_boroughs_and_towns_in_the_Republic_of_Ireland
# list of cities, boroughs and towns in ireland   (THE FIRST ARGUMENT IS WHAT APPEARS ON DATABASE, THE SECOND IS WHAT THE USER SELECTS ON THE DROPDOWN  )
ireland_places = [('DUBLIN 1', "D1"), ('DUBLIN 2', "D2"), ('DUBLIN 3', "D3"), ('DUBLIN 4', "D4"), ('DUBLIN 5', "D5"), ('DUBLIN 6' "D6"), ('DUBLIN 6W', "D6W"), ('DUBLIN 7', "D7"),
                  ('DUBLIN 8', "D8"), ('DUBLIN 9', "D9"), ('DUBLIN 10', "D10"), ('DUBLIN 11', "D11"), ('DUBLIN 12', "D12"), ('DUBLIN 13', "D13"), ('DUBLIN 14', "D14"),
                  ('DUBLIN 15', "D15"), ('DUBLIN 16', "D16"), ('DUBLIN 17', "D17"), ('DUBLIN 18', "D18"), ('DUBLIN 20', "D20"), ('DUBLIN 22', "D22"), ('DUBLIN 24', "D24"),
                  ('DUN LAOGHAIRE', "Dun Laoghaire"), ('RATHDOWN', "Rathdown"), ('FINGAL', "Fingal"), ('CORK', "Cork"), ('LIMERICK', "Limerick"),
                  ('CLARE', "Clare"), ('GALWAY', "Galway"), ('WATERFORD', "Waterford"), ('KILKENNY', "Kilkenny"), ('32', "Drogheda"),
                  ('33', "Louth"), ('34', "Wexford"), ('35', "Sligo"), ('36', "Clonmel"), ('37', "Waterford"),
                  ('BRAY', "Bray"), ('39', "Wicklow"), ('40', "Navan"), ('41', "Ennis"), ('42', "Tralle"), ('43', "Kerry"),
                  ('44', "Carlow"),  ('45', "Laois"), ('46', "Naas"), ('47', "Kildare"), ('48', "Athlone"), ('49', "Roscommon"),
                  ('50', "Letterkenny"), ('51', "Donegal"), ('52', "Tullamore"), ('53', "Killarney"), ('54', "Arklow"),
                  ('55', "Cobh"), ('56', "Castlebar"), ('57', "Midleton"), ('58', "Mallow"), ('59', "Ballina"), ('60', "Enniscorthy"),
                  ('61', "Cavan"), ('62', "Athy"), ('63', "Longford"), ('64', "Dungarvan"), ('65', "Nenagh"), ('66', "Trim"), ('67', "New Ross"),
                  ('68', "Thurles"), ('69', "Youghal"), ('70', "Monaghan"), ('71', "Buncrana"), ('72', "Ballinasloe"), ('73', "Fermoy"),
                  ('74', "Westport"), ('75', "Carrick-on-Suir"), ('76', "Kells"), ('77', "Birr"), ('78', "Tipperary"), ('79', "Carrickmacross"),
                  ('80', "Kinsale"), ('81', "Listowel"), ('82', "Clonakilty"), ('83', "Cashel"), ('84', "Macroom"),
                  ('85', "Castleblayney"), ('86', "Kilrush"), ('87', "Skibbereen"), ('88', "Bundoran"), ('89', "Templemore"),
                  ('90', "Clones"), ('91', "Newbridge"), ('92', "Portlaoise"), ('93', "Mullingar"), ('94', "Balbriggan"),
                  ('95', "Greystones"), ('96', "Leixlip"), ('97', "Tramore"), ('98', "Shannon"), ('99', "Gorey"),
                  ('100', "Tuam"), ('101', "Edenderry"), ('102', "Bandon"), ('103', "Passage West"), ('104', "Loughrea"),
                  ('105', "Ardee"), ('106', "Mountmellick"), ('107', "Bantry"), ('108', "Muine Bheag"), ('109', "Boyle"),
                  ('110', "Ballyshannon"), ('111', "Cootehill"), ('112', "Ballybay"), ('113', "Belturbet"),
                  ('114', "Lismore"), ('115', "Kilkee"), ('116', "Granard"), ('117', "North Ireland")]


class PostForm(forms.Form):
    # image = forms.FileField()    //future implementation user photo
    text_destination = forms.ChoiceField(choices=ireland_places)
    text_origin = forms.ChoiceField(choices=ireland_places)
    text_date = forms.CharField(widget=forms.TextInput(attrs={'type': 'date'}))
    text_time = forms.CharField(widget=forms.TextInput(attrs={'type': 'time'}))

