from django import forms
#https://en.wikipedia.org/wiki/List_of_cities,_boroughs_and_towns_in_the_Republic_of_Ireland
# list of cities, boroughs and towns in ireland   (THE FIRST ARGUMENT IS WHAT APPEARS ON DATABASE, THE SECOND IS WHAT THE USER SELECTS ON THE DROPDOWN  )
ireland_places = [('DUBLIN 1', "D1"), ('DUBLIN 2', "D2"), ('DUBLIN 3', "D3"), ('DUBLIN 4', "D4"), ('DUBLIN 5', "D5"),
                  ('DUBLIN 6',"D6"), ('DUBLIN 6W', "D6W"), ('DUBLIN 7', "D7"), ('DUBLIN 8', "D8"), ('DUBLIN 9', "D9"),
                  ('DUBLIN 10', "D10"), ('DUBLIN 11', "D11"), ('DUBLIN 12', "D12"), ('DUBLIN 13', "D13"), ('DUBLIN 14', "D14"),
                  ('DUBLIN 15', "D15"), ('DUBLIN 16', "D16"), ('DUBLIN 17', "D17"), ('DUBLIN 18', "D18"), ('DUBLIN 20', "D20"),
                  ('DUBLIN 22', "D22"), ('DUBLIN 24', "D24"), ('DUN LAOGHAIRE', "Dun Laoghaire"), ('RATHDOWN', "Rathdown"), ('FINGAL', "Fingal"),
                  ('CORK', "Cork"), ('LIMERICK', "Limerick"), ('CLARE', "Clare"), ('GALWAY', "Galway"), ('WATERFORD', "Waterford"),
                  ('KILKENNY', "Kilkenny"), ('DROGHEDA', "Drogheda"), ('LOUTH', "Louth"), ('WEXFORD', "Wexford"), ('SLIGO', "Sligo"),
                  ('CLONMEL', "Clonmel"), ('WATERFORD', "Waterford"), ('BRAY', "Bray"), ('WICKLOW', "Wicklow"), ('NAVAN', "Navan"),
                  ('ENNIS', "Ennis"), ('TRALLE', "Tralle"), ('KERRY', "Kerry"), ('CARLOW', "Carlow"),  ('LAOIS', "Laois"),
                  ('NAAS', "Naas"), ('KILDARE', "Kildare"), ('ATHLONE', "Athlone"), ('ROSCOMMON', "Roscommon"),('LETTERKENNY', "Letterkenny"),
                  ('DONEGAL', "Donegal"), ('TULLAMORE', "Tullamore"), ('KILLARNEY', "Killarney"), ('ARKLOW', "Arklow"), ('COBH', "Cobh"),
                  ('CASTLEBAR', "Castlebar"), ('MIDLETON', "Midleton"), ('MALLOW', "Mallow"), ('BALLINA', "Ballina"), ('ENNISCORTHY', "Enniscorthy"),
                  ('CAVAN', "Cavan"), ('ATHY', "Athy"), ('LONGFORD', "Longford"), ('DUNGARVAN', "Dungarvan"), ('NENAGH', "Nenagh"),
                  ('TRIM', "Trim"), ('NEW ROSS', "New Ross"), ('THURLES', "Thurles"), ('YOUGHAL', "Youghal"), ('MONAGHAN', "Monaghan"),
                  ('BUNCRANA', "Buncrana"), ('BALLINASLOE', "Ballinasloe"), ('FERMOY', "Fermoy"), ('WESTPORT', "Westport"), ('CARRICK-ON-SUIR', "Carrick-on-Suir"),
                  ('KELLS', "Kells"), ('BIRR', "Birr"), ('TIPPERARY', "Tipperary"), ('CARRICKMACROSS', "Carrickmacross"),
                  ('KINSALE', "Kinsale"), ('LISTOWEL', "Listowel"), ('CLONAKILTY', "Clonakilty"), ('CASHEL', "Cashel"), ('MACROOM', "Macroom"),
                  ('CASTLEBLAYNEY', "Castleblayney"), ('KILRUSH', "Kilrush"), ('SKIBBEREEN', "Skibbereen"), ('BUNDORAN', "Bundoran"), ('TEMPLEMORE', "Templemore"),
                  ('CLONES', "Clones"), ('NEWBRIDGE', "Newbridge"), ('PORTLAOISE', "Portlaoise"), ('MULLINGAR', "Mullingar"), ('BALBRIGGAN', "Balbriggan"),
                  ('GREYSTONES', "Greystones"), ('LEIXLIP', "Leixlip"), ('TRAMORE', "Tramore"), ('SHANNON', "Shannon"), ('GOREY', "Gorey"),
                  ('TUAM', "Tuam"), ('EDENDERRY', "Edenderry"), ('BANDON', "Bandon"), ('PASSAGE WEST', "Passage West"), ('LOUGHREA', "Loughrea"),
                  ('ARDEE', "Ardee"), ('MOUNTMELLICK', "Mountmellick"), ('BANTRY', "Bantry"), ('MUINE BHEAG', "Muine Bheag"), ('BOYLE', "Boyle"),
                  ('BALLYSHANNON', "Ballyshannon"), ('COOTEHILL', "Cootehill"), ('BALLYBAY', "Ballybay"), ('BELTURBET', "Belturbet"),
                  ('LISMORE', "Lismore"), ('KILKEE', "Kilkee"), ('GRANARD', "Granard"), ('NORTH IRELAND', "North Ireland")]


class PostFormRequest(forms.Form):

    # user = forms.()
    text_destination = forms.ChoiceField(choices=ireland_places)
    text_origin = forms.ChoiceField(choices=ireland_places)
    text_date = forms.CharField(widget=forms.TextInput(attrs={'type': 'date'}))
    text_time = forms.CharField(widget=forms.TextInput(attrs={'type': 'time'}))
    # image = forms.FileField()    //future implementation user photo


class PostFormOffer(forms.Form):

    # user = forms.CharField()
    text_destination = forms.ChoiceField(choices=ireland_places)
    text_origin = forms.ChoiceField(choices=ireland_places)
    text_date = forms.CharField(widget=forms.TextInput(attrs={'type': 'date'}))
    text_time = forms.CharField(widget=forms.TextInput(attrs={'type': 'time'}))

  # image = forms.FileField()    //future implementation user photo

