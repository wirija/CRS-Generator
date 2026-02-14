from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "urn:oecd:ties:isocrstypes:v1"


class CountryCodeType(Enum):
    """
    ISO-3166 Alpha 2 country codes.

    :cvar AF: AFGHANISTAN
    :cvar AX: ALAND ISLANDS
    :cvar AL: ALBANIA
    :cvar DZ: ALGERIA
    :cvar AS: AMERICAN SAMOA
    :cvar AD: ANDORRA
    :cvar AO: ANGOLA
    :cvar AI: ANGUILLA
    :cvar AQ: ANTARCTICA
    :cvar AG: ANTIGUA AND BARBUDA
    :cvar AR: ARGENTINA
    :cvar AM: ARMENIA
    :cvar AW: ARUBA
    :cvar AU: AUSTRALIA
    :cvar AT: AUSTRIA
    :cvar AZ: AZERBAIJAN
    :cvar BS: BAHAMAS
    :cvar BH: BAHRAIN
    :cvar BD: BANGLADESH
    :cvar BB: BARBADOS
    :cvar BY: BELARUS
    :cvar BE: BELGIUM
    :cvar BZ: BELIZE
    :cvar BJ: BENIN
    :cvar BM: BERMUDA
    :cvar BT: BHUTAN
    :cvar BO: BOLIVIA, PLURINATIONAL STATE OF
    :cvar BQ: BONAIRE, SINT EUSTATIUS AND SABA
    :cvar BA: BOSNIA AND HERZEGOVINA
    :cvar BW: BOTSWANA
    :cvar BV: BOUVET ISLAND
    :cvar BR: BRAZIL
    :cvar IO: BRITISH INDIAN OCEAN TERRITORY
    :cvar BN: BRUNEI DARUSSALAM
    :cvar BG: BULGARIA
    :cvar BF: BURKINA FASO
    :cvar BI: BURUNDI
    :cvar KH: CAMBODIA
    :cvar CM: CAMEROON
    :cvar CA: CANADA
    :cvar CV: CABO VERDE
    :cvar KY: CAYMAN ISLANDS
    :cvar CF: CENTRAL AFRICAN REPUBLIC
    :cvar TD: CHAD
    :cvar CL: CHILE
    :cvar CN: CHINA
    :cvar CX: CHRISTMAS ISLAND
    :cvar CC: COCOS (KEELING) ISLANDS
    :cvar CO: COLOMBIA
    :cvar KM: COMOROS
    :cvar CG: CONGO
    :cvar CD: CONGO, THE DEMOCRATIC REPUBLIC OF THE
    :cvar CK: COOK ISLANDS
    :cvar CR: COSTA RICA
    :cvar CI: COTE D'IVOIRE
    :cvar HR: CROATIA
    :cvar CU: CUBA
    :cvar CW: CURACAO
    :cvar CY: CYPRUS
    :cvar CZ: CZECHIA
    :cvar DK: DENMARK
    :cvar DJ: DJIBOUTI
    :cvar DM: DOMINICA
    :cvar DO: DOMINICAN REPUBLIC
    :cvar EC: ECUADOR
    :cvar EG: EGYPT
    :cvar SV: EL SALVADOR
    :cvar GQ: EQUATORIAL GUINEA
    :cvar ER: ERITREA
    :cvar EE: ESTONIA
    :cvar ET: ETHIOPIA
    :cvar FK: FALKLAND ISLANDS (MALVINAS)
    :cvar FO: FAROE ISLANDS
    :cvar FJ: FIJI
    :cvar FI: FINLAND
    :cvar FR: FRANCE
    :cvar GF: FRENCH GUIANA
    :cvar PF: FRENCH POLYNESIA
    :cvar TF: FRENCH SOUTHERN TERRITORIES
    :cvar GA: GABON
    :cvar GM: GAMBIA
    :cvar GE: GEORGIA
    :cvar DE: GERMANY
    :cvar GH: GHANA
    :cvar GI: GIBRALTAR
    :cvar GR: GREECE
    :cvar GL: GREENLAND
    :cvar GD: GRENADA
    :cvar GP: GUADELOUPE
    :cvar GU: GUAM
    :cvar GT: GUATEMALA
    :cvar GG: GUERNSEY
    :cvar GN: GUINEA
    :cvar GW: GUINEA-BISSAU
    :cvar GY: GUYANA
    :cvar HT: HAITI
    :cvar HM: HEARD ISLAND AND MCDONALD ISLANDS
    :cvar VA: HOLY SEE (VATICAN CITY STATE)
    :cvar HN: HONDURAS
    :cvar HK: HONG KONG
    :cvar HU: HUNGARY
    :cvar IS: ICELAND
    :cvar IN: INDIA
    :cvar ID: INDONESIA
    :cvar IR: IRAN, ISLAMIC REPUBLIC OF
    :cvar IQ: IRAQ
    :cvar IE: IRELAND
    :cvar IM: ISLE OF MAN
    :cvar IL: ISRAEL
    :cvar IT: ITALY
    :cvar JM: JAMAICA
    :cvar JP: JAPAN
    :cvar JE: JERSEY
    :cvar JO: JORDAN
    :cvar KZ: KAZAKHSTAN
    :cvar KE: KENYA
    :cvar KI: KIRIBATI
    :cvar KP: KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF
    :cvar KR: KOREA, REPUBLIC OF
    :cvar KW: KUWAIT
    :cvar KG: KYRGYZSTAN
    :cvar LA: LAO PEOPLE'S DEMOCRATIC REPUBLIC
    :cvar LV: LATVIA
    :cvar LB: LEBANON
    :cvar LS: LESOTHO
    :cvar LR: LIBERIA
    :cvar LY: LIBYA
    :cvar LI: LIECHTENSTEIN
    :cvar LT: LITHUANIA
    :cvar LU: LUXEMBOURG
    :cvar MO: MACAO
    :cvar MK: NORTH MACEDONIA
    :cvar MG: MADAGASCAR
    :cvar MW: MALAWI
    :cvar MY: MALAYSIA
    :cvar MV: MALDIVES
    :cvar ML: MALI
    :cvar MT: MALTA
    :cvar MH: MARSHALL ISLANDS
    :cvar MQ: MARTINIQUE
    :cvar MR: MAURITANIA
    :cvar MU: MAURITIUS
    :cvar YT: MAYOTTE
    :cvar MX: MEXICO
    :cvar FM: MICRONESIA, FEDERATED STATES OF
    :cvar MD: MOLDOVA, REPUBLIC OF
    :cvar MC: MONACO
    :cvar MN: MONGOLIA
    :cvar ME: MONTENEGRO
    :cvar MS: MONTSERRAT
    :cvar MA: MOROCCO
    :cvar MZ: MOZAMBIQUE
    :cvar MM: MYANMAR
    :cvar NA: NAMIBIA
    :cvar NR: NAURU
    :cvar NP: NEPAL
    :cvar NL: NETHERLANDS
    :cvar NC: NEW CALEDONIA
    :cvar NZ: NEW ZEALAND
    :cvar NI: NICARAGUA
    :cvar NE: NIGER
    :cvar NG: NIGERIA
    :cvar NU: NIUE
    :cvar NF: NORFOLK ISLAND
    :cvar MP: NORTHERN MARIANA ISLANDS
    :cvar NO: NORWAY
    :cvar OM: OMAN
    :cvar PK: PAKISTAN
    :cvar PW: PALAU
    :cvar PS: PALESTINE, STATE OF
    :cvar PA: PANAMA
    :cvar PG: PAPUA NEW GUINEA
    :cvar PY: PARAGUAY
    :cvar PE: PERU
    :cvar PH: PHILIPPINES
    :cvar PN: PITCAIRN
    :cvar PL: POLAND
    :cvar PT: PORTUGAL
    :cvar PR: PUERTO RICO
    :cvar QA: QATAR
    :cvar RE: REUNION
    :cvar RO: ROMANIA
    :cvar RU: RUSSIAN FEDERATION
    :cvar RW: RWANDA
    :cvar BL: SAINT BARTHELEMY
    :cvar SH: SAINT HELENA, ASCENSION AND TRISTAN DA CUNHA
    :cvar KN: SAINT KITTS AND NEVIS
    :cvar LC: SAINT LUCIA
    :cvar MF: SAINT MARTIN (FRENCH PART)
    :cvar PM: SAINT PIERRE AND MIQUELON
    :cvar VC: SAINT VINCENT AND THE GRENADINES
    :cvar WS: SAMOA
    :cvar SM: SAN MARINO
    :cvar ST: SAO TOME AND PRINCIPE
    :cvar SA: SAUDI ARABIA
    :cvar SN: SENEGAL
    :cvar RS: SERBIA
    :cvar SC: SEYCHELLES
    :cvar SL: SIERRA LEONE
    :cvar SG: SINGAPORE
    :cvar SX: SINT MAARTEN (DUTCH PART)
    :cvar SK: SLOVAKIA
    :cvar SI: SLOVENIA
    :cvar SB: SOLOMON ISLANDS
    :cvar SO: SOMALIA
    :cvar ZA: SOUTH AFRICA
    :cvar GS: SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS
    :cvar SS: SOUTH SUDAN
    :cvar ES: SPAIN
    :cvar LK: SRI LANKA
    :cvar SD: SUDAN
    :cvar SR: SURINAME
    :cvar SJ: SVALBARD AND JAN MAYEN
    :cvar SZ: ESWATINI
    :cvar SE: SWEDEN
    :cvar CH: SWITZERLAND
    :cvar SY: SYRIAN ARAB REPUBLIC
    :cvar TW: TAIWAN, PROVINCE OF CHINA
    :cvar TJ: TAJIKISTAN
    :cvar TZ: TANZANIA, UNITED REPUBLIC OF
    :cvar TH: THAILAND
    :cvar TL: TIMOR-LESTE
    :cvar TG: TOGO
    :cvar TK: TOKELAU
    :cvar TO: TONGA
    :cvar TT: TRINIDAD AND TOBAGO
    :cvar TN: TUNISIA
    :cvar TR: TURKEY
    :cvar TM: TURKMENISTAN
    :cvar TC: TURKS AND CAICOS ISLANDS
    :cvar TV: TUVALU
    :cvar UG: UGANDA
    :cvar UA: UKRAINE
    :cvar AE: UNITED ARAB EMIRATES
    :cvar GB: UNITED KINGDOM OF GREAT BRITAIN AND NORTHERN IRELAND
    :cvar US: UNITED STATES
    :cvar UM: UNITED STATES MINOR OUTLYING ISLANDS
    :cvar UY: URUGUAY
    :cvar UZ: UZBEKISTAN
    :cvar VU: VANUATU
    :cvar VE: VENEZUELA, BOLIVARIAN REPUBLIC OF
    :cvar VN: VIET NAM
    :cvar VG: VIRGIN ISLANDS, BRITISH
    :cvar VI: VIRGIN ISLANDS, U.S.
    :cvar WF: WALLIS AND FUTUNA
    :cvar EH: WESTERN SAHARA
    :cvar YE: YEMEN
    :cvar ZM: ZAMBIA
    :cvar ZW: ZIMBABWE
    :cvar XK: KOSOVO
    """

    AF = "AF"
    AX = "AX"
    AL = "AL"
    DZ = "DZ"
    AS = "AS"
    AD = "AD"
    AO = "AO"
    AI = "AI"
    AQ = "AQ"
    AG = "AG"
    AR = "AR"
    AM = "AM"
    AW = "AW"
    AU = "AU"
    AT = "AT"
    AZ = "AZ"
    BS = "BS"
    BH = "BH"
    BD = "BD"
    BB = "BB"
    BY = "BY"
    BE = "BE"
    BZ = "BZ"
    BJ = "BJ"
    BM = "BM"
    BT = "BT"
    BO = "BO"
    BQ = "BQ"
    BA = "BA"
    BW = "BW"
    BV = "BV"
    BR = "BR"
    IO = "IO"
    BN = "BN"
    BG = "BG"
    BF = "BF"
    BI = "BI"
    KH = "KH"
    CM = "CM"
    CA = "CA"
    CV = "CV"
    KY = "KY"
    CF = "CF"
    TD = "TD"
    CL = "CL"
    CN = "CN"
    CX = "CX"
    CC = "CC"
    CO = "CO"
    KM = "KM"
    CG = "CG"
    CD = "CD"
    CK = "CK"
    CR = "CR"
    CI = "CI"
    HR = "HR"
    CU = "CU"
    CW = "CW"
    CY = "CY"
    CZ = "CZ"
    DK = "DK"
    DJ = "DJ"
    DM = "DM"
    DO = "DO"
    EC = "EC"
    EG = "EG"
    SV = "SV"
    GQ = "GQ"
    ER = "ER"
    EE = "EE"
    ET = "ET"
    FK = "FK"
    FO = "FO"
    FJ = "FJ"
    FI = "FI"
    FR = "FR"
    GF = "GF"
    PF = "PF"
    TF = "TF"
    GA = "GA"
    GM = "GM"
    GE = "GE"
    DE = "DE"
    GH = "GH"
    GI = "GI"
    GR = "GR"
    GL = "GL"
    GD = "GD"
    GP = "GP"
    GU = "GU"
    GT = "GT"
    GG = "GG"
    GN = "GN"
    GW = "GW"
    GY = "GY"
    HT = "HT"
    HM = "HM"
    VA = "VA"
    HN = "HN"
    HK = "HK"
    HU = "HU"
    IS = "IS"
    IN = "IN"
    ID = "ID"
    IR = "IR"
    IQ = "IQ"
    IE = "IE"
    IM = "IM"
    IL = "IL"
    IT = "IT"
    JM = "JM"
    JP = "JP"
    JE = "JE"
    JO = "JO"
    KZ = "KZ"
    KE = "KE"
    KI = "KI"
    KP = "KP"
    KR = "KR"
    KW = "KW"
    KG = "KG"
    LA = "LA"
    LV = "LV"
    LB = "LB"
    LS = "LS"
    LR = "LR"
    LY = "LY"
    LI = "LI"
    LT = "LT"
    LU = "LU"
    MO = "MO"
    MK = "MK"
    MG = "MG"
    MW = "MW"
    MY = "MY"
    MV = "MV"
    ML = "ML"
    MT = "MT"
    MH = "MH"
    MQ = "MQ"
    MR = "MR"
    MU = "MU"
    YT = "YT"
    MX = "MX"
    FM = "FM"
    MD = "MD"
    MC = "MC"
    MN = "MN"
    ME = "ME"
    MS = "MS"
    MA = "MA"
    MZ = "MZ"
    MM = "MM"
    NA = "NA"
    NR = "NR"
    NP = "NP"
    NL = "NL"
    NC = "NC"
    NZ = "NZ"
    NI = "NI"
    NE = "NE"
    NG = "NG"
    NU = "NU"
    NF = "NF"
    MP = "MP"
    NO = "NO"
    OM = "OM"
    PK = "PK"
    PW = "PW"
    PS = "PS"
    PA = "PA"
    PG = "PG"
    PY = "PY"
    PE = "PE"
    PH = "PH"
    PN = "PN"
    PL = "PL"
    PT = "PT"
    PR = "PR"
    QA = "QA"
    RE = "RE"
    RO = "RO"
    RU = "RU"
    RW = "RW"
    BL = "BL"
    SH = "SH"
    KN = "KN"
    LC = "LC"
    MF = "MF"
    PM = "PM"
    VC = "VC"
    WS = "WS"
    SM = "SM"
    ST = "ST"
    SA = "SA"
    SN = "SN"
    RS = "RS"
    SC = "SC"
    SL = "SL"
    SG = "SG"
    SX = "SX"
    SK = "SK"
    SI = "SI"
    SB = "SB"
    SO = "SO"
    ZA = "ZA"
    GS = "GS"
    SS = "SS"
    ES = "ES"
    LK = "LK"
    SD = "SD"
    SR = "SR"
    SJ = "SJ"
    SZ = "SZ"
    SE = "SE"
    CH = "CH"
    SY = "SY"
    TW = "TW"
    TJ = "TJ"
    TZ = "TZ"
    TH = "TH"
    TL = "TL"
    TG = "TG"
    TK = "TK"
    TO = "TO"
    TT = "TT"
    TN = "TN"
    TR = "TR"
    TM = "TM"
    TC = "TC"
    TV = "TV"
    UG = "UG"
    UA = "UA"
    AE = "AE"
    GB = "GB"
    US = "US"
    UM = "UM"
    UY = "UY"
    UZ = "UZ"
    VU = "VU"
    VE = "VE"
    VN = "VN"
    VG = "VG"
    VI = "VI"
    WF = "WF"
    EH = "EH"
    YE = "YE"
    ZM = "ZM"
    ZW = "ZW"
    XK = "XK"


class CurrCodeType(Enum):
    """
    The appropriate currency code from the ISO 4217 three-byte alpha
    version for the currency in which a monetary amount is expressed.

    :cvar AED: UAE Dirham: UNITED ARAB EMIRATES
    :cvar AFN: Afghani: AFGHANISTAN
    :cvar ALL: Lek: ALBANIA
    :cvar AMD: Armenian Dram: ARMENIA
    :cvar ANG: Netherlands Antillean Guilder: CURACAO; SINT MAARTEN
        (DUTCH PART)
    :cvar AOA: Kwanza: ANGOLA
    :cvar ARS: Argentine Peso: ARGENTINA
    :cvar AUD: Australian Dollar: AUSTRALIA; CHRISTMAS ISLAND; COCOS
        (KEELING) ISLANDS; HEARD ISLAND AND McDONALD ISLANDS; KIRIBATI;
        NAURU; NORFOLK ISLAND; TUVALU
    :cvar AWG: Aruban Florin: ARUBA
    :cvar AZN: Azerbaijan Manat: AZERBAIJAN
    :cvar BAM: Convertible Mark: BOSNIA AND HERZEGOVINA
    :cvar BBD: Barbados Dollar: BARBADOS
    :cvar BDT: Taka: BANGLADESH
    :cvar BGN: Bulgarian Lev: BULGARIA
    :cvar BHD: Bahraini Dinar: BAHRAIN
    :cvar BIF: Burundi Franc: BURUNDI
    :cvar BMD: Bermudian Dollar: BERMUDA
    :cvar BND: Brunei Dollar: BRUNEI DARUSSALAM
    :cvar BOB: Boliviano: BOLIVIA, PLURINATIONAL STATE OF
    :cvar BOV: Mvdol: BOLIVIA, PLURINATIONAL STATE OF
    :cvar BRL: Brazilian Real: BRAZIL
    :cvar BSD: Bahamian Dollar: BAHAMAS
    :cvar BTN: Ngultrum: BHUTAN
    :cvar BWP: Pula: BOTSWANA
    :cvar BYN: Belarusian Ruble: BELARUS
    :cvar BYR: Historic use: Belarussian Ruble: BELARUS
    :cvar BZD: Belize Dollar: BELIZE
    :cvar CAD: Canadian Dollar: CANADA
    :cvar CDF: Congolese Franc: CONGO, THE DEMOCRATIC REPUBLIC OF
    :cvar CHE: WIR Euro: SWITZERLAND
    :cvar CHF: Swiss Franc: LIECHTENSTEIN; SWITZERLAND
    :cvar CHW: WIR Franc: SWITZERLAND
    :cvar CLF: Unidad de Fomento: CHILE
    :cvar CLP: Chilean Peso: CHILE
    :cvar CNY: Yuan Renminbi: CHINA
    :cvar COP: Colombian Peso: COLOMBIA
    :cvar COU: Unidad de Valor Real: COLOMBIA
    :cvar CRC: Costa Rican Colon: COSTA RICA
    :cvar CUC: Peso Convertible: CUBA
    :cvar CUP: Cuban Peso: CUBA
    :cvar CVE: Cabo Verde Escudo: CABO VERDE
    :cvar CZK: Czech Koruna: CZECHIA
    :cvar DJF: Djibouti Franc: DJIBOUTI
    :cvar DKK: Danish Krone: DENMARK; FAROE ISLANDS; GREENLAND
    :cvar DOP: Dominican Peso: DOMINICAN REPUBLIC
    :cvar DZD: Algerian Dinar: ALGERIA
    :cvar EGP: Egyptian Pound: EGYPT
    :cvar ERN: Nakfa: ERITREA
    :cvar ETB: Ethiopian Birr: ETHIOPIA
    :cvar EUR: Euro: ALAND ISLANDS; ANDORRA; AUSTRIA; BELGIUM; CYPRUS;
        ESTONIA; EUROPEAN UNION; FINLAND; FRANCE; FRENCH GUIANA; FRENCH
        SOUTHERN TERRITORIES; GERMANY; GREECE; GUADELOUPE; HOLY SEE
        (VATICAN CITY STATE); IRELAND; ITALY; LATVIA; LITHUANIA;
        LUXEMBOURG; MALTA; MARTINIQUE; MAYOTTE; MONACO; MONTENEGRO;
        NETHERLANDS; PORTUGAL; REUNION; SAINT BARTHELEMY; SAINT MARTIN
        (FRENCH PART); SAINT PIERRE AND MIQUELON; SAN MARINO; SLOVAKIA;
        SLOVENIA; SPAIN; Vatican City State (HOLY SEE)
    :cvar FJD: Fiji Dollar: FIJI
    :cvar FKP: Falkland Islands Pound: FALKLAND ISLANDS (MALVINAS)
    :cvar GBP: Pound Sterling: GUERNSEY; ISLE OF MAN; JERSEY; UNITED
        KINGDOM OF GREAT BRITAIN AND NORTHERN IRELAND
    :cvar GEL: Lari: GEORGIA
    :cvar GHS: Ghana Cedi: GHANA
    :cvar GIP: Gibraltar Pound: GIBRALTAR
    :cvar GMD: Dalasi: GAMBIA
    :cvar GNF: Guinean Franc: GUINEA
    :cvar GTQ: Quetzal: GUATEMALA
    :cvar GYD: Guyana Dollar: GUYANA
    :cvar HKD: Hong Kong Dollar: HONG KONG
    :cvar HNL: Lempira: HONDURAS
    :cvar HRK: Kuna: CROATIA
    :cvar HTG: Gourde: HAITI
    :cvar HUF: Forint: HUNGARY
    :cvar IDR: Rupiah: INDONESIA
    :cvar ILS: New Israeli Sheqel: ISRAEL
    :cvar INR: Indian Rupee: BHUTAN; INDIA
    :cvar IQD: Iraqi Dinar: IRAQ
    :cvar IRR: Iranian Rial: IRAN, ISLAMIC REPUBLIC OF
    :cvar ISK: Iceland Krona: ICELAND
    :cvar JMD: Jamaican Dollar: JAMAICA
    :cvar JOD: Jordanian Dinar: JORDAN
    :cvar JPY: Yen: JAPAN
    :cvar KES: Kenyan Shilling: KENYA
    :cvar KGS: Som: KYRGYZSTAN
    :cvar KHR: Riel: CAMBODIA
    :cvar KMF: Comorian Franc : COMOROS
    :cvar KPW: North Korean Won: KOREA, DEMOCRATIC PEOPLE’S REPUBLIC OF
    :cvar KRW: Won: KOREA, REPUBLIC OF
    :cvar KWD: Kuwaiti Dinar: KUWAIT
    :cvar KYD: Cayman Islands Dollar: CAYMAN ISLANDS
    :cvar KZT: Tenge: KAZAKHSTAN
    :cvar LAK: Lao Kip: LAO PEOPLE’S DEMOCRATIC REPUBLIC
    :cvar LBP: Lebanese Pound: LEBANON
    :cvar LKR: Sri Lanka Rupee: SRI LANKA
    :cvar LRD: Liberian Dollar: LIBERIA
    :cvar LSL: Loti: LESOTHO
    :cvar LTL: Historic use: Lithuanian Litas: LITHUANIA
    :cvar LVL: Historic use: Latvian Lats: LATVIA
    :cvar LYD: Libyan Dinar: LIBYA
    :cvar MAD: Moroccan Dirham: MOROCCO; WESTERN SAHARA
    :cvar MDL: Moldovan Leu: MOLDOVA, REPUBLIC OF
    :cvar MGA: Malagasy Ariary: MADAGASCAR
    :cvar MKD: Denar: MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF
    :cvar MMK: Kyat: MYANMAR
    :cvar MNT: Tugrik: MONGOLIA
    :cvar MOP: Pataca: MACAO
    :cvar MRO: Historic use: Ouguiya: MAURITANIA
    :cvar MRU: Ouguiya: MAURITANIA
    :cvar MUR: Mauritius Rupee: MAURITIUS
    :cvar MVR: Rufiyaa: MALDIVES
    :cvar MWK: Malawi Kwacha: MALAWI
    :cvar MXN: Mexican Peso: MEXICO
    :cvar MXV: Mexican Unidad de Inversion (UDI): MEXICO
    :cvar MYR: Malaysian Ringgit: MALAYSIA
    :cvar MZN: Mozambique Metical: MOZAMBIQUE
    :cvar NAD: Namibia Dollar: NAMIBIA
    :cvar NGN: Naira: NIGERIA
    :cvar NIO: Cordoba Oro: NICARAGUA
    :cvar NOK: Norwegian Krone: BOUVET ISLAND; NORWAY; SVALBARD AND JAN
        MAYEN
    :cvar NPR: Nepalese Rupee: NEPAL
    :cvar NZD: New Zealand Dollar: COOK ISLANDS; NEW ZEALAND; NIUE;
        PITCAIRN; TOKELAU
    :cvar OMR: Rial Omani: OMAN
    :cvar PAB: Balboa: PANAMA
    :cvar PEN: Sol: PERU
    :cvar PGK: Kina: PAPUA NEW GUINEA
    :cvar PHP: Philippine Peso: PHILIPPINES
    :cvar PKR: Pakistan Rupee: PAKISTAN
    :cvar PLN: Zloty: POLAND
    :cvar PYG: Guarani: PARAGUAY
    :cvar QAR: Qatari Rial: QATAR
    :cvar RON: Romanian Leu: ROMANIA
    :cvar RSD: Serbian Dinar: SERBIA
    :cvar RUB: Russian Ruble: RUSSIAN FEDERATION
    :cvar RWF: Rwanda Franc: RWANDA
    :cvar SAR: Saudi Riyal: SAUDI ARABIA
    :cvar SBD: Solomon Islands Dollar: SOLOMON ISLANDS
    :cvar SCR: Seychelles Rupee: SEYCHELLES
    :cvar SDG: Sudanese Pound: SUDAN
    :cvar SEK: Swedish Krona: SWEDEN
    :cvar SGD: Singapore Dollar: SINGAPORE
    :cvar SHP: Saint Helena Pound: SAINT HELENA, ASCENSION AND TRISTAN
        DA CUNHA
    :cvar SLL: Leone: SIERRA LEONE
    :cvar SOS: Somali Shilling: SOMALIA
    :cvar SRD: Surinam Dollar: SURINAME
    :cvar SSP: South Sudanese Pound: SOUTH SUDAN
    :cvar STD: Historic use: Dobra: SAO TOME AND PRINCIPE
    :cvar STN: Dobra: SAO TOME AND PRINCIPE
    :cvar SVC: El Salvador Colon: EL SALVADOR
    :cvar SYP: Syrian Pound: SYRIAN ARAB REPUBLIC
    :cvar SZL: Lilangeni: ESWATINI
    :cvar THB: Baht: THAILAND
    :cvar TJS: Somoni: TAJIKISTAN
    :cvar TMT: Turkmenistan New Manat: TURKMENISTAN
    :cvar TND: Tunisian Dinar: TUNISIA
    :cvar TOP: Pa’anga: TONGA
    :cvar TRY: Turkish Lira: TURKEY
    :cvar TTD: Trinidad and Tobago Dollar: TRINIDAD AND TOBAGO
    :cvar TWD: New Taiwan Dollar: TAIWAN, PROVINCE OF CHINA
    :cvar TZS: Tanzanian Shilling: TANZANIA, UNITED REPUBLIC OF
    :cvar UAH: Hryvnia: UKRAINE
    :cvar UGX: Uganda Shilling: UGANDA
    :cvar USD: US Dollar: AMERICAN SAMOA; BONAIRE; SINT EUSTATIUS AND
        SABA; BRITISH INDIAN OCEAN TERRITORY; ECUADOR; EL SALVADOR;
        GUAM; HAITI; MARSHALL ISLANDS; MICRONESIA, FEDERATED STATES OF;
        NORTHERN MARIANA ISLANDS; PALAU; PANAMA; PUERTO RICO; TIMOR-
        LESTE; TURKS AND CAICOS ISLANDS; UNITED STATES; UNITED STATES
        MINOR OUTLYING ISLANDS; VIRGIN ISLANDS (BRITISH); VIRGIN ISLANDS
        (US)
    :cvar USN: US Dollar (Next day): UNITED STATES
    :cvar USS: Historic use: US Dollar (Same day): UNITED STATES
    :cvar UYI: Uruguay Peso en Unidades Indexadas (UI): URUGUAY
    :cvar UYU: Peso Uruguayo: URUGUAY
    :cvar UYW: Unidad Previsional: URUGUAY
    :cvar UZS: Uzbekistan Sum: UZBEKISTAN
    :cvar VEF: Historic use: Bolivar: VENEZUELA, BOLIVARIAN REPUBLIC OF
    :cvar VES: Bolívar Soberano: VENEZUELA, BOLIVARIAN REPUBLIC OF
    :cvar VND: Dong: VIET NAM
    :cvar VUV: Vatu: VANUATU
    :cvar WST: Tala: SAMOA
    :cvar XAF: CFA Franc BEAC: CAMEROON; CENTRAL AFRICAN REPUBLIC; CHAD;
        CONGO; EQUATORIAL GUINEA; GABON
    :cvar XAG: Silver: ZZ11_Silver
    :cvar XAU: Gold: ZZ08_Gold
    :cvar XBA: Bond Markets Unit European Composite Unit (EURCO):
        ZZ01_Bond Markets Unit European_EURCO
    :cvar XBB: Bond Markets Unit European Monetary Unit (E.M.U.-6):
        ZZ02_Bond Markets Unit European_EMU-6
    :cvar XBC: Bond Markets Unit European Unit of Account 9 (E.U.A.-9):
        ZZ03_Bond Markets Unit European_EUA-9
    :cvar XBD: Bond Markets Unit European Unit of Account 17
        (E.U.A.-17): ZZ04_Bond Markets Unit European_EUA-17
    :cvar XCD: East Caribbean Dollar: ANGUILLA; ANTIGUA AND BARBUDA;
        DOMINICA; GRENADA; MONTSERRAT; SAINT KITTS AND NEVIS; SAINT
        LUCIA; SAINT VINCENT AND THE GRENADINES
    :cvar XDR: SDR (Special Drawing Right): INTERNATIONAL MONETARY FUND
        (IMF)
    :cvar XFU: Historic use: UIC-Franc: ZZ05_UIC-Franc
    :cvar XOF: CFA Franc BCEAO: BENIN; BURKINA FASO; COTE D'IVOIRE;
        GUINEA-BISSAU; MALI; NIGER; SENEGAL; TOGO
    :cvar XPD: Palladium: ZZ09_Palladium
    :cvar XPF: CFP Franc: FRENCH POLYNESIA; NEW CALEDONIA; WALLIS AND
        FUTUNA
    :cvar XPT: Platinum: ZZ10_Platinum
    :cvar XSU: Sucre: SISTEMA UNITARIO DE COMPENSACION REGIONAL DE PAGOS
        "SUCRE"
    :cvar XUA: ADB Unit of Account: MEMBER COUNTRIES OF THE AFRICAN
        DEVELOPMENT BANK GROUP
    :cvar XXX: The codes assigned for transactions where no currency is
        involved: ZZ07_No_Currency
    :cvar YER: Yemeni Rial: YEMEN
    :cvar ZAR: Rand: LESOTHO; NAMIBIA; SOUTH AFRICA
    :cvar ZMW: Zambian Kwacha: ZAMBIA
    :cvar ZWL: Zimbabwe Dollar: ZIMBABWE
    """

    AED = "AED"
    AFN = "AFN"
    ALL = "ALL"
    AMD = "AMD"
    ANG = "ANG"
    AOA = "AOA"
    ARS = "ARS"
    AUD = "AUD"
    AWG = "AWG"
    AZN = "AZN"
    BAM = "BAM"
    BBD = "BBD"
    BDT = "BDT"
    BGN = "BGN"
    BHD = "BHD"
    BIF = "BIF"
    BMD = "BMD"
    BND = "BND"
    BOB = "BOB"
    BOV = "BOV"
    BRL = "BRL"
    BSD = "BSD"
    BTN = "BTN"
    BWP = "BWP"
    BYN = "BYN"
    BYR = "BYR"
    BZD = "BZD"
    CAD = "CAD"
    CDF = "CDF"
    CHE = "CHE"
    CHF = "CHF"
    CHW = "CHW"
    CLF = "CLF"
    CLP = "CLP"
    CNY = "CNY"
    COP = "COP"
    COU = "COU"
    CRC = "CRC"
    CUC = "CUC"
    CUP = "CUP"
    CVE = "CVE"
    CZK = "CZK"
    DJF = "DJF"
    DKK = "DKK"
    DOP = "DOP"
    DZD = "DZD"
    EGP = "EGP"
    ERN = "ERN"
    ETB = "ETB"
    EUR = "EUR"
    FJD = "FJD"
    FKP = "FKP"
    GBP = "GBP"
    GEL = "GEL"
    GHS = "GHS"
    GIP = "GIP"
    GMD = "GMD"
    GNF = "GNF"
    GTQ = "GTQ"
    GYD = "GYD"
    HKD = "HKD"
    HNL = "HNL"
    HRK = "HRK"
    HTG = "HTG"
    HUF = "HUF"
    IDR = "IDR"
    ILS = "ILS"
    INR = "INR"
    IQD = "IQD"
    IRR = "IRR"
    ISK = "ISK"
    JMD = "JMD"
    JOD = "JOD"
    JPY = "JPY"
    KES = "KES"
    KGS = "KGS"
    KHR = "KHR"
    KMF = "KMF"
    KPW = "KPW"
    KRW = "KRW"
    KWD = "KWD"
    KYD = "KYD"
    KZT = "KZT"
    LAK = "LAK"
    LBP = "LBP"
    LKR = "LKR"
    LRD = "LRD"
    LSL = "LSL"
    LTL = "LTL"
    LVL = "LVL"
    LYD = "LYD"
    MAD = "MAD"
    MDL = "MDL"
    MGA = "MGA"
    MKD = "MKD"
    MMK = "MMK"
    MNT = "MNT"
    MOP = "MOP"
    MRO = "MRO"
    MRU = "MRU"
    MUR = "MUR"
    MVR = "MVR"
    MWK = "MWK"
    MXN = "MXN"
    MXV = "MXV"
    MYR = "MYR"
    MZN = "MZN"
    NAD = "NAD"
    NGN = "NGN"
    NIO = "NIO"
    NOK = "NOK"
    NPR = "NPR"
    NZD = "NZD"
    OMR = "OMR"
    PAB = "PAB"
    PEN = "PEN"
    PGK = "PGK"
    PHP = "PHP"
    PKR = "PKR"
    PLN = "PLN"
    PYG = "PYG"
    QAR = "QAR"
    RON = "RON"
    RSD = "RSD"
    RUB = "RUB"
    RWF = "RWF"
    SAR = "SAR"
    SBD = "SBD"
    SCR = "SCR"
    SDG = "SDG"
    SEK = "SEK"
    SGD = "SGD"
    SHP = "SHP"
    SLL = "SLL"
    SOS = "SOS"
    SRD = "SRD"
    SSP = "SSP"
    STD = "STD"
    STN = "STN"
    SVC = "SVC"
    SYP = "SYP"
    SZL = "SZL"
    THB = "THB"
    TJS = "TJS"
    TMT = "TMT"
    TND = "TND"
    TOP = "TOP"
    TRY = "TRY"
    TTD = "TTD"
    TWD = "TWD"
    TZS = "TZS"
    UAH = "UAH"
    UGX = "UGX"
    USD = "USD"
    USN = "USN"
    USS = "USS"
    UYI = "UYI"
    UYU = "UYU"
    UYW = "UYW"
    UZS = "UZS"
    VEF = "VEF"
    VES = "VES"
    VND = "VND"
    VUV = "VUV"
    WST = "WST"
    XAF = "XAF"
    XAG = "XAG"
    XAU = "XAU"
    XBA = "XBA"
    XBB = "XBB"
    XBC = "XBC"
    XBD = "XBD"
    XCD = "XCD"
    XDR = "XDR"
    XFU = "XFU"
    XOF = "XOF"
    XPD = "XPD"
    XPF = "XPF"
    XPT = "XPT"
    XSU = "XSU"
    XUA = "XUA"
    XXX = "XXX"
    YER = "YER"
    ZAR = "ZAR"
    ZMW = "ZMW"
    ZWL = "ZWL"
