
# Chat-Bot utilizando API COVID19 - INDIA:

Para acessar as informações do COVID19 da India foi acessado a api https://api.covid19india.org/data.json 
para que ele busque as informações dos estados que compõe a India. Abaixo segue os dados da API da INDIA acessado no dia 19/06/2021.

 { "activeCases": 760019,
  "activeCasesNew": -38637,
  "recovered": 28678390,
  "recoveredNew": 97743,
  "deaths": 385137,
  "deathsNew": 1647,
  "previousDayTests": 1902009,
  "totalCases": 29823546,
  "sourceUrl": "https://www.mohfw.gov.in/",
  "lastUpdatedAtApify": "2021-06-19T14:00:00.000Z",
  "readMe": "https://github.com/zpelechova/covid-in/blob/master/README.md",
  "regionData": [
    {
      "region": "Andaman and Nicobar Islands",
      "activeCases": 108,
      "newInfected": 4,
      "recovered": 7128,
      "newRecovered": 24,
      "deceased": 127,
      "newDeceased": 0,
      "totalInfected": 7363
    },
    {
      "region": "Andhra Pradesh",
      "activeCases": 67629,
      "newInfected": -2202,
      "recovered": 1759390,
      "newRecovered": 8486,
      "deceased": 12224,
      "newDeceased": 57,
      "totalInfected": 1839243
    },
    {
      "region": "Arunachal Pradesh",
      "activeCases": 2599,
      "newInfected": -114,
      "recovered": 29934,
      "newRecovered": 322,
      "deceased": 159,
      "newDeceased": 1,
      "totalInfected": 32692
    },
    {
      "region": "Assam",
      "activeCases": 36978,
      "newInfected": -1162,
      "recovered": 436043,
      "newRecovered": 4835,
      "deceased": 4138,
      "newDeceased": 33,
      "totalInfected": 477159
    },
    {
      "region": "Bihar",
      "activeCases": 3548,
      "newInfected": -256,
      "recovered": 705967,
      "newRecovered": 594,
      "deceased": 9536,
      "newDeceased": 9,
      "totalInfected": 719051
    },
    {
      "region": "Chandigarh",
      "activeCases": 431,
      "newInfected": -1,
      "recovered": 60123,
      "newRecovered": 47,
      "deceased": 804,
      "newDeceased": 2,
      "totalInfected": 61358
    },
    {
      "region": "Chhattisgarh",
      "activeCases": 10062,
      "newInfected": -620,
      "recovered": 966414,
      "newRecovered": 1122,
      "deceased": 13368,
      "newDeceased": 7,
      "totalInfected": 989844
    },
    {
      "region": "Dadra and Nagar Haveli and Daman and Diu",
      "activeCases": 71,
      "newInfected": 0,
      "recovered": 10425,
      "newRecovered": 8,
      "deceased": 4,
      "newDeceased": 0,
      "totalInfected": 10500
    },
    {
      "region": "Delhi",
      "activeCases": 2445,
      "newInfected": -109,
      "recovered": 1404688,
      "newRecovered": 260,
      "deceased": 24900,
      "newDeceased": 14,
      "totalInfected": 1432033
    },
    {
      "region": "Goa",
      "activeCases": 3599,
      "newInfected": -225,
      "recovered": 157353,
      "newRecovered": 534,
      "deceased": 2975,
      "newDeceased": 6,
      "totalInfected": 163927
    },
    {
      "region": "Gujarat",
      "activeCases": 7230,
      "newInfected": -519,
      "recovered": 804668,
      "newRecovered": 776,
      "deceased": 10023,
      "newDeceased": 5,
      "totalInfected": 821921
    },
    {
      "region": "Haryana",
      "activeCases": 2940,
      "newInfected": -287,
      "recovered": 754924,
      "newRecovered": 460,
      "deceased": 9183,
      "newDeceased": 36,
      "totalInfected": 767047
    },
    {
      "region": "Himachal Pradesh",
      "activeCases": 3193,
      "newInfected": -237,
      "recovered": 193421,
      "newRecovered": 576,
      "deceased": 3429,
      "newDeceased": 5,
      "totalInfected": 200043
    },
    {
      "region": "Jammu and Kashmir",
      "activeCases": 10094,
      "newInfected": -508,
      "recovered": 296360,
      "newRecovered": 1171,
      "deceased": 4234,
      "newDeceased": 8,
      "totalInfected": 310688
    },
    {
      "region": "Jharkhand",
      "activeCases": 1811,
      "newInfected": -135,
      "recovered": 337362,
      "newRecovered": 274,
      "deceased": 5097,
      "newDeceased": 2,
      "totalInfected": 344270
    },
    {
      "region": "Karnataka",
      "activeCases": 137072,
      "newInfected": -9675,
      "recovered": 2625447,
      "newRecovered": 15290,
      "deceased": 33602,
      "newDeceased": 168,
      "totalInfected": 2796121
    },
    {
      "region": "Kerala",
      "activeCases": 108117,
      "newInfected": -876,
      "recovered": 2665354,
      "newRecovered": 12147,
      "deceased": 11833,
      "newDeceased": 90,
      "totalInfected": 2785304
    },
    {
      "region": "Ladakh",
      "activeCases": 433,
      "newInfected": -49,
      "recovered": 19097,
      "newRecovered": 75,
      "deceased": 200,
      "newDeceased": 0,
      "totalInfected": 19730
    },
    {
      "region": "Lakshadweep",
      "activeCases": 347,
      "newInfected": -52,
      "recovered": 9000,
      "newRecovered": 67,
      "deceased": 45,
      "newDeceased": 0,
      "totalInfected": 9392
    },
    {
      "region": "Madhya Pradesh",
      "activeCases": 2727,
      "newInfected": -257,
      "recovered": 777630,
      "newRecovered": 339,
      "deceased": 8707,
      "newDeceased": 28,
      "totalInfected": 789064
    },
    {
      "region": "Maharashtra",
      "activeCases": 137851,
      "newInfected": -5197,
      "recovered": 5699983,
      "newRecovered": 14347,
      "deceased": 116674,
      "newDeceased": 648,
      "totalInfected": 5954508
    },
    {
      "region": "Manipur",
      "activeCases": 9246,
      "newInfected": 144,
      "recovered": 52667,
      "newRecovered": 447,
      "deceased": 1033,
      "newDeceased": 12,
      "totalInfected": 62946
    },
    {
      "region": "Meghalaya",
      "activeCases": 4819,
      "newInfected": 210,
      "recovered": 38792,
      "newRecovered": 431,
      "deceased": 771,
      "newDeceased": 9,
      "totalInfected": 44382
    },
    {
      "region": "Mizoram",
      "activeCases": 3816,
      "newInfected": 84,
      "recovered": 12858,
      "newRecovered": 228,
      "deceased": 76,
      "newDeceased": 1,
      "totalInfected": 16750
    },
    {
      "region": "Nagaland",
      "activeCases": 2059,
      "newInfected": -309,
      "recovered": 21571,
      "newRecovered": 364,
      "deceased": 467,
      "newDeceased": 1,
      "totalInfected": 24097
    },
    {
      "region": "Odisha",
      "activeCases": 37139,
      "newInfected": -2483,
      "recovered": 829851,
      "newRecovered": 6252,
      "deceased": 3508,
      "newDeceased": 37,
      "totalInfected": 870498
    },
    {
      "region": "Puducherry",
      "activeCases": 4125,
      "newInfected": -208,
      "recovered": 108462,
      "newRecovered": 557,
      "deceased": 1714,
      "newDeceased": 4,
      "totalInfected": 114301
    },
    {
      "region": "Punjab",
      "activeCases": 8829,
      "newInfected": -650,
      "recovered": 566568,
      "newRecovered": 1229,
      "deceased": 15771,
      "newDeceased": 33,
      "totalInfected": 591168
    },
    {
      "region": "Rajasthan",
      "activeCases": 3783,
      "newInfected": -479,
      "recovered": 938101,
      "newRecovered": 620,
      "deceased": 8884,
      "newDeceased": 9,
      "totalInfected": 950768
    },
    {
      "region": "Sikkim",
      "activeCases": 2900,
      "newInfected": -7,
      "recovered": 15868,
      "newRecovered": 166,
      "deceased": 290,
      "newDeceased": 3,
      "totalInfected": 19058
    },
    {
      "region": "Tamil Nadu",
      "activeCases": 89009,
      "newInfected": -11514,
      "recovered": 2286653,
      "newRecovered": 19860,
      "deceased": 30835,
      "newDeceased": 287,
      "totalInfected": 2406497
    },
    {
      "region": "Telangana",
      "activeCases": 19029,
      "newInfected": -492,
      "recovered": 588259,
      "newRecovered": 1897,
      "deceased": 3546,
      "newDeceased": 12,
      "totalInfected": 610834
    },
    {
      "region": "Tripura",
      "activeCases": 4715,
      "newInfected": -158,
      "recovered": 56425,
      "newRecovered": 596,
      "deceased": 642,
      "newDeceased": 5,
      "totalInfected": 61782
    },
    {
      "region": "Uttarakhand",
      "activeCases": 3231,
      "newInfected": -240,
      "recovered": 328040,
      "newRecovered": 456,
      "deceased": 7017,
      "newDeceased": 6,
      "totalInfected": 338288
    },
    {
      "region": "Uttar Pradesh",
      "activeCases": 5343,
      "newInfected": -676,
      "recovered": 1676458,
      "newRecovered": 774,
      "deceased": 22081,
      "newDeceased": 51,
      "totalInfected": 1703882
    },
    {
      "region": "West Bengal",
      "activeCases": 22691,
      "newInfected": 618,
      "recovered": 1437106,
      "newRecovered": 2112,
      "deceased": 17240,
      "newDeceased": 58,
      "totalInfected": 1477037
    }
  ]
}


### Para fazer o Bot funcionar no prompt de comando deve-se executar:

 ``` rasa train 
  ``` rasa run actions
   ``` em um outro terminal executar rasa shell
    ``` para o bot funcionar com interação, deve-se acessar a pasta public, e abrir o index, e no teriminal executar:
            rasa run -m models --enable-api --cors "*" --debug

### As entradas esperadas para o bot responder!!!
```
Your input ->  oi                                                                                                                            
Oi! Como você está? Eu mostro os casos de COVID19 da India, digite um estado ex:Assam,Arunachal Pradesh,Bihar!!!
Your input ->  bem                                                                                                                           
Ótimo!
Your input -> Aqui você digita algum estado da India exemplos -> ... Assam, Bihar....,


``` O bot irá acessar a API e retornará as informações conforme mostra abaixo do estado de:
Assam
Active cases are 35631
, confirmed cases are 477159
, Total deaths are 4138
, Total patient recovered are 436043

```

