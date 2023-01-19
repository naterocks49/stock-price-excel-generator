import json

main_list = [
        "AMKR",
        "AMLX",
        "AMN",
        "AMNB",
        "AMOT",
        "AMPE",
        "AMPH",
        "AMRC",
        "AMRK",
        "AMRS",
        "AMRX",
        "AMSC",
        "AMSF",
        "AMSWA",
        "AMTB",
        "AMTI",
        "AMTX",
        "AMWD",
        "AMWL",
        "ANAB",
        "ANAT",
        "ANDE",
        "ANF",
        "ANGN",
        "ANGO",
        "ANIK",
        "ANIP",
        "ANNX",
        "AOMR",
        "AORT",
        "AOSL",
        "AOUT",
        "APAM",
        "APEI",
        "APG",
        "APLE",
        "APLS",
        "APLT",
        "APOG",
        "APPF",
        "APPH",
        "APPN",
        "APPS",
        "APTS",
        "APYX",
        "AQB",
        "AQUA",
        "AR",
        "ARAY",
        "ARCB",
        "ARCH",
        "ARCT",
        "ARDX",
        "ARGO",
        "ARI",
        "ARIS",
        "ARKO",
        "ARLO",
        "ARNC",
        "AROC",
        "AROW",
        "ARQT",
        "ARR",
        "ARRY",
        "ARTNA",
        "ARVN",
        "ARWR",
        "ASAN",
        "ASB",
        "ASGN",
        "ASIX",
        "ASLE",
        "ASO",
        "ASPN",
        "ASTE",
        "ASXC",
        "ATCX",
        "ATEC",
        "ATEN",
        "ATER",
        "ATEX",
        "ATGE",
        "ATHA",
        "ATHX",
        "ATI",
        "ATKR",
        "ATLC",
        "ATNI",
        "ATNX",
        "ATOM",
        "ATOS",
        "ATRA",
        "ATRC",
        "ATRI",
        "ATRO",
        "ATRS",
        "ATSG",
        "AUB",
        "AUD",
        "AURA",
        "AVA",
        "AVAH",
        "AVAV",
        "AVD",
        "AVDX",
        "AVID",
        "AVIR",
        "AVNS",
        "AVNT",
        "AVNW",
        "AVO",
        "AVRO",
        "AVTE",
        "AVTX",
        "AVXL",
        "AVYA",
        "AWH",
        "AWR",
        "AX",
        "AXDX",
        "AXGN",
        "AXL",
        "AXNX",
        "AXSM",
        "AXTI",
        "AZZ",
        "B",
        "BALY",
        "BANC",
        "BAND",
        "BANF",
        "BANR",
        "BASE",
        "BATRA",
        "BATRK",
        "BBBY",
        "BBCP",
        "BBIO",
        "BBSI",
        "BCAB",
        "BCC",
        "BCEL",
        "BCO",
        "BCOR",
        "BCOV",
        "BCPC",
        "BCRX",
        "BDC",
        "BDN",
        "BDSX",
        "BDTX",
        "BE",
        "BEAM",
        "BECN",
        "BEEM",
        "BFC",
        "BFLY",
        "BFS",
        "BFST",
        "BGCP",
        "BGFV",
        "BGS",
        "BH",
        "BHB",
        "BHE",
        "BHG",
        "BHLB",
        "BHR",
        "BHVN",
        "BIG",
        "BIGC",
        "BIPC",
        "BJ",
        "BJRI",
        "BKD",
        "BKE",
        "BKH",
        "BKU",
        "BL",
        "BLBD",
        "BLFS",
        "BLFY",
        "BLI",
        "BLKB",
        "BLMN",
        "BLNK",
        "BLUE",
        "BLX",
        "BMEA",
        "BMI",
        "BMRC",
        "BNED",
        "BNFT",
        "BNGO",
        "BNL",
        "BOC",
        "BOLT",
        "BOOM",
        "BOOT",
        "BOX",
        "BPMC",
        "BRBR",
        "BRBS",
        "BRC",
        "BRKL",
        "BRMK",
        "BRP",
        "BRSP",
        "BRT",
        "BRY",
        "BSET",
        "BSIG",
        "BSRR",
        "BTAI",
        "BTRS",
        "BTU",
        "BTX",
        "BUSE",
        "BV",
        "BVH",
        "BVS",
        "BW",
        "BWB",
        "BXC",
        "BXMT",
        "BY",
        "BYRN",
        "BYSI",
        "BZH",
        "CAC",
        "CADE",
        "CAKE",
        "CAL",
        "CALM",
        "CALX",
        "CAMP",
        "CAR",
        "CARA",
        "CARE",
        "CARG",
        "CARS",
        "CASA",
        "CASH",
        "CASS",
        "CATC",
        "CATO",
        "CATY",
        "CBAY",
        "CBNK",
        "CBRL",
        "CBT",
        "CBU",
        "CCB",
        "CCBG",
        "CCCC",
        "CCF",
        "CCMP",
        "CCNE",
        "CCO",
        "CCOI",
        "CCRD",
        "CCRN",
        "CCS",
        "CCSI",
        "CCXI",
        "CDAK",
        "CDE",
        "CDLX",
        "CDMO",
        "CDNA",
        "CDRE",
        "CDXC",
        "CDXS",
        "CDZI",
        "CEIX",
        "CELC",
        "CELH",
        "CENT",
        "CENTA",
        "CENX",
        "CERE",
        "CERS",
        "CEVA",
        "CFB",
        "CFFN",
        "CGEM",
        "CHCO",
        "CHCT",
        "CHEF",
        "CHK",
        "CHRS",
        "CHS",
        "CHUY",
        "CHX",
        "CIA",
        "CIM",
        "CINC",
        "CIO",
        "CIR",
        "CIVB",
        "CIVI",
        "CIX",
        "CLAR",
        "CLBK",
        "CLDT",
        "CLDX",
        "CLFD",
        "CLNE",
        "CLNN",
        "CLPR",
        "CLPT",
        "CLSK",
        "CLVS",
        "CLW",
        "CMBM",
        "CMC",
        "CMCO",
        "CMP",
        "CMPR",
        "CMRE",
        "CMRX",
        "CMTL",
        "CNDT",
        "CNK",
        "CNMD",
        "CNNE",
        "CNO",
        "CNOB",
        "CNS",
        "CNSL",
        "CNTY",
        "CNVY",
        "CNX",
        "CNXN",
        "COCO",
        "COGT",
        "COHU",
        "COKE",
        "COLB",
        "COLL",
        "CONN",
        "COOK",
        "COOP",
        "CORT",
        "COUR",
        "COWN",
        "CPE",
        "CPF",
        "CPK",
        "CPRX",
        "CPS",
        "CPSI",
        "CRAI",
        "CRBU",
        "CRC",
        "CRDA",
        "CRDF",
        "CRDO",
        "CRGY",
        "CRIS",
        "CRK",
        "CRMD",
        "CRMT",
        "CRNC",
        "CRNX",
        "CROX",
        "CRS",
        "CRSR",
        "CRTX",
        "CRVL",
        "CSGS",
        "CSII",
        "CSR",
        "CSSE",
        "CSTE",
        "CSTL",
        "CSTM",
        "CSTR",
        "CSV",
        "CSWI",
        "CTBI",
        "CTKB",
        "CTLP",
        "CTMX",
        "CTO",
        "CTOS",
        "CTRE",
        "CTRN",
        "CTS",
        "CTSO",
        "CTT",
        "CTXR",
        "CUBI",
        "CUE",
        "CURI",
        "CURO",
        "CURV",
        "CUTR",
        "CVBF",
        "CVCO",
        "CVET",
        "CVGI",
        "CVGW",
        "CVI",
        "CVLG",
        "CVLT",
        "CVM",
        "CVRX",
        "CWEN",
        "CWENA",
        "CWH",
        "CWK",
        "CWST",
        "CWT",
        "CXW",
        "CYH",
        "CYRX",
        "CYT",
        "CYTK",
        "CZNC",
        "DAKT",
        "DAN",
        "DAWN",
        "DBD",
        "DBI",
        "DBRG",
        "DCO",
        "DCOM",
        "DCPH",
        "DDD",
        "DDS",
        "DEA",
        "DEN",
        "DENN",
        "DFIN",
        "DGICA",
        "DGII",
        "DHC",
        "DHIL",
        "DHT",
        "DIBS",
        "DICE",
        "DIN",
        "DIOD",
        "DJCO",
        "DK",
        "DLTH",
        "DLX",
        "DM",
        "DMRC",
        "DMS",
        "DMTK",
        "DNAY",
        "DNLI",
        "DNMR",
        "DNOW",
        "DNUT",
        "DOC",
        "DOCN",
        "DOMO",
        "DOOR",
        "DORM",
        "DOUG",
        "DRH",
        "DRIO",
        "DRQ",
        "DRRX",
        "DS",
        "DSGN",
        "DSKE",
        "DSP",
        "DTC",
        "DTIL",
        "DVAX",
        "DX",
        "DXPE",
        "DY",
        "DYN",
        "DZSI",
        "EAF",
        "EAR",
        "EAT",
        "EB",
        "EBC",
        "EBET",
        "EBF",
        "EBIX",
        "EBS",
        "EBTC",
        "ECOL",
        "ECOM",
        "ECPG",
        "ECVT",
        "EDIT",
        "EEX",
        "EFC",
        "EFSC",
        "EGAN",
        "EGBN",
        "EGHT",
        "EGLE",
        "EGP",
        "EGRX",
        "EHTH",
        "EIG",
        "EIGR",
        "ELF",
        "ELY",
        "ELYM",
        "EME",
        "EMKR",
        "ENDP",
        "ENFN",
        "ENR",
        "ENS",
        "ENSG",
        "ENTA",
        "ENV",
        "ENVA",
        "EOLS",
        "EOSE",
        "EPAC",
        "EPAY",
        "EPC",
        "EPRT",
        "EPZM",
        "EQBK",
        "EQC",
        "ERAS",
        "ERII",
        "ESCA",
        "ESE",
        "ESGR",
        "ESMT",
        "ESNT",
        "ESPR",
        "ESRT",
        "ESTE",
        "ETD",
        "ETNB",
        "ETRN",
        "ETWO",
        "EVC",
        "EVCM",
        "EVER",
        "EVH",
        "EVI",
        "EVLO",
        "EVOP",
        "EVRI",
        "EVTC",
        "EWCZ",
        "EWTX",
        "EXLS",
        "EXPI",
        "EXPO",
        "EXTR",
        "EYE",
        "EYPT",
        "EZPW",
        "FA",
        "FARO",
        "FATE",
        "FBC",
        "FBIO",
        "FBK",
        "FBMS",
        "FBNC",
        "FBP",
        "FBRT",
        "FBRX",
        "FC",
        "FCBC",
        "FCEL",
        "FCF",
        "FCFS",
        "FCPT",
        "FDBC",
        "FDMT",
        "FDP",
        "FELE",
        "FF",
        "FFBC",
        "FFIC",
        "FFIN",
        "FFWM",
        "FGEN",
        "FHI",
        "FHTX",
        "FIBK",
        "FISI",
        "FIX",
        "FIXX",
        "FIZZ",
        "FLGT",
        "FLIC",
        "FLL",
        "FLNT",
        "FLR",
        "FLWS",
        "FLXS",
        "FLYW",
        "FMBH",
        "FMNB",
        "FMTX",
        "FN",
        "FNA",
        "FNCH",
        "FNKO",
        "FNLC",
        "FOA",
        "FOCS",
        "FOE",
        "FOLD",
        "FOR",
        "FORA",
        "FORM",
        "FORR",
        "FOSL",
        "FOXF",
        "FPI",
        "FRBA",
        "FRBK",
        "FREE",
        "FREQ",
        "FRG",
        "FRGI",
        "FRME",
        "FRO",
        "FROG",
        "FRPH",
        "FRST",
        "FSBC",
        "FSBW",
        "FSP",
        "FSR",
        "FSS",
        "FTCI",
        "FTHM",
        "FUBO",
        "FUL",
        "FULC",
        "FULT",
        "FUV",
        "FWRD",
        "FWRG",
        "FXLV",
        "GABC",
        "GAN",
        "GATO",
        "GATX",
        "GBCI",
        "GBIO",
        "GBL",
        "GBOX",
        "GBT",
        "GBX",
        "GCI",
        "GCMG",
        "GCO",
        "GCP",
        "GDEN",
        "GDOT",
        "GDYN",
        "GEF",
        "GEFB",
        "GEO",
        "GERN",
        "GES",
        "GEVO",
        "GFF",
        "GHC",
        "GHL",
        "GIC",
        "GIII",
        "GKOS",
        "GLDD",
        "GLNG",
        "GLRE",
        "GLSI",
        "GLT",
        "GLUE",
        "GMRE",
        "GMS",
        "GMTX",
        "GNK",
        "GNL",
        "GNLN",
        "GNOG",
        "GNTY",
        "GNUS",
        "GNW",
        "GOEV",
        "GOGO",
        "GOLF",
        "GOOD",
        "GOSS",
        "GPI",
        "GPMT",
        "GPRE",
        "GPRO",
        "GRBK",
        "GRC",
        "GRPH",
        "GRPN",
        "GRTS",
        "GRWG",
        "GSAT",
        "GSBC",
        "GSHD",
        "GT",
        "GTBP",
        "GTHX",
        "GTLS",
        "GTN",
        "GTY",
        "GTYH",
        "GVA",
        "GWRS",
        "HA",
        "HAE",
        "HAFC",
        "HALO",
        "HARP",
        "HASI",
        "HAYN",
        "HBB",
        "HBCP",
        "HBIO",
        "HBNC",
        "HBT",
        "HCAT",
        "HCC",
        "HCCI",
        "HCI",
        "HCKT",
        "HCSG",
        "HEAR",
        "HEES",
        "HELE",
        "HFFG",
        "HFWA",
        "HGEN",
        "HGV",
        "HI",
        "HIBB",
        "HIFS",
        "HL",
        "HLI",
        "HLIO",
        "HLIT",
        "HLNE",
        "HLTH",
        "HLX",
        "HMN",
        "HMPT",
        "HMST",
        "HMTV",
        "HNGR",
        "HNI",
        "HNST",
        "HOFT",
        "HOFV",
        "HOMB",
        "HONE",
        "HOOK",
        "HOPE",
        "HOV",
        "HOWL",
        "HP",
        "HPK",
        "HQI",
        "HQY",
        "HR",
        "HRI",
        "HRMY",
        "HRT",
        "HRTG",
        "HRTX",
        "HSC",
        "HSII",
        "HSKA",
        "HSTM",
        "HT",
        "HTBI",
        "HTBK",
        "HTH",
        "HTLD",
        "HTLF",
        "HUBG",
        "HURN",
        "HVT",
        "HWC",
        "HWKN",
        "HY",
        "HYFM",
        "HYLN",
        "HYRE",
        "HZO",
        "IAS",
        "IBCP",
        "IBEX",
        "IBIO",
        "IBOC",
        "IBP",
        "IBRX",
        "IBTX",
        "ICAD",
        "ICFI",
        "ICHR",
        "ICPT",
        "ICVX",
        "IDCC",
        "IDEX",
        "IDT",
        "IDYA",
        "IEA",
        "IESC",
        "IGMS",
        "IGT",
        "IHRT",
        "IIIN",
        "IIIV",
        "IIPR",
        "IIVI",
        "IKNA",
        "ILPT",
        "IMAX",
        "IMGN",
        "IMGO",
        "IMKTA",
        "IMPL",
        "IMRX",
        "IMUX",
        "IMVT",
        "IMXI",
        "INBK",
        "INBX",
        "INDB",
        "INDT",
        "INFI",
        "INFN",
        "INFU",
        "INGN",
        "INN",
        "INNV",
        "INO",
        "INSG",
        "INSM",
        "INSP",
        "INST",
        "INSW",
        "INT",
        "INTA",
        "INVA",
        "INVE",
        "INZY",
        "IOSP",
        "IPAR",
        "IPI",
        "IPSC",
        "IRBT",
        "IRDM",
        "IRMD",
        "IRT",
        "IRTC",
        "IRWD",
        "ISEE",
        "ISO",
        "ITCI",
        "ITGR",
        "ITI",
        "ITIC",
        "ITOS",
        "ITRI",
        "IVC",
        "IVR",
        "JACK",
        "JANX",
        "JBSS",
        "JBT",
        "JELD",
        "JJSF",
        "JNCE",
        "JOAN",
        "JOE",
        "JOUT",
        "JRVR",
        "JYNT",
        "KAI",
        "KALA",
        "KALU",
        "KALV",
        "KAMN",
        "KAR",
        "KBAL",
        "KBH",
        "KBR",
        "KDNY",
        "KE",
        "KELYA",
        "KFRC",
        "KFY",
        "KIDS",
        "KIRK",
        "KLDO",
        "KLIC",
        "KLTR",
        "KMPH",
        "KMT",
        "KN",
        "KNSA",
        "KNSL",
        "KNTE",
        "KNTK",
        "KOD",
        "KODK",
        "KOP",
        "KOPN",
        "KOS",
        "KPTI",
        "KREF",
        "KRG",
        "KRNY",
        "KRO",
        "KRON",
        "KROS",
        "KRT",
        "KRTX",
        "KRUS",
        "KRYS",
        "KTB",
        "KTOS",
        "KURA",
        "KVHI",
        "KW",
        "KWR",
        "KYMR",
        "KZR",
        "LAB",
        "LABP",
        "LADR",
        "LANC",
        "LAND",
        "LASR",
        "LAUR",
        "LAW",
        "LAZY",
        "LBAI",
        "LBC",
        "LBRT",
        "LC",
        "LCII",
        "LCTX",
        "LCUT",
        "LE",
        "LEGH",
        "LEU",
        "LFST",
        "LGFA",
        "LGFB",
        "LGIH",
        "LGND",
        "LHCG",
        "LILA",
        "LILAK",
        "LIND",
        "LIVN",
        "LKFN",
        "LL",
        "LLNW",
        "LMAT",
        "LMNR",
        "LNDC",
        "LNN",
        "LNTH",
        "LOB",
        "LOCO",
        "LOTZ",
        "LOVE",
        "LPG",
        "LPI",
        "LPRO",
        "LPSN",
        "LQDT",
        "LRN",
        "LSCC",
        "LSEA",
        "LSF",
        "LTC",
        "LTH",
        "LTHM",
        "LTRPA",
        "LUNA",
        "LUNG",
        "LVLU",
        "LVO",
        "LXFR",
        "LXP",
        "LXRX",
        "LYEL",
        "LZB",
        "M",
        "MAC",
        "MANT",
        "MARA",
        "MASS",
        "MATW",
        "MATX",
        "MAX",
        "MAXR",
        "MBI",
        "MBII",
        "MBIN",
        "MBIO",
        "MBUU",
        "MBWM",
        "MC",
        "MCB",
        "MCBC",
        "MCBS",
        "MCFT",
        "MCRB",
        "MCRI",
        "MCS",
        "MD",
        "MDC",
        "MDGL",
        "MDRX",
        "MDVL",
        "MDXG",
        "MEC",
        "MED",
        "MEDP",
        "MEG",
        "MEI",
        "MEIP",
        "MESA",
        "MFA",
        "MG",
        "MGEE",
        "MGI",
        "MGNI",
        "MGNX",
        "MGPI",
        "MGRC",
        "MGTA",
        "MGTX",
        "MGY",
        "MHLD",
        "MHO",
        "MILE",
        "MIME",
        "MIRM",
        "MITK",
        "MLAB",
        "MLI",
        "MLKN",
        "MLNK",
        "MLR",
        "MMAT",
        "MMI",
        "MMS",
        "MMSI",
        "MNKD",
        "MNMD",
        "MNRL",
        "MNRO",
        "MNTV",
        "MOD",
        "MODN",
        "MODV",
        "MOFG",
        "MOGA",
        "MORF",
        "MOV",
        "MP",
        "MPAA",
        "MPB",
        "MPLN",
        "MPX",
        "MRC",
        "MRNS",
        "MRSN",
        "MRTN",
        "MSBI",
        "MSEX",
        "MSGE",
        "MSTR",
        "MTDR",
        "MTEM",
        "MTH",
        "MTOR",
        "MTRN",
        "MTRX",
        "MTSI",
        "MTW",
        "MTX",
        "MUR",
        "MUSA",
        "MVBF",
        "MVIS",
        "MWA",
        "MXCT",
        "MXL",
        "MYE",
        "MYGN",
        "MYRG",
        "NAPA",
        "NARI",
        "NAT",
        "NATH",
        "NATR",
        "NAVI",
        "NBEV",
        "NBHC",
        "NBR",
        "NBTB",
        "NCBS",
        "NCMI",
        "NDLS",
        "NEO",
        "NEOG",
        "NESR",
        "NEX",
        "NEXI",
        "NFBK",
        "NG",
        "NGM",
        "NGMS",
        "NGVC",
        "NGVT",
        "NH",
        "NHC",
        "NHI",
        "NJR",
        "NKLA",
        "NKTX",
        "NL",
        "NLS",
        "NLTX",
        "NMIH",
        "NMRK",
        "NMTR",
        "NNBR",
        "NNI",
        "NODK",
        "NOG",
        "NOTV",
        "NOVA",
        "NOVT",
        "NP",
        "NPCE",
        "NPK",
        "NPO",
        "NPTN",
        "NR",
        "NRC",
        "NRIM",
        "NRIX",
        "NSA",
        "NSIT",
        "NSP",
        "NSSC",
        "NSTG",
        "NTB",
        "NTCT",
        "NTGR",
        "NTLA",
        "NTST",
        "NTUS",
        "NUS",
        "NUVA",
        "NUVB",
        "NUVL",
        "NVEC",
        "NVEE",
        "NVRO",
        "NVTA",
        "NWBI",
        "NWE",
        "NWLI",
        "NWN",
        "NWPX",
        "NX",
        "NXGN",
        "NXRT",
        "NYMT",
        "OAS",
        "OB",
        "OBNK",
        "OCDX",
        "OCFC",
        "OCGN",
        "OCN",
        "OCUL",
        "OCX",
        "ODC",
        "ODP",
        "OEC",
        "OFC",
        "OFG",
        "OFIX",
        "OFLX",
        "OGS",
        "OI",
        "OII",
        "OIS",
        "OLMA",
        "OLP",
        "OM",
        "OMCL",
        "OMER",
        "OMGA",
        "OMI",
        "OMIC",
        "ONB",
        "ONCR",
        "ONCT",
        "ONEM",
        "ONEW",
        "ONTF",
        "ONTO",
        "OOMA",
        "OPCH",
        "OPI",
        "OPK",
        "OPRT",
        "OPRX",
        "OPY",
        "ORA",
        "ORC",
        "ORGO",
        "ORIC",
        "ORMP",
        "ORRF",
        "OSBC",
        "OSIS",
        "OSPN",
        "OSTK",
        "OSUR",
        "OSW",
        "OTLK",
        "OTRK",
        "OTTR",
        "OUST",
        "OUT",
        "OVV",
        "OXM",
        "OYST",
        "PACB",
        "PACK",
        "PAHC",
        "PAR",
        "PARR",
        "PASG",
        "PATK",
        "PAVM",
        "PAYA",
        "PBF",
        "PBFS",
        "PBH",
        "PBI",
        "PBYI",
        "PCH",
        "PCRX",
        "PCSB",
        "PCT",
        "PCVX",
        "PCYO",
        "PD",
        "PDCE",
        "PDCO",
        "PDFS",
        "PDLI",
        "PDM",
        "PEB",
        "PEBO",
        "PECO",
        "PETQ",
        "PETS",
        "PFBC",
        "PFC",
        "PFGC",
        "PFIS",
        "PFS",
        "PFSI",
        "PGC",
        "PGEN",
        "PGNY",
        "PGRE",
        "PGTI",
        "PHAT",
        "PHR",
        "PI",
        "PING",
        "PIPR",
        "PJT",
        "PKE",
        "PKOH",
        "PLAB",
        "PLAY",
        "PLBY",
        "PLCE",
        "PLM",
        "PLMR",
        "PLOW",
        "PLPC",
        "PLRX",
        "PLSE",
        "PLUS",
        "PLXS",
        "PLYM",
        "PMT",
        "PMVP",
        "PNM",
        "PNTG",
        "POLY",
        "POR",
        "POWI",
        "POWL",
        "POWW",
        "PPBI",
        "PPTA",
        "PRA",
        "PRAA",
        "PRAX",
        "PRCH",
        "PRCT",
        "PRDO",
        "PRFT",
        "PRG",
        "PRGS",
        "PRIM",
        "PRK",
        "PRLB",
        "PRLD",
        "PRMW",
        "PRO",
        "PRPL",
        "PRTA",
        "PRTG",
        "PRTH",
        "PRTK",
        "PRTS",
        "PRTY",
        "PRVA",
        "PRVB",
        "PSB",
        "PSMT",
        "PSN",
        "PSNL",
        "PSTL",
        "PSTX",
        "PTCT",
        "PTEN",
        "PTGX",
        "PTLO",
        "PTSI",
        "PTVE",
        "PUMP",
        "PVBC",
        "PWSC",
        "PYXS",
        "PZN",
        "PZZA",
        "QCRH",
        "QLYS",
        "QMCO",
        "QNST",
        "QTNT",
        "QTRX",
        "QTWO",
        "QUOT",
        "RAD",
        "RADI",
        "RAIN",
        "RAMP",
        "RAPT",
        "RBB",
        "RBBN",
        "RBCAA",
        "RC",
        "RCEL",
        "RCII",
        "RCKT",
        "RCKY",
        "RCM",
        "RCUS",
        "RDFN",
        "RDN",
        "RDNT",
        "RDUS",
        "REAL",
        "REFI",
        "REGI",
        "REKR",
        "RELY",
        "RENT",
        "REPL",
        "REPX",
        "RES",
        "RETA",
        "REV",
        "REVG",
        "REX",
        "REZI",
        "RFL",
        "RGNX",
        "RGP",
        "RGR",
        "RGS",
        "RHP",
        "RICK",
        "RIDE",
        "RIGL",
        "RILY",
        "RIOT",
        "RLAY",
        "RLGT",
        "RLI",
        "RLJ",
        "RLMD",
        "RLYB",
        "RM",
        "RMAX",
        "RMBS",
        "RMNI",
        "RMO",
        "RMR",
        "RNA",
        "RNST",
        "ROAD",
        "ROCC",
        "ROCK",
        "ROG",
        "ROIC",
        "ROLL",
        "RPAY",
        "RPD",
        "RPHM",
        "RPID",
        "RPT",
        "RRBI",
        "RRC",
        "RRGB",
        "RRR",
        "RSI",
        "RUBY",
        "RUSHA",
        "RUSHB",
        "RUTH",
        "RVLV",
        "RVMD",
        "RVNC",
        "RVP",
        "RWT",
        "RXDX",
        "RXRX",
        "RXST",
        "RXT",
        "RYAM",
        "RYI",
        "RYTM",
        "SAFE",
        "SAFM",
        "SAFT",
        "SAH",
        "SAIA",
        "SAIL",
        "SANA",
        "SANM",
        "SASR",
        "SATS",
        "SAVA",
        "SAVE",
        "SB",
        "SBCF",
        "SBGI",
        "SBH",
        "SBRA",
        "SBSI",
        "SBTX",
        "SCHL",
        "SCHN",
        "SCL",
        "SCOR",
        "SCS",
        "SCSC",
        "SCU",
        "SCVL",
        "SCWX",
        "SDGR",
        "SDIG",
        "SEAS",
        "SEEL",
        "SEER",
        "SELB",
        "SEM",
        "SENEA",
        "SENS",
        "SERA",
        "SESN",
        "SFBS",
        "SFIX",
        "SFL",
        "SFM",
        "SFNC",
        "SFST",
        "SFT",
        "SG",
        "SGC",
        "SGH",
        "SGHT",
        "SGMO",
        "SGRY",
        "SGTX",
        "SHAK",
        "SHEN",
        "SHO",
        "SHOO",
        "SHYF",
        "SI",
        "SIBN",
        "SIEN",
        "SIG",
        "SIGA",
        "SIGI",
        "SILK",
        "SITC",
        "SITM",
        "SJI",
        "SJW",
        "SKIN",
        "SKT",
        "SKY",
        "SKYT",
        "SKYW",
        "SLAB",
        "SLCA",
        "SLDB",
        "SLP",
        "SLQT",
        "SM",
        "SMBC",
        "SMBK",
        "SMCI",
        "SMED",
        "SMMF",
        "SMMT",
        "SMP",
        "SMPL",
        "SMSI",
        "SMTC",
        "SNBR",
        "SNCY",
        "SNDX",
        "SNEX",
        "SNPO",
        "SNSE",
        "SOI",
        "SONO",
        "SOVO",
        "SP",
        "SPFI",
        "SPNE",
        "SPNS",
        "SPNT",
        "SPPI",
        "SPRB",
        "SPRO",
        "SPSC",
        "SPT",
        "SPTN",
        "SPWH",
        "SPWR",
        "SPXC",
        "SQZ",
        "SR",
        "SRCE",
        "SRDX",
        "SRG",
        "SRI",
        "SRNE",
        "SRRK",
        "SRT",
        "SSB",
        "SSD",
        "SSP",
        "SSTI",
        "SSTK",
        "STAA",
        "STAG",
        "STAR",
        "STBA",
        "STC",
        "STEM",
        "STEP",
        "STER",
        "STGW",
        "STIM",
        "STKS",
        "STNG",
        "STOK",
        "STON",
        "STRA",
        "STRL",
        "STRO",
        "STTK",
        "STXS",
        "SUM",
        "SUMO",
        "SUPN",
        "SURF",
        "SVC",
        "SWAV",
        "SWBI",
        "SWIM",
        "SWM",
        "SWN",
        "SWTX",
        "SWX",
        "SXC",
        "SXI",
        "SXT",
        "SYBT",
        "SYNA",
        "SYRS",
        "TA",
        "TALO",
        "TALS",
        "TARS",
        "TAST",
        "TBBK",
        "TBI",
        "TBK",
        "TBPH",
        "TCBI",
        "TCBK",
        "TCBX",
        "TCMD",
        "TCRR",
        "TCRT",
        "TCS",
        "TCX",
        "TDS",
        "TDW",
        "TELL",
        "TEN",
        "TENB",
        "TERN",
        "TEX",
        "TG",
        "TGH",
        "TGI",
        "TGNA",
        "TGTX",
        "TH",
        "THC",
        "THFF",
        "THR",
        "THRM",
        "THRX",
        "THRY",
        "THS",
        "TIG",
        "TIL",
        "TILE",
        "TIPT",
        "TISI",
        "TITN",
        "TK",
        "TKNO",
        "TLIS",
        "TLS",
        "TLYS",
        "TMCI",
        "TMDX",
        "TMHC",
        "TMP",
        "TMST",
        "TNC",
        "TNET",
        "TNK",
        "TNXP",
        "TNYA",
        "TOWN",
        "TPB",
        "TPC",
        "TPH",
        "TPIC",
        "TPTX",
        "TR",
        "TRC",
        "TRDA",
        "TREE",
        "TRHC",
        "TRMK",
        "TRN",
        "TRNO",
        "TRNS",
        "TROX",
        "TRS",
        "TRST",
        "TRTN",
        "TRTX",
        "TRUP",
        "TRVN",
        "TSAT",
        "TSC",
        "TSE",
        "TSHA",
        "TSVT",
        "TTCF",
        "TTEC",
        "TTEK",
        "TTGT",
        "TTI",
        "TTMI",
        "TUP",
        "TVTX",
        "TVTY",
        "TWI",
        "TWNK",
        "TWO",
        "TWOU",
        "TWST",
        "TXMD",
        "TXRH",
        "TYRA",
        "UAVS",
        "UBA",
        "UBSI",
        "UCBI",
        "UCTT",
        "UDMY",
        "UE",
        "UEC",
        "UEIC",
        "UFCS",
        "UFI",
        "UFPI",
        "UFPT",
        "UHT",
        "UIHC",
        "UIS",
        "ULCC",
        "ULH",
        "UMBF",
        "UMH",
        "UNF",
        "UNFI",
        "UNIT",
        "UPLD",
        "UPWK",
        "URBN",
        "URG",
        "URGN",
        "USD",
        "USER",
        "USLM",
        "USM",
        "USNA",
        "USPH",
        "USX",
        "UTL",
        "UTMD",
        "UTZ",
        "UUUU",
        "UVE",
        "UVSP",
        "UVV",
        "VALU",
        "VAPO",
        "VATE",
        "VBIV",
        "VBTX",
        "VC",
        "VCEL",
        "VCYT",
        "VEC",
        "VECO",
        "VEL",
        "VERA",
        "VERI",
        "VERU",
        "VERV",
        "VG",
        "VGR",
        "VHC",
        "VHI",
        "VIA",
        "VIAV",
        "VICR",
        "VIEW",
        "VIGL",
        "VINC",
        "VIR",
        "VIRX",
        "VITL",
        "VIVO",
        "VKTX",
        "VLDR",
        "VLGEA",
        "VLY",
        "VMD",
        "VNDA",
        "VOR",
        "VOXX",
        "VPG",
        "VRA",
        "VRAY",
        "VRCA",
        "VRE",
        "VREX",
        "VRNS",
        "VRNT",
        "VRRM",
        "VRTS",
        "VRTV",
        "VSEC",
        "VSH",
        "VSTM",
        "VSTO",
        "VTGN",
        "VTOL",
        "VTYX",
        "VUZI",
        "VVI",
        "VVNT",
        "VXRT",
        "WABC",
        "WAFD",
        "WASH",
        "WBT",
        "WCC",
        "WD",
        "WDFC",
        "WEBR",
        "WERN",
        "WETF",
        "WGO",
        "WHD",
        "WINA",
        "WING",
        "WIRE",
        "WK",
        "WKHS",
        "WLDN",
        "WLFC",
        "WLL",
        "WLLAW",
        "WLLBW",
        "WLY",
        "WMK",
        "WNC",
        "WOR",
        "WOW",
        "WRE",
        "WRLD",
        "WSBC",
        "WSBF",
        "WSC",
        "WSFS",
        "WSR",
        "WTBA",
        "WTI",
        "WTS",
        "WTTR",
        "WVE",
        "WW",
        "WWW",
        "XBIT",
        "XENT",
        "XGN",
        "XHR",
        "XL",
        "XLO",
        "XMTR",
        "XNCR",
        "XOMA",
        "XPEL",
        "XPER",
        "XPOF",
        "XPRO",
        "XXII",
        "YELL",
        "YELP",
        "YEXT",
        "YMAB",
        "YORW",
        "ZD",
        "ZEUS",
        "ZGNX",
        "ZNTL",
        "ZUMZ",
        "ZUO",
        "ZVIA",
        "ZWS",
        "ZY",
        "ZYXI"
    ]


with open('ticker_lists.json', "r") as f:
    a = json.load(f)["all"]

for t in main_list:
    if t not in a:
        main_list.remove(t)

with open('ticker_lists.json', "w") as f:
    json.dump(main_list, f, indent=4)